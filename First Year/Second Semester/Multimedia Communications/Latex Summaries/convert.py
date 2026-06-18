#!/usr/bin/env python3
"""1:1 converter: Obsidian-flavoured Markdown (Summaries/*.md) -> LaTeX book chapters."""
import os, re, sys

SRC = "../Summaries"
OUTDIR = "chapters"

CALLOUT_COLOR = {
    "important": "red!70!black",
    "example":   "green!55!black",
    "note":      "blue!60!black",
    "tip":       "green!55!black",
    "warning":   "orange!80!black",
}

def chap_num(fname):
    return int(re.match(r"(\d+)\.", fname).group(1))

# ----- inline formatting -------------------------------------------------
def esc(text):
    """Escape LaTeX specials in plain text (no math/code spans inside)."""
    repl = {
        "\\": r"\textbackslash{}",
        "&": r"\&", "%": r"\%", "#": r"\#", "$": r"\$",
        "_": r"\_", "{": r"\{", "}": r"\}",
        "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    }
    out = []
    for ch in text:
        out.append(repl.get(ch, ch))
    return "".join(out)

def inline(text):
    """Convert inline markdown to LaTeX, protecting math and code spans."""
    placeholders = []
    def stash(s):
        placeholders.append(s)
        return f"\x00{len(placeholders)-1}\x00"

    # protect inline code first
    text = re.sub(r"`([^`]+)`", lambda m: stash(("code", m.group(1))), text)
    # protect inline math
    text = re.sub(r"\$(.+?)\$", lambda m: stash(("math", m.group(1))), text)

    # wiki links [[#a|b]] -> b ; [[a|b]] -> b ; [[a]] -> a
    text = re.sub(r"\[\[[^\]|]*\|([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)

    # escape specials (markers * and ` survive)
    text = esc(text)

    # bold then italic
    text = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"\\textit{\1}", text)

    # restore placeholders
    def restore(m):
        kind, val = placeholders[int(m.group(1))]
        if kind == "math":
            return f"${val}$"
        # code: escape specials, render as texttt
        return r"\texttt{" + esc(val) + r"}"
    text = re.sub(r"\x00(\d+)\x00", restore, text)
    return text

# ----- image -------------------------------------------------------------
IMG_RE = re.compile(r"!\[\[Pics/([^/]+)/([^\]|]+?)(?:\|(\d+))?\]\]")

def img_line(m, n):
    name = m.group(2).strip()
    px = int(m.group(3)) if m.group(3) else 480
    frac = min(round(px / 600.0, 3), 1.0)
    w = r"\linewidth" if frac >= 1.0 else f"{frac}\\linewidth"
    return f"\\begin{{center}}\\includegraphics[width={w}]{{ch{n:02d}/{name}}}\\end{{center}}"

# ----- table -------------------------------------------------------------
def is_table_sep(line):
    return bool(re.match(r"^\s*\|?[\s:|-]+\|?\s*$", line)) and "-" in line

def split_row(line):
    line = line.strip()
    if line.startswith("|"): line = line[1:]
    if line.endswith("|"): line = line[:-1]
    return [c.strip() for c in line.split("|")]

def render_table(rows):
    header = split_row(rows[0])
    sep = split_row(rows[1])
    ncol = len(header)
    aligns = []
    for i in range(ncol):
        s = sep[i] if i < len(sep) else "---"
        l, r = s.startswith(":"), s.endswith(":")
        aligns.append("c" if l and r else ("r" if r else "l"))
    colspec = "|" + "|".join(aligns) + "|"
    out = ["\\begin{center}\\fitwidth{%", f"\\begin{{tabular}}{{{colspec}}}", "\\hline"]
    out.append(" & ".join(f"\\textbf{{{inline(c)}}}" for c in header) + " \\\\ \\hline")
    for r in rows[2:]:
        cells = split_row(r)
        cells += [""] * (ncol - len(cells))
        out.append(" & ".join(inline(c) for c in cells[:ncol]) + " \\\\ \\hline")
    out += ["\\end{tabular}}", "\\end{center}"]
    return "\n".join(out)

# ----- main block converter (recursive for callouts) ---------------------
def convert(lines, n):
    out = []
    i = 0
    para = []
    def flush_para():
        if para:
            out.append(inline(" ".join(para).strip()))
            out.append("")
            para.clear()

    while i < len(lines):
        line = lines[i]
        s = line.strip()

        # blank
        if s == "":
            flush_para(); i += 1; continue

        # heading
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            flush_para()
            lvl = len(m.group(1)); title = inline(m.group(2).strip())
            cmd = {1:"chapter",2:"section",3:"subsection",4:"subsubsection",
                   5:"paragraph",6:"subparagraph"}[lvl]
            out.append(f"\\{cmd}{{{title}}}"); out.append("")
            i += 1; continue

        # fenced code / mermaid
        if s.startswith("```"):
            flush_para()
            lang = s[3:].strip()
            j = i + 1; buf = []
            while j < len(lines) and not lines[j].strip().startswith("```"):
                buf.append(lines[j]); j += 1
            label = "Diagram (Mermaid source):" if lang == "mermaid" else None
            if label:
                out.append(f"\\begin{{center}}\\footnotesize\\itshape {label}\\end{{center}}")
            out.append("\\begin{verbatim}")
            out.extend(buf)
            out.append("\\end{verbatim}"); out.append("")
            i = j + 1; continue

        # block math $$ ... $$
        if s == "$$":
            flush_para()
            j = i + 1; buf = []
            while j < len(lines) and lines[j].strip() != "$$":
                buf.append(lines[j]); j += 1
            out.append("\\[")
            out.extend(buf)
            out.append("\\]"); out.append("")
            i = j + 1; continue

        # image
        im = IMG_RE.match(s)
        if im:
            flush_para()
            out.append(img_line(im, n)); i += 1; continue

        # blockquote / callout
        if s.startswith(">"):
            flush_para()
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                inner = re.sub(r"^\s*>\s?", "", lines[i])
                buf.append(inner); i += 1
            cm = re.match(r"^\s*\[!(\w+)\]\s*(.*)$", buf[0])
            if cm:
                ctype = cm.group(1).lower()
                color = CALLOUT_COLOR.get(ctype, "gray!60!black")
                title = inline(cm.group(2).strip()) if cm.group(2).strip() else ctype.capitalize()
                body = convert(buf[1:], n)
                out.append(f"\\begin{{calloutbox}}{{{color}}}{{{title}}}")
                out.append(body.rstrip())
                out.append("\\end{calloutbox}"); out.append("")
            else:
                out.append("\\begin{quote}")
                out.append(convert(buf, n).rstrip())
                out.append("\\end{quote}"); out.append("")
            continue

        # table
        if s.startswith("|") and i + 1 < len(lines) and is_table_sep(lines[i+1]):
            flush_para()
            buf = [lines[i], lines[i+1]]; j = i + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                buf.append(lines[j]); j += 1
            out.append(render_table(buf)); out.append("")
            i = j; continue

        # unordered list
        if re.match(r"^\s*[-*]\s+", line):
            flush_para()
            out.append("\\begin{itemize}")
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                item = re.sub(r"^\s*[-*]\s+", "", lines[i]).rstrip()
                out.append(f"  \\item {inline(item)}"); i += 1
            out.append("\\end{itemize}"); out.append("")
            continue

        # ordered list
        if re.match(r"^\s*\d+\.\s+", line):
            flush_para()
            out.append("\\begin{enumerate}")
            while i < len(lines) and re.match(r"^\s*\d+\.\s+", lines[i]):
                item = re.sub(r"^\s*\d+\.\s+", "", lines[i]).rstrip()
                out.append(f"  \\item {inline(item)}"); i += 1
            out.append("\\end{enumerate}"); out.append("")
            continue

        # paragraph text
        para.append(s); i += 1

    flush_para()
    # collapse >2 blank lines
    txt = "\n".join(out)
    txt = re.sub(r"\n{3,}", "\n\n", txt)
    return txt

def main():
    files = sorted([f for f in os.listdir(SRC)
                    if f.endswith(".md") and re.match(r"\d+\.", f)],
                   key=chap_num)
    inputs = []
    for f in files:
        n = chap_num(f)
        with open(os.path.join(SRC, f), encoding="utf-8") as fh:
            lines = fh.read().split("\n")
        body = convert(lines, n)
        outpath = os.path.join(OUTDIR, f"{n:02d}.tex")
        with open(outpath, "w", encoding="utf-8") as fh:
            fh.write(body.strip() + "\n")
        inputs.append(f"{n:02d}.tex")
        print(f"{f}  ->  {outpath}")
    return inputs

if __name__ == "__main__":
    main()

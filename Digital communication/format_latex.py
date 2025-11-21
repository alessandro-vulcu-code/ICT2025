import re

def format_latex(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    formatted_lines = []
    buffer = ""

    for line in lines:
        line = line.strip()
        if not line:
            if buffer:
                formatted_lines.append(buffer + "\n\n")
                buffer = ""
            continue

        # Basic joining: if buffer ends with a letter and line starts with a letter, join with space
        if buffer and buffer[-1].isalnum() and line[0].isalnum():
             buffer += " " + line
        else:
            if buffer:
                formatted_lines.append(buffer + "\n")
            buffer = line

    if buffer:
        formatted_lines.append(buffer + "\n")

    # Now process the joined lines for math
    final_lines = []
    for line in formatted_lines:
        # Math replacements
        line = re.sub(r'N C', r'\\mathcal{N}_{\\mathbb{C}}', line)
        line = re.sub(r'E\[', r'\\mathbb{E}[', line)
        line = re.sub(r'R x', r'R_x', line)
        line = re.sub(r'\\mu x', r'\\mu_x', line)
        line = re.sub(r'\\sigma\s*2', r'\\sigma^2', line)
        line = re.sub(r'\\sqrt\s*(\\rho\w*)', r'\\sqrt{\1}', line) # heuristic for sqrt
        
        # Section detection (heuristic)
        if re.match(r'^(Intro|Primer|Mutual information|Differential entropy)', line, re.IGNORECASE) and len(line) < 50:
            line = f"\\section{{{line}}}"
        
        final_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(final_lines)

if __name__ == "__main__":
    format_latex('cleaned_text.txt', 'formatted_text.tex')

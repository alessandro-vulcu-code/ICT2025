import re
import os

def clean_latex(text):
    """Pulisce il testo LaTeX per Anki."""
    # Rimuove i commenti LaTeX
    text = re.sub(r'(?<!\\)%.*', '', text)
    # Converte $$ ... $$ in \[ ... \] per compatibilità MathJax totale
    text = re.sub(r'\$\$(.*?)\$\$', r'\[ \1 \]', text, flags=re.DOTALL)
    # Rimuove spazi bianchi eccessivi
    return text.strip()

def latex_to_anki(input_file):
    if not os.path.exists(input_file):
        print(f"Errore: Il file {input_file} non esiste.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split per capitoli: cerca \chapter*{Titolo}
    # La regex cattura il titolo e tutto il testo fino al capitolo successivo
    chapters = re.split(r'\\chapter\*\{(.*?)\}', content)

    for i in range(1, len(chapters), 2):
        deck_name = chapters[i].strip().replace(" ", "_").replace("/", "-")
        deck_body = chapters[i+1]

        # Trova i blocchi domanda + risposta come unità singola
        pattern = re.compile(
            r'\\begin\{question\}(.*?)\\end\{question\}\s*\\begin\{answer\}(.*?)\\end\{answer\}',
            re.DOTALL
        )

        cards = pattern.findall(deck_body)

        if not cards:
            continue

        output_filename = f"anki_{deck_name}.txt"
        with open(output_filename, 'w', encoding='utf-8') as out:
            for q_text, a_text in cards:
                front = clean_latex(q_text).replace('\n', ' ')
                # Per il retro usiamo <br> per i newline, così Anki renderizza il testo a capo
                back = clean_latex(a_text).replace('\n', ' <br> ')

                # Separatore TAB tra Fronte e Retro
                out.write(f"{front}\t{back}\n")

        print(f"Mazzo '{deck_name}' generato: {len(cards)} card(s).")

if __name__ == "__main__":
    # Cambia qui il nome del tuo file sorgente
    latex_to_anki('FiberOptics.tex')

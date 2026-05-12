> Trascrivi un PDF in Markdown e salvalo in `ToSummarize/`.

## Input

Il file PDF viene passato come argomento: `/trascrivi <percorso/al/file.pdf>`

## Istruzioni

1. Leggi il PDF con il tool `Read`.
2. Trascrivi il contenuto **fedelmente**:
   - Testo normale → Markdown normale
   - Titoli e sezioni → heading Markdown (`#`, `##`, ecc.)
   - Formule matematiche → LaTeX inline `$...$` o block `$$...$$`
   - Tabelle → tabelle Markdown
   - Liste → liste Markdown
   - Figure/immagini → descrizione testuale `[Figura: descrizione]`
3. Non omettere nulla. Non riassumere. Non aggiungere commenti tuoi.
4. Salva il risultato in `ToSummarize/<nome_file>.md` (stessa directory del PDF o nella cartella del progetto corrente, a seconda del contesto).
   - Nome file: stesso del PDF, estensione cambiata in `.md`
   - Se la cartella `ToSummarize/` non esiste, creala.

## Output

Conferma: `Trascritto → ToSummarize/<nome_file>.md`

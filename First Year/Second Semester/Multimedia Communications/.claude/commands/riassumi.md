> Riassumi un file Markdown trascritto da PDF e salvalo in `Summaries/`.

## Input

`/riassumi <percorso/al/file.md>`

Il file è tipicamente in `ToSummarize/`. Materia: **Multimedia Communications** (compressione, trasmissione multimediale, stima del moto, probabilità, codifica, protocolli).

---

## Istruzioni

### 1. Lingua

Rileva la lingua del testo sorgente. Scrivi il riassunto **nella stessa lingua**. Non tradurre.

---

### 2. Struttura obbligatoria del riassunto

#### a) Indice interattivo (inizio file)

```markdown
## Table of Contents

- [[#Section Title|Section Title]]
- [[#Section Title 2|Section Title 2]]
  - [[#Subsection|Subsection]]
...
```

Usa link interni Obsidian (`[[#anchor|label]]`). Genera anchor dal titolo della sezione.

#### b) Corpo del riassunto

- Gerarchia heading: `#` titolo doc → `##` capitolo → `###` sezione → `####` sottosezione
- **Bold** per termini tecnici, definizioni, concetti chiave introdotti per la prima volta
- *Italic* per enfasi, nomi di metodi, acronimi espansi
- Formule matematiche: LaTeX inline `$...$` o block `$$...$$` — trascrivi **fedele all'originale**
- Liste puntate per enumerazioni, liste numerate per sequenze/algoritmi
- Tabelle Markdown dove utile per confronti o parametri

#### c) Teoremi e risultati importanti → callout `[!Important]`

```markdown
> [!Important] Nome Teorema / Lemma / Proprietà
> Enunciato fedele.
> $$formula$$
> **Dimostrazione (sketch):** ...  ← solo se presente nel testo
> **Intuizione:** spiegazione semplice per studente.
```

Usa questo callout per: teoremi, lemmi, corollari, definizioni fondamentali, bound importanti (Shannon, Nyquist, ecc.).

#### d) Esempi numerici → callout `[!Example]`

```markdown
> [!Example] Titolo esempio
> **Dati:** ...
> **Svolgimento:**
> $$calcolo$$
> **Risultato:** ...
```

#### e) Placeholder immagini

Ogni volta che nel testo originale è presente un riferimento a figura, grafico, diagramma o immagine, inserisci:

```markdown
![[PLACEHOLDER_Fig_N — descrizione breve]]
```

Dove `N` è il numero figura originale (se presente) o un contatore progressivo.

#### f) Tabella riassuntiva (fine file)

Tabella Markdown con le colonne rilevanti per la sezione trattata. Esempi tipici:

| Concetto | Formula / Valore | Note |
|----------|-----------------|------|

oppure per tecniche di compressione:

| Tecnica | Tipo | Lossy/Lossless | Uso tipico |
|---------|------|---------------|------------|

Adatta le colonne al contenuto reale del documento.

---

### 3. Qualità del contenuto

- Non omettere formule, definizioni o passaggi logici chiave
- Se un concetto è implicito nel testo ma necessario per capire, aggiungilo con nota *(nota: ...)*
- Non inventare. Se qualcosa è ambiguo nel sorgente, riportalo com'è
- Mantieni il rigore tecnico di un corso universitario magistrale
- Il riassunto deve essere **autosufficiente**: uno studente deve capire senza rileggere il PDF

---

### 4. Salvataggio

- Percorso output: `Notes/<nome_file>.md` (stessa base name del file input)
- Se `Notes/` non esiste, creala
- Conferma: `Riassunto → Summaries/<nome_file>.md`

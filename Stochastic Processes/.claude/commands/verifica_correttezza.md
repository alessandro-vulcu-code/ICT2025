# /verifica_correttezza

Confronta trascrizione e riassunto. Correggi errori, aggiungi mancanze, rimuovi incoerenze.

## Input

`/verifica_correttezza <percorso/trascrizione.md> <percorso/riassunto.md>`

- `trascrizione.md` → file in `ToSummarize/` (fonte di verità)
- `riassunto.md` → file in `Summaries/` (da verificare e correggere)

---

## Istruzioni

### 1. Lettura

Leggi entrambi i file per intero prima di procedere.

---

### 2. Controllo incrociato — checklist

Per ogni sezione della trascrizione, verifica nel riassunto:

#### a) Completezza
- Ogni **teorema, lemma, corollario** presente in trascrizione ha callout `[!Important]` nel riassunto?
- Ogni **formula** rilevante è riportata in LaTeX corretto?
- Ogni **esempio numerico** ha callout `[!Example]`?
- Ogni **definizione fondamentale** è in bold alla prima occorrenza?
- Placeholder `![[PLACEHOLDER_Fig_N]]` per ogni figura/grafico citato?
- Indice copre tutte le sezioni?
- Tabella riassuntiva finale include tutti i concetti chiave?

#### b) Correttezza
- Formule nel riassunto coincidono **simbolo per simbolo** con la trascrizione?
- Enunciati dei teoremi non sono parafrasati in modo che cambi il significato?
- Condizioni/ipotesi dei teoremi sono riportate (non solo la tesi)?
- Valori numerici, unità di misura, indici corretti?

#### c) Coerenza
- Terminologia consistente con la trascrizione (stesso nome per stesso concetto)?
- Gerarchia heading rispetta la struttura originale del documento?
- Ordine delle sezioni segue l'originale?

---

### 3. Output del controllo

Prima di modificare, produci report sintetico:

```
## Report verifica

### Errori (da correggere)
- [sezione] [problema] → [correzione]

### Mancanze (da aggiungere)
- [cosa manca] → [dove inserire]

### OK
- [lista sezioni verificate senza problemi]
```

---

### 4. Modifica

Dopo il report, applica **tutte** le correzioni direttamente al file `riassunto.md`:

- Correggi formule errate
- Aggiungi teoremi/esempi mancanti nel punto corretto della gerarchia
- Aggiusta terminologia incoerente
- Aggiungi placeholder figure mancanti
- Aggiorna indice e tabella riassuntiva finale se il contenuto cambia

Non toccare parti già corrette.

---

### 5. Conferma

```
Verifica completata.
Errori corretti: N
Sezioni integrate: M
File aggiornato → Summaries/<nome_file>.md
```

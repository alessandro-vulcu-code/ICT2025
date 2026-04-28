> /trascrivi <trascrizione> <riassunto>

Sei un esperto di Big Data Computing. Ti vengono forniti due documenti ($ARGUMENTS):
1. La **trascrizione fedele** del documento originale del corso
2. Il **riassunto** prodotto dalla trascrizione

Esegui un controllo incrociato sistematico e, se necessario, aggiorna il riassunto direttamente.

---

## 1. Procedura di verifica

Confronta trascrizione e riassunto controllando:

- **Completezza:** ogni teorema, lemma, definizione, bound, algoritmo e esempio presente nella trascrizione è rappresentato nel riassunto? Se manca qualcosa di rilevante, aggiungilo.
- **Fedeltà delle formule:** ogni formula nel riassunto corrisponde esattamente a quella nella trascrizione? Correggi eventuali errori LaTeX o trascrizioni imprecise.
- **Chiarezza:** ci sono sezioni del riassunto ambigue, incomplete o che presuppongono conoscenze non introdotte? Espandile quel tanto che basta per renderle autosufficenti, senza aggiungere contenuto non presente nella trascrizione.
- **Struttura:** la gerarchia di heading, i callout `[!Important]` e `[!Example]`, la tabella riassuntiva e il Table of Contents riflettono correttamente la struttura della trascrizione?
- **Dimostrazioni:** IMPORTANTE: i teoremi, le definizioni e le rispettive dimostrazioni che sono scritte a mano, sono FONDAMENTALI per l'esame in quanto verranno chieste. Pertanto, vanno riportate per intero. Puoi riformulare o sistemare le frasi, ma il contenuto deve assolutamente essere riportato per intero dalla trascrizione al riassunto. In caso non fosse così, devi scrivere la dimostrazione completa ove mancasse.

---

## 2. Output della verifica

Prima di aggiornare, produci un breve report in questa forma:

```
## Report verifica

### Elementi mancanti
- <elenco puntato di ciò che mancava>

### Formule da correggere
- <elenco puntato con originale → corretto>

### Sezioni poco chiare espanse
- <elenco puntato>

### Nessuna modifica necessaria
<scrivi questa riga solo se il riassunto è già completo e corretto>
```

---

## 3. Aggiornamento del riassunto

Se il report evidenzia problemi, aggiorna direttamente il file del riassunto (`Notes/<nome_file>.md`) integrando le correzioni. Non riscrivere da zero: modifica solo le parti carenti, aggiungendo le sezioni o i callout mancanti nel punto corretto della struttura esistente.

Alla fine conferma: `Riassunto aggiornato → Notes/<nome_file>.md`

Se non ci sono problemi, non toccare il file e scrivi solo: `Verifica completata: nessuna modifica necessaria.`

---
name: riassumi-webapp
description: Summarize and clean a Markdown note from Web Applications course. Use when the user invokes /riassumi, asks to riassumi/sintetizza/riorganizza a Markdown document, or wants an exam-ready summary of a lecture on servlets, JSP, REST, HTTP, HTML, CSS, JavaScript, SQL, Docker, Git, Maven, security, or web architecture.
---

> Riassumi un file Markdown di Web Applications e salvalo in `Notes/`.

## Input

`/riassumi <percorso/al/file.md>`

Il file è tipicamente in `MD Converted/`. Materia: **Web Applications** (architettura web, Servlet, JSP, REST, HTTP, HTML5, CSS, JavaScript, SQL, Docker, Git, Maven, sicurezza web, AJAX, MIME).

---

## Istruzioni

### 1. Lingua

Rileva la lingua del testo sorgente (INGLESE). Scrivi il riassunto **nella stessa lingua**. Non tradurre.

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
- *Italic* per enfasi, nomi di tecnologie, acronimi espansi
- Formule e URL: inline code o blocco dove appropriato
- Liste puntate per enumerazioni, liste numerate per sequenze/procedure/algoritmi
- Tabelle Markdown per confronti, parametri HTTP, attributi SQL, configurazioni

#### c) Concetti fondamentali → callout `[!Important]`

```markdown
> [!Important] Concetto / Definizione / Protocollo
> Descrizione fedele.
> ```codice o schema```
> **Intuizione:** spiegazione semplice per studente.
```

Usa per: architetture (MVC, REST, client-server), protocolli (HTTP request/response, sessioni), meccanismi di sicurezza (XSS, SQL injection, CSRF, autenticazione), ciclo di vita (Servlet lifecycle, bean scope), standard importanti.

#### d) Esempi di codice e configurazione → callout `[!Example]`

```markdown
> [!Example] Titolo esempio
> **Contesto:** ...
> **Codice:**
> ```java
> // snippet fedele all'originale
> ```
> **Spiegazione:** ...
```

Usa per: snippet Servlet/JSP, query SQL, chiamate REST, configurazioni XML/YAML/Docker, esempi HTML/CSS/JS significativi.

#### e) Warning e best practice → callout `[!Warning]`

```markdown
> [!Warning] Vulnerabilità / Anti-pattern
> Descrizione del problema.
> **Mitigazione:** ...
```

Usa per: vulnerabilità di sicurezza (XSS, SQL injection, CSRF), anti-pattern architetturali, deprecazioni, errori comuni.

#### f) Immagini

Nella cartella assets trovi delle immagini. Alcune sono duplicate o comunque immagini di abbellimento del pdf che non serve inserire. Le immagini che non mostrano nulla di sostaziale non metterle, invece quelle che mostrano schemi/grafici/elenchi/speigazioni, importale.

Se ritieni che manchi qualche figura invece, inserisci:

```markdown
![[PLACEHOLDER_Fig_N — descrizione breve]]
```

Dove `N` è il numero figura originale (se presente) o un contatore progressivo.
Le immagini esistenti che usi e importi le metti dentro la cartella "Figures" che sarà dentro "Notes"

#### g) Tabella riassuntiva (fine file)

Tabella Markdown con le colonne rilevanti per la sezione trattata. Esempi tipici:

| Concetto | Descrizione | Note |
|----------|-------------|------|

oppure per HTTP:

| Metodo HTTP | Semantica | Idempotente | Body |
|-------------|-----------|-------------|------|

oppure per tecnologie web:

| Tecnologia | Lato | Scopo | Esempio |
|------------|------|-------|---------|

Adatta le colonne al contenuto reale del documento.

---

### 3. Qualità del contenuto

- Non omettere snippet di codice, configurazioni o passaggi logici chiave
- Se un concetto è implicito nel testo ma necessario per capire, aggiungilo con nota *(nota: ...)*
- Non inventare. Se qualcosa è ambiguo nel sorgente, riportalo com'è
- Mantieni il rigore tecnico di un corso universitario magistrale
- Il riassunto deve essere **autosufficiente**: uno studente deve capire senza rileggere il PDF originale
- Per codice: usa il language tag corretto (`java`, `xml`, `sql`, `html`, `css`, `javascript`, `bash`, `json`, `yaml`, `dockerfile`)

---

### 4. Salvataggio

- Percorso output: `Notes/<nome_file>.md` (stessa base name del file input)
- Se `Notes/` non esiste, creala
- Conferma: `Riassunto → Notes/<nome_file>.md`

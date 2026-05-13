# Introduction to Web Applications — Web Applications 2025-26

## Table of Contents

- [[#A Bit of History|A Bit of History]]
  - [[#Vannevar Bush: The Memex (1945)|Vannevar Bush: The Memex (1945)]]
  - [[#Ted Nelson: Hypertext (1963/1965)|Ted Nelson: Hypertext (1963/1965)]]
  - [[#Douglas Engelbart: NLS System (1962–1968)|Douglas Engelbart: NLS System (1962–1968)]]
  - [[#Halasz/Moran/Trigg: NoteCards (1983–1987)|Halasz/Moran/Trigg: NoteCards (1983–1987)]]
  - [[#Tim Berners-Lee: World Wide Web (1989–1991)|Tim Berners-Lee: World Wide Web (1989–1991)]]
  - [[#Browser Timeline|Browser Timeline]]
- [[#Evolution of the Web|Evolution of the Web]]
  - [[#Web 1.0 — Read Web|Web 1.0 — Read Web]]
  - [[#Web 2.0 — Read/Write Web|Web 2.0 — Read/Write Web]]
  - [[#Web 3.0 — Semantic Web|Web 3.0 — Semantic Web]]
  - [[#Deep Web and Dark Web|Deep Web and Dark Web]]
  - [[#Web3|Web3]]
- [[#Distributed Applications|Distributed Applications]]
  - [[#Application Layers|Application Layers]]
  - [[#Balancing Application Load|Balancing Application Load]]
  - [[#Single-tier Architecture|Single-tier Architecture]]
  - [[#Two-tier Architecture|Two-tier Architecture]]
  - [[#Three-tier Architecture|Three-tier Architecture]]
  - [[#Web Applications as Three-tier|Web Applications as Three-tier]]
  - [[#Web Applications and the Network Stack|Web Applications and the Network Stack]]
- [[#Summary Table|Summary Table]]

---

## A Bit of History

### Vannevar Bush: The Memex (1945)

**Vannevar Bush** (1890–1974), Director of the *Office of Scientific Research and Development* (OSRD).

In July 1945, Bush published *"As We May Think"* in *The Atlantic Monthly* — a visionary article describing the **Memex**, a hypothetical device for storing and retrieving linked information. First conceptual precursor to hypertext and the Web.

### Ted Nelson: Hypertext (1963/1965)

**Theodor Holm Nelson** (born 1937) — philosopher, sociologist, ICT pioneer.

- Coined the term **hypertext** in 1963; first published in print in 1965 (interview at Vassar College, NY)
- **Project Xanadu** (1960–1998): first hypertext project; released open source in 2014
  - Features: *transcopyright*, original context, **bi-directional links**, versioning

### Douglas Engelbart: NLS System (1962–1968)

**Douglas Carl Engelbart** (1925–2013), Augmentation Research Center Lab at Stanford Research Institute.

- **NLS** (*oN-Line System*) — first system to use: mouse, hyperlinks, windows, presentation programs
- **"Mother of All Demos"**: presented at ACM/IEEE Fall Joint Computer Conference, 1968

### Halasz/Moran/Trigg: NoteCards (1983–1987)

- Developed at **Xerox** in LISP; one of the most successful hypertext systems of the era
- Goal: support analysts in **collecting and organising information** to prepare summary reports
- Extensible through a LISP-based programming language

### Tim Berners-Lee: World Wide Web (1989–1991)

- Proposed the Web in **1989** and again in **1990** as a linked information system for managing large project outputs at **CERN**
- Simplified prior hypertext research; perfect "marriage" with the Internet
- Internal CERN development: 1990
- **First website**: 1991 at `http://info.cern.ch/`

### Browser Timeline

**Early browsers (1990–1993):**

| Year | Browser | Origin | Notes |
|------|---------|--------|-------|
| 1990–1991 | WorldWideWeb/Nexus | Tim Berners-Lee/CERN | WYSIWYG browser/editor on NeXT |
| 1991–1992 | Line Mode Browser | Nicola Pellow/CERN | Text-only; many platforms |
| 1992 | Lynx | University of Kansas | Textual; Unix → multiplatform; still supported |
| 1993 | **Mosaic** | Univ. of Illinois Urbana-Champaign | First graphical multi-platform browser; **popularised the Web** |

**Modern browsers:**

| Year | Browser |
|------|---------|
| 1994 | Netscape Navigator |
| 1995 | Microsoft Internet Explorer |
| 1996 | Opera |
| 1998 | Mozilla Foundation (open source, from Netscape) |
| 2003 | Safari |
| 2004 | Firefox (superseded Netscape Navigator) |
| 2008 | Google Chrome |
| 2015 | Microsoft Edge (superseded Internet Explorer) |

---

## Evolution of the Web

### Web 1.0 — Read Web

> [!Important] Web 1.0 — "Read Web" / Informative Web
> **Period:** roughly 1990–2000
>
> **Key technologies:** HTTP, HTML, MIME, URL
>
> **Main features:**
> - Static web pages
> - Dynamic web pages
> - Web portals
>
> **Intuition:** One-way content flow — a WebMaster/Producer publishes content; Passive Consumers read it.

![[intro-web10.jpg]]

### Web 2.0 — Read/Write Web

> [!Important] Web 2.0 — "Read/Write Web" / Participative Web
> **Period:** roughly 2000–2010, still ongoing
>
> **Key technologies:** XML, AJAX, JSON
>
> **Main features:**
> - Social media
> - Web services
> - [SOAP]
> - **REST**
>
> **Intuition:** Users both consume and produce content. Web services enable machine-to-machine communication.

### Web 3.0 — Semantic Web

> [!Important] Web 3.0 — "Web of Data" / Intelligent Web
> **Period:** roughly 2010 onwards
>
> *Note: was supposed to be Web 2.0 — the two evolutions happened in different order than anticipated.*
>
> **Key technologies:** RDF, OWL, SPARQL
>
> **Main features:**
> - Machine-processable / machine-executable information
> - Linked (Open) Data
> - Big Data
>
> **Intuition:** Data on the Web has machine-readable semantics — computers can reason over it, not just display it.

### Deep Web and Dark Web

**Deep Web:**
- Web content **not indexed** by standard search engines (login-protected pages, databases, internal systems)
- Estimated ~500× the size of the indexable/surface Web
- Estimated >1 billion structured data sets (as of Feb 2011)
- Exists since Web 1.0; nowadays often confused with the Dark Web

**Dark Web:**
- **Anonymous** and confidential access to Web/Internet
- Uses **onion routing** and strong cryptography
- Tools: *Tor* (anonymous access), *I2P* (anonymous hosting)
- Very often used for illegal activities

### Web3

- **Decentralized** web; data controlled by users, not central platforms
- **Blockchain**-based infrastructure
- Includes: cryptocurrencies, *Decentralized Finance* (DeFi), *Non-Fungible Tokens* (NFT)

---

## Distributed Applications

### Application Layers

> [!Important] Three-Layer Application Model
> Every application is logically divided into three layers:
>
> | Layer | Also Called | Responsibilities |
> |-------|-------------|-----------------|
> | **Presentation Logic** | Interface / User Logic | Manages user interaction; defines format and visualisation of information; accepts and validates user input |
> | **Application Logic** | Business Logic | Defines and controls flow of operations; defines basic data operations and constraints (business rules) |
> | **Data Logic** | — | Manages persistent data storage; searches and retrieves data; ensures data consistency |
>
> **Intuition:** Separation of concerns — each layer has a distinct responsibility. Different architectures decide *where* each layer physically runs.

### Balancing Application Load

The three layers can be distributed across machines in different ways, giving rise to single-tier, two-tier, and three-tier architectures.

![[intro-load-balancing.jpg]]

### Single-tier Architecture

**Terminal/Mainframe** model — all three layers run on the mainframe; terminals are "dumb" (no processing).

| Pros | Cons |
|------|------|
| Easy to implement | Full computational load on mainframe (single point of failure) |
| No client management | Poor scalability |

### Two-tier Architecture

Two variants depending on where the "fat" side lives:

**Fat Client / Server:**
- **Fat client**: Presentation Logic + Application Logic on client
- **Database server**: Data Logic on server
- Client does most processing

![[intro-two-tier-fat-client.jpg]]

**Client / Fat Server:**
- **Client**: Presentation Logic only
- **Database + Application server**: Application Logic + Data Logic on server

![[intro-two-tier-fat-server.jpg]]

| Pros | Cons |
|------|------|
| Easy to implement | Client maintenance (fat client variant) |
| Possibility to balance load | Scalability limitations |

### Three-tier Architecture

**Client / Middleware / Server** — three separate tiers:

- **Thin client**: Presentation Logic only
- **Application server**: Application Logic (middleware)
- **Database server(s)**: Data Logic

![[intro-three-tier.jpg]]

| Pros | Cons |
|------|------|
| Easy client maintenance | Higher implementation complexity |
| Possibility to balance load | |
| High scalability | |

### Web Applications as Three-tier

> [!Important] Web Applications = Three-tier Architecture
> Web applications are a specific instance of the three-tier architecture:
>
> | Tier | Component |
> |------|-----------|
> | **Thin Client** | Browser (any device) |
> | **Middleware** | Web + Application Server |
> | **Data** | Database Server(s) |
>
> **Main properties:**
> - Based on **standard and ubiquitous** server-side technologies (already in most IT infrastructures)
> - **No client management** required — the client is the browser
> - Clients are **ubiquitous**: desktop and mobile devices
> - Users are **already familiar** with basic interaction patterns (browser navigation, forms, links)
>
> **Intuition:** The browser becomes the universal thin client — no installation, no updates on the user side.

![[intro-webapp-three-tier.jpg]]

### Web Applications and the Network Stack

> [!Important] HTTP over the Network Stack
> Web app communication maps onto the standard TCP/IP stack:
>
> | Layer | Protocol |
> |-------|---------|
> | Application | **HTTP** |
> | Transport | TCP / UDP |
> | Network | IP |
> | Host-Physical | Physical link |
>
> Client sends **Request** → Server sends **Response** — all carried over HTTP at the application layer.
>
> **Intuition:** HTTP is just an application-layer protocol riding on top of TCP/IP — the same infrastructure used by all Internet services.

![[intro-network-stack.jpg]]

---

## Summary Table

### Web Evolution

| Era | Period | Technologies | Features |
|-----|--------|-------------|---------|
| **Web 1.0** | ~1990–2000 | HTTP, HTML, MIME, URL | Static/dynamic pages, web portals; one-way content |
| **Web 2.0** | ~2000–2010+ | XML, AJAX, JSON, REST | Social media, web services, user-generated content |
| **Web 3.0** | ~2010+ | RDF, OWL, SPARQL | Semantic/linked data, machine-readable, Big Data |
| **Web3** | present | Blockchain | Decentralized, DeFi, NFT, user-controlled data |

### Architecture Comparison

| Architecture | Tiers | Where Logic Lives | Client Type | Scalability | Complexity |
|---|---|---|---|---|---|
| **Single-tier** | 1 | All on mainframe | Dumb terminal | Low | Low |
| **Two-tier (Fat Client)** | 2 | Pres+App on client; Data on server | Fat client | Medium | Medium |
| **Two-tier (Fat Server)** | 2 | Pres on client; App+Data on server | Thin client | Medium | Medium |
| **Three-tier** | 3 | Separated: client / app server / DB | Thin client | High | High |
| **Web Application** | 3 (special case) | Browser / Web+App server / DB | Browser | High | Medium |

### Key Historical Milestones

| Year | Person/Org | Contribution |
|------|-----------|-------------|
| 1945 | Vannevar Bush | Memex concept — linked information |
| 1963/1965 | Ted Nelson | Coined "hypertext"; Project Xanadu |
| 1962–1968 | Douglas Engelbart | NLS: first mouse, hyperlinks, windows |
| 1983–1987 | Halasz/Moran/Trigg (Xerox) | NoteCards hypertext system |
| 1989–1991 | Tim Berners-Lee (CERN) | World Wide Web proposal + first website |
| 1993 | UIUC | Mosaic browser — popularised the Web |
| 2008 | Google | Chrome browser |

## Questions

1. How did early hypertext systems such as Memex, Project Xanadu, NLS, and NoteCards anticipate ideas that later became central to the Web?
2. Why was Tim Berners-Lee's World Wide Web successful compared with earlier hypertext systems, especially in relation to the Internet?
3. How did graphical browsers such as Mosaic change the adoption and usability of the Web?
4. How would you compare Web 1.0, Web 2.0, Web 3.0, and Web3 in terms of technologies, users, and data ownership?
5. What is the difference between the Semantic Web idea of Web 3.0 and the blockchain-based idea of Web3?
6. How do the Deep Web and the Dark Web differ, and why is confusing them conceptually misleading?
7. What responsibilities belong to presentation logic, application logic, and data logic in a distributed application?
8. How does load distribution change when moving from single-tier to two-tier and then to three-tier architectures?
9. Why does the fat client variant of two-tier architecture create maintenance problems compared with a thin client architecture?
10. Why are web applications considered a specific case of three-tier architecture?
11. What advantages does the browser provide as a universal thin client for web applications?
12. How does the web application diagram map browsers, web/application servers, and database servers to the three logical layers?
13. How does HTTP fit into the TCP/IP network stack, and why is it described as an application-layer protocol?
14. If a web application becomes slow under load, which tier or layer would you investigate first, and what evidence would guide that decision?
15. How do scalability and implementation complexity trade off across single-tier, two-tier, three-tier, and web application architectures?

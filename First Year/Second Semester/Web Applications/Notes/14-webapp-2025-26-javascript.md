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

![[js-dom-tree.jpg]]

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

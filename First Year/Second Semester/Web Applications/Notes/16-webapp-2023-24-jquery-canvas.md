# jQuery & HTML5 Canvas

## Table of Contents

- [[#jQuery|jQuery]]
  - [[#jQuery Basics|jQuery Basics]]
  - [[#jQuery Objects|jQuery Objects]]
  - [[#Queries and Query Results|Queries and Query Results]]
  - [[#Creating DOM Elements|Creating DOM Elements]]
  - [[#Each() Method|Each() Method]]
  - [[#jQuery Getters and Setters|jQuery Getters and Setters]]
  - [[#Getting and Setting HTML Attributes|Getting and Setting HTML Attributes]]
  - [[#Getting and Setting CSS Attributes|Getting and Setting CSS Attributes]]
  - [[#Getting and Setting CSS Classes|Getting and Setting CSS Classes]]
  - [[#Getting and Setting HTML Form Values|Getting and Setting HTML Form Values]]
  - [[#Getting and Setting Element Content|Getting and Setting Element Content]]
  - [[#Altering the DOM|Altering the DOM]]
  - [[#Handling Events with jQuery|Handling Events with jQuery]]
  - [[#AJAX with jQuery|AJAX with jQuery]]
- [[#HTML5 Canvas|HTML5 Canvas]]
  - [[#The Canvas Element|The Canvas Element]]
  - [[#The Rendering Context|The Rendering Context]]
  - [[#The Canvas Grid|The Canvas Grid]]
  - [[#Drawing Rectangles|Drawing Rectangles]]
  - [[#Drawing Paths|Drawing Paths]]
  - [[#Arcs|Arcs]]
  - [[#Using Images|Using Images]]
  - [[#Saving and Restoring State|Saving and Restoring State]]
  - [[#Transformations|Transformations]]
  - [[#Basic Animations|Basic Animations]]
- [[#Summary Table|Summary Table]]

---

# jQuery

## jQuery Basics

> [!Important] What is jQuery
> **jQuery** is a fast, small, feature-rich *JavaScript* library (jquery.com) that provides a simple, cross-browser-consistent API for:
> - Selecting elements with CSS-style selectors
> - Manipulating the DOM tree
> - Attaching event listeners without fallback code
>
> **Intuition:** "write less, do more" — tasks that need many lines of vanilla JS collapse to single calls.

The library defines a single global function `jQuery()`, aliased as **`$`**.

```javascript
var divs = $("div");  // returns jQuery object wrapping all <div> elements
```

jQuery objects expose many methods that operate on the entire matched set and support **method chaining**:

```javascript
$("p.details").css("background-color", "yellow").show("fast");
```

## jQuery Objects

A **jQuery object** is array-like and carries these properties:

| Property | Description |
|----------|-------------|
| `length` | Number of matched elements |
| `selector` | Selector string used at creation |
| `context` | Second argument to `$()`, or `document` |
| `jquery` | Version string — test for existence to distinguish jQuery objects from plain arrays |

## Queries and Query Results

Passing a CSS selector string to `$()` returns a jQuery object of matched elements.

```javascript
$("body").length   // 1
$("body")[0]       // the raw DOM element
```

Equivalents:

| Array-style | jQuery-style |
|-------------|--------------|
| `.length`   | `.size()` |
| `[i]`       | `.get(i)` |
| —           | `.toArray()` — converts to plain JS array |

## Creating DOM Elements

If the string passed to `$()` starts with `<tag...>`, jQuery interprets it as HTML and creates new DOM nodes:

```javascript
var img = $("<img/>", {
    src: url,
    css: { borderWidth: 5 },
    click: handleClick
});
```

## Each() Method

`each()` iterates over all elements in a jQuery object, similar to `Array.forEach()`:

```javascript
$("li").each(function(index, element) {
    console.log(index, element);
});
```

*(nota: explicit iteration with `each()` is rare — most jQuery methods implicitly operate on the full matched set.)*

---

## jQuery Getters and Setters

> [!Important] Dual-role methods
> jQuery uses **a single method as both getter and setter**:
> - **Setter:** pass a value → sets on *every* element in the set → returns jQuery object (chainable)
> - **Getter:** no value → queries *only the first* element → returns a single value (must be last in chain)
>
> Setters also accept **objects** (set multiple properties at once) or **functions** (compute value dynamically).

### Getting and Setting HTML Attributes

`attr()` — getter and setter for HTML attributes:

```javascript
// setter — single
$("a").attr("href", "allMyHrefsAreTheSameNow.html");

// setter — object form
$("a").attr({
    title: "all titles are the same too!",
    href:  "somethingNew.html"
});

// getter
$("a").attr("href");
```

### Getting and Setting CSS Attributes

`css()` — works like `attr()` but targets inline/computed CSS styles. Querying returns the *computed* value (from stylesheet or inline style).

```javascript
// setter
$("h1").css("fontSize", "100px");
$("h1").css({ fontSize: "100px", color: "red" });

// getter (camelCase or kebab-case both accepted)
$("h1").css("fontSize");
$("h1").css("font-size");
```

### Getting and Setting CSS Classes

| Method | Effect |
|--------|--------|
| `addClass("cls")` | Add class to all matched elements |
| `removeClass("cls")` | Remove class from all matched elements |
| `toggleClass("cls")` | Add if absent, remove if present |
| `hasClass("cls")` | Returns boolean — test only |

```javascript
var h1 = $("h1");
h1.addClass("big");
h1.removeClass("big");
h1.toggleClass("big");
if (h1.hasClass("big")) { ... }
```

### Getting and Setting HTML Form Values

`val()` — queries/sets the `value` attribute of form elements and manages selection state for checkboxes, radio buttons, and `<select>`.

```javascript
// setter with function (trims whitespace from text inputs)
$("input[type=text].tags").val(function(index, value) {
    return value.trim();
});

// getters
var singleValues   = $("#single").val();
var multipleValues = $("#multiple").val();   // array for multi-select
```

### Getting and Setting Element Content

| Method | Getter behaviour | Setter behaviour |
|--------|-----------------|-----------------|
| `text()` | Plain text of *all* descendants of all matched elements | Replaces content as plain text |
| `html()` | HTML content of *first* matched element only | Replaces content as HTML |

---

## Altering the DOM

### Inserting and Replacing Elements

> [!Important] Insertion methods — two directions
> Every insertion operation has two method forms:
> - `$(target).method(content)` — target-first
> - `$(content).method(target)` — content-first (the `*To` / `*After` / `*Before` / `*All` variants)
>
> If content already exists in the DOM it is **moved**; if inserted in multiple places it is **cloned**.

| Operation | `$(target).method(content)` | `$(content).method(target)` |
|-----------|-----------------------------|-----------------------------|
| Insert at end of target | `append()` | `appendTo()` |
| Insert at start of target | `prepend()` | `prependTo()` |
| Insert after target | `after()` | `insertAfter()` |
| Insert before target | `before()` | `insertBefore()` |
| Replace target with content | `replaceWith()` | `replaceAll()` |

> [!Example] Common insertion calls
> ```javascript
> $("#log").append("<br/>" + message);
> $("p").prepend("<b>Hello </b>");
> $("h1").before("<hr/>");
> $("h1").after("<hr/>");
> $("hr").replaceWith("<br/>");
> ```

### Copying Elements

`clone()` — returns a deep copy (element + all descendants) as a jQuery object. Use it when you need to place a copy without moving the original.

> [!Example] clone() usage
> **Before:**
> ```html
> <div class="container">
>   <div class="hello">Hello</div>
>   <div class="goodbye">Goodbye</div>
> </div>
> ```
> **Code:**
> ```javascript
> $(".hello").clone().appendTo(".goodbye");
> ```
> **After:**
> ```html
> <div class="container">
>   <div class="hello">Hello</div>
>   <div class="goodbye">
>     Goodbye
>     <div class="hello">Hello</div>
>   </div>
> </div>
> ```

### Wrapping Elements

| Method | Effect |
|--------|--------|
| `wrap()` | Wraps each matched element individually |
| `wrapInner()` | Wraps the *contents* of each matched element |
| `wrapAll()` | Wraps all matched elements together as a group |

```javascript
$("h1").wrap(document.createElement("i"));
$(".inner").wrapInner("<div class='new'></div>");
$(".inner").wrapAll("<div class='new'></div>");
```

### Deleting Elements

| Method | Effect |
|--------|--------|
| `empty()` | Removes all *children* of matched elements |
| `remove([selector])` | Removes matched elements **and** their event handlers / data |
| `detach()` | Like `remove()` but preserves event handlers / data (for temporary removal + reinsertion) |
| `unwrap()` | Removes the *parent* of each matched element, keeping the element and its siblings |

---

## Handling Events with jQuery

### Simple Event Handler Registration

jQuery provides shortcut methods for all common browser events. Registering on a jQuery set binds the handler to *every* matched element in one call:

```javascript
$("p").click(function() {
    $(this).css("background-color", "gray");
});
```

### Event Handler Registration Methods

Common shortcut methods (full list in slides):

`blur()`, `change()`, `click()`, `dblclick()`, `focus()`, `focusin()`, `focusout()`, `keydown()`, `keypress()`, `keyup()`, `load()`, `mousedown()`, `mouseenter()`, `mouseleave()`, `mousemove()`, `mouseout()`, `mouseover()`, `mouseup()`, `resize()`, `scroll()`, `select()`, `submit()`, `unload()`

### bind() and unbind()

`bind()` registers a handler for a named event type, allowing more advanced options. `$("p").click(f)` and `$("p").bind("click", f)` are equivalent.

Multiple events can be bound at once with a space-separated list:

```javascript
$("a").bind("mouseenter mouseleave", f);
// equivalent shortcut:
$("a").hover(f);
```

`unbind()` deregisters handlers registered via jQuery (not via `addEventListener()`):

```javascript
$("*").unbind();                         // deregister all handlers on all elements
$("a").unbind("mouseover mouseout");     // deregister specific events
```

---

## AJAX with jQuery

> [!Important] Why jQuery AJAX
> Different browsers historically used different AJAX syntax. jQuery provides a unified API that handles cross-browser differences transparently.

### $.ajax()

The core low-level function — all other jQuery AJAX methods build on top of it. Accepts an options object:

```javascript
$.ajax({
    method: "POST",
    url:    "some.jsp",
    data:   { name: "John", location: "Boston" }
}).done(function(msg) {
    alert("Data Saved: " + msg);
});
```

Data passed as an object is automatically serialized to `application/x-www-form-urlencoded`.

### $.get()

HTTP GET request. Returns cached data by design.

```javascript
$.get("test.jsp", { name: "John", time: "2pm" })
    .done(function(data, status) {
        alert("Data Loaded: " + data + "\nStatus: " + status);
    });
```

### $.post()

HTTP POST request — sends data in the request body.

```javascript
$.post("test.jsp", { name: "John", time: "2pm" })
    .done(function(data) {
        alert("Data Loaded: " + data);
    });
```

### $.getScript()

Loads and immediately executes a JavaScript file via GET:

```javascript
$.getScript("ajax/test.js", function(data, textStatus, jqxhr) {
    console.log(data);          // returned data
    console.log(textStatus);    // "success"
    console.log(jqxhr.status);  // 200
});
```

### $.getJSON()

Loads JSON-encoded data via GET and parses it automatically:

```javascript
$.getJSON("ajax/test.json", function(data) {
    var items = [];
    $.each(data, function(key, val) {
        items.push("<li id='" + key + "'>" + val + "</li>");
    });
    $("<ul/>", { "class": "my-new-list", html: items.join("") }).appendTo("body");
});
```

### .load()

Loads HTML from a URL and injects it into matched elements — the simplest AJAX method:

```javascript
$(selector).load(URL, data, callback);
```

| Variant | Example |
|---------|---------|
| Load full page | `$("#result").load("ajax/test.html")` |
| Load fragment | `$("#result").load("ajax/test.html #container")` |
| POST (object data) | `$("#address").load("address.jsp", { zipcode:"02134" })` |

Callback parameters: `responseText`, `statusTxt`, `xhr`.

*(nota: if `data` is an object, POST is used; otherwise GET.)*

---

# HTML5 Canvas

## The Canvas Element

> [!Important] `<canvas>` element
> `<canvas>` provides a **fixed-size bitmap drawing surface** manipulated entirely via JavaScript. It is similar to `<img>` but has no `src` or `alt` attributes.
>
> ```html
> <canvas id="tutorial" width="150" height="150"></canvas>
> ```
>
> - Default size: **300 × 150 px** when width/height omitted
> - CSS can resize the element but scales the bitmap — mismatched aspect ratio causes distortion
> - **Intuition:** think of it as a pixel buffer; JS issues drawing commands, browser rasterizes them.

## The Rendering Context

The canvas is blank initially. To draw, obtain the **rendering context**:

```javascript
var canvas = document.getElementById("tutorial");
if (canvas.getContext) {
    var ctx = canvas.getContext("2d");  // CanvasRenderingContext2D
}
```

> [!Example] Minimal canvas setup
> **Context:** full HTML page initializing a canvas on load
> ```html
> <!DOCTYPE html>
> <html>
>   <head>
>     <script>
>       function draw() {
>         var canvas = document.getElementById("tutorial");
>         if (canvas.getContext) {
>           var ctx = canvas.getContext("2d");
>         }
>       }
>     </script>
>     <style>canvas { border: 1px solid black; }</style>
>   </head>
>   <body onload="draw();">
>     <canvas id="tutorial" width="150" height="150"></canvas>
>   </body>
> </html>
> ```

## The Canvas Grid

![[Figures/slide-051-fig-01.jpg|560]]

- Origin **(0,0)** is at the **top-left** corner
- X increases rightward, Y increases downward
- 1 grid unit = 1 pixel by default
- The grid can be translated, rotated, and scaled via transformation methods

## Drawing Rectangles

`<canvas>` natively supports **only rectangles** as primitive shapes. All other shapes require paths.

| Function | Effect |
|----------|--------|
| `fillRect(x, y, w, h)` | Draws a solid filled rectangle |
| `strokeRect(x, y, w, h)` | Draws a rectangular outline |
| `clearRect(x, y, w, h)` | Clears a rectangle (makes it fully transparent) |

> [!Example] Nested rectangles
> ```javascript
> ctx.fillRect(25, 25, 100, 100);   // black filled square
> ctx.clearRect(45, 45, 60, 60);    // transparent hole inside
> ctx.strokeRect(50, 50, 50, 50);   // outline inside the hole
> ```
> ![[Figures/slide-052-fig-01.jpg|520]]

## Drawing Paths

A **path** is a list of points connected by line segments (straight or curved, any width/color). Paths can be open or closed.

Steps to draw with a path:

1. `beginPath()` — start a new path (clears previous subpaths)
2. Issue drawing commands (`lineTo`, `arc`, etc.)
3. `closePath()` *(optional)* — draws a straight line back to path start
4. `stroke()` — render the outline
5. `fill()` — render the filled interior

### Moving the Pen

`moveTo(x, y)` — repositions the drawing cursor without drawing. Use it after `beginPath()` or to start disconnected subpaths.

> [!Example] Triangle via path
> ```javascript
> ctx.beginPath();
> ctx.moveTo(75, 50);
> ctx.lineTo(100, 75);
> ctx.lineTo(100, 25);
> ctx.fill();
> ```

### Lines

`lineTo(x, y)` — draws a straight line from the current pen position to `(x, y)`. The start is the end of the previous command; use `moveTo()` to change it.

## Arcs

Two methods for drawing arcs and circles:

| Method | Signature | Notes |
|--------|-----------|-------|
| `arc()` | `arc(x, y, radius, startAngle, endAngle, anticlockwise)` | Angles in **radians**, measured from positive x-axis |
| `arcTo()` | `arcTo(x1, y1, x2, y2, radius)` | Arc via two control points, connected to previous point by straight line |

*(nota: `anticlockwise` defaults to `false` — i.e., clockwise.)*

> [!Example] Smiley face with arcs
> ```javascript
> ctx.beginPath();
> ctx.arc(75, 75, 50, 0, Math.PI * 2, true);  // outer circle
> ctx.moveTo(110, 75);
> ctx.arc(75, 75, 35, 0, Math.PI, false);      // mouth (clockwise = smile)
> ctx.moveTo(65, 65);
> ctx.arc(60, 65, 5, 0, Math.PI * 2, true);   // left eye
> ctx.moveTo(95, 65);
> ctx.arc(90, 65, 5, 0, Math.PI * 2, true);   // right eye
> ctx.stroke();
> ```
> ![[Figures/slide-057-fig-01.jpg|500]]

## Using Images

Two-step process:

1. Obtain an `HTMLImageElement` reference (or another canvas, or a URL)
2. Call `drawImage()` to render it

`drawImage(image, x, y)` — draws the image at coordinates `(x, y)`.

> [!Example] Load image then draw path overlay
> ```javascript
> var img = new Image();
> img.onload = function() {
>     ctx.drawImage(img, 0, 0);
>     ctx.beginPath();
>     ctx.moveTo(30, 96);
>     ctx.lineTo(70, 66);
>     ctx.lineTo(103, 76);
>     ctx.lineTo(170, 15);
>     ctx.stroke();
> };
> img.src = 'backdrop.png';
> ```
> ![[Figures/slide-059-fig-01.jpg|540]]

## Saving and Restoring State

> [!Important] Canvas state stack
> Canvas state is managed as a **LIFO stack**:
> - `save()` — pushes current state onto stack
> - `restore()` — pops last saved state and applies it
>
> State includes: transformations (translate/rotate/scale), style attributes, clipping path.
>
> **Intuition:** wrap each isolated drawing operation in `save()` / `restore()` to avoid side effects between draw calls.

## Transformations

### translate()

Moves the canvas origin to a different grid point.

```javascript
ctx.translate(x, y);  // x = horizontal offset, y = vertical offset
```

Best practice: call `save()` before translating, `restore()` after, rather than computing a reverse translation.

### rotate()

Rotates the canvas **clockwise** around the **current origin** by `angle` radians.

```javascript
ctx.rotate(angle);
```

To rotate around a different point: `translate()` to that point first, then `rotate()`.

## Basic Animations

Animation loop steps per frame:

1. **Clear** — `clearRect()` to erase previous frame
2. **Save state** — `save()` if settings change per frame
3. **Draw** — render the new frame
4. **Restore state** — `restore()` if saved

### Controlling an Animation

| Function | Description |
|----------|-------------|
| `setInterval(fn, delay)` | Calls `fn` every `delay` ms — good for autonomous animations |
| `setTimeout(fn, delay)` | Calls `fn` once after `delay` ms — good for event-driven step-forward |
| `requestAnimationFrame(cb)` | Browser calls `cb` before next repaint — preferred for smooth animations |

*(nota: `requestAnimationFrame` is the modern standard — it syncs to display refresh rate and pauses when tab is hidden, saving CPU.)*

---

## Summary Table

### jQuery Methods

| Category | Method(s) | Effect |
|----------|-----------|--------|
| Selection | `$("selector")` | Returns jQuery object of matched elements |
| HTML attributes | `attr(name[, val])` | Get/set HTML attributes |
| CSS styles | `css(prop[, val])` | Get/set CSS properties |
| CSS classes | `addClass`, `removeClass`, `toggleClass`, `hasClass` | Manage class list |
| Form values | `val([v])` | Get/set input value / selection state |
| Content | `text([v])`, `html([v])` | Get/set text or HTML content |
| Insert (target-first) | `append`, `prepend`, `before`, `after`, `replaceWith` | DOM insertion |
| Insert (content-first) | `appendTo`, `prependTo`, `insertBefore`, `insertAfter`, `replaceAll` | DOM insertion |
| Copy / wrap / delete | `clone`, `wrap`, `wrapInner`, `wrapAll`, `empty`, `remove`, `detach`, `unwrap` | DOM manipulation |
| Events | `click`, `bind`, `unbind`, and 20+ shortcuts | Event registration |
| AJAX low-level | `$.ajax(options)` | Full-control HTTP request |
| AJAX shortcuts | `$.get`, `$.post`, `$.getScript`, `$.getJSON` | Common request patterns |
| AJAX inject | `.load(url[, data][, cb])` | Fetch HTML and inject into element |

### Canvas Drawing API

| API | Method | Notes |
|-----|--------|-------|
| Context | `getContext("2d")` | Entry point for all 2D drawing |
| Rectangles | `fillRect`, `strokeRect`, `clearRect` | Only native primitive |
| Paths | `beginPath`, `closePath`, `stroke`, `fill`, `moveTo`, `lineTo` | General shape drawing |
| Arcs | `arc(x,y,r,start,end,ccw)`, `arcTo(x1,y1,x2,y2,r)` | Angles in radians |
| Images | `drawImage(img, x, y)` | Render external image onto canvas |
| State | `save()`, `restore()` | Stack-based state management |
| Transform | `translate(x,y)`, `rotate(angle)` | Coordinate system manipulation |
| Animation | `setInterval`, `setTimeout`, `requestAnimationFrame` | Frame scheduling |

---

## Questions

1. How does the jQuery `$()` function behave differently when it receives a CSS selector, a raw DOM element, or an HTML fragment such as ` $("<p>text</p>")`?
2. What is a jQuery object, and how is it different from a single raw DOM element even when it contains only one matched node?
3. Explain the getter/setter pattern used by methods such as `attr()`, `css()`, `val()`, `text()`, and `html()`. Why do getter calls usually end a jQuery chain?
4. Compare `text()` and `html()`. In which situations is `text()` safer, and when is `html()` necessary?
5. Why are class methods such as `addClass()`, `removeClass()`, and `toggleClass()` often preferable to changing many CSS properties directly with `css()`?
6. Compare target-first insertion methods (`append`, `prepend`, `before`, `after`, `replaceWith`) with content-first methods (`appendTo`, `prependTo`, `insertBefore`, `insertAfter`, `replaceAll`).
7. What is the difference between moving an existing DOM element and copying it with `clone()` before inserting it somewhere else?
8. Compare `empty()`, `remove()`, `detach()`, and `unwrap()`. Which method preserves jQuery data and event handlers, and why can that matter?
9. How does jQuery simplify event registration compared with older cross-browser DOM APIs? Explain the role of shortcuts such as `click()` and lower-level methods such as `bind()` and `unbind()`.
10. Compare `$.ajax()`, `$.get()`, `$.post()`, `$.getScript()`, `$.getJSON()`, and `.load()`. Which one gives the most control, and which ones are shortcuts for common cases?
11. What does it mean that `<canvas>` is a fixed-size bitmap drawing surface? Why can resizing it with CSS distort the drawing?
12. Using the canvas coordinate-system figure, explain where the origin is, how the `x` and `y` axes grow, and why one canvas unit usually corresponds to one pixel.
13. Explain the difference between `fillRect()`, `strokeRect()`, and `clearRect()`. How does the nested-rectangle example illustrate their effects?
14. Describe the normal workflow for drawing custom shapes with paths: `beginPath()`, `moveTo()`, `lineTo()`, `closePath()`, `stroke()`, and `fill()`. Why is `moveTo()` important in the smiley-face example?
15. Why should images be drawn only after `img.onload` fires, and how do `save()`, `restore()`, `translate()`, `rotate()`, and `requestAnimationFrame()` help build clean canvas animations?

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

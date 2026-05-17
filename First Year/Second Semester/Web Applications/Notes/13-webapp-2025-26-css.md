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

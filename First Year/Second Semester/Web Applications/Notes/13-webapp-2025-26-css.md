# CSS — Web Applications 2025-26

## Table of Contents

- [[#Introduction|Introduction]]
  - [[#History|History]]
  - [[#How CSS Works|How CSS Works]]
- [[#Attaching CSS to HTML|Attaching CSS to HTML]]
  - [[#External Style Sheets|External Style Sheets]]
  - [[#Embedded Style Sheets|Embedded Style Sheets]]
  - [[#Inline Styles|Inline Styles]]
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

![[css-html-tree.jpg]]

---

## Attaching CSS to HTML

Three methods, from most to least recommended:

### External Style Sheets

Separate `.css` file linked from `<head>`:

```html
<link rel="stylesheet" type="text/css" href="styles.css" />
```

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

![[css-selectors-1.jpg]]

![[css-selectors-2.jpg]]

![[css-selectors-3.jpg]]

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

---

## Text and Typefaces

### Font Families

Generic families (browser fallbacks):
- `serif` — e.g., Georgia, Times New Roman
- `sans-serif` — e.g., Arial, Verdana
- `monospace` — e.g., Courier New
- `cursive`, `fantasy`

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

![[css-box-model.jpg]]

**Total occupied width:**
```
left-margin + left-border + left-padding + width
+ right-padding + right-border + right-margin
```

> [!Important] Box Model Width Formula
> `width` property = content width only (not including padding/border/margin).
> To include padding/border: `box-sizing: border-box;` makes `width` = content + padding + border.
> **Intuition:** by default, adding padding makes the box *bigger* than `width`. `border-box` is often preferred for predictable layouts.

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

Padding **not inherited**. Adds to total box size (unless `box-sizing: border-box`).

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
| `inline-block` | Inline flow but respects width/height |
| `none` | **Removes element from layout entirely** — no space reserved |

`visibility: hidden` — element invisible but **space preserved** in layout.

> [!Important] display:none vs visibility:hidden
> `display: none` collapses the space; `visibility: hidden` hides but keeps space.
> **Intuition:** `display:none` is like deleting from layout; `visibility:hidden` is like painting it white.

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

![[css-grid-layout.jpg]]

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

Design principle: breakpoints should be determined by **content**, not device sizes. Layout should look good at *any* width — a breakpoint is needed when the design starts to break, not when a specific device appears.

**Mobile-first** is easier: start with simple single-column layout, progressively add columns/features at wider breakpoints.

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
| **Colors** | `rgb()`, `#hex`, `hsl()`, `rgba()`, `hsla()` | RGBA/HSLA for transparency |
| **Box model** | content + padding + border + margin | `box-sizing: border-box` simplifies |
| **Overflow** | `visible/hidden/scroll/auto` | `hidden` clips; `auto` adds scrollbar when needed |
| **display: none** | removes from flow | vs `visibility: hidden` keeps space |
| **position: relative** | offset from normal pos | space preserved |
| **position: absolute** | relative to nearest non-static ancestor | removed from flow |
| **position: fixed** | relative to viewport | stays during scroll |
| **float** | `float: left/right` | use `clear` to stop wrap |
| **Flexbox** | `display: flex` | 1D layout; row or column |
| **Grid** | `display: grid` | 2D layout; `fr` unit |
| **Viewport meta** | `width=device-width, initial-scale=1` | Required for mobile |
| **Media query** | `@media only screen and (min-width: 40em)` | Mobile-first: min-width queries |

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
11. Why does `box-sizing: border-box` make layout calculations more predictable?
12. How do `display: none` and `visibility: hidden` differ in their effect on layout?
13. How do static, relative, absolute, and fixed positioning change an element's relationship to normal flow and its containing block?
14. What problems can floats cause, and how does `clear` or an overflow-based clearfix address them?
15. When would you choose Flexbox, Grid, or a combination of both for page layout?
16. Why does responsive design require the viewport meta tag, media queries, and content-driven breakpoints?
17. How does a mobile-first approach change the structure of CSS compared with starting from a desktop layout?

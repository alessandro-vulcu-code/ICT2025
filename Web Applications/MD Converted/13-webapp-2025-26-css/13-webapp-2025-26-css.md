# 13-webapp-2025-26-css

_Source: `13-webapp-2025-26-css.pdf`_

## Slide 1 - CSS

CSS

Web Applications
Master Degree in Computer Engineering

Master Degree in Cybersecurity
Master Degree in ICT for Internet and Multimedia

Academic Year 2025/2026

Nicola Ferro

Intelligent Interactive Information Access (IIIA) Hub

![Figura 1 dalla slide 1](assets/slide-001-fig-01.jpg)

## Slide 2 - Outline

Outline

Introduction to CSS

Color Property

CSS and Text

The box Model

Floating and Positioning

Responsive Web Design

![Figura 1 dalla slide 2](assets/slide-002-fig-01.jpg)

## Slide 3 - Introduction to CSS

Introduction to CSS

![Figura 1 dalla slide 3](assets/slide-003-fig-01.jpg)

## Slide 4 - How to Make Web Pages Attractive

How to Make Web Pages Attractive

Cascading Style Sheets (CSS) is the W3C standard for defining the presentation
of documents written in HTML.

Presentation, refers to the way the document is displayed or delivered to the user.

CSS allows you to create rules that specify how the content of an element should
appear.

![Figura 1 dalla slide 4](assets/slide-004-fig-01.jpg)

## Slide 5 - Choose your Own Style

Choose your Own Style

“With great power comes great responsibility.”

![Figura 1 dalla slide 5](assets/slide-005-fig-01.jpg)

## Slide 6 - Choose your Own Style

Choose your Own Style

“With great power comes great responsibility.”

![Figura 1 dalla slide 6](assets/slide-006-fig-01.jpg)

## Slide 7 - Choose your Own Style

Choose your Own Style

![Figura 1 dalla slide 7](assets/slide-007-fig-01.jpg)

## Slide 8 - Choose your Own Style

Choose your Own Style

![Figura 1 dalla slide 8](assets/slide-008-fig-01.jpg)

## Slide 9 - Choose your Own Style

Choose your Own Style

![Figura 1 dalla slide 9](assets/slide-009-fig-01.jpg)

## Slide 10 - Choose your Own Style

Choose your Own Style

![Figura 1 dalla slide 10](assets/slide-010-fig-01.jpg)

## Slide 11 - The Benefits of CSS

The Benefits of CSS

Precise type and layout controls. You can achieve print-
like precision using CSS.

Less work. You can change the appearance of an entire
site by editing one style sheet.

Reliable browser support. Every browser in current use
supports CSS.

Example: http://www.csszengarden.com/

![Figura 1 dalla slide 11](assets/slide-011-fig-01.jpg)

## Slide 12 - The Benefits of CSS

The Benefits of CSS

Precise type and layout controls. You can achieve print-
like precision using CSS.

Less work. You can change the appearance of an entire
site by editing one style sheet.

Reliable browser support. Every browser in current use
supports CSS.

Example: http://www.csszengarden.com/

## Slide 13 - CSS History

CSS History

CSS was first proposed by Håkon Wium Lie on October
10, 1994. At the time, Lie was working with Tim Berners-
Lee at CERN.

The CSS 1 specification was completed in 1996. Browser
CSS support was typically incomplete and had many
bugs that prevented CSS from being usefully adopted.

CSS level 2 specification was developed by the W3C and
published as a recommendation in May 1998.

The earliest CSS 3 drafts were published in June 1999.

## Slide 14 - Cascading Style Sheets 3

Cascading Style Sheets 3

![Figura 1 dalla slide 14](assets/slide-014-fig-01.jpg)

## Slide 15 - Thinking Inside the Box

Thinking Inside the Box

The key to understanding how CSS works is to imagine that
there is an invisible box around every HTML element.

CSS allows you to create rules that control the way that each
individual box (and the contents of that box) is presented.

Without CSS for the borders
With CSS

![Figura 1 dalla slide 15](assets/slide-015-fig-01.jpg)

## Slide 16 - Block & Inline Elements: a reminder

Block & Inline Elements: a reminder

Remember that there is a difference between block and inline
elements

Block elements look like they start a new line

Inline elements flow with the text and do not start on a new line
(<b>, <i>, <span>, <img>)

In the example of the previous slide, block elements are shown
with red borders, and inline elements have green borders

Using CSS, we can add borders around any of the boxes
corresponding to the elements, specifying the width and
height, or add a background color

## Slide 17 - Document Structure: a reminder

Document Structure: a reminder

An HTML document can be seen as a tree

html

head
body

title
style
h1
p
p
h2
p
p
p
h2
p
p

meta

em
img
em
em

![Figura 1 dalla slide 17](assets/slide-017-fig-01.jpg)

![Figura 2 dalla slide 17](assets/slide-017-fig-02.jpg)

## Slide 18 - CSS Recipe

CSS Recipe

1. Start with a document that has been marked up in

HTML.

2. Write style rules for how you’d like certain elements to

look.

3. Attach the style rules to the document. When the

browser displays the document, it follows your rules for
rendering elements.

![Figura 1 dalla slide 18](assets/slide-018-fig-01.jpg)

## Slide 19 - Attaching the Style to the Document

Attaching the Style to the Document

There are three ways to apply style information to an
HTML:

External style sheets is a separate, text-only document that
contains a number of style rules. It must be named with the .css
suffix. The .css document is then linked to or imported into one or
more HTML documents.

Embedded style sheets is placed in a document using the style
element, and its rules apply only to that document. The style
element must be placed in the head of the document.

Inline styles, to apply properties and values to a single element
using the style attribute in the element itself.

## Slide 20 - Attaching the Style to the Document

Attaching the Style to the Document

There are three ways to apply style information to an
HTML:

External style sheets is a separate, text-only document that
contains a number of style rules. It must be named with the .css
suffix. The .css document is then linked to or imported into one or
more HTML documents.

Embedded style sheets is placed in a document using the style
element, and its rules apply only to that document. The style
element must be placed in the head of the document.

Inline styles, to apply properties and values to a single element
using the style attribute in the element itself.

![Figura 1 dalla slide 20](assets/slide-020-fig-01.jpg)

## Slide 21 - Attaching the Style to the Document

Attaching the Style to the Document

There are three ways to apply style information to an
HTML:

External style sheets is a separate, text-only document that
contains a number of style rules. It must be named with the .css
suffix. The .css document is then linked to or imported into one or
more HTML documents.

Embedded style sheets is placed in a document using the style
element, and its rules apply only to that document. The style
element must be placed in the head of the document.

Inline styles, to apply properties and values to a single element
using the style attribute in the element itself.

![Figura 1 dalla slide 21](assets/slide-021-fig-01.jpg)

## Slide 22 - External CSS

External CSS

The <link> element can be used in an HTML document to tell
the browser where to find the CSS file used to style the page.

It is an empty element (meaning it does not need a closing tag),
and it lives inside the <head> element.

It should use three attributes:

href: this specifies the path to the CSS file (which is often placed in a
folder called css or styles).

type: this attribute specifies the type of document being linked to. The
value should be text/css.

rel: this specifies the relationship between the HTML page and the file it is
linked to. The value should be stylesheet when linking to a CSS file.

## Slide 23 - External CSS: Example

External CSS: Example

<!DOCTYPE html>
<html>

<head>

<title>Using External CSS</title>
<link href="css/styles.css" type=“text/css"
rel="stylesheet" />
</head>
<body>

<h1>Potatoes</h1>
<p>There are dozens of different potato varieties.
They are usually described as early, second early and
maincrop.
</p>
</body>
</html>

body {
    font-family: arial;
    background-color: rgb(185,179,175);}
h1 {
    color: rgb(255,255,255);}

![Figura 1 dalla slide 23](assets/slide-023-fig-01.jpg)

## Slide 24 - Multiple Style Sheets

Multiple Style Sheets

Some authors take a modular approach to stylesheets,
creating separate stylesheets to control typography,
layout, forms, tables, even different styles for each sub-
section of a site.

There are two ways to add multiple style sheets to a
page:

Your HTML page can link to one style sheet and that stylesheet
can use the @import rule to import other style sheets.

In the HTML you can use a separate <link> element for each style
sheet.

## Slide 25 - Multiple CSS Example 1

Multiple CSS Example 1

<!DOCTYPE html>
<html>

<head>

<title>Multiple Style Sheets - Import</title>
<link rel="stylesheet" type="text/css"
      href="css/styles.css" />

</head>
  <body>

  <!-- HTML page content here -->
  </body>
</html>

@import url("tables.css");
@import url("typography.css");
body {
  color: #666666;
  background-color: #f8f8f8;
  text-align: center;}
#page {
  width: 600px;
  text-align: left;
  margin-left: auto;
  margin-right: auto;
  border: 1px solid #d6d6d6;
  padding: 20px;}
h3 {
  color: #547ca0;}

![Figura 1 dalla slide 25](assets/slide-025-fig-01.jpg)

## Slide 26 - Multiple CSS Example 2

Multiple CSS Example 2

<!DOCTYPE html>
<html>

<head>

<title>Multiple Style Sheets - Link</title>
<link rel="stylesheet" type="text/css"
      href="css/site.css" />

   <link rel="stylesheet" type="text/css"
      href="css/tables.css" />

   <link rel="stylesheet" type="text/css"
      href="css/typography.css" />

</head>
<body>

<!-- HTML page content here -->
</body>
</html>

![Figura 1 dalla slide 26](assets/slide-026-fig-01.jpg)

## Slide 27 - Internal CSS

Internal CSS

CSS rules can be included within an HTML page by placing them
inside a <style> element, which usually sits inside the <head>
element of the page.

The <style> element should use the type attribute to indicate that
the styles are specified in CSS. The value should be text/css.

When building a site with more than one page, you should use an
external CSS style sheet. This:

Allows all pages to use the same style rules (rather than repeating them in
each page).

Keeps the content separate from how the page looks.

Means you can change the styles used across all pages by altering just one
file (rather than each individual page).

## Slide 28 - Internal CSS: Example

Internal CSS: Example

<!DOCTYPE html>
<html>

<head>

<title>Using Internal CSS</title>
<style type="text/css">

body {

font-family: arial;
background-color: rgb(185,179,175);}
h1 {

color: rgb(255,255,255);}
</style>
</head>
<body>

<h1>Potatoes</h1>

<p>There are dozens of different potato varieties. They
are usually described as early, second early and
maincrop.</p>
</body>
</html>

## Slide 29 - Inline Style

Inline Style

<h1 style="color: red">Introduction</h1>

<h1 style="color: red; margin-top:
2em">Introduction</h1>

The style attribute in a HTML element allows you to apply
properties and values to that single element.

Inline styles should be avoided, they are problematic in that
they mix the presentation information with the structural
markup. They also make it more difficult to make changes
because every style attribute must be hunted down in the
source.

## Slide 30 - Write the Rules

Write the Rules

A style sheet is made
up of one or more style
instructions, called
rules or rule sets

They describe how an
element or group of
elements should be
displayed.

Each rule selects an
element and declares
how it should look

![Figura 1 dalla slide 30](assets/slide-030-fig-01.jpg)

## Slide 31 - Selector and Declaration

Selector and Declaration

CSS works by associating rules with HTML elements.

A CSS rule contains two parts: a selector and a
declaration:

Selectors indicate which element the rule applies to.

Declarations indicate how the elements referred to in the selector
should be styled.

Declarations are split into two parts (a property and a value), and
are separated by a colon.

p {

font-family: Arial;}

![Figura 1 dalla slide 31](assets/slide-031-fig-01.jpg)

## Slide 32 - Selector

Selector

h1 { color: green; }

p {

font-size: small;
font-family: sans-serif;
}

In this example h1 and p elements are used as selectors. This

is called an element type selector, and it is the most basic
type of selector. The properties defined for each rule will apply
to every h1 and p element in the document, respectively.

Note: CSS selectors are case sensitive.

![Figura 1 dalla slide 32](assets/slide-032-fig-01.jpg)

## Slide 33 - Declarations

Declarations

p {

font-size: small;
font-family: sans-serif;
}

The declaration is made up of a property/value pair. There
can be more than one declaration in a single rule.

Each declaration must end with a semicolon to keep it
separate from the following declaration.

Values are dependent on the property. Some properties
take length measurements, some take color values, and
others have a predefined list of keywords.

## Slide 34 - CSS Selectors Types

CSS Selectors Types

Selector
Meaning
Example

Universal
Selector

Applies to all the elements
in the document.

*{}
Targets all elements on the
page

Type Selector Matches element names
h1, h2, h3 {}
Targets the <h1>, <h2> and
<h3> elements

Class
Selector

Matches an element whose
class attribute has a value
that matches the one
specified after the period (or
full stop) symbol.

.note {}
Targets any element whose
class attribute has a value of
note
p.note {}

Targets only <p> elements
whose class attribute has a
value of note

![Figura 1 dalla slide 34](assets/slide-034-fig-01.jpg)

## Slide 35 - CSS Selectors Types

CSS Selectors Types

Selector
Meaning
Example

Id Selector
Matches an element whose id
attribute has a value that matches
the one specified after the pound
or hash symbol

#introduction {}
Targets the element whose
id attribute has a value of
introduction

Child
Selector

Matches an element that is a
direct child of another

li>a {}
Targets any <a> elements
that are children of an <li>
element (but not other <a>
elements in the page)

Descendant
Selector

Matches an element that is a
descendent of another specified
element (not just a direct child of
that element)

p a {}
Targets any <a> elements
that sit inside a <p>
element, even if there are
other elements nested
between them

![Figura 1 dalla slide 35](assets/slide-035-fig-01.jpg)

## Slide 36 - CSS Selectors Types

CSS Selectors Types

Selector
Meaning
Example

Matches an element that is
the next sibling of another

Adjacent
Sibling
Selector

h1+p {}
Targets the first <p>
element after any <h1>
element (but not other
<p> elements)

General
Sibling
Selector

Matches an element that is a
sibling of another, although it
does not have to be the
directly preceding element

h1~p {}
If you had two <p>
elements that are
siblings of an <h1>
element, this rule would
apply to both

![Figura 1 dalla slide 36](assets/slide-036-fig-01.jpg)

## Slide 37 - Pseudo Class Selector

Pseudo Class Selector

The browser keeps track of:

Whether a link was already clicked (the color changes);

Whether the cursor is over an element (hover state);

Whether a form element has been checked or disabled;

…

Pseudo-class selectors are used to apply styles to
elements in these states.

Pseudo-class selectors are indicated by the colon (:)
character. They typically go immediately after an element
name, for example: li:first-child.

## Slide 38 - Link Pseudo-Classes

Link Pseudo-Classes

a:link {

color: maroon; }
a:visited {

color: gray; }

Link pseudo-classes are a type of dynamic pseudo-class
because they are applied as the result of the user interacting
with the page rather than something in the markup.

:link, applies a style to unclicked (unvisited) links

:visited, applies a style to links that have already been clicked

![Figura 1 dalla slide 38](assets/slide-038-fig-01.jpg)

## Slide 39 - User Action Pseudo-Classes

User Action Pseudo-Classes

input:focus {

background-color: yellow;}
a:hover {

color: maroon;
background-color: #ffd9d9;}
a:active {

color: red;
background-color: #ffd9d9; }

Another type of dynamic pseudo-class targets element states that result from direct
user actions.

:focus, applies when the element is selected and ready for input;

:hover, applies when the mouse pointer is over the element;

:active, applies when the element (such a link or button) is in the process of
being clicked or tapped.

## Slide 40 - Group Selectors

Group Selectors

h1 { border: 1px solid blue; }

h2 { border: 1px solid blue; }

p { border: 1px solid blue; }

em { border: 1px solid blue; }

img { border: 1px solid blue; }

h1, h2, p, em, img { border: 1px solid blue; }

![Figura 1 dalla slide 40](assets/slide-040-fig-01.jpg)

## Slide 41 - How CSS Rules Cascade

How CSS Rules Cascade

If there are two or more rules that apply to the same element, it is
important to understand which will take precedence.

Specificity: if one selector is more specific than the others, the more
specific rule will take precedence over more general ones.

Last rule: if the two selectors are identical, the latter of the two will take
precedence.

You can add !important after any property value to indicate that it should
be considered more important than other rules that apply to the same
element.

By understanding how CSS rules cascade we can write simpler style
sheets since we can start by creating more generic rules and then
override properties on individual elements that need to appear differently

## Slide 42 - Inheritance Example

Inheritance Example

If you specify the font-family or color properties on the <body> element, they will
apply to most child elements. This is because the value of the font-family property
is inherited by child elements. It saves you from having to apply these properties to
as many elements (and results in simpler style sheets).

The background-color or border properties are not inherited by child elements.

Note that some style sheet properties inherit and others do not. In general,
properties related to the styling of text (font size, color, style) are passed down.
Properties such as borders, margins, backgrounds, and so on, that affect the
boxed area around the element tend not to be passed down (https://www.w3.org/
TR/CSS/#properties).

Any property applied to a specific element will override the inherited values for that
property.

You can force a lot of properties to inherit values from their parent elements by
using inherit for the value of the properties.

## Slide 43 - Inheritance Example

Inheritance Example

If you specify the font-family or color properties on the <body> element, they will
apply to most child elements. This is because the value of the font-family property
is inherited by child elements. It saves you from having to apply these properties to
as many elements (and results in simpler style sheets).

The background-color or border properties are not inherited by child elements.

Note that some style sheet properties inherit and others do not. In general,
properties related to the styling of text (font size, color, style) are passed down.
Properties such as borders, margins, backgrounds, and so on, that affect the
boxed area around the element tend not to be passed down (https://www.w3.org/
TR/CSS/#properties).

Any property applied to a specific element will override the inherited values for that
property.

You can force a lot of properties to inherit values from their parent elements by
using inherit for the value of the properties.

![Figura 1 dalla slide 43](assets/slide-043-fig-01.jpg)

## Slide 44 - Inheritance Example

Inheritance Example

If you specify the font-family or color properties on the <body> element, they will
apply to most child elements. This is because the value of the font-family property
is inherited by child elements. It saves you from having to apply these properties to
as many elements (and results in simpler style sheets).

The background-color or border properties are not inherited by child elements.

Note that some style sheet properties inherit and others do not. In general,
properties related to the styling of text (font size, color, style) are passed down.
Properties such as borders, margins, backgrounds, and so on, that affect the
boxed area around the element tend not to be passed down (https://www.w3.org/
TR/CSS/#properties).

Any property applied to a specific element will override the inherited values for that
property.

You can force a lot of properties to inherit values from their parent elements by
using inherit for the value of the properties.

![Figura 1 dalla slide 44](assets/slide-044-fig-01.jpg)

## Slide 45 - CSS inheritance: Example

CSS inheritance: Example

![Figura 1 dalla slide 45](assets/slide-045-fig-01.jpg)

## Slide 46 - CSS inheritance: Example

CSS inheritance: Example

![Figura 1 dalla slide 46](assets/slide-046-fig-01.jpg)

## Slide 47 - CSS inheritance: Example

CSS inheritance: Example

The tags <h1> and <p> inherited the font family and the
font color.

The padding is not inherited by default (it could very
easily “break” the page).

We used the CSS rule padding:inherit to make it inherited by the
elements of class page.

The background-color specified for the div of class page
is inherited by <h1> and <p>.

![Figura 1 dalla slide 47](assets/slide-047-fig-01.jpg)

## Slide 48 - Style Sheet Hierarchy

Style Sheet Hierarchy

Style information can come from various sources, listed here
from the most general to the more specific. Items lower in the list
will override items above in the list:

Browser default settings

User style settings (set in a browser as a “reader style sheet”)

Linked external style sheet (added with the link element)

Imported style sheets (added with the @import function)

Embedded style sheets (added with the style element)

Inline style information (added with the style attribute in an opening tag)

Any style rule marked !important by the author

Any style rule marked !important by the reader (user)

## Slide 49 - Color

Color

![Figura 1 dalla slide 49](assets/slide-049-fig-01.jpg)

## Slide 50 - Foreground Color

Foreground Color

The color property allows you to specify the color of text
inside an element.

You can specify any color in CSS in one of four ways:

RGB Values

HEX Codes

/* rgb value */
p {

Color Names

HSLA

color: rgb(100,100,90);}
/* hex code */
h2 {
  color: #ee3e80;}
/* color name */
h1 {
  color: DarkCyan;}

![Figura 1 dalla slide 50](assets/slide-050-fig-01.jpg)

## Slide 51 - Background Color

Background Color

CSS treats each HTML element as if it appears in a box,
and the background-color property sets the color of
the background for that box.

The background color is specified in the same three ways
you can specify foreground colors: RGB values, hex
codes, and color names.

If you do not specify a background color, then the
background is transparent.

By default, most browser windows have a white
background.

## Slide 52 - Understanding Color

Understanding Color

Every color on a computer screen is created by mixing amounts of red,
green, and blue. To find the color you desire, it is possible to use a color
picker

Computer monitors are made up of thousands of tiny squares called pixels

When the screen is turned off, it is black because it is not emitting any light.
When lit, each pixel can be a different color, thus creating a picture

The color on every pixel is expressed in terms of a mix of red, green a blue.
The same happens on each display we use

Conventional OLED pixel arrangement vs polychromatic OLED pixel arrangement

![Figura 1 dalla slide 52](assets/slide-052-fig-01.jpg)

## Slide 53 - RGB

RGB

RGB is an additive color model in which red, green, and
blue light are added together to reproduce an array of
colors. The purpose of the model is for sensing,
representation, and display of images in electronic systems

First developed by Sir Isaac Newton. First color circle in
1666

![Figura 1 dalla slide 53](assets/slide-053-fig-01.jpg)

## Slide 54 - RGB

RGB

In CSS it is possible to specify a color as an RGB value, using the formula:
rgb(red, green, blue)

Each parameter defines the intensity of the color, between 0 and 255

The RGB color wheel represents the 3 light sources used to produce colors on a
TV or computer screen

The primary colors are Red, Green, and Blue. The secondary colors are created by
mixing primary colors

![Figura 1 dalla slide 54](assets/slide-054-fig-01.jpg)

## Slide 55 - RGB

RGB

![Figura 1 dalla slide 55](assets/slide-055-fig-01.jpg)

## Slide 56 - Color Names

Color Names

![Figura 1 dalla slide 56](assets/slide-056-fig-01.jpg)

## Slide 57 - CSS3 Opacity

CSS3 Opacity

p.one {
  background-color: rgb(0,0,0);
  opacity: 0.5;}
p.two {
  background-color: rgb(0,0,0);
  background-color: rgba(0,0,0,0.5);}

CSS3 introduces the opacity property which allows you to
specify the opacity of an element and any of its child elements.

The value is a number between 0.0 and 1.0 (0: completely
transparent, 1: normal color).

The CSS3 rgba property allows you to specify a color, just like
you would with an RGB value, but adds a fourth value to indicate
opacity.

## Slide 58 - HEX

HEX

A hexadecimal color is specified in the form #RRGGBB,
where RR (red), GG (green), and BB (blue) are hexadecimal
integers specifying the components of the color.

In CSS a color can be specified in hexadecimal in the form
#rrggbb

The values vary between 00 and ff (same as decimal 0-255)

<h1 style=“background-color:#ff0000;”>Title</h1>

![Figura 1 dalla slide 58](assets/slide-058-fig-01.jpg)

## Slide 59 - HSL Colors

HSL Colors

CSS3 introduces an entirely new and intuitive way to specify
colors using hue, saturation, and lightness values.

Hue represents the color. It is often represented as a color circle where
the angle represents the color. It is near the colloquial idea of color.

Saturation is the amount of gray in a color, is represented as a
percentage. At maximum saturation there would be no gray in the
color. At minimum saturation, the color would be mostly gray (a shade
of gray)

Lightness is the amount of white (lightness) or black (darkness) in a
color, is represented as a percentage. At 100% the color is white, at
0% it is black, at 50% it is normal

Brightness is a different concept: it only adds light, while lightness offers both black
and white

## Slide 60 - HSL Colors

HSL Colors

![Figura 1 dalla slide 60](assets/slide-060-fig-01.jpg)

## Slide 61 - HSL and HSLA

HSL and HSLA

body {

background-color: #C8C8C8;
background-color: hsl(0,0%,78%);}
p{

background-color: #ffffff;
background-color: hsla(0,100%,100%,0.5);}

The hsla color property allows you to specify color

properties using hue, saturation, and lightness, and adds a
fourth value which represents transparency (just like the
rgba property).

![Figura 1 dalla slide 61](assets/slide-061-fig-01.jpg)

## Slide 62 - Contrast

Contrast

:=E

6756

;327C;

1=<B@/AB

1=<B@/AB

1=<B@/AB

When picking foreground and background colors, it is important
to ensure that there is enough contrast for the text to be legible.

Text is harder to read when there is low contrast between
background and foreground colors, and easier to read when there
is higher contrast between background and foreground colors.

If you want people to read a lot of text, too much contrast can
make it harder to read, too. Then, for long spans of text, reducing
the contrast a little bit improves readability.

![Figura 1 dalla slide 62](assets/slide-062-fig-01.jpg)

![Figura 2 dalla slide 62](assets/slide-062-fig-02.jpg)

![Figura 3 dalla slide 62](assets/slide-062-fig-03.jpg)

## Slide 63 - Colors - Useful Links

Colors - Useful Links

http://hslpicker.com/

http://colorbrewer2.org/

https://coolors.co/

https://www.w3schools.com/colors/colors_theory.asp

![Figura 1 dalla slide 63](assets/slide-063-fig-01.jpg)

## Slide 64 - CSS and Text

CSS and Text

![Figura 1 dalla slide 64](assets/slide-064-fig-01.jpg)

## Slide 65 - Typeface Terminology

Typeface Terminology

SERIF Serif fonts have extra details on the ends of the
main strokes of the letters. These details are known as
serifs

In print, serif fonts were traditionally used for long passages of text
because they were considered easier to read

![Figura 1 dalla slide 65](assets/slide-065-fig-01.jpg)

## Slide 66 - Typeface Terminology

Typeface Terminology

SANS-SERIF Sans-serif fonts have straight ends to
letters, and therefore have a much cleaner design.

Screens have a lower resolution than print. So, if the text is small,
sans-serif fonts can be clearer to read

![Figura 1 dalla slide 66](assets/slide-066-fig-01.jpg)

## Slide 67 - Typeface Terminology

Typeface Terminology

MONOSPACE Every letter in a monospace (or fixed-
width) font is the same width. (Non-monospace fonts
have different widths.)

Monospace fonts are commonly used for code because they align
nicely, making the text easier to follow.

![Figura 1 dalla slide 67](assets/slide-067-fig-01.jpg)

## Slide 68 - Typeface Terminology

Typeface Terminology

CURSIVE Cursive fonts either have joining strokes, or other
cursive characteristics, such as handwriting styles

FANTASY These are usually decorative fonts and therefore
often used for titles. They are not designed for long bodies
of text

![Figura 1 dalla slide 68](assets/slide-068-fig-01.jpg)

## Slide 69 - Typeface Terminology

Typeface Terminology

When choosing a typeface, it is important to understand that a browser will usually only
display it if it’s installed on that user’s computer. Browsers are supposed to support at
least one typeface from each of the groups above.

Serif fonts have extra details, sans-serif fonts have a much cleaner design.

As a result, sites often use a small set of typefaces that are installed on most computers.

It is possible to specify more than one typeface and create an order of preference (in
case the user does not have our first choice of typeface installed). This is referred to as
font stack

![Figura 1 dalla slide 69](assets/slide-069-fig-01.jpg)

## Slide 70 - How to specify typefaces

How to specify typefaces

The font-family property allows us to specify the typeface that
should be used for any text inside the elements to which a CSS rule
applies

The value of this property is the name of the typeface we want to use

We can specify a list of fonts separated by commas so that, if the user
does not have our first choice of typeface installed, the browser can try
to use an alternative font from the list

It is also common to end with a generic font name for that type of font

If a font name is made up of more than one word, it should be put in
double quotes

Designers suggest pages usually look better if they use no more than
three typefaces on a page

## Slide 71 - How to specify typefaces

How to specify typefaces

<style type="text/css">

body {

font-family: Georgia, Times, serif;}
h1, h2 {

font-family: Arial, Verdana, sans-serif;}
.credits {

font-family: "Courier New", Courier, monospace;}
</style>
…

<body>

<h1>Briards</h1>
<p class="credits">by Ivy Duckett</p>
<p class="intro">The <a class="breed" href="http://en.wikipedia.org/wiki/
Briard">briard</a>, or berger de brie, is a large breed of dog traditionally used as
a herder and guardian of sheep.</p>

<h2>Breed History</h2>
<p>The briard, which is believed to have originated in France, has been bred
for centuries to herd and to protect sheep. The breed was used by the French Army as
sentries, messengers and to search for wounded soldiers because of its fine sense of
hearing. Briards were used in the First World War almost to the point of extinction.
Currently the population of briards is slowly recovering. Charlemagne, Napoleon,
Thomas Jefferson and Lafayette all owned briards.</p>

</body>
</html>

![Figura 1 dalla slide 71](assets/slide-071-fig-01.jpg)

## Slide 72 - How to specify typefaces

How to specify typefaces

<style type="text/css">

body {

font-family: Georgia, Times, serif;}
h1, h2 {

font-family: Arial, Verdana, sans-serif;}
.credits {

font-family: "Courier New", Courier, monospace;}
</style>
…

<body>

<h1>Briards</h1>
<p class="credits">by Ivy Duckett</p>
<p class="intro">The <a class="breed" href="http://en.wikipedia.org/wiki/
Briard">briard</a>, or berger de brie, is a large breed of dog traditionally used as
a herder and guardian of sheep.</p>

<h2>Breed History</h2>
<p>The briard, which is believed to have originated in France, has been bred
for centuries to herd and to protect sheep. The breed was used by the French Army as
sentries, messengers and to search for wounded soldiers because of its fine sense of
hearing. Briards were used in the First World War almost to the point of extinction.
Currently the population of briards is slowly recovering. Charlemagne, Napoleon,
Thomas Jefferson and Lafayette all owned briards.</p>

</body>
</html>

![Figura 1 dalla slide 72](assets/slide-072-fig-01.jpg)

## Slide 73 - How to specify the size

How to specify the size

The font-size property enables us to specify a size for the
font. There are several ways to specify it. Among them:

pixels commonly used because they allow web designers very
precise control over how much space their text takes up. The
number of pixels is followed by the letters px. Pixels are relative to
the resolution of the screen. If a screen has a lower resolution, the
same type size will appear larger

percentages the default size of text in browsers is 16px. So a
size of 75% would be the equivalent of 12px, and 200% would be
32px

![Figura 1 dalla slide 73](assets/slide-073-fig-01.jpg)

## Slide 74 - Thinking Inside the Box

Thinking Inside the Box

(The box model)

![Figura 1 dalla slide 74](assets/slide-074-fig-01.jpg)

## Slide 75 - The Box Model

The Box Model

According to the box model, every element in a
document generates a box to which different properties
can be applied:

Control the dimensions of your boxes

Create borders around boxes

Set margins and padding for boxes

Show and hide boxes

![Figura 1 dalla slide 75](assets/slide-075-fig-01.jpg)

## Slide 76 - The Element Box

The Element Box

Outer Edge
Inner Edge
Border

Margin Area

Padding Area

Content Area

![Figura 1 dalla slide 76](assets/slide-076-fig-01.jpg)

## Slide 77 - The Box Components

The Box Components

Content area: the core of the element box

Inner edge: the edges of the content area. In real pages, the edge of the content
area would be invisible.

Padding: the padding is the area held between the content area and an optional
border. Padding is optional.

Border: is a line (or stylized line) that surrounds the element and its padding.
Borders are also optional.

Margin: is an optional amount of space added on the outside of the border.
Margins are always transparent, allowing the background of the parent element
to show through.

Outer edge: the outside edges of the margin area. This is the total area the
element takes up on the page, and it includes the width of the content area plus
the total amount of padding, border, and margins applied to the element.

## Slide 78 - Sizing the Content Box

Sizing the Content Box

p{

width: 500px;

height: 150px;

padding: 20px;

border: 2px solid gray;
margin: 20px;
}

The width and height properties are applied to the

content box.

In this example the resulting width of your box will be:

20px+2px+20px+500px width+20px+2px+20px=584pixels

(total visible box 544 pixels).

![Figura 1 dalla slide 78](assets/slide-078-fig-01.jpg)

![Figura 2 dalla slide 78](assets/slide-078-fig-02.jpg)

## Slide 79 - Box Dimensions

Box Dimensions

To specify the size of a box you can use

Pixels: they allow designers to accurately control the box size.

Percentages: the size of the box is relative to the size of the
browser window or, if the box is encased within another box, it is
a percentage of the size of the containing box.

Em: the size of the box is based on the size of text within it.

Designers have started to use percentages and ems
more for measurements as they try to create designs that
are flexible across devices which have different-sized
screens.

## Slide 80 - Specifying Height

Specifying Height

It is less common to specify the height of elements, since it is better to keep the
height calculated automatically allowing the element box to change based on the
font size, user settings, or other factors.

If you do specify a height for an element containing text, be sure to also consider
what happens should the content not fit with the overflow property.

Values of the overflow property:

visible (default) allows the content to hang out over the element box so that it all can be
seen.

hidden: the content that does not fit does not appear beyond the edges of the element’s
content area.

scroll: when scroll is specified, scrollbars are added to the element box to let users scroll
through the content. Be aware that when you set the value to scroll, the scrollbars will always be
there, even if the content fits in the specified height just fine.

auto: allows the browser to decide how to handle overflow. In most cases, scrollbars are
added only when the content doesn’t fit and they are needed.

## Slide 81 - Padding

Padding

The padding property allows you to specify how much space

should appear between the content of an element and its border.

You can specify different values for each side of a box using:

padding-top

padding-right

padding-bottom

padding-left

Or you can use a shorthand, where the values are in clockwise
order: top, right, bottom, left (TRouBLe): padding: 10px 5px
3px 1px;

The value of the padding property is not inherited by child elements.

## Slide 82 - Borders

Borders

According to the CSS specification, if there is no border
style specified, the border does not exist. In other words,
you must always declare the style of the border, or the
other border properties will be ignored.

Border properties are:

border-width (thickness)

border-style

border-color

border (shorthand)

![Figura 1 dalla slide 82](assets/slide-082-fig-01.jpg)

## Slide 83 - Border Width

Border Width

The border-width property is used to control the width of a border. The value
of this property can either be given in pixels or using one of the following values:

thin

medium

thick

You can control the individual size of borders using four separate properties:

border-top-width

border-right-width

border-bottom-width

border-left-width

You can also specify different widths for the four border values in one property
(clockwise order: top, right, bottom, left.): border-width: 2px 1px 1px
2px;

![Figura 1 dalla slide 83](assets/slide-083-fig-01.jpg)

## Slide 84 - Border Style

Border Style

You can control the style of a border using the border-style property. This
property can take the following values:

solid: a single solid line

dotted: a series of square dots

dashed: a series of short lines

double: two solid lines

groove: appears to be carved into the page

ridge: appears to stick out from the page

inset: appears embedded into the page

outset: looks like it is coming out of the screen

hidden / none: no border is shown

You can individually change the styles of different borders using: border-top-
style, border-left-style, border-right-style, border-bottom-
style

![Figura 1 dalla slide 84](assets/slide-084-fig-01.jpg)

## Slide 85 - Border Color

Border Color

You can specify the color of a border using the border-color
property with either RGB values, hex codes, CSS color names, or
HSL values.

It is possible to individually control the colors of the borders on
different sides of a box using:

border-top-color

border-right-color

border-bottom-color

border-left-color

It is also possible to use a shorthand to control all four border colors in
the one property (clockwise order: top, right, bottom, left): border-
color: darkcyan deeppink darkcyan deeppink;

![Figura 1 dalla slide 85](assets/slide-085-fig-01.jpg)

## Slide 86 - Shorthand Border

Shorthand Border

The border property allows you to provide style, width,

and color values in one declaration, one side at a time.

Again, you can specify the appearance of specific sides,
or use the border property to change all four sides at
once.

h1 { border-left: red .5em solid; }

h2 { border-bottom: 1px solid; }
p.example { border: 2px dotted #663; }

![Figura 1 dalla slide 86](assets/slide-086-fig-01.jpg)

## Slide 87 - Rounded Corners

Rounded Corners

You can put rounded corners on elements using the CSS
border-radius property.

There are individual corner properties as well as a border-
radius shorthand.

Circular borders: border-radius: 5px 20px 40px
60px;

Elliptical borders: (horizontal radius and vertical radius):
border-top-right-radius: 100px 50px;

![Figura 1 dalla slide 87](assets/slide-087-fig-01.jpg)

## Slide 88 - Other CSS 3 Borders Properties

Other CSS 3 Borders Properties

border-image: the border-image property applies an image to the border of
any box. It takes a background image and slices it into nine pieces. This
property requires three pieces of information:

The URL of the image;

Where to slice the image;

What to do with the straight edges: (stretch, repeat, round).

box-shadow: the box-shadow property allows you to add a drop shadow
around a box. It must use at least the first of these two values as well as a color:

Horizontal offset: negative values position the shadow to the left of the box.

Vertical offset: negative values position the shadow to the top of the box.

Blur distance: if omitted, the shadow is a solid line like a border.

Spread of shadow: if used, a positive value will cause the shadow to expand in all
directions, and a negative value will make it contract.

Examples: https://www.w3schools.com/cssref/css3_pr_border-image.asp

## Slide 89 - Margin

Margin

p { margin: 20px;}
p#B {

margin-top: 2em;

margin-right: 250px;
margin-bottom: 1em;
margin-left: 4em;}

The margin is an optional amount of space that you can add on the outside of
the border. Margins keep elements from bumping into one another.

The side-specific and shorthand margin properties work like the padding

properties.

ems, pixels, and percentages are the most common ways to specify margins.

Recall that if the width of a box is specified then the margin is added to the
width of the box.

The value of the margin property is not inherited by child elements.

![Figura 1 dalla slide 89](assets/slide-089-fig-01.jpg)

## Slide 90 - Display Roles

Display Roles

The display property defines the type of element box an element
generates in the layout, it is one of the most important CSS
property for controlling layout.

The property specifies if and how an element is displayed.

Every HTML element has a default display value, depending on its
type. For most elements, this default value is block or inline.

The block elements always start on a new line and take the full
width available (they stretch out to the left and right as far as they
can)

An inline element does not start on a new line and only takes up as
much width as necessary

## Slide 91 - Display Roles

Display Roles

In addition to the familiar inline and block display roles, you
can also make elements display as list items or the various
parts of a table.

The W3C discourages the random reassigning of display roles
for HTML elements.

A useful value for the display property is none, which removes
the content from the normal flow entirely (commonly used with
JavaScript). Unlike visibility: hidden, which just
makes the element invisible but holds the space it would have
occupied blank, display: none removes the content, and
the space it would have occupied is closed up.

## Slide 92 - Display Roles

Display Roles

A common example is making inline list elements <li> for
horizontal menus (e.g. for navigation bar)

li {

  display: inline;

}

<p>Display a list of links as a horizontal menu:</p>

<ul>

  <li><a href="/html/default.asp" target="_blank">HTML</a></li>

  <li><a href="/css/default.asp" target="_blank">CSS</a></li>

  <li><a href="/js/default.asp" target="_blank">JavaScript</a></li>

</ul>

![Figura 1 dalla slide 92](assets/slide-092-fig-01.jpg)

![Figura 2 dalla slide 92](assets/slide-092-fig-02.jpg)

## Slide 93 - Display Roles

Display Roles

A common example is making inline list elements <li> for
horizontal menus (e.g. for navigation bar)

li {

  display: inline;

}

<p>Display a list of links as a horizontal menu:</p>

<ul>

  <li><a href="/html/default.asp" target="_blank">HTML</a></li>

  <li><a href="/css/default.asp" target="_blank">CSS</a></li>

  <li><a href="/js/default.asp" target="_blank">JavaScript</a></li>

</ul>

![Figura 1 dalla slide 93](assets/slide-093-fig-01.jpg)

## Slide 94 - Floating and Positioning

Floating and Positioning

![Figura 1 dalla slide 94](assets/slide-094-fig-01.jpg)

## Slide 95 - Normal Flow

Normal Flow

Text elements are laid out from top to bottom in the order
in which they appear in the source, and from left to right.

Block elements stack up on top of one another and fill the
available width of the browser window or other containing
element.

Inline elements and text characters line up next to one
another to fill the block elements.

When the window or containing element is resized, the
block elements expand or contract to the new width, and
the inline content reflows to fit.

## Slide 96 - Normal Flow

Normal Flow

Inline content reflows to fit the width of the block.

Text elements are laid out from top to bottom in the order
in which they appear in the source, and from left to right.

a b c d e f g h i j k l m n o p q r s t u v w x y z

<p>

a b c d e f g h i j k l
m n o p q r s t u v
w x y z

Blocks are layed out in the
order in which they appear in
the source.

<p>

Block elements stack up on top of one another and fill the
available width of the browser window or other containing
element.

<h1>

Each block starts on a new line.

<h1>

<p>

<p>

Inline elements and text characters line up next to one
another to fill the block elements.

<p>

<p>

Blocks fill the available width.

When the window or containing element is resized, the
block elements expand or contract to the new width, and
the inline content reflows to fit.

![Figura 1 dalla slide 96](assets/slide-096-fig-01.jpg)

## Slide 97 - Normal Flow

Normal Flow

The normal flow is the default way in which browsers treat
HTML elements, thus there is no need of a CSS property
to indicate that elements should appear in normal flow.

Anyway, the syntax would be:

position: static;

![Figura 1 dalla slide 97](assets/slide-097-fig-01.jpg)

## Slide 98 - Relative Positioning

Relative Positioning

Relative positioning moves an element in relation to where it would have
been in normal flow: shifting it to the top, right, bottom, or left of where it
would have been placed.

This does not affect the position of surrounding elements; they stay in the
position they would be in in normal flow.

The space it would have occupied is preserved and continues to influence
the layout of surrounding content.

The element can potentially overlap other elements.

![Figura 1 dalla slide 98](assets/slide-098-fig-01.jpg)

## Slide 99 - Relative Positioning

Relative Positioning

Use the properties top, bottom, left, and right to control
the positioning of the element

b {

position: relative;
top: 30px;

left: 60px;
background-color: fuchsia;
}

![Figura 1 dalla slide 99](assets/slide-099-fig-01.jpg)

## Slide 100 - Relative Positioning

Relative Positioning

Use the properties top, bottom, left, and right to control
the positioning of the element

b {

position: relative;
top: 30px;

left: 60px;
background-color: fuchsia;
}

![Figura 1 dalla slide 100](assets/slide-100-fig-01.jpg)

## Slide 101 - Absolute Positioning

Absolute Positioning

Absolute positioning places the element in relation to its
containing element. It is taken out of normal flow,
meaning that it does not affect the position of any
surrounding elements (as they simply ignore the space it
would have taken up).

The element is positioned relative to its nearest containing
block.

b {

position: absolute;
top: 30px;

left: 60px;
background-color: fuchsia;
}

## Slide 102 - Absolute Positioning

Absolute Positioning

Absolute positioning places the element in relation to its
containing element. It is taken out of normal flow,
meaning that it does not affect the position of any
surrounding elements (as they simply ignore the space it
would have taken up).

The element is positioned relative to its nearest containing
block.

b {

position: absolute;
top: 30px;

left: 60px;
background-color: fuchsia;
}

![Figura 1 dalla slide 102](assets/slide-102-fig-01.jpg)

## Slide 103 - Absolute Positioning

Absolute Positioning

![Figura 1 dalla slide 103](assets/slide-103-fig-01.jpg)

![Figura 2 dalla slide 103](assets/slide-103-fig-02.jpg)

## Slide 104 - Absolute Positioning

Absolute Positioning

![Figura 1 dalla slide 104](assets/slide-104-fig-01.jpg)

![Figura 2 dalla slide 104](assets/slide-104-fig-02.jpg)

![Figura 3 dalla slide 104](assets/slide-104-fig-03.jpg)

## Slide 105 - Absolute Positioning

Absolute Positioning

![Figura 1 dalla slide 105](assets/slide-105-fig-01.jpg)

![Figura 2 dalla slide 105](assets/slide-105-fig-02.jpg)

![Figura 3 dalla slide 105](assets/slide-105-fig-03.jpg)

## Slide 106 - Absolute Positioning

Absolute Positioning

![Figura 1 dalla slide 106](assets/slide-106-fig-01.jpg)

![Figura 2 dalla slide 106](assets/slide-106-fig-02.jpg)

![Figura 3 dalla slide 106](assets/slide-106-fig-03.jpg)

![Figura 4 dalla slide 106](assets/slide-106-fig-04.jpg)

## Slide 107 - Absolute Positioning

Absolute Positioning

![Figura 1 dalla slide 107](assets/slide-107-fig-01.jpg)

![Figura 2 dalla slide 107](assets/slide-107-fig-02.jpg)

![Figura 3 dalla slide 107](assets/slide-107-fig-03.jpg)

![Figura 4 dalla slide 107](assets/slide-107-fig-04.jpg)

## Slide 108 - Fixed Positioning

Fixed Positioning

This is a form of absolute positioning that positions

the element in relation to the browser window (viewport),
as opposed to the containing element.

Elements with fixed positioning do not affect the position
of surrounding elements.

Fixed elements are often used for menus that stay in the
same place at the top, bottom, or side of a screen so
they are always available, even when the content scrolls.

position: fixed;

![Figura 1 dalla slide 108](assets/slide-108-fig-01.jpg)

## Slide 109 - Fixed Positioning

Fixed Positioning

This is a form of absolute positioning that positions

the element in relation to the browser window (viewport),
as opposed to the containing element.

Elements with fixed positioning do not affect the position
of surrounding elements.

Fixed elements are often used for menus that stay in the
same place at the top, bottom, or side of a screen so
they are always available, even when the content scrolls.

position: fixed;

![Figura 1 dalla slide 109](assets/slide-109-fig-01.jpg)

## Slide 110 - Fixed Positioning

Fixed Positioning

![Figura 1 dalla slide 110](assets/slide-110-fig-01.jpg)

![Figura 2 dalla slide 110](assets/slide-110-fig-02.jpg)

![Figura 3 dalla slide 110](assets/slide-110-fig-03.jpg)

## Slide 111 - Floating

Floating

img {

float: right; }

The float property moves an element as far as possible

to the left or right, allowing the following content to wrap
around it.

Floats are one of the primary tools of modern CSS-
based web design, used to create multicolumn layouts,
navigation toolbars, and table-like alignment without
tables.

## Slide 112 - Key Behaviors of Floating Elements

Key Behaviors of Floating Elements

A floated element is like an island in a stream: they are not
in the flow, but the stream has to flow around them. This
behavior is unique to floated elements.

Floats stay in the content area of the containing element: it
is also important to note that the floated element is placed
within the content area (the inner edges) of the element
that contains it. It does not extend into the padding area.

Margins are maintained: in addition, margins are held on
all sides of the floated element. In other words, the entire
element box, from outer edge to outer edge, is floated.

## Slide 113 - Key Behaviors of Floating Elements

Key Behaviors of Floating Elements

A floated element is like an island in a stream: they are not
in the flow, but the stream has to flow around them. This
behavior is unique to floated elements.

Floats stay in the content area of the containing element: it
is also important to note that the floated element is placed
within the content area (the inner edges) of the element
that contains it. It does not extend into the padding area.

Margins are maintained: in addition, margins are held on
all sides of the floated element. In other words, the entire
element box, from outer edge to outer edge, is floated.

![Figura 1 dalla slide 113](assets/slide-113-fig-01.jpg)

## Slide 114 - Floating Block Elements

Floating Block Elements

You must provide a width for floated block elements: If
you do not provide a width value, the width of the floated
block will be set to auto, which fills the available width of
the browser window or other containing element.

Elements do not float higher than their reference in the
source: a floated block will float to the left or right relative
to where it occurs in the source, allowing the following
elements in the flow to wrap around it. It will stay below
any block elements that precede it in the flow (in effect, it
is “blocked” by them).

## Slide 115 - Side by Side Element

Side by Side Element

The float property is commonly used to place boxes next to
each other.

When elements are floated, the height of the boxes can affect
where the following elements sit.

body {

width: 750px;
font-family: Arial, Verdana, sans-serif;
color: #665544;}
p {

width: 230px;
float: left;
margin: 5px;
padding: 5px;
background-color: #efefef;}

## Slide 116 - Side by Side Element

Side by Side Element

<!DOCTYPE html>¬
<html>¬

<head>¬

<title>Ili Pika</title>¬
<link href="style-1.css" type="text/css" rel="stylesheet" />¬
</head>¬
<body>¬

<div>¬

<h1>Ili Pika</h1>¬
</div>¬
<div>¬

<p>The Ili pika is a species of mammal in the family Ochotonidae,
endemic to northwest China. </p>¬

<p>After its discovery in 1983, it was not documented again until
2014. Its population is declining due to largely unknown causes, and it is
currently considered to be endangered, with approximately less than 1,000
left.</p>¬

<p>The Ili pika somewhat resembles a short-eared rabbit. </p>¬
<p>It has brightly colored hair and displays large rusty-red spots
on forehead, crown, and the sides of the neck. </p>¬

<p>It is endemic to the Tian Shan mountains of northwest Chinese
province Xinjiang. A recent census indicated that the Ili pika may have been
extirpated from the Jilimalale and Hutubi South Mountains.</p>¬

<p>The Ili pika inhabits talus areas on high cliff faces. This
species constructs haypiles and is a generalized herbivore.</p>¬

</div>¬
</body>¬
</html>

![Figura 1 dalla slide 116](assets/slide-116-fig-01.jpg)

## Slide 117 - Side by Side Element

Side by Side Element

<!DOCTYPE html>¬
<html>¬

<head>¬

<title>Ili Pika</title>¬
<link href="style-1.css" type="text/css" rel="stylesheet" />¬
</head>¬
<body>¬

<div>¬

<h1>Ili Pika</h1>¬
</div>¬
<div>¬

<p>The Ili pika is a species of mammal in the family Ochotonidae,
endemic to northwest China. </p>¬

<p>After its discovery in 1983, it was not documented again until
2014. Its population is declining due to largely unknown causes, and it is
currently considered to be endangered, with approximately less than 1,000
left.</p>¬

<p>The Ili pika somewhat resembles a short-eared rabbit. </p>¬
<p>It has brightly colored hair and displays large rusty-red spots
on forehead, crown, and the sides of the neck. </p>¬

<p>It is endemic to the Tian Shan mountains of northwest Chinese
province Xinjiang. A recent census indicated that the Ili pika may have been
extirpated from the Jilimalale and Hutubi South Mountains.</p>¬

<p>The Ili pika inhabits talus areas on high cliff faces. This
species constructs haypiles and is a generalized herbivore.</p>¬

</div>¬
</body>¬
</html>

![Figura 1 dalla slide 117](assets/slide-117-fig-01.jpg)

## Slide 118 - Side by Side Element

Side by Side Element

<!DOCTYPE html>¬
<html>¬

<head>¬

<title>Ili Pika</title>¬
<link href="style-1.css" type="text/css" rel="stylesheet" />¬
</head>¬
<body>¬

<div>¬

<h1>Ili Pika</h1>¬
</div>¬
<div>¬

<p>The Ili pika is a species of mammal in the family Ochotonidae,
endemic to northwest China. </p>¬

<p>After its discovery in 1983, it was not documented again until
2014. Its population is declining due to largely unknown causes, and it is
currently considered to be endangered, with approximately less than 1,000
left.</p>¬

<p>The Ili pika somewhat resembles a short-eared rabbit. </p>¬
<p>It has brightly colored hair and displays large rusty-red spots
on forehead, crown, and the sides of the neck. </p>¬

<p>It is endemic to the Tian Shan mountains of northwest Chinese
province Xinjiang. A recent census indicated that the Ili pika may have been
extirpated from the Jilimalale and Hutubi South Mountains.</p>¬

<p>The Ili pika inhabits talus areas on high cliff faces. This
species constructs haypiles and is a generalized herbivore.</p>¬

</div>¬
</body>¬
</html>

![Figura 1 dalla slide 118](assets/slide-118-fig-01.jpg)

## Slide 119 - Clearing Floated Elements

Clearing Floated Elements

Applying the clear property to an element prevents it from
appearing next to a floated element and forces it to start
against the next available “clear” space below the float.

left: the left-hand side of the box should not touch any other
elements appearing in the same containing element.

right: the right-hand side of the box will not touch elements
appearing in the same containing element.

both: neither the left nor right-hand sides of the box will touch
elements appearing in the same containing element.

none: elements can touch either side.

.clear { clear: left;}

![Figura 1 dalla slide 119](assets/slide-119-fig-01.jpg)

## Slide 120 - Clearing Floated Elements

Clearing Floated Elements

<!DOCTYPE html>¬
<html>¬

<head>¬

<title>Ili Pika</title>¬
<link href="style-2.css" type="text/css" rel="stylesheet" />¬
</head>¬
<body>¬

<div>¬

<h1>Ili Pika</h1>¬
</div>¬
<div>¬

<p>The Ili pika is a species of mammal in the family Ochotonidae,
endemic to northwest China. </p>¬

<p>After its discovery in 1983, it was not documented again until
2014. Its population is declining due to largely unknown causes, and it is
currently considered to be endangered, with approximately less than 1,000
left.</p>¬

<p>The Ili pika somewhat resembles a short-eared rabbit. </p>¬
<p class = "clear">It has brightly colored hair and displays large
rusty-red spots on forehead, crown, and the sides of the neck. </p>¬

<p>It is endemic to the Tian Shan mountains of northwest Chinese
province Xinjiang. A recent census indicated that the Ili pika may have been
extirpated from the Jilimalale and Hutubi South Mountains.</p>¬

<p>The Ili pika inhabits talus areas on high cliff faces. This
species constructs haypiles and is a generalized herbivore.</p>¬

</div>¬
</body>¬
</html>

![Figura 1 dalla slide 120](assets/slide-120-fig-01.jpg)

## Slide 121 - Clearing Floated Elements

Clearing Floated Elements

<!DOCTYPE html>¬
<html>¬

<head>¬

<title>Ili Pika</title>¬
<link href="style-2.css" type="text/css" rel="stylesheet" />¬
</head>¬
<body>¬

<div>¬

<h1>Ili Pika</h1>¬
</div>¬
<div>¬

<p>The Ili pika is a species of mammal in the family Ochotonidae,
endemic to northwest China. </p>¬

<p>After its discovery in 1983, it was not documented again until
2014. Its population is declining due to largely unknown causes, and it is
currently considered to be endangered, with approximately less than 1,000
left.</p>¬

<p>The Ili pika somewhat resembles a short-eared rabbit. </p>¬
<p class = "clear">It has brightly colored hair and displays large
rusty-red spots on forehead, crown, and the sides of the neck. </p>¬

<p>It is endemic to the Tian Shan mountains of northwest Chinese
province Xinjiang. A recent census indicated that the Ili pika may have been
extirpated from the Jilimalale and Hutubi South Mountains.</p>¬

<p>The Ili pika inhabits talus areas on high cliff faces. This
species constructs haypiles and is a generalized herbivore.</p>¬

</div>¬
</body>¬
</html>

![Figura 1 dalla slide 121](assets/slide-121-fig-01.jpg)

## Slide 122 - Clearing Floated Elements

Clearing Floated Elements

![Figura 1 dalla slide 122](assets/slide-122-fig-01.jpg)

![Figura 2 dalla slide 122](assets/slide-122-fig-02.jpg)

## Slide 123 - Clearing Floated Elements

Clearing Floated Elements

![Figura 1 dalla slide 123](assets/slide-123-fig-01.jpg)

## Slide 124 - Parent of Floated Elements

Parent of Floated Elements

If a containing element only contains floated elements,
some browsers will treat it as if it is zero pixels tall.

The CSS solution adds two CSS rules to the containing
element:

The overflow property is given a value auto.

The width property is set to 100%.

div.float_container {
  border: 1px solid #665544;
  overflow: auto;
  width: 100%;}

## Slide 125 - Parent of Floated Elements

Parent of Floated Elements

<!DOCTYPE html>¬
<html>¬

<head>¬

<title>Ili Pika</title>¬
<link href="style-3.css" type="text/css" rel="stylesheet" />¬
</head>¬
<body>¬

<div>¬

<h1>Ili Pika</h1>¬
</div>¬
<div class = "float_container">¬

<p>The Ili pika is a species of mammal in the family Ochotonidae,
endemic to northwest China. </p>¬

<p>After its discovery in 1983, it was not documented again until
2014. Its population is declining due to largely unknown causes, and it is
currently considered to be endangered, with approximately less than 1,000
left.</p>¬

<p>The Ili pika somewhat resembles a short-eared rabbit. </p>¬
<p class = "clear">It has brightly colored hair and displays large
rusty-red spots on forehead, crown, and the sides of the neck. </p>¬

<p>It is endemic to the Tian Shan mountains of northwest Chinese
province Xinjiang. A recent census indicated that the Ili pika may have been
extirpated from the Jilimalale and Hutubi South Mountains.</p>¬

<p>The Ili pika inhabits talus areas on high cliff faces. This
species constructs haypiles and is a generalized herbivore.</p>¬

</div>¬
</body>¬
</html>

![Figura 1 dalla slide 125](assets/slide-125-fig-01.jpg)

## Slide 126 - Parent of Floated Elements

Parent of Floated Elements

<!DOCTYPE html>¬
<html>¬

<head>¬

<title>Ili Pika</title>¬
<link href="style-3.css" type="text/css" rel="stylesheet" />¬
</head>¬
<body>¬

<div>¬

<h1>Ili Pika</h1>¬
</div>¬
<div class = "float_container">¬

<p>The Ili pika is a species of mammal in the family Ochotonidae,
endemic to northwest China. </p>¬

<p>After its discovery in 1983, it was not documented again until
2014. Its population is declining due to largely unknown causes, and it is
currently considered to be endangered, with approximately less than 1,000
left.</p>¬

<p>The Ili pika somewhat resembles a short-eared rabbit. </p>¬
<p class = "clear">It has brightly colored hair and displays large
rusty-red spots on forehead, crown, and the sides of the neck. </p>¬

<p>It is endemic to the Tian Shan mountains of northwest Chinese
province Xinjiang. A recent census indicated that the Ili pika may have been
extirpated from the Jilimalale and Hutubi South Mountains.</p>¬

<p>The Ili pika inhabits talus areas on high cliff faces. This
species constructs haypiles and is a generalized herbivore.</p>¬

</div>¬
</body>¬
</html>

![Figura 1 dalla slide 126](assets/slide-126-fig-01.jpg)

## Slide 127 - Fixed Width Layout

Fixed Width Layout

Fixed width layout designs do not change size as the user
increases or decreases the size of their browser window.
Measurements tend to be given in pixels.

Disadvantages

Advantages

Pixel values are accurate at
controlling size and positioning
of elements.

If the user's screen is a much
higher resolution than the
designer's screen, the page
can look smaller and text can
be harder to read.

Great control over the
appearance and position of
items.

You can end up with big gaps
around the edge of a page.

![Figura 1 dalla slide 127](assets/slide-127-fig-01.jpg)

## Slide 128 - Liquid Layout

Liquid Layout

Liquid layout designs stretch and contract as the user
increases or decreases the size of their browser window. They
tend to use percentages.

Disadvantages

Advantages

If you do not control the width of
sections of the page then the design
can look very different than you
intended.

Pages expand to fill the entire
browser window so there are no
spaces around the page on a large
screen.

If the user has a wide window, lines of
text can become very long.

If the user has a small window, the
page can contract to fit it.

The design is tolerant of users
setting.

If the user has a very narrow window,
you can end up with few words on
each line.

![Figura 1 dalla slide 128](assets/slide-128-fig-01.jpg)

## Slide 129 - Flexbox Layout

Flexbox Layout

Flexbox (Flexible Box Layout) serves for arranging elements
either in rows or columns (not both), so a one-dimensional
layout

A Flexbox always consists of:

a Flex Container - the parent (container) <div> element

The flex container becomes flexible by setting the display property to flex.

The CSS properties we can use for the flex container are: flex-direction,
flex-wrap, flex-flow, justify-content, align-items, align-
content

Flex Items - the items inside the container <div>

The CSS properties we can use for flex items are: order, flex-grow, flex-
shrink, flex-basis, flex, align-self

## Slide 130 - Flexbox Example

Flexbox Example

.flex-container {
  display: flex;
  flex-direction: column-reverse;
}
p {

width: 230px;
margin: 5px;
padding: 5px;
background-color: #efefef;}

## Slide 131 - Grid Layout

Grid Layout

A Grid Layout offers a grid-based layout system, with both
rows and columns, so a two-dimensional layout

A Grid Layout always consists of:

a Grid Container - the parent (container) <div> element

The flex container becomes flexible by setting the display property

to grid or inline-grid.

The CSS properties we can use for the grid container are: grid-template-

columns, grid-template-rows, justify-content, align-items, align-
content

Grid Items - the items inside the container <div>

The CSS properties we can use for grid items are: grid-column-start, grid-

column-end, grid-row-start, grid-row-end, justify-self, align-
self

## Slide 132 - Grid Layout Example

Grid Layout Example

.grid-container {
  display: grid;
  grid-template-columns: 1fr 2fr auto;
  grid-template-rows: 2fr 1fr;
}

p {

width: 230px;
margin: 5px;
padding: 5px;
background-color: #efefef;}

![Figura 1 dalla slide 132](assets/slide-132-fig-01.jpg)

## Slide 133 - Grid Layout Example

Grid Layout Example

.grid-container {
  display: grid;
  grid-template-columns: 1fr 2fr auto;
  grid-template-rows: 2fr 1fr;
}

p {

width: 230px;
margin: 5px;
padding: 5px;
background-color: #efefef;}

![Figura 1 dalla slide 133](assets/slide-133-fig-01.jpg)

## Slide 134 - Responsive Web Design

Responsive Web Design

![Figura 1 dalla slide 134](assets/slide-134-fig-01.jpg)

## Slide 135 - History of Web Design

History of Web Design

Up until the last few years, websites were designed so they would
look well on the most common sizes of desktop and laptop screens.

Early 2000s, ideas of fluid design and liquid layout: these techniques
used percentage-based widths to allow a web page’s design to flow
to fit the width of the screen, so it could take advantage of the
available space on wider screens.

When mobile phones with Internet access first became available the
easiest solution was to simply make separate mobile websites with a
fixed page width that would fit on small screen.

As more and more device sizes arrived on the market, it was no
longer sustainable to create separate websites for every possible
screen size.

## Slide 136 - Introduction of Media Queries

Introduction of Media Queries

Without having to create separate sites, how can a website be
displayed with different layouts both on narrow and wide screens?
Media queries.

The CSS @media rule allows you to display different CSS styles
based on device qualities without affecting the HTML.

CSS3 proposed a detailed specification for media queries which
includes precise queries based on media (device) features, such as
width, height, orientation, resolution, and color capability.

Media queries can rearrange your layout, but responsive design
wouldn’t work without a flexibility: this means that every horizontal
measurement on your site needs to be in flexible units (ems or
percentage) rather than inflexible pixels.

![Figura 1 dalla slide 136](assets/slide-136-fig-01.jpg)

## Slide 137 - Introduction of Media Queries

Introduction of Media Queries

Example: change the font size of an element on different
screen sizes

![Figura 1 dalla slide 137](assets/slide-137-fig-01.jpg)

## Slide 138 - Introduction of Media Queries

Introduction of Media Queries

Example: change the font size of an element on different
screen sizes

![Figura 1 dalla slide 138](assets/slide-138-fig-01.jpg)

## Slide 139 - Why Responsive Design?

Why Responsive Design?

Getting the right design on every device, you don’t run
the risk that users will be viewing the mobile version of a
site on their desktop monitors, or vice versa.

Less work, you only have to create one website, one
design, one set of code, and one set of content.

Optimized for search, a separate mobile site, with a
separate set of URLs, can create issues with your site’s
placement in search results.

![Figura 1 dalla slide 139](assets/slide-139-fig-01.jpg)

## Slide 140 - Viewport

Viewport

The viewport meta element is the key to making a
responsive site work.

Viewport: area on the computer or device screen where you
are viewing a web page.

Desktop viewport: browser window without the menus,
toolbars, scrollbar, and everything else that’s part of the
browser itself.

Mobile viewport: the viewport width is the same as the
screen width.

The viewport is different from the screen size.

## Slide 141 - Viewport

Viewport

The viewport meta element is the key to making a
responsive site work.

Viewport: area on the computer or device screen where you
are viewing a web page.

Desktop viewport: browser window without the menus,
toolbars, scrollbar, and everything else that’s part of the
browser itself.

Mobile viewport: the viewport width is the same as the
screen width.

The viewport is different from the screen size.

![Figura 1 dalla slide 141](assets/slide-141-fig-01.jpg)

## Slide 142 - Viewport

Viewport

<meta name="viewport" content="width=device-
width, initial-scale=1">

width attribute tells the browser how to scale the web page, for

a responsive site, the value width=device-width tells the

browser to render the page at full size, whatever the size may be .

The initial-scale attribute tells the browser how to scale the

web page when it’s first loaded on the screen (the zoom factor).

Using the value initial-scale=1 means that the page will be

rendered at the size determined by the width attribute, and will not
be zoomed in or out.

## Slide 143 - Media Queries

Media Queries

CSS media queries allow you to apply different style
declarations based on qualities of the device the website
is being viewed on, most commonly the width of the
viewport.

Sort of if/then statement.

body { background-color: green; }

@media only screen and (min-width: 40em) {

body { background-color: blue; }
}

## Slide 144 - Media Queries

Media Queries

The @media rule is used in media queries to apply different
styles for different media types/devices.

They are a popular technique for delivering a tailored style
sheet (thus achieving responsive web design) to desktops,
laptops, tablets, mobile phones etc.

It is possible also to specify that certain styles are only for
printed documents, or for screen readers with the media
types: print, screen, speech

On the other hand, media features are used to provide specific
details to media queries, allowing to test for specific features
of the device.

## Slide 145 - Media Query Structure

Media Query Structure

@media not|only mediatype and (mediafeature
and|or|not mediafeature) {

CSS code;
}

Meaning of keywords:

only: prevents older browsers that do not support media queries with media
features from applying the specified styles. It has no effect on modern browsers.

not: inverts the meaning of an entire media query

and: combines a media feature with a media type or other media features

curly braces surround all the CSS that will be applied if the entire media
query is true.

The keywords are optional, but if you use not or only you must specify a
media type

## Slide 146 - Media Query Example

Media Query Example

@media only screen and (min-width: 40em) {

body { background-color: blue; }

p { padding: 5px 5%; }

.example { color: red; }
}

Following the @media are one or more expressions:

only: cause those older browsers to ignore the whole query. It is ignored in

modern browsers.

screen: is the media type.

(min-width: 40em): media feature expression (valid here if screens are

wider than 40em).

curly braces surround all the CSS that will be applied if the entire media
query is true.

![Figura 1 dalla slide 146](assets/slide-146-fig-01.jpg)

## Slide 147 - Media Types

Media Types

The available media types are:

all: default. Used for all the media type devices

print: used for printers

screen: used for computer screens, tables, smart-phones etc.

speech: used for screen-readers that read the page out loud

![Figura 1 dalla slide 147](assets/slide-147-fig-01.jpg)

## Slide 148 - Media Features

Media Features

Examples of media features are:

width: the viewport width.

max-width: maximum width of the display area, such as a browser

window (expression considered true if the width is <= of max-width).

min-width: minimum width of the display area, such as a browser window

(expression considered true if the width is > of min-width).

aspect-ratio: The ratio between the width and the height of the

viewport.

![Figura 1 dalla slide 148](assets/slide-148-fig-01.jpg)

## Slide 149 - Media Features

Media Features

Viewport width and height (width, height);

Screen width and height (device-width, device-

height);

Orientation, landscape or portrait (orientation);

Ratio of the viewport (aspect-ratio);

Ratio of the device screen (device-aspect-ratio);

Resolution of the device screen (resolution).

![Figura 1 dalla slide 149](assets/slide-149-fig-01.jpg)

## Slide 150 - How to Use Media Queries

How to Use Media Queries

There are three possibility to use media queries:

1. Writing media queries inside the stylesheets

2. Tell the browser that the entire stylesheet should

only be applied if a media query is true, and
ignored if the media query is not true.

3. Include a media query as an attribute to the

<style> element in the <head> of a page.

![Figura 1 dalla slide 150](assets/slide-150-fig-01.jpg)

## Slide 151 - How to Use Media Queries

How to Use Media Queries

There are three possibility to use media queries:

1. Writing media queries inside the stylesheets

2. Tell the browser that the entire stylesheet should

only be applied if a media query is true, and
ignored if the media query is not true.

3. Include a media query as an attribute to the

<style> element in the <head> of a page.

![Figura 1 dalla slide 151](assets/slide-151-fig-01.jpg)

## Slide 152 - How to Use Media Queries

How to Use Media Queries

Option 2

<link rel="stylesheet" href="styles/mainstyles.css">
<link rel="stylesheet" href="styles/printstyles.css"
media=“print">
<link rel="stylesheet" href="styles/widerscreen.css"
media="only screen and (min-width: 40em)">

Option 3

<style media="only screen and (min-width: 40em)”>

...
</style>

![Figura 1 dalla slide 152](assets/slide-152-fig-01.jpg)

![Figura 2 dalla slide 152](assets/slide-152-fig-02.jpg)

## Slide 153 - How to Use Media Queries

How to Use Media Queries

Option 2

<link rel="stylesheet" href="styles/mainstyles.css">
<link rel="stylesheet" href="styles/printstyles.css"
media=“print">
<link rel="stylesheet" href="styles/widerscreen.css"
media="only screen and (min-width: 40em)">

Option 3

<style media="only screen and (min-width: 40em)”>

...
</style>

![Figura 1 dalla slide 153](assets/slide-153-fig-01.jpg)

![Figura 2 dalla slide 153](assets/slide-153-fig-02.jpg)

## Slide 154 - Breakpoints

Breakpoints

A breakpoint is the point at which you use a media query
to change the design. It breaks your design into two (or
more) variations.

A design range is the range of screen sizes. Each design
range gets a different variation of the design.

The design needs to look good at any width, not just at
certain points.

![Figura 1 dalla slide 154](assets/slide-154-fig-01.jpg)

## Slide 155 - Breakpoints

Breakpoints

A breakpoint is the point at which you use a media query
to change the design. It breaks your design into two (or
more) variations.

A design range is the range of screen sizes. Each design
range gets a different variation of the design.

The design needs to look good at any width, not just at
certain points.

## Slide 156 - Designing Responsively

Designing Responsively

Progressive enhancement is the idea that you start with the basics,
and add on from there for browsers and devices that can handle
more.

Designing with grids: the design is made up of multiple columns of
equal widths, with equal gutters (margins) between them, and
everything on the page is based around those columns.

Design for small screen first, it is much easier to create a layout and
then make it bigger than it is to make a layout smaller (pages load
faster on smaller devices, you design your media queries to react
when the screen becomes larger)

Examples at https://www.w3schools.com/css/tryit.asp?
filename=tryresponsive_breakpoints

## Slide 157 - Take Away

Take Away

Keep the structure and the presentation separate;

The power of CSS;

Cascading and Inheritance rules.

![Figura 1 dalla slide 157](assets/slide-157-fig-01.jpg)

## Slide 158 - Further Readings

Further Readings

Hart-Davis, G. (2023). Teach Yourself VISUALLY HTML and CSS,
2nd edition. John Wiley & Sons.

Duckett, J. (2011). HTML and CSS: Design and Build Websites.
John Wiley & Sons.

Frain, B. (2012). Responsive Web Design with HTML5 and
CSS3. Packt Publishing Ltd.

Peterson, C. (2014). Learning Responsive Web Design: a
Beginner's Guide. " O'Reilly Media, Inc.".

Robbins, J. N. (2012). Learning Web Design: A Beginner's
Guide to HTML, CSS, JavaScript, and Web Graphics. "O'Reilly
Media, Inc.".

## Slide 159 - Slide 159

![Figura 1 dalla slide 159](assets/slide-159-fig-01.jpg)

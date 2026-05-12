# 11-webapp-2025-26-html5

_Source: `11-webapp-2025-26-html5.pdf`_

## Slide 1 - HTML 5

HTML 5

Web Applications
Master Degree in Computer Engineering

Master Degree in Cybersecurity
Master Degree in ICT for Internet and Multimedia

Academic Year 2025/2026

Nicola Ferro

Intelligent Interactive Information Access (IIIA) Hub

![Figura 1 dalla slide 1](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-001-fig-01.jpg)

## Slide 2 - Outline

Outline

Introduction to HTML

Main Elements

HTML5 New Elements

![Figura 1 dalla slide 2](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-002-fig-01.jpg)

## Slide 3 - Introduction to HTML

Introduction to HTML

![Figura 1 dalla slide 3](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-003-fig-01.jpg)

## Slide 4 - Doctype

Doctype

Each web page should begin with a DOCTYPE declaration
to tell a browser which version of HTML the page is using.

HTML5
<!DOCTYPE html>

HTML 4

<!DOCTYPE html PUBLIC
  "-//W3C//DTD HTML 4.01 Transitional//EN"
  "http://www.w3.org/TR/html4/loose.dtd">

Transitional
XHTML 1.0

<!DOCTYPE html PUBLIC
  "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/
   xhtml1-transitional.dtd">

Strict XHTML
1.0

<!DOCTYPE html PUBLIC
  "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/
   xhtml1-strict.dtd">

![Figura 1 dalla slide 4](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-004-fig-01.jpg)

## Slide 5 - HTML Base Elements

HTML Base Elements

<!DOCTYPE html>

Root element

<html>

<head>

<meta charset="utf-8">

<title>This is the Title of the Page</title>

Shown by the browser on the current tab

</head>

<body>

<h1>This is the body of the Page</h1>

<p>Anything within the body of a web page is displayed

in the main browser window.</p>

</body>

</html>

![Figura 1 dalla slide 5](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-005-fig-01.jpg)

## Slide 6 - HTML Base Elements

HTML Base Elements

![Figura 1 dalla slide 6](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-006-fig-01.jpg)

## Slide 7 - Meta Elements

Meta Elements

<meta charset="utf-8">

The <meta> elements provide information about the document
itself, they can be used to provide all sorts of information.

The <meta> element is an empty element so it does not have a
closing tag.

The meta elements are not displayed by the browser, but are
machine parsable and are usually placed within the head element.

In this example, it specifies the character encoding used in the
document.

## Slide 8 - Meta Elements

Meta Elements

Typically used to specify character set, page description,
keywords, author of the document, and viewport settings (the
viewport is the user’s visible area of a web page, and it varies with
the device)

Metadata is used by browsers (to understand how to display the
content), search engines (by using the specified keywords), and
other web services

<meta name=“keywords” content=“web applications, Unipd”>

<meta name=“author” content=“John Smith”>

<meta http-equiv=“refresh” content=“30”>

![Figura 1 dalla slide 8](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-008-fig-01.jpg)

## Slide 9 - Element Review: Document Structure

Element Review: Document Structure

Element Description

body
Identifies the body of the document that holds the content

head
Identifies the head of the document that contains information
about the document

html
The root element that contains all the other elements

meta
Provides information about the document

title
Gives the page a title

![Figura 1 dalla slide 9](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-009-fig-01.jpg)

![Figura 2 dalla slide 9](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-009-fig-02.jpg)

## Slide 10 - Structural Markup

Structural Markup

A markup that gives information about the structure of a document

It provides information about divisions, titles, sections, paragraphs, or
other aspects of the structure of a document

e.g., the <h1> tag usually changes the formatting on the text it contains, but it
also provides structural information concerning the level of a heading it describes

In HTML4 the <div> and <span> tags were used as generic container elements
to give structure to the page

Some examples of structural elements in HTML5 are: <header>, <footer>,
<nav>, <article>, <section>, <aside>

These tags also carry a semantic meaning, thus they are also semantic markup

Generally speaking, many websites share the same structure: a header,
navigation menu, main content, sidebars, footer

## Slide 11 - Semantic Markup

Semantic Markup

Semantic markup are text elements that are not intended to affect the
structure of your web pages, but they do add extra information to the
pages.

Examples: <h1> indicates the most important heading at the beginning
of the document, <em> indicates where emphasis should be placed, and
<blockquote> indicates that a block of text is a quotation.

Browsers often display the contents of these elements in

a different way.

They should not be used to change the way that the text looks; their
purpose is to describe the content of a web page more accurately.

i.e., you should not use <h1> (or any other HTML tag) because it “looks good” for
your purpose. You should use it because the text contained in the tag has the
importance of a title. For the appearance of that text, we will use CSS

## Slide 12 - Block and Inline Elements

Block and Inline Elements

Browsers show HTML elements in one of two ways:

Block elements always appear on a new line. Examples of block
elements: <h1>, <p>, <ul>, <li>, <div>.

Inline elements sit within a block level element and do not start on
a new line. Examples of inline elements: <a>, <em>, <img>,
<span> elements.

Block Elements
Inline Elements

![Figura 1 dalla slide 12](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-012-fig-01.jpg)

## Slide 13 - Text

Text

![Figura 1 dalla slide 13](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-013-fig-01.jpg)

## Slide 14 - Headings

Headings

<h1>This is a Main Heading</h1>

<h2>This is a Level 2 Heading</h2>

<h3>This is a Level 3 Heading</h3>

<h4>This is a Level 4 Heading</h4>

<h5>This is a Level 5 Heading</h5>

<h6>This is a Level 6 Heading</h6>

![Figura 1 dalla slide 14](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-014-fig-01.jpg)

## Slide 15 - Headings

Headings

<h1>This is a Main Heading</h1>

<h2>This is a Level 2 Heading</h2>

<h3>This is a Level 3 Heading</h3>

<h4>This is a Level 4 Heading</h4>

<h5>This is a Level 5 Heading</h5>

<h6>This is a Level 6 Heading</h6>

![Figura 1 dalla slide 15](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-015-fig-01.jpg)

## Slide 16 - Headings

Headings

HTML has six "levels" of headings: <h1> is used for main headings, <h2> is
used for subheadings, and so on

Browsers display the contents of headings at different sizes. The contents
of an <h1> element is the largest, and the contents of an <h6> element is
the smallest.

Browsers also automatically add some white space (a margin) before and
after a heading (more about margins later in CSS)

The CSS allows you to control the size of text, its color, and the used fonts.

Search engines use headings to index the structure and content of your
web pages, use them with good reason if you want to be correctly retrieved.

Use heading to make headings only, don’t use them to make the text big or
bold.

## Slide 17 - Paragraphs

Paragraphs

A paragraphs is usually a block of text, and always starts on a new
line (it is an example of block element, more on this later).

Defined by the <p> tag.

Browsers automatically add a margin before and after a paragraph.

With HTML, you cannot be sure, or known in advance, how your
HTML will be displayed. Large and small screens and resized
windows will produce different results.

In HTML you cannot change how the text (or other elements) are
displayed by adding extra spaces or extra lines in the HTML code:
the browser will automatically remove any extra spaces and lines
when rendering the page. We will need to use CSS.

## Slide 18 - Paragraph

Paragraph

<p> A paragraph consists of one or more sentences
that form a self-contained unit of discourse. The
start of a paragraph is indicated by a new line.</p>

<p>Text is easier to understand when it is split up
into units of text. For example, a book may have
chapters. Chapters can have subheadings. Under each
heading there will be one or more paragraphs.</p>

Paragraphs may contain text, images, and other inline
elements, but they may not contain headings, lists,
sectioning elements, or any element that typically displays as
a block by default.

## Slide 19 - Paragraph

Paragraph

<p> A paragraph consists of one or more sentences
that form a self-contained unit of discourse. The
start of a paragraph is indicated by a new line.</p>

<p>Text is easier to understand when it is split up
into units of text. For example, a book may have
chapters. Chapters can have subheadings. Under each
heading there will be one or more paragraphs.</p>

Paragraphs may contain text, images, and other inline
elements, but they may not contain headings, lists,
sectioning elements, or any element that typically displays as
a block by default.

![Figura 1 dalla slide 19](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-019-fig-01.jpg)

## Slide 20 - Bold and Italic

Bold and Italic

<p>This is how we make a word appear <b>bold</
b>.</p>

<p>Inside a product description you might see
some <b>key features</b> in bold.</p>

<p>This is how we make a word appear
<i>italic</i>.</p>

<p>It's a potato <i>Solanum teberosum</i>.</p>

<p>Captain Cook sailed to Australia on the
<i>Endeavour</i>.</p>

## Slide 21 - Bold and Italic

Bold and Italic

<p>This is how we make a word appear <b>bold</
b>.</p>

<p>Inside a product description you might see
some <b>key features</b> in bold.</p>

<p>This is how we make a word appear
<i>italic</i>.</p>

<p>It's a potato <i>Solanum teberosum</i>.</p>

<p>Captain Cook sailed to Australia on the
<i>Endeavour</i>.</p>

![Figura 1 dalla slide 21](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-021-fig-01.jpg)

## Slide 22 - Strong and Emphasis

Strong and Emphasis

<p><strong>Beware:</strong> Pickpockets
operate in this area.</p>

<p>This toy has many small pieces and is
<strong>not suitable for children under
five years old</strong>.</p>

<p>I <em>think</em> Ivy was the first.</p>
<p>I think <em>Ivy</em> was the first.</p>
<p>I think Ivy was the <em>first</em>.</p>

![Figura 1 dalla slide 22](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-022-fig-01.jpg)

## Slide 23 - Strong and Emphasis

Strong and Emphasis

<p><strong>Beware:</strong> Pickpockets
operate in this area.</p>

<p>This toy has many small pieces and is
<strong>not suitable for children under
five years old</strong>.</p>

<p>I <em>think</em> Ivy was the first.</p>
<p>I think <em>Ivy</em> was the first.</p>
<p>I think Ivy was the <em>first</em>.</p>

![Figura 1 dalla slide 23](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-023-fig-01.jpg)

## Slide 24 - Line Breaks and Horizontal Rules

Line Breaks and Horizontal Rules

To add a line break inside the middle of a paragraph you can
use the line break tag <br />.

To create a break between themes — such as a change of
topic in a book or a new scene in a play — you can add a
paragraph-level thematic break (horizontal rule) between
sections using the <hr /> tag.

empty elements: do not have any words between an opening
and closing tag.

An empty element usually has only one tag: before the closing
angled bracket of an empty element there will often be a
space and a forward slash character.

## Slide 25 - More Text Elements

More Text Elements

Element
Description

<sup>
Contains characters that should be superscript

<sub>
Contains characters that should be subscript

<blockquote> Used for long quotes that take up an entire paragraph

<q>
Used for short quotes that sit within a paragraph

<abbr>
Used for abbreviations or acronyms, a title attribute on the
opening tag is used to specify the full term

<address>
Contains contact details for the author of the page

<ins>
Shows text that has been inserted into a document

<del>
Show text that has been deleted from a document

<s>
Indicates some text that is no longer accurate or relevant,
but that should not be deleted

![Figura 1 dalla slide 25](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-025-fig-01.jpg)

## Slide 26 - Lists

Lists

![Figura 1 dalla slide 26](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-026-fig-01.jpg)

## Slide 27 - Type of Lists

Type of Lists

HTML provides elements for marking up three types of lists:

Ordered lists: are lists in which the sequence of the items is
important, each item in the list is numbered;

Unordered lists: collections of items that appear in no particular
order, begin with a bullet point, rather than characters that
indicate order;

Description lists: lists that consist of name and value pairs,
including but not limited to terms and definitions.

All list elements (the lists themselves and its items) are displayed as
block elements by default, which means that they start on a new
line and have some space above and below.

## Slide 28 - Ordered List

Ordered List

The ordered list is created with the <ol> element.

Each item in the list is placed between an opening <li> (list
item) tag and a closing </li> tag.

The CSS list-style-type property can be used to change
the bullets and numbers for lists.

<ol>

<li>Chop potatoes into quarters</li>
<li>Simmer in salted water for 15-20 minutes until
tender</li>
<li>Heat milk, butter and nutmeg</li>
<li>Drain potatoes and mash</li>
<li>Mix in the milk mixture</li>
</ol>

## Slide 29 - Ordered List

Ordered List

The ordered list is created with the <ol> element.

Each item in the list is placed between an opening <li> (list
item) tag and a closing </li> tag.

The CSS list-style-type property can be used to change
the bullets and numbers for lists.

<ol>

<li>Chop potatoes into quarters</li>
<li>Simmer in salted water for 15-20 minutes until
tender</li>
<li>Heat milk, butter and nutmeg</li>
<li>Drain potatoes and mash</li>
<li>Mix in the milk mixture</li>
</ol>

## Slide 30 - Unordered List

Unordered List

The unordered list is created with the <ul> element.

Each item in the list is placed between an opening <li> (list
item) tag and a closing </li> tag.

The CSS list-style-type property can be used to change the the
type of bullet points (circles, squares, diamonds and so on).

<ul>

<li>1kg King Edward potatoes</li>
<li>100ml milk</li>
<li>50g salted butter</li>
<li>Freshly grated nutmeg</li>
<li>Salt and pepper to taste</li>
</ul>

## Slide 31 - Unordered List

Unordered List

The unordered list is created with the <ul> element.

Each item in the list is placed between an opening <li> (list
item) tag and a closing </li> tag.

The CSS list-style-type property can be used to change the the
type of bullet points (circles, squares, diamonds and so on).

<ul>

<li>1kg King Edward potatoes</li>
<li>100ml milk</li>
<li>50g salted butter</li>
<li>Freshly grated nutmeg</li>
<li>Salt and pepper to taste</li>
</ul>

![Figura 1 dalla slide 31](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-031-fig-01.jpg)

## Slide 32 - Description List

Description List

The description list is created with the <dl> element. Inside the <dl>
element you will usually see pairs of <dt> and <dd> elements.

<dt> is used to contain the the definition term.

<dd> is used to contain the actual definition.

<dl>

<dt>Sashimi</dt>
<dd>Sliced raw fish that is served with condiments such as shredded
daikon radish or ginger root, wasabi and soy sauce</dd>
<dt>Scale</dt>
<dd>A device used to accurately measure the weight of ingredients</
dd>
<dd>A technique by which the scales are removed from the skin of a
fish</dd>
<dt>Scamorze</dt>
<dt>Scamorzo</dt>
<dd>An Italian cheese usually made from whole cow's milk (although it
was traditionally made from buffalo milk)</dd>
</dl>

## Slide 33 - Description List

Description List

The description list is created with the <dl> element. Inside the <dl>
element you will usually see pairs of <dt> and <dd> elements.

<dt> is used to contain the the definition term.

<dd> is used to contain the actual definition.

<dl>

<dt>Sashimi</dt>
<dd>Sliced raw fish that is served with condiments such as shredded
daikon radish or ginger root, wasabi and soy sauce</dd>
<dt>Scale</dt>
<dd>A device used to accurately measure the weight of ingredients</
dd>
<dd>A technique by which the scales are removed from the skin of a
fish</dd>
<dt>Scamorze</dt>
<dt>Scamorzo</dt>
<dd>An Italian cheese usually made from whole cow's milk (although it
was traditionally made from buffalo milk)</dd>
</dl>

![Figura 1 dalla slide 33](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-033-fig-01.jpg)

## Slide 34 - Nested Lists

Nested Lists

<ol>

You can put a second list inside an
<li> element to create a sub-list or
nested list.

<li></li>
<li>

<ul>

Browsers display nested lists
indented further than the parent list.

<li></li>
<li></li>
<li></li>
</ul>
</li>
</ol>

In nested unordered lists, the
browser will usually change the style
of the bullet point too, while the
numbering style is not changed by
default when you nest ordered lists.

![Figura 1 dalla slide 34](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-034-fig-01.jpg)

## Slide 35 - Links

Links

![Figura 1 dalla slide 35](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-035-fig-01.jpg)

## Slide 36 - Anchor Syntax

Anchor Syntax

Links are the defining feature of the web because they allow
you to move from one web page to another, enabling the
very idea of browsing or surfing

Links are created using the anchor element: <a>

Users can click on anything between the opening <a> tag
and the closing </a> tag. You specify which page you
want to link to using the href attribute.

The text the user clicks on
The linked page

<a href="http://www.imdb.com">IMDB</a>

![Figura 1 dalla slide 36](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-036-fig-01.jpg)

## Slide 37 - Link Text

Link Text

The text between the opening <a> tag and closing </a> tag is
known as link text.

Where possible, your link text should explain where visitors will
be taken if they click on it (rather than just saying "click here”).

Nearly all graphical browsers display linked text as blue and
underlined by default. Visited links are generally displayed in
purple.

If you choose to change your link colors, keep them consistent
throughout your site so as not to confuse your users.

In HTML5, you can put any element in an <a> element, even
block elements.

## Slide 38 - The href Attribute

The href Attribute

The href (hypertext reference) attribute provides the address of
the page or resource (its URL) to the browser.

The URL can point to other HTML documents or to other web
resources, such as images, audio, and video files.

There are two ways to specify the URL:

Absolute URLs provide the full URL for the document, including the
protocol (http://), the domain name, and the pathname as necessary.
Absolute URLs are used when pointing to a document on the Web (i.e.,
not on your own server);

Relative URLs describe the pathname to a file relative to the current
document. Relative URLs can be used when you are linking to another
document on your own site (i.e., on the same server).

## Slide 39 - Email and Telephone Links

Email  and Telephone Links

The <a> element can be used to:

Create a link that starts up the user's email program and
addresses an email to a specified email address, the href
attribute starts with mailto: and is followed by the email address
you want the email to be sent to;

Create a link that dial a phone number, the href attribute starts
with tel: and is followed by the telephone number you want the
email to be sent to.

<a href="mailto:jon@example.org">Email Jon</a>

<a href="tel:+18005551212">Call us free at (800) 555-1212</a>

![Figura 1 dalla slide 39](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-039-fig-01.jpg)

## Slide 40 - Opening Links in a New Window

Opening Links in a New Window

If you want a link to open in a new window, you can use the target
attribute on the opening <a> tag. The value of this attribute should
be _blank.

Link to be opened in a new window are used to point to another
website, to ease the user to return to the source page.

Opening new windows can be problematic:

New windows may be confusing to some users;

new windows may be perceived as an annoyance rather than a convenience.

<a href="http://www.imdb.com" target="_blank"> Internet Movie
Database</a>

![Figura 1 dalla slide 40](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-040-fig-01.jpg)

## Slide 41 - Linking to a Page Fragment

Linking to a Page Fragment

Useful to provide shortcuts to information at the bottom of
a long, scrolling page or for getting back to the top of a
page with just one click or tap.

Two part process:

1. Identifying the destination: use the id attribute (can be used on

every HTML element), the value of the id attribute should start with
a letter or an underscore (not a number or any other character) and
it is has to be unique: it has to appear only once in the document;

2. Linking to the destination: use the <a> element, but the value of the

href attribute starts with the # symbol, followed by the value of the
id attribute of the element you want to link to.

## Slide 42 - Linking to a Page Fragment

Linking to a Page Fragment

<h1 id="top">Film-Making Terms</h1>
<a href="#arc_shot">Arc Shot</a><br />
<a href="#interlude">Interlude</a><br />
<a href="#prologue">Prologue</a><br /><br />
<h2 id="arc_shot">Arc Shot</h2>
<p>A shot in which the subject is photographed by an

encircling or moving camera</p>
<h2 id=“interlude">Interlude</h2>
<p>A brief, intervening film scene or sequence, not

specifically tied to the plot, that appears within a
film</p>
<h2 id=“prologue">Prologue</h2>
<p>A speech, preface, introduction, or brief scene

preceding the the main action or plot of a film;
contrast to epilogue</p>
<p><a href="#top">Top</a></p>

## Slide 43 - Linking to a Fragment in Another Page

Linking to a Fragment in Another Page

To link to a specific part of a different page (whether on
the same site or a different website) a similar technique
can be used.

The href attribute will contain the address for the page,
followed by the # symbol and the value of the id attribute
that is used on the element you are linking to.

<a href=“http://www.htmlandcssbook.com/index.html#bottom”>

![Figura 1 dalla slide 43](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-043-fig-01.jpg)

## Slide 44 - Images

Images

![Figura 1 dalla slide 44](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-044-fig-01.jpg)

## Slide 45 - Adding Images

Adding Images

To add an image into the page you need to use an <img>
element. This is an empty element (which means there is no
closing tag). It must carry the following two attributes:

src: (source) tells the browser where it can find the image file.
This will usually be a relative URL pointing to an image on your
own site.

alt: (alternate text) provides a text description of the image
which describes the image if you cannot see it.

title: provides additional information about the image. Most
browsers will display the content of this attribute in a tooltip
when the user hovers over the image.

## Slide 46 - Adding Images

Adding Images

The <img> element use two other attributes that specify its size:

height: this specifies the height of the image in pixels;

width: this specifies the width of the image in pixels.

It is better to specify the size of images using CSS rather than
HTML.

<img src="figure/quokka.jpg" alt="A family
of quokka" title="The quokka is an
Australian marsupial that is similar in
size to the domestic cat." width="314"
height="315"/>

![Figura 1 dalla slide 46](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-046-fig-01.jpg)

## Slide 47 - Adding Images

Adding Images

The <img> element use two other attributes that specify its size:

height: this specifies the height of the image in pixels;

width: this specifies the width of the image in pixels.

It is better to specify the size of images using CSS rather than
HTML.

<img src="figure/quokka.jpg" alt="A family
of quokka" title="The quokka is an
Australian marsupial that is similar in
size to the domestic cat." width="314"
height="315"/>

![Figura 1 dalla slide 47](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-047-fig-01.jpg)

## Slide 48 - Placing Images

Placing Images

 <img> is an inline element, when the browser window is
resized, the line of images reflows to fill the new width.

Where an image is placed in the code will affect how it is
displayed:

Before a paragraph

Inside the start of a paragraph

In the middle of a paragraph

New websites should use CSS to control the alignment of
images (instead of the align attribute).

![Figura 1 dalla slide 48](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-048-fig-01.jpg)

## Slide 49 - Placing Images

Placing Images

<img src="figure/quokka.jpg" alt="A family of quokka" width="100"
height="100" />

<p>The quokka (Setonix brachyurus), the only member of the genus
Setonix, is a small macropod about the size of a domestic cat. Like
other marsupials in the macropod family (such as kangaroos and
wallabies), the quokka is herbivorous and mainly nocturnal.</p>
<hr />

<p><img src="figure/quokka.jpg" alt="A family of quokka"
width="100" height="100" />The quokka (Setonix brachyurus), the
only member of the genus Setonix, is a small macropod about the
size of a domestic cat. Like other marsupials in the macropod
family (such as kangaroos and wallabies), the quokka is herbivorous
and mainly nocturnal.</p>
<hr />

<p>The quokka (Setonix brachyurus), the only member of the genus
Setonix, is a small macropod about the size of a domestic cat. <img
src="figure/quokka.jpg" alt="A family of quokka" width="100"
height="100" />Like other marsupials in the macropod family (such
as kangaroos and wallabies), the quokka is herbivorous and mainly
nocturnal.</p>

## Slide 50 - Placing Images

Placing Images

<img src="figure/quokka.jpg" alt="A family of quokka" width="100"
height="100" />

<p>The quokka (Setonix brachyurus), the only member of the genus
Setonix, is a small macropod about the size of a domestic cat. Like
other marsupials in the macropod family (such as kangaroos and
wallabies), the quokka is herbivorous and mainly nocturnal.</p>
<hr />

<p><img src="figure/quokka.jpg" alt="A family of quokka"
width="100" height="100" />The quokka (Setonix brachyurus), the
only member of the genus Setonix, is a small macropod about the
size of a domestic cat. Like other marsupials in the macropod
family (such as kangaroos and wallabies), the quokka is herbivorous
and mainly nocturnal.</p>
<hr />

<p>The quokka (Setonix brachyurus), the only member of the genus
Setonix, is a small macropod about the size of a domestic cat. <img
src="figure/quokka.jpg" alt="A family of quokka" width="100"
height="100" />Like other marsupials in the macropod family (such
as kangaroos and wallabies), the quokka is herbivorous and mainly
nocturnal.</p>

![Figura 1 dalla slide 50](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-050-fig-01.jpg)

## Slide 51 - Figure and Figure Caption

Figure and Figure Caption

HTML5 has introduced a new <figure> element to contain images
and their caption <figcaption>.

You can have more than one image inside the <figure> element as
long as they all share the same caption.

Before these elements were created there was no way to
associate an <img> element with its caption.

<figure>

<img src="figure/quokka.jpg" alt="A family of
quokka" width="314" height="315" />
<br />
<figcaption>The quokka is an Australian
marsupial.</figcaption>
</figure>

## Slide 52 - Figure and Figure Caption

Figure and Figure Caption

HTML5 has introduced a new <figure> element to contain images
and their caption <figcaption>.

You can have more than one image inside the <figure> element as
long as they all share the same caption.

Before these elements were created there was no way to
associate an <img> element with its caption.

<figure>

<img src="figure/quokka.jpg" alt="A family of
quokka" width="314" height="315" />
<br />
<figcaption>The quokka is an Australian
marsupial.</figcaption>
</figure>

![Figura 1 dalla slide 52](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-052-fig-01.jpg)

## Slide 53 - Tables

Tables

![Figura 1 dalla slide 53](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-053-fig-01.jpg)

## Slide 54 - Basic Table Structure

Basic Table Structure

The <table> element is used to create a table.

The <tr> (table row) tag indicates the start of each row, and </
tr> indicates the end of the row.

Each cell of a table is represented using <td> and </td> tags
(table data).

The <th> (table header) element is used just like the <td>
element but its purpose is to represent the heading for either a
column or a row.

The scope attribute on the <th> element indicates whether it is a
heading for a column (value equals to col) or a row (value equals
to row).

## Slide 55 - Table Structure

Table Structure

<table>

<tr>

<th></th>
<th scope=“col">Saturday</th>
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

## Slide 56 - Table Structure

Table Structure

<table>

<tr>

<th></th>
<th scope=“col">Saturday</th>
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

## Slide 57 - Other Table Elements and Attributes

Other Table Elements and Attributes

Element
Description

<td>
• colspan="number"
• rowspan="number"

Establishes a cell within a table row
• Number of columns the cell should span
• Number of rows the cell should span

<th>
• colspan="number"
• rowspan="number"
• scope="row|col"

Number of columns the cell should span
• Number of rows the cell should span
• Number of columns the cell should span
• Associates the header with a row or a column

<tbody>
Identifies the table body row group

<tfoot>
Identifies the table footer row group

<thead>
Identifies the table header row group

<caption>
Gives the table a title that displays in the browse

## Slide 58 - Forms

Forms

![Figura 1 dalla slide 58](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-058-fig-01.jpg)

## Slide 59 - Form Controls

Form Controls

Types of form controls:

Adding Text

Submitting Forms

Text input (single line)

Submitting Buttons

Password input

Image Buttons

Text area

Uploading File

Making Choices

File upload

Radio buttons

Checkboxes

Drop-down boxes

![Figura 1 dalla slide 59](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-059-fig-01.jpg)

## Slide 60 - Form Structure

Form Structure

Form controls live inside a <form> element.

The <form> element carries:

action (mandatory): its value is the URL for the page on the server
that will receive the information in the form when it is submitted.

method: forms can be sent using GET or POST (default: GET).

id: its value is used to identify the form distinctly from other
elements on the page.

<form action="http://www.example.com/subscribe.jsp"
method="get" id="subscription">

<p>This is where the form controls will appear.</p>
</form>

![Figura 1 dalla slide 60](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-060-fig-01.jpg)

## Slide 61 - Text Input

Text Input

The <input> element is used to create several different form
controls. The value of the type attribute determines what kind of
input they will be creating:

type=“text”: creates a single-line text input.

type=“password”: creates a text box that acts just like a single-line text input,
except the characters are blocked out.

name: the value of this attribute identifies the form control and is
sent along with the information they enter to the server (to
differentiate between various pieces of inputted data, information is
sent from the browser to the server using name/value pairs).

maxlength: limits the number of characters a user may enter into
the text field.

## Slide 62 - Text Input

Text Input

<form action="http://www.example.com/
login.jsp">

<p>Username:

<input type="text" name="username"
maxlength="30" />
</p>
<p>Password:

<input type="password" name="password"
maxlength="30" />
</p>
</form>

![Figura 1 dalla slide 62](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-062-fig-01.jpg)

## Slide 63 - Text Input

Text Input

<form action="http://www.example.com/
login.jsp">

<p>Username:

<input type="text" name="username"
maxlength="30" />
</p>
<p>Password:

<input type="password" name="password"
maxlength="30" />
</p>
</form>

## Slide 64 - Difference Between Id and Name Attributes

Difference Between Id and Name Attributes

Id Attribute:

Name Attribute:

The name attribute provides the variable
name for the control.

Every HTML element can carry the id
attribute.

The id value must be unique.

The name value do not need to be
unique.

It is used to uniquely identify that
element from other elements on the
page.

When a user enters a comment in a
control field, it would be passed to the
server as a name/value pair.

Useful with CSS and javascript.

All form control elements must include a
name attribute (except submit) so the
form-processing application can sort the
information.

The web application that processes the
data is  programmed to look for specific
variable names.

![Figura 1 dalla slide 64](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-064-fig-01.jpg)

## Slide 65 - Text Area

Text Area

The <textarea> element is used to create a mutli-line

text input.

Unlike other input elements this is not an empty element.

Any text that appears between the opening <textarea> and
closing </textarea> tags will appear in the text box when the
page loads, if the user does not delete it, this message will be
sent to the server along with whatever the user has typed.

<form action="http://www.example.com/comments.jsp">

<p>What did you think of this course?</p>
<textarea name="comments" cols="20" rows="4">Enter
your comments...</textarea>
</form>

## Slide 66 - Text Area

Text Area

The <textarea> element is used to create a mutli-line

text input.

Unlike other input elements this is not an empty element.

Any text that appears between the opening <textarea> and
closing </textarea> tags will appear in the text box when the
page loads, if the user does not delete it, this message will be
sent to the server along with whatever the user has typed.

<form action="http://www.example.com/comments.jsp">

<p>What did you think of this course?</p>
<textarea name="comments" cols="20" rows="4">Enter
your comments...</textarea>
</form>

![Figura 1 dalla slide 66](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-066-fig-01.jpg)

## Slide 67 - Radio Buttons and Checkboxes

Radio Buttons and Checkboxes

Use the <input> element with:

type=“radio”: radio buttons allow users to pick just one of a number of
options.

type=“checkbox”: checkboxes allow users to select (and unselect) one
or more options in answer to a question.

name: the value of the name attribute should be the same for all of the
radio buttons or checkboxes used to answer a question.

value: the value sent to the server for the selected option, the value of
each of the buttons in a group should be different.

checked: the checked attribute can be used to indicate which value (if
any) should be selected when the page loads. The value of this attribute
is checked.

## Slide 68 - Radio Buttons and Checkboxes

Radio Buttons and Checkboxes

<form action=“http://www.example.com/profile.jsp">

<p>Please select your favorite genre:

<br />
<input type="radio" name="genre" value="rock"
checked="checked" /> Rock
<input type="radio" name="genre" value="pop" /> Pop
<input type="radio" name="genre" value="jazz" /> Jazz
</p>
<p>Please select your favorite music service(s):

<br />
<input type="checkbox" name="service" value="itunes"
checked="checked" /> iTunes
<input type="checkbox" name="service"
value="lastfm" /> last.fm
<input type="checkbox" name="service" value="spotify"
/> Spotify
</p>
</form>

## Slide 69 - Radio Buttons and Checkboxes

Radio Buttons and Checkboxes

<form action=“http://www.example.com/profile.jsp">

<p>Please select your favorite genre:

<br />
<input type="radio" name="genre" value="rock"
checked="checked" /> Rock
<input type="radio" name="genre" value="pop" /> Pop
<input type="radio" name="genre" value="jazz" /> Jazz
</p>
<p>Please select your favorite music service(s):

<br />
<input type="checkbox" name="service" value="itunes"
checked="checked" /> iTunes
<input type="checkbox" name="service"
value="lastfm" /> last.fm
<input type="checkbox" name="service" value="spotify"
/> Spotify
</p>
</form>

## Slide 70 - Drop Down List

Drop Down List

The <select> element is used to create a drop down list box
(select box).

It contains two or more <option> elements.

The words between the opening <option> and closing </
option> tags will be shown to the user in the drop down box.

The <option> element uses the value attribute to indicate the
value that is sent to the server along with the name.

The selected attribute can be used to indicate the option that
should be selected when the page loads, otherwise the first
option will be shown.

## Slide 71 - Drop Down List

Drop Down List

<form action="http://www.example.com/
profile.jsp">

<p>What device do you listen to music on?</p>
<select name="devices">

<option value="ipod">iPod</option>
<option value="radio">Radio</option>
<option value="computer">Computer</option>
</select>
</form>

![Figura 1 dalla slide 71](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-071-fig-01.jpg)

## Slide 72 - Drop Down List

Drop Down List

<form action="http://www.example.com/
profile.jsp">

<p>What device do you listen to music on?</p>
<select name="devices">

<option value="ipod">iPod</option>
<option value="radio">Radio</option>
<option value="computer">Computer</option>
</select>
</form>

## Slide 73 - File Input Box and Submit Button

File Input Box and Submit Button

The <input> element with:

type=“file”: allows users to upload files. It creates a box
that looks like a text input followed by a browse button,
that allows the user to select a file from their computer to
be uploaded.

type=“submit”: creates a submit button. The value
attribute is used to control the text that appears

on a button.

type=“image”: uses an image for the submit button.

## Slide 74 - File Input Box and Submit Button

File Input Box and Submit Button

<form action="http://www.example.com/
upload.jsp" method="post">

<p>Upload your song in MP3 format:</p>
<input type="file" name="user-song" />
<br />
<input type="submit" value="Upload" />
</form>

![Figura 1 dalla slide 74](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-074-fig-01.jpg)

## Slide 75 - File Input Box and Submit Button

File Input Box and Submit Button

<form action="http://www.example.com/
upload.jsp" method="post">

<p>Upload your song in MP3 format:</p>
<input type="file" name="user-song" />
<br />
<input type="submit" value="Upload" />
</form>

## Slide 76 - HTML5 Input

HTML5 Input

HTML5 introduces new form controls with the <input> element:

type=“date”: date input control

type=“range”: slider input

type=“email”

type=“url”

type=“search”

type=“color”: color selector

HTML5 supports form validation, the browser can give users
messages if the form control has not been filled in correctly.

Traditionally, form validation has been performed using
JavaScript.

## Slide 77 - DataList

DataList

The <datalist> element allows the author to provide a
drop-down menu of suggested values for any type of text
input.

It gives the user some shortcuts to select from, but if
none are selected, the user can still type in her own text.

The list attribute in the input element to associate it with
the id of its respective datalist.

![Figura 1 dalla slide 77](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-077-fig-01.jpg)

## Slide 78 - DataList

DataList

<form action="http://www.example.com/education.jsp"
method="post">

<p>Education completed: </p>
<input type="text" list="edulevel"
name="education">
<datalist id="edulevel">

<option value="High School">
<option value="Bachelors Degree”>
<option value="Masters Degree”>
<option value=“PhD">
</datalist>
</form>

![Figura 1 dalla slide 78](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-078-fig-01.jpg)

## Slide 79 - DataList

DataList

<form action="http://www.example.com/education.jsp"
method="post">

<p>Education completed: </p>
<input type="text" list="edulevel"
name="education">
<datalist id="edulevel">

<option value="High School">
<option value="Bachelors Degree”>
<option value="Masters Degree”>
<option value=“PhD">
</datalist>
</form>

![Figura 1 dalla slide 79](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-079-fig-01.jpg)

## Slide 80 - Extra Markup

Extra Markup

![Figura 1 dalla slide 80](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-080-fig-01.jpg)

## Slide 81 - Comments

Comments

If you want to add a comment to your code that will not
be visible in the user's browser, you can add the text
between these characters: <!-- comment goes
here -->

Although comments are not visible to users in the main
browser window, they can be viewed by anyone who
looks at the source code behind the page.

![Figura 1 dalla slide 81](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-081-fig-01.jpg)

## Slide 82 - Class Attribute

Class Attribute

Every HTML element can carry a class attribute.

The class attribute identifies several elements as being
different from the other elements on the page, its value
should describe the class it belongs to.

The class attribute on any element can share the same value.

<p class="important">Some important text
here.</p>
<p>Some other text here.</p>
<p class="important admittance">Some
important text here regarding the
admittance.</p>

## Slide 83 - Groups in a Block and Inline

Groups in a Block and Inline

The <div> element allows you to group a set of elements
together in one block-level box.

The <span> element acts like an inline equivalent of the
<div> element.

Using an id or class attribute on the <div> or <span>
elements means that you can create CSS style rules to
change the appearance of all the elements contained
within them.

![Figura 1 dalla slide 83](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-083-fig-01.jpg)

## Slide 84 - HTML 5, New Elements

HTML 5, New Elements

![Figura 1 dalla slide 84](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-084-fig-01.jpg)

## Slide 85 - HTML 5 New Elements

HTML 5 New Elements

article

figure

rp

aside

footer

rt

audio

header

ruby

bdi

hgroup

section

canvas

keygen

source

command

mark

summary

datalist

meter

time

details

nav

track

embed

output

video

figcaption

progress

wbr

![Figura 1 dalla slide 85](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-085-fig-01.jpg)

## Slide 86 - Page Layout

Page Layout

HTML 4: web page authors used <div> elements to
group together related elements on the page (such as the
elements that form a header, an article, footer or sidebar),
and used class or id attributes to indicate the role of the
<div> element in the structure of the page.

HTML5: introduces a new set of elements that allow you
to divide up the parts of a page. The names of these
elements indicate the kind of content you will find in them.

![Figura 1 dalla slide 86](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-086-fig-01.jpg)

## Slide 87 - Page Layout

Page Layout

Traditional HTML Layout
New HTML5 Layout

<body>

<body>

<div id="page">

<div id="page">

<div id="header">

<header>

<nav>

<div id="nav">

<div id="content">

<div id="content">

<aside>

<div id=
"sidebar">

<article>

<div class="article">

<article>

<div class="article">

<footer>

<div id="footer">

![Figura 1 dalla slide 87](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-087-fig-01.jpg)

## Slide 88 - Headers and Footers

Headers and Footers

The <header> and <footer> elements can be used for:

The main header or footer that appears at the top or bottom of every page on the site.

A header or footer for an individual <article> or <section> within the page.

The <nav> element is used to contain the major navigational blocks on the
site such as the primary site navigation.

<header>

<h1>Yoko's Kitchen</h1>

<nav>

<ul>

<li><a href="" class=“current">home</a></li>
<li><a href="">classes</a></li>

<li><a href="">catering</a></li>

<li><a href="">about</a></li>

<li><a href="">contact</a></li>
</ul>
</nav>
</header>

## Slide 89 - Article, Section, and Aside

Article, Section, and Aside

The <article> element acts as a container for any section of a page
that could stand alone (a blog entry, a comment or forum post).

The <section> element groups related content together, and
typically each section would have its own heading. It may contain
several distinct <article> elements that have a common theme or
purpose.

The <aside> element has two purposes:

When the <aside> element is used inside an <article> element, it should
contain information that is related to the article but not essential to its overall
meaning.

When the <aside> element is used outside of an <article> element, it acts as
a container for content that is related to the entire page.

## Slide 90 - Linking Block Elements

Linking Block Elements

HTML5 allows web page authors to place an <a> element around a block
level element that contains child elements. This allows you to turn an entire
block into a link.

<a href="introduction.html">

<article>

<figure>

<img src=“images/bok-choi.jpg" alt="Bok Choi" />
<figcaption>Bok Choi</figcaption>
</figure>
<hgroup>

<h2>Japanese Vegetarian</h2>
<h3>Five week course in London</h3>
</hgroup>

<p>A five week introduction to traditional Japanese
vegetarian meals, teaching you a selection of rice and
noodle dishes.
</p>
</article>
</a>

## Slide 91 - HTML 5 API

HTML 5 API

HTML5 introduces many APIs (Application Programming Interfaces) for the
creation of web applications. APIs standardize tasks that traditionally required
proprietary plug-ins or custom programming. The following APIs are part of the
W3C HTML5 specification:

Media API, for playback of video and audio files;

Session History API, for exposing the browser history;

Offline Web Applications API, which allows web resources to be used while offline;

Editing API, to create in-browser text editors;

Drag and Drop API;

Canvas API, for two dimensional drawing;

Web Storage API, allows data to be stored in the browser’s cache;

Geolocation API, lets users share longitude and latitude information;

Web Workers API, that allows scripts to run in the background;

Web Sockets API, that maintains an open connection between the client and the server.

![Figura 1 dalla slide 91](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-091-fig-01.jpg)

## Slide 92 - Video

Video

The <video> element embeds a video file in the web page.

The video resource can be provided with the src attribute or with
one or more <source> elements inside the video element to
provide several video format options.

There is still debate regarding the supported video formats for
the video element. No file format is supported by all browsers.

<video controls>
  <source src="somevideo.webm" type="video/webm">
  <source src="somevideo.mp4" type="video/mp4">
  I'm sorry; your browser doesn't support HTML5
video in WebM with VP8/VP9 or MP4 with H.264.
</video>

## Slide 93 - Video

Video

<video src="highlight_reel.mp4" width="640" height="480"
poster="highlight_still.jpg" controls autoplay>

</video>

width and height (pixel measurement): size of the box the
embedded media player takes up on the screen.

poster: provides the location (url) of a still image to use in place of
the video before it plays.

controls: prompts the browser to display its built-in media
controls, (play/pause button, “seeker”, volume).

autoplay: makes the video start playing automatically once it has
downloaded enough of the media file (to be avoided).

## Slide 94 - Audio

Audio

The <audio> element uses the same attributes as the video element, with
the exception of width, height, and poster (because there is nothing to
display!).

Preload: suggests the browser whether the audio data should be fetched
or not:

preload=“auto”: the audio should be fetched as soon as the page loads.

preload=“none”: wait until the user presses the play button and then fetch the video.

preload=“metadata”: loads information about the media file, but not the media itself.

<audio id="soundtrack" controls preload="auto">
<source src="soundtrack.mp3" type="audio/mp3">
<source src="soundtrack.ogg" type="audio/ogg">
<source src="soundtrack.webm" type="audio/webm">
</audio>

![Figura 1 dalla slide 94](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-094-fig-01.jpg)

## Slide 95 - Canvas

Canvas

The <canvas> element creates an area on a web page that you
can draw on using a set of JavaScript functions for creating
lines, shapes, fills, text, animations, and so on.

Everything on the canvas is generated with scripting, that
means it is dynamic and can draw things on the fly and respond
to user input.

You add a canvas space to the page with the canvas element
and specify the dimensions with the width and height attributes.

<canvas width="600" height="400" id="my_first_canvas">

Your browser does not support HTML5 canvas. Try using
Chrome, Firefox, Safari or Internet Explorer 9.
</canvas>

## Slide 96 - Take Away

Take Away

Keep the structure (HTML) separated from the
presentation (CSS) and the behaviour (JavaScript) of your
Web page.

Use HTML elements properly, that is you must account
for the semantic meaning of each element.

![Figura 1 dalla slide 96](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-096-fig-01.jpg)

## Slide 97 - Online Resources

Online Resources

HTML5 documentation:

https://html.spec.whatwg.org/multipage/

W3C Tutorial:

https://www.w3schools.com/

Mozilla Developer Network (MDN):

https://developer.mozilla.org/it/docs/Web/HTML

![Figura 1 dalla slide 97](First%20Year/Second%20Semester/Web%20Applications/MD%20Converted/11-webapp-2025-26-html5/assets/slide-097-fig-01.jpg)

## Slide 98 - Slide 98

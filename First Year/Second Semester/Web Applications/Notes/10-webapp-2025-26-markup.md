# 10 — Markup Languages

_Source: `10-webapp-2025-26-markup.pdf` — Web Applications, Master Degree, A.Y. 2025/2026, Prof. Nicola Ferro_

---

## Table of Contents

- [[#Markup — Definition and Types|Markup — Definition and Types]]
  - [[#Types of Markup|Types of Markup]]
- [[#SGML|SGML]]
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

![[markup-xml-tree.jpg]]

*Figure: XML document as a tree — RSS example. `rss` → `channel` → `title`, `link`, `description`, `item`(s). Each `item` → `title`, `pubDate`, `link`, `guid`, `description`.*

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
>  </channel>
> </rss>
> ```

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

![[markup-dom-interfaces.jpg]]

*Figure: DOM interface hierarchy — `Node` (root interface) → `ProcessingInstruction`, `Document`, `Element`, `Attr`, `CharacterData` → `Text`, `Comment`.*

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
>            targetNamespace="http://www.rssboard.org">
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

![[markup-json-object-syntax.jpg]]

*Figure: JSON object railroad diagram — `{ string : value , ... }`*

![[markup-json-array-value-syntax.jpg]]

*Figure: JSON array + value railroad diagram — array is `[ value , ... ]`; value can be string, number, object, array, true, false, null.*

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

![[markup-jackson-core-api.jpg]]

*Figure: `com.fasterxml.jackson.core` package summary — key classes: `JsonFactory` (main factory, creates parsers/generators), `JsonParser` (reading), `JsonGenerator` (writing).*

![[markup-jackson-jsonparser-api.jpg]]

*Figure: `JsonParser` class API — key methods: `nextToken()`, `nextFieldName()`, `getIntValue()`, `getText()`, `getValueAsString()`, `isClosed()`, `currentToken()`.*

| Jackson Class | Role |
|---------------|------|
| `JsonFactory` | Main factory — creates `JsonParser` and `JsonGenerator` instances |
| `JsonParser` | Pull streaming API for **reading** JSON content |
| `JsonGenerator` | Streaming API for **writing** JSON content |
| `JsonToken` | Enum of token types: `START_OBJECT`, `END_OBJECT`, `FIELD_NAME`, `VALUE_STRING`, `VALUE_NUMBER_INT`, … |

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
| **SGML** | Meta-markup language | GML (IBM, 1974) | Defines DTD concept; parent of HTML and XML | DTD |
| **HTML4** | Markup application of SGML | SGML | Web pages; mixes content and presentation | none (loose) |
| **HTML5** | Evolved HTML | SGML/HTML4 | Separates content from presentation; semantic tags | none (loose) |
| **CSS** | Style language | W3C recommendation | Presentation rules decoupled from HTML structure | — |
| **XML** | Meta-markup application of SGML | SGML | Semi-structured data exchange; interoperability | DTD or XSD |
| **DTD** | Document type language | SGML | Validates XML structure; non-XML syntax; no data types | — |
| **XML Schema (XSD)** | Document type language | W3C recommendation | Validates XML; XML syntax; rich data types; namespace support | — |
| **XML Namespace** | XML mechanism | W3C recommendation | Prevents element name clashes when mixing languages | — |
| **DOM** | XML/HTML API | W3C recommendation | In-memory tree; bi-directional; high memory use | — |
| **SAX** | XML parsing API | Open source | Push streaming; callbacks; low memory | — |
| **StAX** | XML parsing API | JSR-173 | Pull streaming; low memory; writable | — |
| **JSON** | Data interchange format | ECMA-404, RFC 8259 | Lightweight; objects + arrays; browser-native | JSON Schema |
| **JSON Schema** | Validation format | RFC draft | Structural validation of JSON | — |
| **Jackson** | Java JSON library | FasterXML | `JsonFactory` → `JsonParser`/`JsonGenerator` | — |

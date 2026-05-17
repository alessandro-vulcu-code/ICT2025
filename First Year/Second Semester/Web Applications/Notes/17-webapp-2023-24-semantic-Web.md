# Semantic Web & Linked Data
## Table of Contents

- [[#Evolution of the Web|Evolution of the Web]]
- [[#Data vs Information|Data vs Information]]
- [[#Semantic Representation of Knowledge|Semantic Representation of Knowledge]]
- [[#RDF — Resource Description Framework|RDF — Resource Description Framework]]
  - [[#RDF Triples|RDF Triples]]
  - [[#RDF Serialization Formats|RDF Serialization Formats]]
- [[#SPARQL|SPARQL]]
- [[#Linked Data|Linked Data]]
  - [[#Linked Data Principles|Linked Data Principles]]
  - [[#Linked Open Data Cloud|Linked Open Data Cloud]]
- [[#FAIR Principles|FAIR Principles]]
- [[#Notable Datasets|Notable Datasets]]
  - [[#DBpedia|DBpedia]]
  - [[#Wikidata|Wikidata]]
- [[#Overall Web Vision|Overall Web Vision]]
- [[#Summary Table|Summary Table]]

---

# Evolution of the Web

> [!Important] Web of Documents → Web of Data
> - **Web 1.0/2.0 (Web of Documents):** hypertext of resources (HTML pages, images) for *human* browsing
> - **Web 3.0 (Web of Data):** adds *data resources* (genomics, clinical trials, IoT streams, statistical data) connected via **typed links**, making structure and semantics explicit and accessible to both humans and machines
>
> **Intuition:** the key shift is that machines can now interpret the connections, not just follow hyperlinks.

![[Figures/slide-003-fig-01.jpg|560]]

---

# Data vs Information

Raw numbers (e.g., `123`, `91`, `38.5`, `7`) carry no meaning without context. **Information** = data + **schema (metadata)** that names what each value represents.

![[Figures/slide-006-fig-01.jpg|560]]

*Example: the numbers become meaningful when labelled as Name=Luca, Age=7, Temperature=38.5°C, Heartbeat=123 bpm, Pressure=91.*

> [!Important] The Interoperability Problem
> Different databases may store the same real-world facts using different schemas, identifiers, and formats. Making them interoperate requires a common, explicit, machine-readable representation — the core motivation for the **Semantic Web**.

---

# Semantic Representation of Knowledge

Three complementary layers:

| Layer | Technology | Represents |
|-------|-----------|-----------|
| **Ontology** | *OWL* | Abstract concepts and their relationships (e.g., "the concept of Dog") |
| **Linked Data** | *RDF* | Specific instances (e.g., "my dog Linneo") |
| **Knowledge Graph/Base** | combination | Full graph of facts connecting instances through typed relations |

*(nota: OWL = Web Ontology Language; RDF = Resource Description Framework)*

---

# RDF — Resource Description Framework

## RDF Triples

> [!Important] RDF Data Model
> RDF represents information as a set of **triples**:
>
> ```
> (Subject, Predicate, Object)
>   URI       URI        URI or Literal
> ```
>
> Each triple asserts that a relationship (predicate) holds between two resources (subject and object). A set of triples forms an **RDF graph** — a directed, node-arc-node diagram.
>
> **Intuition:** every fact is a sentence with exactly three parts: who, what relationship, and what/who.
>
> _Reference: W3C RDF 1.1 Recommendation (2014)_

![[Figures/slide-009-fig-01.jpg|560]]

### RDF Graph Example

The following facts about Bob, Alice, and the Mona Lisa form a connected RDF graph:

![[Figures/slide-010-fig-01.jpg|560]]

With explicit URIs and typed literals:

![[Figures/slide-011-fig-01.jpg|600]]

Key triples represented:

| Subject | Predicate | Object |
|---------|-----------|--------|
| `http://example.org/bob#me` | `rdf:type` | `foaf:Person` |
| `http://example.org/bob#me` | `foaf:knows` | `http://example.org/alice#me` |
| `http://example.org/bob#me` | `schema:birthDate` | `"1990-07-04"^^xsd:date` |
| `http://example.org/bob#me` | `foaf:topic_interest` | `wd:Q12418` (Mona Lisa) |
| `wd:Q12418` | `dcterms:title` | `"Mona Lisa"` |
| `wd:Q12418` | `dcterms:creator` | `dbpedia:Leonardo_da_Vinci` |

*(nota: `^^xsd:date` is the typed literal syntax — `^^` separates the value from its datatype URI.)*

## RDF Serialization Formats

The same RDF graph can be encoded in multiple concrete syntaxes:

### RDF/XML

```xml
<?xml version="1.0" encoding="utf-8"?>
<rdf:RDF
    xmlns:dcterms="http://purl.org/dc/terms/"
    xmlns:foaf="http://xmlns.com/foaf/0.1/"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:schema="http://schema.org/">
  <rdf:Description rdf:about="http://example.org/bob#me">
    <rdf:type rdf:resource="http://xmlns.com/foaf/0.1/Person"/>
    <schema:birthDate rdf:datatype="http://www.w3.org/2001/XMLSchema#date">1990-07-04</schema:birthDate>
    <foaf:knows rdf:resource="http://example.org/alice#me"/>
    <foaf:topic_interest rdf:resource="http://www.wikidata.org/entity/Q12418"/>
  </rdf:Description>
  <rdf:Description rdf:about="http://www.wikidata.org/entity/Q12418">
    <dcterms:title>Mona Lisa</dcterms:title>
    <dcterms:creator rdf:resource="http://dbpedia.org/resource/Leonardo_da_Vinci"/>
  </rdf:Description>
</rdf:RDF>
```

### JSON-LD

```json
{
  "@context": "example-context.json",
  "@id": "http://example.org/bob#me",
  "@type": "Person",
  "birthdate": "1990-07-04",
  "knows": "http://example.org/alice#me",
  "interest": {
    "@id": "http://www.wikidata.org/entity/Q12418",
    "title": "Mona Lisa",
    "subject_of": "http://data.europeana.eu/item/04802/243FA8618938F4117025F17A8B813C5F9AA4D619",
    "creator": "http://dbpedia.org/resource/Leonardo_da_Vinci"
  }
}
```

### N-Triples

One triple per line — the most verbose but simplest format:

```
<http://example.org/bob#me> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> .
<http://example.org/bob#me> <http://xmlns.com/foaf/0.1/knows> <http://example.org/alice#me> .
<http://example.org/bob#me> <http://schema.org/birthDate> "1990-07-04"^^<http://www.w3.org/2001/XMLSchema#date> .
<http://example.org/bob#me> <http://xmlns.com/foaf/0.1/topic_interest> <http://www.wikidata.org/entity/Q12418> .
<http://www.wikidata.org/entity/Q12418> <http://purl.org/dc/terms/title> "Mona Lisa" .
<http://www.wikidata.org/entity/Q12418> <http://purl.org/dc/terms/creator> <http://dbpedia.org/resource/Leonardo_da_Vinci> .
```

### Turtle

Compact, human-readable — supports prefixes and grouped statements:

```turtle
BASE   <http://example.org/>
PREFIX foaf:    <http://xmlns.com/foaf/0.1/>
PREFIX xsd:     <http://www.w3.org/2001/XMLSchema#>
PREFIX schema:  <http://schema.org/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX wd:      <http://www.wikidata.org/entity/>

GRAPH <http://example.org/bob>
{
  <bob#me>
      a foaf:Person ;
      foaf:knows <alice#me> ;
      schema:birthDate "1990-07-04"^^xsd:date ;
      foaf:topic_interest wd:Q12418 .
}

GRAPH <https://www.wikidata.org/wiki/Special:EntityData/Q12418>
{
  wd:Q12418
      dcterms:title "Mona Lisa" ;
      dcterms:creator <http://dbpedia.org/resource/Leonardo_da_Vinci> .
}
```

| Format | Readability | Use case |
|--------|-------------|----------|
| RDF/XML | Low | XML ecosystem integration |
| JSON-LD | Medium | Web APIs, JavaScript apps |
| N-Triples | Low | Bulk data exchange, streaming |
| Turtle | High | Human authoring, configuration |
| RDFa | Embedded in HTML | Annotating web pages |
| TriG | Medium | Named graphs (multi-graph docs) |

---

# SPARQL

> [!Important] SPARQL — Simple Protocol and RDF Query Language
> **SPARQL** is the W3C standard query language for RDF graphs, analogous to SQL for relational databases. It provides languages and protocols to query and manipulate RDF graph content stored in an **RDF store** (triplestore) or served over the web.
>
> _Reference: W3C SPARQL 1.1 Recommendation (2013)_

> [!Example] SPARQL — Count friends per person
> **Context:** RDF graph at `http://example.org/alice` with `foaf:knows` triples between persons
> ```sparql
> PREFIX foaf: <http://xmlns.com/foaf/0.1/>
> SELECT ?name (COUNT(?friend) AS ?count)
> WHERE {
>     ?person foaf:name ?name .
>     ?person foaf:knows ?friend .
> }
> GROUP BY ?person ?name
> ```
> **Result:**
> | name | count |
> |------|-------|
> | Alice | 3 |
> | Bob | 1 |
> | Charlie | 1 |
>
> **Explanation:** `?person`, `?name`, `?friend` are SPARQL variables. The WHERE clause matches triples by pattern; GROUP BY + COUNT aggregates over bound variables.

![[Figures/slide-016-fig-01.jpg|600]]

*(nota: SPARQL results can be serialized as XML, JSON, CSV — the image shows the XML result format.)*

---

# Linked Data

> [!Important] What is Linked Data
> **Linked Data** is the practice of applying the general Web architecture to sharing *structured data* at global scale — using the Web to connect data that was previously isolated or linked only through proprietary means.
>
> **Linked Open Data (LOD)** = Linked Data published under an open license.
>
> _Heath & Bizer (2011). Linked Data: Evolving the Web into a Global Data Space._

## Linked Data Principles

Tim Berners-Lee's four principles:

1. **Use URIs as names for things** — identify not just web documents but real-world objects and abstract concepts via URI references
2. **Use HTTP URIs** — so the names can be looked up (*dereferenced*) over HTTP to retrieve a description of the identified resource
3. **When someone looks up a URI, provide useful information using RDF and SPARQL** — use standard formats so machines can interpret the response
4. **Include links to other URIs** — so consumers can discover more related resources. In Linked Data, these typed hyperlinks are called **RDF links** (distinct from classic HTML hyperlinks)

## Linked Open Data Cloud

The LOD Cloud visualises thousands of interlinked open datasets across domains: Cross-Domain, Geography, Government, Life Sciences, Linguistics, Media, Publications, Social Networking, User Generated.

![[Figures/slide-021-fig-01.jpg|600]]

The scale of the cloud reveals a key practical problem: **how to find and share the specific data of interest** among thousands of interconnected sources.

---

# FAIR Principles

> [!Important] FAIR Data Principles
> Published by Wilkinson et al. (2016) in *Nature Scientific Data*. FAIR defines requirements for scientific data management so data can be found and reused by both humans and machines.
>
> | Principle | Requirement |
> |-----------|-------------|
> | **Findable** | (Meta)data assigned globally unique persistent identifier; described with rich metadata; registered/indexed in searchable resource; metadata includes identifier of the data it describes |
> | **Accessible** | (Meta)data retrievable by identifier via standardised open protocol; protocol supports auth/authorisation; **metadata remain accessible even if data are no longer available** |
> | **Interoperable** | (Meta)data use formal, accessible, broadly applicable knowledge representation language; use FAIR-compliant vocabularies; include qualified references to other (meta)data |
> | **Reusable** | (Meta)data richly described with accurate attributes; released with clear data usage license; associated with provenance; meet domain-relevant community standards |
>
> **Intuition:** FAIR is a checklist for publishing data so that future automated agents (not just humans) can locate, access, combine, and reuse it without manual intervention.

---

# Notable Datasets

## DBpedia

**DBpedia** extracts structured information from Wikipedia and publishes it as Linked Data, enabling SPARQL queries over Wikipedia's content.

- Website: [dbpedia.org](https://www.dbpedia.org) — "Global and Unified Access to Knowledge Graphs"
- Data includes: persons, places, works, organizations, with their properties and relations
- Central hub in the LOD Cloud — many datasets link to DBpedia URIs as a common reference point

## Wikidata

**Wikidata** is a free, collaborative, multilingual knowledge base operated by the Wikimedia Foundation.

- Provides machine-readable structured data for Wikipedia and other Wikimedia projects
- Every item has a stable URI (e.g., `http://www.wikidata.org/entity/Q12418` for the Mona Lisa)
- Used as a source of identifiers and links across the LOD Cloud

---

# Overall Web Vision

![[Figures/slide-028-fig-01.jpg|580]]

The W3C Web technology stack is layered:

| Layer | Technologies |
|-------|-------------|
| **Foundation** | Internet → URI/IRI, HTTP → Web Architectural Principles |
| **Data** | XML Infoset, RDF(S) Graph |
| **Core standards** | XML, Namespaces, Schemas, XQuery/XPath, XSLT, DOM, RDF/XML, SPARQL |
| **Web Applications** | XHTML, SVG, CSS, XSL, XForms, SMIL |
| **Semantic Web** | OWL, SKOS, GRDDL, RDFa, POWDER, RIF |
| **Web Services** | SOAP, WSDL, WS-CDL, WS-A |
| **Privacy/Security** | P3P, XML Sig, XML Enc, XKMS |
| **Cross-cutting** | Accessibility, Internationalization, Device Independence, Quality Assurance |

The Semantic Web stack (OWL, SKOS, RDFa, etc.) sits at the same architectural level as Web Applications — it is part of the same unified "One Web" vision, not a separate system.

---

## Summary Table

| Technology / Concept | Role | Standard | Notes |
|---------------------|------|----------|-------|
| **RDF** | Data model for facts | W3C Rec (2014) | Triples: Subject–Predicate–Object |
| **URI** | Global identifier for any resource | IETF/W3C | HTTP URIs enable dereferencing |
| **RDF/XML** | RDF serialization | W3C | XML-based, verbose |
| **Turtle** | RDF serialization | W3C | Compact, human-readable |
| **N-Triples** | RDF serialization | W3C | One triple per line, streaming |
| **JSON-LD** | RDF serialization | W3C | JSON-compatible, web-friendly |
| **SPARQL** | Query language for RDF | W3C Rec (2013) | Like SQL for triplestores |
| **OWL** | Ontology language | W3C | Defines classes, properties, axioms |
| **Linked Data** | Publishing practice | Tim Berners-Lee (4 principles) | HTTP URIs + RDF + cross-links |
| **LOD** | Linked Data under open license | community | LOD Cloud = thousands of datasets |
| **FAIR** | Data quality principles | Wilkinson et al. (2016) | Findable, Accessible, Interoperable, Reusable |
| **DBpedia** | Wikipedia as Linked Data | open community | Central LOD Cloud hub |
| **Wikidata** | Multilingual knowledge base | Wikimedia Foundation | Stable URIs for entities |
| **Knowledge Graph** | Instance-level fact store | various | Built from RDF + ontologies |

---

## Questions

1. Explain the evolution from the Web of Documents to the Web of Data. What changes when links connect data entities instead of only human-readable pages?
2. Using the data/schema/metadata figure, explain the difference between raw data and information. Why is metadata necessary for interoperability?
3. What is the role of an ontology in the Semantic Web, and how does OWL help define classes, properties, constraints, and axioms?
4. Compare ontology, Linked Data, knowledge graph, and knowledge base. How do these concepts relate to each other?
5. Explain the RDF triple model. What are the subject, predicate, and object, and why are URIs important for subjects and predicates?
6. In RDF, why can the object of a triple be either another URI or a literal value? Use the Bob, Alice, birth date, and Mona Lisa example to illustrate both cases.
7. Convert part of the Bob/Mona Lisa graph into RDF triples. Which nodes are resources, which values are literals, and which edges are predicates?
8. Compare RDF/XML, Turtle, N-Triples, JSON-LD, RDFa, and TriG as RDF serialization formats. Which ones are more human-readable, web-friendly, or stream-friendly?
9. What are prefixes in RDF serializations, and why do they make examples such as `foaf:name`, `rdf:type`, and `dcterms:title` easier to read?
10. Explain how a SPARQL `SELECT` query matches graph patterns with variables such as `?person`, `?name`, and `?friend`.
11. In the SPARQL example with `COUNT(?friend)` and `GROUP BY`, why is grouping needed, and what does the resulting table represent?
12. Compare SPARQL with SQL. What is similar about querying, and what changes when the underlying data model is a graph instead of tables?
13. State Tim Berners-Lee's four Linked Data principles. Why do HTTP URIs and dereferencing matter?
14. What is the difference between Linked Data and Linked Open Data? Why does the LOD Cloud create a practical discovery problem despite having many interconnected datasets?
15. Explain the FAIR principles: Findable, Accessible, Interoperable, and Reusable. Why can metadata remain important even when the original data are no longer available?

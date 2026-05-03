Namespace

• It represents a set of facilities that directly belongs together (e.g., the code of a library) because of
  • logical relationships
  • the functionality these facilities provide

• Members of a namespace are all in scope

• Namespaces are open, i.e., it is possible to add members to a namespace from multiple locations
  • E.g., consider multiple classes in a namespace, defined in multiple files

```javascript
namespace TextLibrary {
  // a library for text
  class Line { /* ... */ };
  class Text { /* ... */ };
}; // end of namespace TextLibrary
```

---

**Immagini estratte:**

![Figura estratta 1](images/p05_img01.jpg)

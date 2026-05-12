auto Type Specifier

• automatically infer the type of the variable from the type of the initializer
• do not use the {} initializer with auto – otherwise the type becomes a std::initializer_list<T>
• int a1 = 2292;
  auto a2 = 2292; // a2 is int
• advantage if the type has a long name
• std::vector<T>::iterator a1 = vec.begin();
  auto a1 = vec.begin();

• Use it mainly in small scopes (hard to debug in large scopes)

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p17_img01.jpg)

Automatic overload resolution

• The compiler compares the types of actual and formal arguments – it uses the function that provides the best match, with rules in the following order:
  1. Exact match (no or trivial conversions – array to pointer or viceversa, T to const T)
  2. Match using promotions (to integral types with larger ranges, to floating-point values with higher precision)
  3. Match using standard conversions (int – double, etc)
  4. Match using user-defined conversions
  5. Match using ellipsis
• If two different matches are identified at the highest level of a match, the compiler gives an error
• The return type is not considered for resolution
• Functions in different scopes are not overloaded, i.e., the compiler exactly know which one should be used without the need to resolve

---

**Immagini estratte:**

![Figura estratta 1](images/p23_img01.jpg)

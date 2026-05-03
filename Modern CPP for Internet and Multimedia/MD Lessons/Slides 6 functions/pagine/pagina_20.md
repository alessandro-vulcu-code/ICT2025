Unspecified number of arguments

There are different ways to deal with an unknown number of arguments

1. Variadic templates (arbitrary number of arbitrary types) (more on this when we will study templates)
2. Use `std::initializer_list<T>` (arbitrary number of the same type)
3. Ellipsis (...) (arbitrary number of arbitrary types)
   - not type-safe (the compiler does not know a-priori which are the types of the possible arguments)
   - some user-defined types may not work
   - this may cause errors: use it only if 1 and 2 are not an option

1 and 2 are type safe

---

**Immagini estratte:**

![Figura estratta 1](images/p20_img01.jpg)

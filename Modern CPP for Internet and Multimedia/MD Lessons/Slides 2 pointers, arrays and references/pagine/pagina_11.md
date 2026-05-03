Pointers and arrays

• The name of an array can be used as a pointer to its first element
  ```c
  int v[] = {1,2,3,4};
  int* p1 = v;
  int* p2 = &v[0];
  bool pointToSameAddress {p1 == p2}; //this is true
  ```
  ```c
  int* pOneBeyondLast = v + 4;
  int* pOther = v + 7;
  ```

all the position outside the range [v + 0, v + size] are undefined: do not do that! Risk of overwriting other variables or segfault

• it is valid to have a pointer to the element beyond the last element of the array, but it cannot be read from or written to
• useful to implement low-level algorithms

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)

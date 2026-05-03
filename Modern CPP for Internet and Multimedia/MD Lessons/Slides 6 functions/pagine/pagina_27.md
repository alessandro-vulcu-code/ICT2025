Pointer to function

• It is possible to cast to pointer types to other functions, but this must be avoided (bad practice that can lead to errors, more in the code example for this class)

• They are used to parametrize C-style code
  using CFT = int(*)(const* void, const* void);

// function that sorts elements independently on the
// type of base, using cmp for comparisons
ssort(void* base, int size, CFT cmp);
// cmp is a pointer to a specific implementation
// of a function that compares objects of the actual
// type of base

int cmp1(const void* p, const void* q) // Compare int
{
  return *(static_cast<int*>(p)) - *(static_cast<int*>(q));
}

---

**Immagini estratte:**

![Figura estratta 1](images/p27_img01.jpg)

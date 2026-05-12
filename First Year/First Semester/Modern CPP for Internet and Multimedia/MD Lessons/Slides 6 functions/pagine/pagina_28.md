Pointer to function

• They are used to parametrize C-style code
  using CFT = int(*)(const* void, const* void);

// function that sorts elements independently on the
// type of base, using cmp for comparisons
ssort(void* base, int size, CFT cmp);

// This is not recommended in modern C++, use
  std::vector<int> v {1,3,2,4};
  std::sort(
    v.begin(), v.end(),
    [](const int n1, const int n2) {return n1 < n2;}
  );

lambda function

---

**Immagini estratte:**

![Figura estratta 1](images/p28_img01.jpg)

Shared pointer example

```cpp
int fun1(shared_ptr<T1> sp) { //*use_count=3
  sp... //DO STUFF
  return 0;
} //sp goes out of scope: *use_count=2

main() {
  shared_ptr<T1> sp1 =
    make_shared <T>(val); // *use_count = 1

  auto sp2 = sp1; // *use_count = 2
  int x = fun1(sp1);
} // sp1 and sp2 go out of scope:
// *use count = 0, pointed object is
// destroyed
```

---

**Immagini estratte:**

![Figura estratta 1](First%20Year/Second%20Semester/Multimedia%20Communications/ToSummarize/3.%20Lossless%20coding(1)/images/p17_img01.jpg)

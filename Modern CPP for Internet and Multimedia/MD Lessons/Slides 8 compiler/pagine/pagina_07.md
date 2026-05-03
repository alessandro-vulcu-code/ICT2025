Why is it not compiling?
error: redefinition of ‘int incr(int)’
// ONLY CPP FILES ARE COMPILED: NOT HEADERS!!
// THE COMPILER SEES a unique file (translation unit)
... //code of lines of iostream
inline int incr(int i) {
  return i+;
}
inline int ex(int i) {
  return incr(i+1);
}
inline int incr(int i) {
  return i+;
}
inline int ex2(int i) {
  return incr(i+2);
}
int main() {
  std::cout << ex(1) << ex2(2);
}

---

**Immagini estratte:**

![Figura estratta 1](images/p07_img01.jpg)

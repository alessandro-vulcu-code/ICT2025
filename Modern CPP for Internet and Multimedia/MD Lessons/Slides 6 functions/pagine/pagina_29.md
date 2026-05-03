Macros

• Inherited from C
• Few meaningful uses in C++
  #define MAX_HEIGHT 720
  void f(int a) {
    int b = a + MAX_HEIGHT;
  }

for this scenario, use a constexpr or a const

• a `dumb` preprocessor will simply replace MAX_HEIGHT with what is defined in the macro (720)
• if you want to use MAX_HEIGHT as a name for a member variable (don’t do it), the preprocessor will replace it with 720 and the code will not compile

• They can be used for conditional compilation

---

**Immagini estratte:**

![Figura estratta 1](images/p29_img01.jpg)

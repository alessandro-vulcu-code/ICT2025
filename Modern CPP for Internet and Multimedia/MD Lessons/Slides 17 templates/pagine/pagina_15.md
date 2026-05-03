Function templates

• The need for a function template arises when class templates are used
  • for example, a vector can hold any type to be sorted
    template<typename T> void sort(std::vector<T>&);

• The template type argument is deduced from the function arguments
• Function templates are fundamental for generic programming
• Function templates can be overloaded
  • Same name, different arguments
  • The compiler will select the specialization that is the best fit for the set of arguments

---

**Immagini estratte:**

![Figura estratta 1](images/p15_img01.jpg)

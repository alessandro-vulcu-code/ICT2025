Operator <<

It is generally overloaded to concatenate output on std::cout or other streams

• << for built-in types is directly overloaded in the ostream header
• for user-defined types, it must be overloaded with a non-member function declaration
  • the first argument is of type std::cout – but we cannot add our function declarations into the definition of the ostream class
• if the overloaded operator needs access to the private members of the user-defined type it wants to manipulate:
  • call to a member function
  • friend keyword

---

**Immagini estratte:**

![Figura estratta 1](images/p07_img01.jpg)

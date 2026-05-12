Slicing with copy constructors

• The default copy constructor/assignment performs a member-wise copy

• Slicing issue: when using a pointer to the base class for the derived object (e.g., Employee* to refer to Manager*), the **wrong copy constructor** may be called
  • the copied object contains only the copy of the base members
  • the others are left uninitialized

• Solutions
  • =delete the copy constructor in the base class
  • make the base class private or protected (we will see how)

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)

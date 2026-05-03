Access control - protected

protected data members are usually a design error

• data corruption if improperly used in derived classes
  • use the minimum number of data members in common base classes

• hard to restructure the code (who knows who is using a certain protected member in derived classes)

• protected functions are generally more useful
  • virtual protected functions can be overridden while being hidden from the interface of the object

---

**Immagini estratte:**

![Figura estratta 1](images/p30_img01.jpg)

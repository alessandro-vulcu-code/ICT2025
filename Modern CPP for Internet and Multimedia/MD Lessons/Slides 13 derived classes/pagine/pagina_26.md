Override control

• final
  • a function can be virtual or not
  • different reasons for why a function should not be virtual:
    • it is hard to specify it more without errors
    • there is no need to specify it more

these conditions may become true only after a few derivations

• final prohibits to further override a function that was declared virtual in some upstream base class
• it can be used after a class name to make all methods final and prevent deriving from the class

---

**Immagini estratte:**

![Figura estratta 1](images/p26_img01.jpg)

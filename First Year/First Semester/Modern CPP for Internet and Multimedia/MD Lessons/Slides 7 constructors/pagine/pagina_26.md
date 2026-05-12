Delegating constructors

If multiple constructors need to repeat the same action:
• duplicate the code
• define a function that is called by all the constructors
• define a constructor in terms of another

```cpp
ClassName::ClassName(T1 arg1) : ClassName{f(arg1)} {}
```

• f may be a cast to another type, or conversion from string to int, ect
• this forbids explicit initialization of other members
• very different from calling another constructor in the constructor body (this would simply create another object and do nothing with it)
```

---

**Immagini estratte:**

![Figura estratta 1](images/p26_img01.jpg)

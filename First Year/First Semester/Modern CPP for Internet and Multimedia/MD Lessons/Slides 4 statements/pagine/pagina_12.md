# switch statement - default

• There is a default case
  • Handle the most common case
  • Handle the cases that are not covered by the switch (e.g., by raising an exception)

```c
switch (action)
{
  case 1:
    // code
    break;
  case 2:
    // code
    break;
  default:
    // code
}
```

• Do not use it with enumerators
  • The compiler can warn if the set of cases does not match the set of values of the enumerator

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)

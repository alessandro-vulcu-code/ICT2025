## switch statement - termination

• Terminate the code of the case
  • Use break (exits the switch) or return (exits the function with the switch)
  • Otherwise, the next case is executed ("fall through")
  • Explicitly comment is fall though is intentional

```c
switch (action)
{
    case do_and_print:
        act(value);
        // no need to implement print
        // fall through the next case
    case print:
        print(value)
        break;
    case something_else:
        something(value)
        break;
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p11_img01.jpg)

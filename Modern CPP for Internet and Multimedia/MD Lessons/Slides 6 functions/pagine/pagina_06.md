Returning values

• void to specify that no value is returned
• prefix vs postfix return
• the point and value of the return is specified by a return statement
• There can be more than one return in a function, and the function returns when executing the first of them in the logic flow
• Return with a copy
  • a variable of the returned type is initialized and then returned
  • the memory is reused after the function returns, so never return a pointer or a reference to a local non-static variable

```c
int f(int a) {
  if(a == 0) {
    return 1;
  }
  int b = a * 10;
  return b;
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p06_img01.jpg)

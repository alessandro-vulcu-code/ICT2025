Example of class usage

```cpp
X var {7};
// a variable of type X, initialized to 7

// a function that interacts with var
int f(X var, X* ptr)
{
    int x = var.mf(7); // access using .
    int y = ptr->mf(9); // access using →
    int z = var.m; // error: cannot access
        // private member
}
```

---

**Immagini estratte:**

![Figura estratta 1](p07_img01.jpg)

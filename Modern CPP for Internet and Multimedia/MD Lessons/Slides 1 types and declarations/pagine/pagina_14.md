Scope

```cpp
int global_var {10}; // global index

namespace Example {
int namespace_scope_var {5}; // namespace scope

class ExampleClass {
    int class_scope_var;
    void f() {
        int local_scope_var {2};
        for (int statement_scope_idx = 0;
             statement_scope_idx < local_scope;
             ++statement_scope_idx) {
            std::cout << statement_scope_idx;
        }
    }
} // end of class ExampleClass scope
} // end of namespace Example scope
```

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)

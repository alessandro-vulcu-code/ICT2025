Functions declarations

A function declaration has multiple parts:

• **name** (required)
• **argument list** (required)
  specify the number and type of arguments. The name for each argument is optional for the declaration, required for the definition.
• **return type** (required)
  it may be void, if the function does not return a value
  it can be specified as a prefix or suffix

```cpp
prefix return type name argument list
int sqrt(int number);
auto sqrt(int number) → int;
postfix return type (with auto in the prefix)
```

This is useful for templates, where the type of return is not known a-priori but depends on the type of the arguments.

---

**Immagini estratte:**

![Figura estratta 1](images/p04_img01.jpg)

Pass by reference

• Pass by const lvalue reference void f(const LargeType& a)
• Pass by rvalue reference (e.g., to bind to a temporary object) void f(LargeType& a)

```cpp
void f(vector<int>&); // (non-const) lvalue ref argument
void f(const vector<int>&); // const lvalue ref argument
void f(vector<int>&); // rvalue reference argument

void g(vector<int>& vi, const vector<int>& vci)
{
    f(vi); // call f(vector<int>&)
    f(vci); // call f(const vector<int>&)
    f(vector<int>{1,2,3,4}); // call f(vector<int>&);
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)

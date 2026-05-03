# if conditions – lazy evaluation

• Lazy evaluations
  • Always check the first condition in expressions with logical operators
  • Evaluate the second only it the first is not enough
  • Pay attention when using functions (e.g., with a boolean return type) in conditions

```cpp
bool c1 = false;
bool c2 = true;
if (c1 && c2)
{ // c2 is not evaluated }
if (c2 && c1)
{ // both evaluated }
if (c1 && someFunction(c2))
{
  // someFunction(c2) is not evaluated
  // this may be done on purpose (always comment it!)
  // it could also lead to errors if not done on purpose
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p08_img01.jpg)

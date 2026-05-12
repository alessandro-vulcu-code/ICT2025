Self-reference

• this is a pointer to the object on which the function was called
  • object of type non-const X -> this has type X*, but is considered an rvalue (it is not possible to get its address or assign to it)
  • object of type const X -> this has type const X*

• most uses are implicit (it is not necessary to specify this→member_value in member functions)
• it could be useful to return a reference to it to chain operations

```python
Date& add_year(int year) { y += year; return *this; }
Date& add_month(int month) { m += month; m = m % 12; return *this; }

Date d {10, 05, 2003}
d.add_year(3).add_month(3);
```

this could be this→m but it is not necessary

---

**Immagini estratte:**

![Figura estratta 1](images/p24_img01.jpg)

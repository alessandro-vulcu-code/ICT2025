Lambda function – syntax

Between [] insert the list of parameters that will be captured by the lambda, i.e., passed from the scope where the lambda is created to the scope of lambda.
• By default parameters are passed by const copy
• Writing just = passes all parameters by const copy
• Writing & before the parameter passes them by reference
• Writing just & passes all parameters by reference
• Writing this captures the current object by reference

Between () insert the list of the function parameters, just as in a normal function

```python
[&a] (int x) -> int
```

After -> insert thr returning type

```python
a = a + x;
return a;
```

Between {} insert the body of the function, just as in a normal function

---

**Immagini estratte:**

![Figura estratta 1](images/p28_img01.jpg)

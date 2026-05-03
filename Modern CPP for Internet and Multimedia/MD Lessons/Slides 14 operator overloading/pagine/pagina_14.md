Functors: example

```python
CalculateAverageOfPowers avg{2};
std::vector<float> dataA {0.1, 0.2, 10};

avg = std::for_each(dataA.begin(), dataA.end(), avg);

1. Initialize avg: it will have p = 2 as exponent for the pow operation, n = 0, acc = 0
2. Call the overloaded operator () for avg on the first element of dataA
   • acc += pow(0.1, 2) → acc = 0.01
   • n++ → n = 1
3. Call the overloaded operator () for avg on the second element of dataA
   • acc += pow(0.2, 2) → acc = 0.05
   • n++ → n = 2
4. Call the overloaded operator () for avg on the third element of dataA
   • acc += pow(10, 2) → acc = 100.05
   • n++ → n = 3
5. What if we call getAverage() now?
```

---

**Immagini estratte:**

![Figura estratta 1](images/p14_img01.jpg)

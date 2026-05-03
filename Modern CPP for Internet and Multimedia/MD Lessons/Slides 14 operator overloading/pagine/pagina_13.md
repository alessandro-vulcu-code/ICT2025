Functors: example

• An interesting use is for the std::for_each loop

```cpp
CalculateAverageOfPowers avg{2};
std::vector<float> dataA {0.1, 0.2, 10};
std::vector<float> dataB {1, 2, 3};
std::vector<float> dataC {0.5, 8, 99};

avg = std::for_each(dataA.begin(), dataA.end(), avg);
avg = std::for_each(dataB.begin(), dataB.end(), avg);
avg = std::for_each(dataC.begin(), dataC.end(), avg);
```

call avg for each member of dataA/B/C (and it maintains a state across the different calls!)

---

**Immagini estratte:**

![Figura estratta 1](images/p13_img01.jpg)

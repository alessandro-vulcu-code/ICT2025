Functors

```java
class CalculateAverageOfPowers {
public:
    CalculateAverageOfPowers(float p) :
        acc(0), n(0), p(p) {}
    void operator() (float x) {
        acc += pow(x, p); n++;
    }
    float getAverage() const { return acc / n; }

private:
    float acc; int n; float p;
};

we can call
CalculateAverageOfPowers functor{1};
functor(10); // this is a function call using the operator
// () on the object!
```

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)

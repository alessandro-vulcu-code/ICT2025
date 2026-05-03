Use of lambas – for each

```cpp
int main() {
    std::vector<int> values = {1,2,3};

    std::for_each(values.begin(),values.end(),
        [](int* k) {
            std::cout << "k = " << *k << std::endl;
        });
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p31_img01.jpg)

Use of lambas

```cpp
std::vector<int> values = {1,2,3};
void executeF(const std::function<void(int)>& f) {
    for(int v : values) {
        f(v);
    }
}

int main() {
    auto lambda = [](int k) {
        std::cout << k << std::endl;
    };
    executeF(lambda);
    executeF([](int k) {
        std::cout << "k = " << k << std::endl;
    });
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p30_img01.jpg)

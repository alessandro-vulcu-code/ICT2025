producer – consumer problem

```cpp
int main(){
    std::queue<int> q;
    std::thread trb([&](){
        while(true){
            if(q.size()>0) {
                int val = q.front();
                q.pop();
                //use val somehow...
            }}});

        //some operations
        q.push(17);
        q.push(27);
        ..}
```

• Thread a (e.g.: the main thread) produces resources for Thread b
• Thread b consumes the resources produced by Thread a, as soon as they become available
• Solution 1: busy waiting (or spinning)

---

**Immagini estratte:**

![Figura estratta 1](p05_img01.jpg)

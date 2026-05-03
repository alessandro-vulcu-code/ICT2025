Critical Regions (or Critical Sections)

• The critical region is a sequence of statements where the shared resources (memory, cout,...) is accessed, and that must appear to be executed indivisibly to avoid race conditions

```cpp
//race-condition example
void incr() {
  for (int i = 0; i < 100000; i++){
    a = a + 1;
  }
}
int main() {
  std::thread thr1(incr);
  std::thread thr2(incr);
  thr2.join();
  thr1.join();
}
```

```cpp
//producer-consumer example
std::thread trb([](){
  while(true){
    if(q.size()>0) {
      int val = q.front();
      q.pop();
    }
  });
  //some operations
  q.push(17);
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p06_img01.jpg)

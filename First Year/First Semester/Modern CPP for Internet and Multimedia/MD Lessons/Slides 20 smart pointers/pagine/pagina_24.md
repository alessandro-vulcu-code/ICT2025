Weak Pointer

• `lock()` returns a shared pointer to the object pointed by the weak pointer, so that object can be accessed in safe way
• It returns an empty shared pointer if the weak pointer is expired

```javascript
if(auto tmp_sp = wp.lock()){ //it checks if tmp_sp is not empty
  tmp_sp → getParam();
} // the shared pointer tmp_sp goes out of scope

use_count() checks how many shared pointer points to that object

expired() checks if use_count() = 0
```

---

**Immagini estratte:**

![Figura estratta 1](images/p24_img01.jpg)

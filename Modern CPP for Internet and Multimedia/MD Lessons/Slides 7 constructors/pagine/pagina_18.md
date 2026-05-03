```json
{}: universal and uniform initialization

• a constructor can be called with ( ) or {} or = (in some cases)

• it is usually a good practice to use {} to highlight initialization is happening

• {} is defined as universal and uniform initialization
  X* p = new X{4}; // ok!
  X* p2 = new X=4; // wrong!

• The main reason to use ( ) instead of {} is to make sure a constructor is called for initialization
  • {} may mean a member-wise or initializer-list initialization

std::vector<int> v1 {77}; // 1 element with value 77
std::vector<int> v2 (77); // 77 elements with value 0
```

---

**Immagini estratte:**

![Figura estratta 1](images/p18_img01.jpg)

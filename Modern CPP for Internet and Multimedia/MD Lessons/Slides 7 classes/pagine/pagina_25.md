Static members

• A static member is a variable that is part of a class, but not of a specific object of the class
  • Before the first use, they must be defined!

• There is exactly one copy of a static variable per program

• Static member functions can be called without using an object

• They may introduce concurrency issues with multi-threaded programs

```java
class Date {
    int d, m, y;
    static Date default_date;
public:
    Date(int dd =0, int mm =0, int yy =0);
    // ...
    static void set_default(int dd, int mm, int yy);
    // set default_date to Date(dd,mm,yy)
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p25_img01.jpg)

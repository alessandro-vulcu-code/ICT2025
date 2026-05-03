Static members

```java
class Date {
    int d, m, y;
    static Date default_date;
public:
    Date(int dd =0, int mm =0, int yy =0);
    // ...
    static void set_default(int dd, int mm, int yy);
    // set default_date to Date(dd,mm,yy)
};

// implementation (also in some other parts of the program)

// definition of Date::default_date
Date Date::default_date {16,12,1770};

// definition of Date::set_default
void Date::set_default(int d, int m, int y) {
    // assign new value to default_date
    default_date = {d,m,y};
}
```

---

**Immagini estratte:**

![Figura estratta 1](images/p26_img01.jpg)

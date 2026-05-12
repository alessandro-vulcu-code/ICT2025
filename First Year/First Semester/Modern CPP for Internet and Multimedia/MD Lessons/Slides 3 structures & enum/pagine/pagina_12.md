enum class

enumerators

• Enumerators hold a set of integers named by the user
• In an enum class, the enumerators are
  • scoped – they do not exist out of the enum class and the same enumerator can be used in other enum classes without clashes
  • strongly typed – they do not convert implicitly to int

enum class TrafficLight {green, yellow, red};
TrafficLight a = TrafficLight::red;
int a2 = a; // compilation error
bool a3 {a = 2}; // compilation error

enum class Other {char {green, blue}; // no name clash!

int by default, but it can be changed

---

**Immagini estratte:**

![Figura estratta 1](images/p12_img01.jpg)

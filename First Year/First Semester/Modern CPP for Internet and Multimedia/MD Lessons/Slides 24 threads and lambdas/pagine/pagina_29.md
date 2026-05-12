Lambda function – syntax examples

a is passed by reference

[&a](int x) -> int
{ ... //body}

The function requires an integer parameter

The function returns an int

a is passed by value and can be modified (keyword mutable)

[a](() mutable
{ ... //body}

The function requires no parameters

The function returns nothing (void)

a is passed by value, b by reference

[a,&b](()
{ ... //body}

all passed by value

[=](()
{ ... //body}

all passed by reference

[&](()
{ ... //body}

---

**Immagini estratte:**

![Figura estratta 1](images/p29_img01.jpg)

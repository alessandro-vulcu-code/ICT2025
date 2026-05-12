Non-modifying sequence algorithms

Sequence predicates
• all_of(begin, end, fun)
• any_of(begin, end, fun)
• none_of(begin, end, fun)

fun makes a Boolean check on all the elements, and the predicates return
true if fun is always true
true if fun is true at least once
true if fun is always false

count (begin, end, v)
counts how many elements are equal to v

p=find (begin, end, v)
p points to the first element between begin and end equal to v (if no match, p=end)

---

**Immagini estratte:**

![Figura estratta 1](p23_img01.jpg)

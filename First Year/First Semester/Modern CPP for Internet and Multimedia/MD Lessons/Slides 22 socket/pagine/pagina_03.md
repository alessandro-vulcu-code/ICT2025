HW buffer – stack allocation

How do I create an empty buffer (with all bits set to 0) for the serialization?

Using a C-style array (hdr.serialize(buffer,offset)):

• char buffer[3]; // WRONG, IT HAS RANDOM VALUES
• char buffer[3] = {0,0,0};
• char buffer[3] = {0}; // others will be set to 0
• char buffer[3];
  memset(buffer, 0, max_size); // remember to #include "string.h"

Using a C++ std::array (hdr.serialize(b1.data(),offset)):

• std::array<char,3> b1 = {0}; // b1.data() provides direct access to its underlying C-style array

---

**Immagini estratte:**

![Figura estratta 1](images/p03_img01.jpg)

Send and receive buffer

• Send and receive data to and from socket by using a buffer
• The most usual way is to use a char array
• Operation needed before receive:
  1. `const size_t max_size = 256; // max size that can be received in a single read at maximum`
  2. `char rx_buf[max_size] = {0}; // create a rx buffer`
  3. `memset(buffer, 0, max_size); // before each read set all the buffer fields to 0 (not need at the first read)`
• Operation needed before transmit:
  1. `char tx_buf[256] = {0}; // create a tx buffer`
  2. `tx_buf = "ciao ciao"; // place the data to tx in the buffer`
  3. `size_t size2tx = 9; // save the size of the data to be tx`

---

**Immagini estratte:**

![Figura estratta 1](p22_img01.jpg)

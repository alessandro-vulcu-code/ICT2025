Huffman coding

Huffman discovered how to build the optimal lossless coder for any source with known probabilities. Steps:

1. Create leaf nodes for each symbol, weighted by $p_i$
2. While there’s more than one node:
   - Select two nodes with lowest weights
   - Create a new internal node as their parent
   - Set new node’s weight as sum of children’s weights
3. Assign '0' to left edges, '1' to right edges
4. Read code for each symbol from root to leaf

---

**Immagini estratte:**

![Figura estratta 1](images/p54_img01.jpg)

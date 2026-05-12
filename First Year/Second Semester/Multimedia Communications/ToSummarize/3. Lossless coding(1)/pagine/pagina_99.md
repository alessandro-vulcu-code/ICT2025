# LZW Encoding: Dictionary-Based Logic

## The Greedy Matching Process

- The encoder reads the input stream symbol by symbol.
- For each new input, it checks if the current pattern (Prefix $W + \text{Next } K$) already exists in the dictionary.
- Iterative Search: If $W + K$ is found, the encoder extends the search by reading the next symbol, continuing until a new pattern is encountered.

## Dictionary Evolution and Merging

- Once a new pattern $W + K$ is identified:
  1. The index of the longest known prefix ($W$) is sent to the bitstream.
  2. The new combined pattern ($W + K$) is added to the dictionary.
- Prefix Merging: This mechanism merges known prefixes with new suffixes, allowing the dictionary to naturally evolve and "track" local statistics.

---

**Immagini estratte:**

![Figura estratta 1](p99_img01.jpg)

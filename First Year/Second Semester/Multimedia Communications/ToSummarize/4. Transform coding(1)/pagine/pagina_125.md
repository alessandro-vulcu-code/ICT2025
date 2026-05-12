JPEG Standard: Example of entropy coding

Let us suppose that $DC_{n-1} = 1$. We have to encode:

$$-2 - DC_{n-1} = -3 \quad 0,17 \quad 0,3 \quad 1,4 \quad 0,3 \quad 0,1 \quad 5,-1 \quad 0,-1 \quad 4,-1 \quad 5,-1 \quad EOB$$

We have:

$$DC_p = -3 \quad \text{Category}=2 \rightarrow 011 \quad \text{Value}=-3 \rightarrow 00 \quad 01100$$
$$(R, V) = (0, 17) \quad \text{Run, Category} = (0,5) \rightarrow 11010 \quad \text{Value}=17 \rightarrow 10001 \quad 11010 \quad 10001$$
$$(R, V) = (0, 3) \quad \text{Run, Category} = (0,2) \rightarrow 01 \quad \text{Value}=3 \rightarrow 11 \quad 01 \quad 11$$
$$(R, V) = (1, 4) \quad \text{Run, Category} = (1,3) \rightarrow 1111001 \quad 100 \quad \text{Value}=4 \rightarrow 100 \quad 1101111$$
$$(R, V) = (0, 3) \quad \text{Run, Category} = (0,2) \rightarrow 01 \quad \text{Value}=3 \rightarrow 11 \quad 0111$$
$$(R, V) = (0, 1) \quad \text{Run, Category} = (0,1) \rightarrow 00 \quad \text{Value}=1 \rightarrow 1 \quad 00 \quad 1$$
$$(R, V) = (5, -1) \quad \text{Run, Category} = (5,1) \rightarrow 1111010 \quad \text{Value}=-1 \rightarrow 0 \quad 1111010 \quad 0$$
$$(R, V) = (0, -1) \quad \text{Run, Category} = (0,1) \rightarrow 00 \quad \text{Value}=-1 \rightarrow 0 \quad 00 \quad 0$$
$$(R, V) = (4, -1) \quad \text{Run, Category} = (4,1) \rightarrow 1111011 \quad \text{Value}=1 \rightarrow 1 \quad 1110111 \quad 1$$
$$(R, V) = (5, -1) \quad \text{Run, Category} = (5,1) \rightarrow 1111010 \quad \text{Value}=-1 \rightarrow 0 \quad 1111010 \quad 0$$
EOB

The block is encoded as:
0110011010100010111111001100011100111101010000111011011101001010

Note that this is a prefix-code, thus no "separator" is needed.

We use 66 bits per 64 pixels, averaging $\approx 1.03$ bpp

Note also that it is difficult to tell in advance the number of bits used to encode a block as a function of the quality factor or of the quantization table: thus rate control is not a feature of JPEG.

---

**Immagini estratte:**

![Figura estratta 1](images/p125_img01.jpg)

import os
import glob
import re

descriptions = {
    "images/p04_img01.png": "An abstract illustration showing solid blocks of yellow, cyan, and small squares of dark red and dark blue, representing discrete mapping/indices.",
    "images/p04_img02.png": "An abstract graphic composed of vertical and horizontal overlapping translucent colored rectangles/stripes, representing mapping to a bitstream.",
    "images/p04_img03.png": "An abstract grayscale image showing large rectangular pixels or blocks, demonstrating quantization or pixelated source material.",
    "images/p15_img01.png": "A text snippet listing the prefix code: A: 00, B: 010, C: 1, and the depth definition L_max = 3.",
    "images/p16_img01.png": "A complete, uncolored binary tree diagram down to depth 3, showing the root node splitting into 0 and 1, leading to 8 leaf nodes (000 to 111).",
    "images/p17_img01.png": "A complete binary tree of depth 3 with a dashed ellipse circling all 8 leaf nodes, labeled 2^{L_max}, representing the total capacity of the tree.",
    "images/p18_img01.png": "A binary tree of depth 3 with node 00 highlighted in green. Its descendant leaf nodes (000 and 001) have dashed outlines, illustrating the subtree is blocked by the codeword 00.",
    "images/p19_img01.png": "A binary tree with node 00 in green, and its two dashed descendant leaves enclosed in a dashed ellipse labeled 2^{L_max - l_1}, quantifying the blocked capacity.",
    "images/p20_img01.png": "A binary tree highlighting node 00 and node 010 in green. Since 010 is a leaf node, it occupies only itself.",
    "images/p21_img01.png": "A binary tree showing the leaves occupied by codewords 00 and 010 enclosed together in a dashed ellipse labeled 2^{L_max - l_1} + 2^{L_max - l_2}.",
    "images/p22_img01.png": "A binary tree highlighting all three codewords (00, 010, and 1) in green. The entire right half of the tree (all descendants of node 1) are drawn with dashed outlines to show they are blocked.",
    "images/p23_img01.png": "A binary tree diagram showing all blocked leaf nodes grouped into two dashed ellipses with the label 2^{L_max - l_1} + 2^{L_max - l_2} + 2^{L_max - l_3}, proving Kraft's inequality.",
    "images/p62_img01.png": "A pixel grid showing a black 'T' shape. Basic single-pixel probabilities are listed: P(white) = 86.7% and P(black) = 13.3%.",
    "images/p70_img01.png": "A pixel grid of a 'T' shape displaying probabilities for pairs of pixels (Block coding, K=2), e.g., P(white,white) = 80.0%.",
    "images/p71_img01.png": "A pixel grid of a 'T' shape accompanied by probabilities for 4-pixel blocks (K=4), illustrating block coding.",
    "images/p87_img01.png": "A pixel grid of a 'T' shape displaying 1D conditional probabilities, used to explain Context-Based Arithmetic Coding.",
    "images/p158_img01.png": "A grayscale photograph of a house with a complex roof structure and an antenna, used as a baseline test image for lossless compression.",
    "images/p158_img02.png": "A luminance histogram (gray-level relative frequency) of the raw house image, showing a broad distribution of pixel values across the 0-255 range on a logarithmic scale.",
    "images/p160_img01.png": "A histogram of prediction errors using a 1D horizontal spatial predictor. The errors are compressed into a tight, laplacian-like spike centered at 0.",
    "images/p161_img01.png": "A histogram of prediction errors using an advanced 2D neighborhood predictor, showing an even tighter central spike at 0 than the 1D prediction.",
    "images/p162_img01.png": "A side-by-side heat map of absolute prediction errors (in log scale). The left image uses a 1D predictor, and the right uses a 2D predictor.",
    "images/p171_img01.png": "A side-by-side heat map comparing Neural Predictor errors (left) with 2D Predictor errors (right). The Neural Predictor's map is cleaner and more uniform.",
    "images/p173_img01.png": "A histogram of prediction errors for the Neural Predictor, demonstrating a highly concentrated, sharp distribution around 0.",
    "images/p180_img01.png": "A histogram of prediction errors for the Neural Predictor, identical to the one on page 173.",
    "images/p180_img02.png": "A side-by-side heat map comparing Neural Predictor errors with 2D Predictor errors, identical to the one on page 171."
}

files = glob.glob("ToSummarize/3. Lossless coding/**/*.md", recursive=True)
for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    changed = False
    for img_path, description in descriptions.items():
        pattern = r"(!\[.*?\]\(" + re.escape(img_path) + r"\))(?!\n\n\*Description:)"
        replacement = r"\1\n\n*Description: " + description + "*"
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            content = new_content
            changed = True

    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {file_path}")

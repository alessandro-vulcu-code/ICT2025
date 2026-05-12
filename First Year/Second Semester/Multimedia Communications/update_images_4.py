import os
import glob
import re

descriptions = {
    "images/p57_img01.png": "A 3D scatter plot of a data distribution in the Original Spatial Domain, showing a highly correlated elongated cluster along a diagonal.",
    "images/p57_img02.png": "A 3D scatter plot in the KLT Transformed Domain, showing the same data cluster now aligned with the principal axes, demonstrating decorrelation.",
    "images/p62_img01.png": "Band 1 of a grayscale multi-spectral satellite image.",
    "images/p62_img02.png": "Band 2 of a grayscale multi-spectral satellite image.",
    "images/p62_img03.png": "Band 3 of a grayscale multi-spectral satellite image.",
    "images/p62_img04.png": "Band 4 of a grayscale multi-spectral satellite image.",
    "images/p62_img05.png": "Band 5 of a grayscale multi-spectral satellite image.",
    "images/p62_img06.png": "Band 6 of a grayscale multi-spectral satellite image.",
    "images/p63_img01.png": "Eigenband 1 from the KLT of the multi-spectral image, capturing most of the structural information.",
    "images/p63_img02.png": "Eigenband 2 from the KLT.",
    "images/p63_img03.png": "Eigenband 3 from the KLT.",
    "images/p63_img04.png": "Eigenband 4 from the KLT, appearing mostly as noise.",
    "images/p63_img05.png": "Eigenband 5 from the KLT, appearing mostly as noise.",
    "images/p63_img06.png": "Eigenband 6 from the KLT, appearing mostly as noise.",
    "images/p71_img01.png": "A 2D-DFT magnitude spectrum (log scale) of the house image, showing bright horizontal and vertical lines crossing at the center, illustrating frequency leakage.",
    "images/p71_img02.png": "A grayscale photograph of a house roof with a TV antenna.",
    "images/p72_img01.png": "A 2D-DFT magnitude spectrum (log scale) of the Lena image, showing frequency leakage with bright lines crossing at the center.",
    "images/p72_img02.png": "A grayscale photograph of Lena.",
    "images/p73_img01.png": "A 2D-DFT magnitude spectrum (log scale) of the strawberries and coffee image, showing the cross-like frequency leakage pattern.",
    "images/p73_img02.png": "A grayscale photograph of strawberries in a bowl next to a coffee cup.",
    "images/p74_img01.png": "A 2D-DFT magnitude spectrum (log scale) of the peppers image, displaying cross-like spectral leakage.",
    "images/p74_img02.png": "A grayscale photograph of various peppers.",
    "images/p77_img01.png": "A 3x3 periodized grid tiling of the house image.",
    "images/p77_img02.png": "A 3x3 periodized grid tiling of the house image.",
    "images/p78_img01.png": "A 3x3 periodized grid tiling of the Lena image.",
    "images/p78_img02.png": "A 3x3 periodized grid tiling of the Lena image.",
    "images/p79_img01.png": "A 3x3 periodized grid tiling of the strawberries image.",
    "images/p79_img02.png": "A 3x3 periodized grid tiling of the strawberries image.",
    "images/p80_img01.png": "A 3x3 periodized grid tiling of the peppers image.",
    "images/p80_img02.png": "A 3x3 periodized grid tiling of the peppers image.",
    "images/p88_img01.png": "A 2D-DCT spectrum (log scale) showing traces corresponding to two dominant directions in the image.",
    "images/p88_img02.png": "A grayscale microscopic image of a cantilever or MEMS structure with distinct diagonal features.",
    "images/p89_img01.png": "A 2D-DCT spectrum showing multiple traces and distinct impulse peaks representing the periodic background.",
    "images/p89_img02.png": "A grayscale photograph of multiple matchsticks randomly scattered on a textured fabric background.",
    "images/p89_img03.png": "A 2D-DCT spectrum of the vertically aligned matchsticks, showing fewer traces but retaining the impulses from the fabric background.",
    "images/p89_img04.png": "A grayscale photograph of multiple matchsticks aligned vertically on a textured fabric background.",
    "images/p90_img01.png": "A 1D histogram titled '2D-DCT of house: Percent relative frequency', showing a very sharp peak around 0.",
    "images/p90_img02.png": "A 1D histogram of the house image's pixel values, showing a broad distribution.",
    "images/p90_img03.png": "A 2D-DCT spectrum of the house image.",
    "images/p90_img04.png": "The original grayscale house image.",
    "images/p91_img01.png": "A 1D histogram titled '2D-DCT of lena: Percent relative frequency'.",
    "images/p91_img02.png": "A 1D histogram of the Lena image's pixel values.",
    "images/p91_img03.png": "A 2D-DCT spectrum of the Lena image.",
    "images/p91_img04.png": "The original grayscale Lena image.",
    "images/p92_img01.png": "A 1D histogram titled '2D-DCT of coffee: Percent relative frequency'.",
    "images/p92_img02.png": "A 1D histogram of the strawberries and coffee image's pixel values.",
    "images/p92_img03.png": "A 2D-DCT spectrum of the strawberries and coffee image.",
    "images/p92_img04.png": "The original grayscale image of strawberries and a coffee cup.",
    "images/p93_img01.png": "A 1D histogram titled '2D-DCT of peppers: Percent relative frequency'.",
    "images/p93_img02.png": "A 1D histogram of the peppers image's pixel values.",
    "images/p93_img03.png": "A 2D-DCT spectrum of the peppers image.",
    "images/p93_img04.png": "The original grayscale peppers image.",
    "images/p94_img01.png": "A grid showing the 64 basis functions of an 8x8 Discrete Cosine Transform.",
    "images/p95_img01.png": "A zoomed-in block-based DCT coefficient representation of the strawberries image.",
    "images/p95_img02.png": "An 8x8 block-based DCT coefficient representation of the strawberries image, showing high-energy coefficients as bright spots at the top-left of each block.",
    "images/p95_img03.png": "The original grayscale image of strawberries and coffee.",
    "images/p96_img01.png": "A zoomed-in block-based DCT representation for the peppers image.",
    "images/p96_img02.png": "An 8x8 block-based DCT coefficient representation of the peppers image.",
    "images/p96_img03.png": "The original grayscale peppers image.",
    "images/p99_img01.png": "A color photograph of peppers (resource allocation example variant).",
    "images/p99_img02.png": "A color photograph of peppers (resource allocation example variant).",
    "images/p99_img03.png": "A color photograph of peppers (resource allocation example variant).",
    "images/p99_img04.png": "A color photograph of peppers (resource allocation example variant).",
    "images/p115_img01.png": "A reconstructed 8x8 pixel block (zoomed in, grayscale), showing some compression artifacts.",
    "images/p115_img02.png": "The original 8x8 pixel block (zoomed in, grayscale).",
    "images/p126_img01.png": "A block diagram showing the overall JPEG file format structure (Start of Image, Frame Header, Frame, End of Image).",
    "images/p127_img01.png": "A block diagram detailing the hierarchical structure of a JPEG frame into Scans, Segments, and Blocks.",
    "images/p130_img01.png": "The original color Lena image, uncompressed.",
    "images/p131_img01.png": "The reconstructed color Lena image compressed at Rate=1.02 bpp.",
    "images/p132_img01.png": "The reconstructed color Lena image compressed at Rate=0.75 bpp.",
    "images/p133_img01.png": "The reconstructed color Lena image compressed at Rate=0.50 bpp.",
    "images/p134_img01.png": "The reconstructed color Lena image compressed at Rate=0.31 bpp, showing visible blocking artifacts.",
    "images/p135_img01.png": "The reconstructed color Lena image compressed at Rate=0.21 bpp, showing severe blocking artifacts."
}

files = glob.glob("ToSummarize/4. Transform coding/**/*.md", recursive=True)
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

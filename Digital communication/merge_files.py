def merge_files():
    with open('DigiCom.tex', 'r', encoding='utf-8') as f:
        preamble_content = f.read()
    
    # Remove the placeholder and \end{document}
    preamble_content = preamble_content.replace('% Content will be inserted here', '')
    preamble_content = preamble_content.replace('\\end{document}', '')
    
    with open('formatted_text.tex', 'r', encoding='utf-8') as f:
        body_content = f.read()
        
    final_content = preamble_content + "\n" + body_content + "\n\\end{document}"
    
    with open('DigiCom.tex', 'w', encoding='utf-8') as f:
        f.write(final_content)

if __name__ == "__main__":
    merge_files()

import re

def clean_text(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cleaned_lines = []
    skip_patterns = [
        r'^\d+_pp_\d+_\d+_',  # Matches lines like 08.4_pp_209_294...
        r'^\d{4}\.\d+_pp_',   # Matches lines like 1108.1_pp_...
        r'^\f',               # Form feed characters
        r'^page \d+$',        # Page numbers
        r'^page$',
    ]

    for line in lines:
        # Remove form feed characters
        line = line.replace('\f', '')
        
        # Check if line matches any skip pattern
        should_skip = False
        for pattern in skip_patterns:
            if re.search(pattern, line.strip()):
                should_skip = True
                break
        
        if should_skip:
            continue
            
        # Basic Math Conversions
        line = line.replace('log 2', '\\log_2')
        line = line.replace('∫', '\\int')
        line = line.replace('∞', '\\infty')
        line = line.replace('√', '\\sqrt')
        line = line.replace('≠', '\\neq')
        line = line.replace('≤', '\\leq')
        line = line.replace('≥', '\\geq')
        line = line.replace('∼', '\\sim')
        line = line.replace('μ', '\\mu')
        line = line.replace('π', '\\pi')
        line = line.replace('σ', '\\sigma')
        line = line.replace('ρ', '\\rho')
        line = line.replace('ν', '\\nu')
        line = line.replace('⋆', '^\\star')
        
        cleaned_lines.append(line)

    # Join lines to fix broken paragraphs (simple heuristic)
    # If a line ends with a lowercase letter and the next starts with a lowercase, join them.
    # This is risky for poetry but might work for prose. 
    # For now, let's just write the lines and do manual cleanup later.
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)

if __name__ == "__main__":
    clean_text('extracted_text.txt', 'cleaned_text.txt')

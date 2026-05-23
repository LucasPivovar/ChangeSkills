import glob
import re

html_files = glob.glob('c:/Users/patov/Documents/Projects/ChangeSkills/ChangeSkills/**/*.html', recursive=True)

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace \' with '
    new_content = content.replace(r"\'", "'")
    
    # Remove 'reveal' from verificacao-certificado.html and solicitacao-certificado.html to fix missing form
    if 'verificacao-certificado.html' in file_path or 'solicitacao-certificado.html' in file_path:
        new_content = new_content.replace('class="glass-card reveal"', 'class="glass-card"')
        new_content = new_content.replace('class="container reveal active"', 'class="container active"')

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {file_path}")

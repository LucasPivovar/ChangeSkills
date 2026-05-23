import os
import glob
import re

base_path = r"c:\Users\patov\Documents\Projects\ChangeSkills\ChangeSkills"
html_files = glob.glob(os.path.join(base_path, "**", "*.html"), recursive=True)

updated = 0
for file in html_files:
    rel_path = os.path.relpath(file, base_path)
    depth = rel_path.count(os.sep)
    prefix = "../" * depth if depth > 0 else ""
    link_path = prefix + "area-do-aluno.html"
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace href="#" for the Área do Aluno link.
    # We can split the content by 'Área do Aluno', find the closest preceding '<a href="#"' and replace '#' with link_path
    
    parts = content.split('Área do Aluno')
    new_content = parts[0]
    for i in range(1, len(parts)):
        # Look backwards in new_content for the last '<a '
        last_a_idx = new_content.rfind('<a ')
        if last_a_idx != -1:
            # Check if it has href="#"
            # We replace only the LAST occurrence of href="#" after last_a_idx
            href_idx = new_content.rfind('href="#"', last_a_idx)
            if href_idx != -1:
                new_content = new_content[:href_idx] + f'href="{link_path}"' + new_content[href_idx+8:]
        new_content += 'Área do Aluno' + parts[i]
        
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated += 1
        print(f"Updated {rel_path}")

print(f"Total files updated with Area do Aluno link: {updated}")

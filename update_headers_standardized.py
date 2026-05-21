import os
import re
import glob

base_path = r"c:\Users\patov\OneDrive\Área de Trabalho\Code\Change Skills"
html_files = glob.glob(os.path.join(base_path, "**", "*.html"), recursive=True)

def get_nav_html(depth):
    prefix = "../" * depth
    
    # Paths based on depth
    inicio = f"{prefix}index.html"
    escola = f"{prefix}nossa-escola.html"
    cursos = f"{prefix}index.html#cursos"
    contato = f"{prefix}contato.html"
    
    return f'''<ul class="nav-list" style="display: flex; gap: 3rem; list-style: none; align-items: center;">
                <li style="position: relative;">
                    <a href="{inicio}" style="text-decoration: none; color: var(--primary-dark); font-weight: 600; font-size: 1.1rem; transition: color 0.3s; display: block; padding: 0.5rem 0;" 
                       onmouseover="this.style.color='var(--primary)'; this.querySelector('.nav-line').style.width='100%'" 
                       onmouseout="this.style.color='var(--primary-dark)'; this.querySelector('.nav-line').style.width='0%'">
                        Início
                        <span class="nav-line" style="position: absolute; bottom: 0; left: 0; width: 0; height: 2px; background: var(--primary); transition: width 0.3s;"></span>
                    </a>
                </li>
                <li style="position: relative;">
                    <a href="{escola}" style="text-decoration: none; color: var(--primary-dark); font-weight: 600; font-size: 1.1rem; transition: color 0.3s; display: block; padding: 0.5rem 0;" 
                       onmouseover="this.style.color='var(--primary)'; this.querySelector('.nav-line').style.width='100%'" 
                       onmouseout="this.style.color='var(--primary-dark)'; this.querySelector('.nav-line').style.width='0%'">
                        Nossa Escola
                        <span class="nav-line" style="position: absolute; bottom: 0; left: 0; width: 0; height: 2px; background: var(--primary); transition: width 0.3s;"></span>
                    </a>
                </li>
                <li style="position: relative;">
                    <a href="{cursos}" style="text-decoration: none; color: var(--primary-dark); font-weight: 600; font-size: 1.1rem; transition: color 0.3s; display: block; padding: 0.5rem 0;" 
                       onmouseover="this.style.color='var(--primary)'; this.querySelector('.nav-line').style.width='100%'" 
                       onmouseout="this.style.color='var(--primary-dark)'; this.querySelector('.nav-line').style.width='0%'">
                        Cursos
                        <span class="nav-line" style="position: absolute; bottom: 0; left: 0; width: 0; height: 2px; background: var(--primary); transition: width 0.3s;"></span>
                    </a>
                </li>
                <li style="position: relative;">
                    <a href="{contato}" style="text-decoration: none; color: var(--primary-dark); font-weight: 600; font-size: 1.1rem; transition: color 0.3s; display: block; padding: 0.5rem 0;" 
                       onmouseover="this.style.color='var(--primary)'; this.querySelector('.nav-line').style.width='100%'" 
                       onmouseout="this.style.color='var(--primary-dark)'; this.querySelector('.nav-line').style.width='0%'">
                        Contato
                        <span class="nav-line" style="position: absolute; bottom: 0; left: 0; width: 0; height: 2px; background: var(--primary); transition: width 0.3s;"></span>
                    </a>
                </li>
            </ul>'''

# Pattern to match the nav-list block
pattern = re.compile(r'<ul class="nav-list"[^>]*>[\s\S]*?</ul>')

updated_count = 0
for file in html_files:
    rel_path = os.path.relpath(file, base_path)
    parts = rel_path.split(os.path.sep)
    depth = len(parts) - 1
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if pattern.search(content):
        nav_html = get_nav_html(depth)
        new_content = pattern.sub(nav_html, content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Updated header in: {rel_path} (depth={depth})")
        updated_count += 1
    else:
        print(f"No nav-list match in: {rel_path}")

print(f"Done! Replaced header in {updated_count} files.")

import glob
import re

files = glob.glob('c:/Users/patov/Documents/Projects/ChangeSkills/ChangeSkills/cursos/modalidades/*.html')

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the section and replace its container start and the text div
    pattern = re.compile(
        r'<div class="container" style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">\s*<div class="reveal">.*?</div>\s*<div class="glass-card reveal" style="background: white; padding: 3rem; border-radius: 30px; box-shadow: 0 30px 60px rgba\(0,0,0,0\.08\); border: 1px solid rgba\(0,0,0,0\.03\); position: relative;">',
        re.DOTALL
    )

    replacement = '''<div class="container" style="max-width: 800px; margin: 0 auto;">
                <h2 style="font-size: 2.5rem; color: var(--primary-dark); text-align: center; margin-bottom: 3rem;">Agende sua aula experimental</h2>
                <div class="glass-card reveal" style="background: white; padding: 4rem; border-radius: 40px; box-shadow: 0 30px 60px rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.03); position: relative;">'''

    new_content = pattern.sub(replacement, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")

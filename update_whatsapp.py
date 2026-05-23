import os
import glob
import re

base_path = r"c:\Users\patov\Documents\Projects\ChangeSkills\ChangeSkills"
html_files = []

# Get all html files in all directories and subdirectories
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

updated = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "https://wa.me/5549999124040" in content:
        new_content = content.replace("https://wa.me/5549999124040", "https://wa.me/555481223965")
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated += 1
        print(f"Updated whatsapp number in {os.path.relpath(file, base_path)}")

print(f"Total files updated: {updated}")

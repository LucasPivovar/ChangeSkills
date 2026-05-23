import os
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

count = 0
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    footer_pattern = re.compile(r'(<footer.*?>.*?</footer>)', re.DOTALL | re.IGNORECASE)
    
    def update_footer(match):
        footer_html = match.group(1)
        
        # Replace h4 tags to have the standard accent color
        footer_html = re.sub(r'<h4[^>]*>', r'<h4 style="color: var(--accent); margin-bottom: 2.5rem; font-size: 1.2rem;">', footer_html)
        
        # The links should be white with accent hover. We need to be careful not to break the href.
        # This regex captures the href part and replaces everything else in the tag.
        footer_html = re.sub(
            r'<a\s+href="([^"]+)"(?:\s+style="[^"]*")?(?:\s+onmouseover="[^"]*")?(?:\s+onmouseout="[^"]*")?[^>]*>',
            r'<a href="\1" style="color: white; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color=\'var(--accent)\'" onmouseout="this.style.color=\'white\'">',
            footer_html
        )
        
        return footer_html

    new_content = footer_pattern.sub(update_footer, content)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated footers in {count} files.")

import os
import glob

# Path to the workspace
base_path = r"c:\Users\patov\OneDrive\Área de Trabalho\Code\Change Skills"
html_files = glob.glob(os.path.join(base_path, "**", "*.html"), recursive=True)

nav_target = '<ul style="display: flex; gap: 3rem; list-style: none; align-items: center;">'
nav_replacement = '''
            <button class="mobile-menu-btn" style="display: none; background: transparent; border: none; cursor: pointer; color: var(--primary-dark); z-index: 1001;">
                <i data-lucide="menu" style="width: 32px; height: 32px;"></i>
            </button>
            <ul class="nav-list" style="display: flex; gap: 3rem; list-style: none; align-items: center;">'''

header_end_target = '</header>'
header_end_replacement = '''</header>

    <div class="menu-overlay"></div>'''

script_block = '''
        // Mobile Menu Toggle
        const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
        const navList = document.querySelector('.nav-list');
        const navLinks = document.querySelectorAll('.nav-list a');
        const menuOverlay = document.querySelector('.menu-overlay');

        if(mobileMenuBtn && navList) {
            mobileMenuBtn.addEventListener('click', () => {
                navList.classList.toggle('active');
                if(menuOverlay) menuOverlay.classList.toggle('active');
                
                const icon = mobileMenuBtn.querySelector('i');
                if(navList.classList.contains('active')) {
                    icon.setAttribute('data-lucide', 'x');
                } else {
                    icon.setAttribute('data-lucide', 'menu');
                }
                lucide.createIcons();
            });

            // Close menu when a link is clicked
            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    navList.classList.remove('active');
                    if(menuOverlay) menuOverlay.classList.remove('active');
                    mobileMenuBtn.querySelector('i').setAttribute('data-lucide', 'menu');
                    lucide.createIcons();
                });
            });

            // Close menu when overlay is clicked
            if(menuOverlay) {
                menuOverlay.addEventListener('click', () => {
                    navList.classList.remove('active');
                    menuOverlay.classList.remove('active');
                    mobileMenuBtn.querySelector('i').setAttribute('data-lucide', 'menu');
                    lucide.createIcons();
                });
            }
        }
'''

for file in html_files:
    if "index.html" in file:
        continue # index.html is already done
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False

    if nav_target in content:
        content = content.replace(nav_target, nav_replacement)
        changed = True

    if header_end_target in content and '<div class="menu-overlay"></div>' not in content:
        content = content.replace(header_end_target, header_end_replacement)
        changed = True

    if 'const mobileMenuBtn =' not in content and 'lucide.createIcons();' in content:
        # Some files might have multiple lucide.createIcons(), we only want to append it to the first script block or just replace all instances, but usually it's at the bottom
        # Let's replace the first one that appears inside a script tag
        parts = content.split('lucide.createIcons();', 1)
        if len(parts) == 2:
            content = parts[0] + 'lucide.createIcons();' + script_block + parts[1]
            changed = True

    if changed:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

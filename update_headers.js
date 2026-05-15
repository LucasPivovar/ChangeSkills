const fs = require('fs');
const path = require('path');

const basePath = path.join(__dirname);

function getHtmlFiles(dir, fileList = []) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const filePath = path.join(dir, file);
        if (fs.statSync(filePath).isDirectory()) {
            if (!filePath.includes('.git') && !filePath.includes('assets')) {
                getHtmlFiles(filePath, fileList);
            }
        } else if (file.endsWith('.html') && file !== 'index.html') {
            fileList.push(filePath);
        }
    }
    return fileList;
}

const htmlFiles = getHtmlFiles(basePath);

const navTarget = '<ul style="display: flex; gap: 3rem; list-style: none; align-items: center;">';
const navReplacement = `
            <button class="mobile-menu-btn" style="display: none; background: transparent; border: none; cursor: pointer; color: var(--primary-dark); z-index: 1001;">
                <i data-lucide="menu" style="width: 32px; height: 32px;"></i>
            </button>
            <ul class="nav-list" style="display: flex; gap: 3rem; list-style: none; align-items: center;">`;

const headerEndTarget = '</header>';
const headerEndReplacement = `</header>

    <div class="menu-overlay"></div>`;

const scriptBlock = `
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
`;

let count = 0;

for (const file of htmlFiles) {
    let content = fs.readFileSync(file, 'utf8');
    let changed = false;

    if (content.includes(navTarget)) {
        content = content.replace(navTarget, navReplacement);
        changed = true;
    }

    if (content.includes(headerEndTarget) && !content.includes('<div class="menu-overlay"></div>')) {
        content = content.replace(headerEndTarget, headerEndReplacement);
        changed = true;
    }

    if (!content.includes('const mobileMenuBtn =') && content.includes('lucide.createIcons();')) {
        // Find the first lucide.createIcons() and append scriptBlock
        const parts = content.split('lucide.createIcons();');
        if (parts.length > 1) {
            content = parts[0] + 'lucide.createIcons();' + scriptBlock + parts.slice(1).join('lucide.createIcons();');
            changed = true;
        }
    }

    if (changed) {
        fs.writeFileSync(file, content, 'utf8');
        console.log(`Updated: ${file}`);
        count++;
    }
}

console.log(`Update complete. Modified ${count} files.`);

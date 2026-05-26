/**
 * VIP Premium Multilingual System for Change Skills Idiomas
 * Dynamic client-side language switcher (PT, EN, ES, FR)
 */

(function() {
    // 1. Inject hidden Google Translate container
    const gtContainer = document.createElement('div');
    gtContainer.id = 'google_translate_element';
    gtContainer.style.position = 'absolute';
    gtContainer.style.top = '-9999px';
    gtContainer.style.left = '-9999px';
    gtContainer.style.width = '1px';
    gtContainer.style.height = '1px';
    gtContainer.style.overflow = 'hidden';
    gtContainer.style.opacity = '0';
    document.body.appendChild(gtContainer);

    // 2. Define standard Google Translate initialization callback
    window.googleTranslateElementInit = function() {
        new google.translate.TranslateElement({
            pageLanguage: 'pt',
            includedLanguages: 'pt,en,es,fr',
            layout: google.translate.TranslateElement.InlineLayout.SIMPLE,
            autoDisplay: false
        }, 'google_translate_element');
        
        // Once initialized, apply stored language if not default
        setTimeout(applyStoredLanguage, 800);
    };

    // 3. Load the official Google Translate widget script
    const script = document.createElement('script');
    script.src = 'https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
    script.defer = true;
    document.body.appendChild(script);

    // 4. Inject visual language switcher dropdown on DOMContentLoaded
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', injectLanguageSwitcher);
    } else {
        injectLanguageSwitcher();
    }

    function injectLanguageSwitcher() {
        const navList = document.querySelector('.nav-list');
        if (!navList) return;

        // Prevent duplicate rendering
        if (document.querySelector('.lang-switcher')) return;

        const switcherLi = document.createElement('li');
        switcherLi.style.position = 'relative';
        switcherLi.className = 'lang-switcher-li';
        
        switcherLi.innerHTML = `
            <div class="lang-switcher" style="position: relative; display: inline-block;">
                <button type="button" class="lang-btn" style="background: rgba(0, 71, 255, 0.05); border: 1px solid rgba(0, 71, 255, 0.1); padding: 0.6rem 1.2rem; border-radius: 99px; cursor: pointer; display: flex; align-items: center; gap: 8px; color: var(--primary-dark); font-weight: 600; font-size: 0.95rem; transition: var(--transition);">
                    <i data-lucide="globe" style="width: 16px; height: 16px;"></i>
                    <span class="lang-current">PT</span>
                    <i data-lucide="chevron-down" style="width: 14px; height: 14px; transition: transform 0.3s;"></i>
                </button>
                <div class="lang-dropdown" style="display: none; position: absolute; top: calc(100% + 10px); right: 0; background: rgba(255, 255, 255, 0.92); backdrop-filter: blur(20px); border: 1px solid rgba(0, 71, 255, 0.08); border-radius: 20px; box-shadow: var(--shadow-premium); min-width: 180px; z-index: 1000; overflow: hidden; padding: 0.5rem; flex-direction: column; gap: 4px;">
                    <button type="button" class="lang-option" data-lang="pt" style="background: transparent; border: none; padding: 0.8rem 1rem; text-align: left; cursor: pointer; border-radius: 12px; font-weight: 600; display: flex; align-items: center; gap: 10px; font-size: 0.9rem; color: var(--primary-dark); transition: var(--transition); width: 100%;">
                        <span style="font-size: 1.1rem;">🇧🇷</span> Português (PT)
                    </button>
                    <button type="button" class="lang-option" data-lang="en" style="background: transparent; border: none; padding: 0.8rem 1rem; text-align: left; cursor: pointer; border-radius: 12px; font-weight: 600; display: flex; align-items: center; gap: 10px; font-size: 0.9rem; color: var(--primary-dark); transition: var(--transition); width: 100%;">
                        <span style="font-size: 1.1rem;">🇺🇸</span> English (EN)
                    </button>
                    <button type="button" class="lang-option" data-lang="es" style="background: transparent; border: none; padding: 0.8rem 1rem; text-align: left; cursor: pointer; border-radius: 12px; font-weight: 600; display: flex; align-items: center; gap: 10px; font-size: 0.9rem; color: var(--primary-dark); transition: var(--transition); width: 100%;">
                        <span style="font-size: 1.1rem;">🇪🇸</span> Español (ES)
                    </button>
                    <button type="button" class="lang-option" data-lang="fr" style="background: transparent; border: none; padding: 0.8rem 1rem; text-align: left; cursor: pointer; border-radius: 12px; font-weight: 600; display: flex; align-items: center; gap: 10px; font-size: 0.9rem; color: var(--primary-dark); transition: var(--transition); width: 100%;">
                        <span style="font-size: 1.1rem;">🇫🇷</span> Français (FR)
                    </button>
                </div>
            </div>
        `;

        navList.appendChild(switcherLi);

        // Render Lucide icons if available
        if (window.lucide) {
            window.lucide.createIcons();
        }

        const langBtn = switcherLi.querySelector('.lang-btn');
        const langDropdown = switcherLi.querySelector('.lang-dropdown');
        const chevron = langBtn.querySelector('[data-lucide="chevron-down"]');

        // Toggle dropdown open/closed
        langBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            const isOpen = langDropdown.style.display === 'flex';
            langDropdown.style.display = isOpen ? 'none' : 'flex';
            if (chevron) {
                chevron.style.transform = isOpen ? 'rotate(0)' : 'rotate(180deg)';
            }
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', function() {
            langDropdown.style.display = 'none';
            if (chevron) {
                chevron.style.transform = 'rotate(0)';
            }
        });

        // Handle language option clicks
        const options = switcherLi.querySelectorAll('.lang-option');
        options.forEach(function(opt) {
            opt.addEventListener('click', function(e) {
                e.stopPropagation();
                const lang = opt.getAttribute('data-lang');
                changeLanguage(lang);
                langDropdown.style.display = 'none';
                if (chevron) {
                    chevron.style.transform = 'rotate(0)';
                }
            });
        });

        // Sync visual UI state with current language choice
        const currentLang = localStorage.getItem('selectedLanguage') || 'pt';
        updateSwitcherUI(currentLang);
    }

    function updateSwitcherUI(lang) {
        const langLabel = document.querySelector('.lang-current');
        if (langLabel) {
            langLabel.textContent = lang.toUpperCase();
        }
        
        // Highlight chosen language, reset others
        document.querySelectorAll('.lang-option').forEach(function(opt) {
            const isCurrent = opt.getAttribute('data-lang') === lang;
            if (isCurrent) {
                opt.style.background = 'rgba(0, 71, 255, 0.08)';
                opt.style.color = 'var(--primary)';
            } else {
                opt.style.background = 'transparent';
                opt.style.color = 'var(--primary-dark)';
            }
        });
    }

    function changeLanguage(langCode) {
        const translateSelect = document.querySelector('.goog-te-combo');
        if (translateSelect) {
            translateSelect.value = langCode;
            translateSelect.dispatchEvent(new Event('change'));
            localStorage.setItem('selectedLanguage', langCode);
            updateSwitcherUI(langCode);
        } else {
            // If combo-box is not loaded yet, wait and try again
            setTimeout(function() {
                changeLanguage(langCode);
            }, 150);
        }
    }

    function applyStoredLanguage() {
        const storedLang = localStorage.getItem('selectedLanguage');
        if (storedLang && storedLang !== 'pt') {
            changeLanguage(storedLang);
        }
    }
})();

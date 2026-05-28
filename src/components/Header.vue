<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { Globe, ChevronDown, Menu, X } from '@lucide/vue'
import { currentLang, t } from '@/i18n'

const router = useRouter()
const isMobileMenuOpen = ref(false)
const isDropdownOpen = ref(false)

const languages = [
  { code: 'pt', label: 'Português (PT)', flag: '🇧🇷' },
  { code: 'en', label: 'English (EN)', flag: '🇺🇸' },
  { code: 'es', label: 'Español (ES)', flag: '🇪🇸' },
  { code: 'fr', label: 'Français (FR)', flag: '🇫🇷' }
]

function toggleMobileMenu() {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}

function closeMobileMenu() {
  isMobileMenuOpen.value = false
}

function toggleDropdown(e) {
  e.stopPropagation()
  isDropdownOpen.value = !isDropdownOpen.value
}

function closeDropdown() {
  isDropdownOpen.value = false
}

// Close dropdown when clicking anywhere else
onMounted(() => {
  document.addEventListener('click', closeDropdown)
})

function changeLanguage(langCode) {
  currentLang.value = langCode
  closeDropdown()
}

// Scroll behavior fallback for route hashes
function handleLinkClick(hash) {
  closeMobileMenu()
  if (hash) {
    router.push({ path: '/', hash: hash })
  }
}
</script>

<template>
  <header class="global-header">
    <nav class="container nav-container">
      <!-- Logo Brand -->
      <RouterLink to="/" class="logo-link">
        <img src="/assets/img/logo-change.png?v=2" alt="Logo Change Skills" class="logo-img">
      </RouterLink>
      
      <!-- Mobile hamburger toggle button -->
      <button class="mobile-menu-btn" @click="toggleMobileMenu" aria-label="Menu principal">
        <component :is="isMobileMenuOpen ? X : Menu" class="mobile-icon" />
      </button>

      <!-- Desktop navigation list -->
      <ul class="nav-list" :class="{ 'active': isMobileMenuOpen }">
        <li>
          <RouterLink to="/" class="nav-link-item" @click="closeMobileMenu">{{ t('home') }}</RouterLink>
        </li>
        <li>
          <RouterLink to="/nossa-escola" class="nav-link-item" @click="closeMobileMenu">{{ t('school') }}</RouterLink>
        </li>
        <li>
          <a href="/#cursos" class="nav-link-item" @click.prevent="handleLinkClick('#cursos')">{{ t('courses') }}</a>
        </li>
        <li>
          <RouterLink to="/contato" class="nav-link-item" @click="closeMobileMenu">{{ t('contact') }}</RouterLink>
        </li>
        <li>
          <RouterLink to="/area-do-aluno" class="nav-link-item" @click="closeMobileMenu">{{ t('studentArea') }}</RouterLink>
        </li>

        <!-- Language switcher dropdown embedded dynamically in navigation list -->
        <li class="lang-switcher-li">
          <div class="lang-switcher">
            <button type="button" class="lang-btn" @click="toggleDropdown">
              <Globe class="lang-globe-icon" />
              <span class="lang-current">{{ currentLang.toUpperCase() }}</span>
              <ChevronDown class="lang-chevron-icon" :style="{ transform: isDropdownOpen ? 'rotate(180deg)' : 'rotate(0)' }" />
            </button>
            
            <transition name="fade-slide">
              <div v-if="isDropdownOpen" class="lang-dropdown">
                <button 
                  v-for="lang in languages" 
                  :key="lang.code"
                  type="button" 
                  class="lang-option" 
                  :class="{ 'selected': currentLang === lang.code }"
                  @click="changeLanguage(lang.code)"
                >
                  <span class="lang-option-flag">{{ lang.flag }}</span> {{ lang.label }}
                </button>
              </div>
            </transition>
          </div>
        </li>
      </ul>
    </nav>
  </header>
  
  <!-- Overlay for active mobile menu -->
  <div v-if="isMobileMenuOpen" class="menu-overlay active" @click="closeMobileMenu"></div>
</template>

<style scoped>
.global-header {
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 1000;
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
}

.nav-container {
  height: 80px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo-link {
  transition: transform 0.3s;
}
.logo-link:hover {
  transform: scale(1.05);
}

.logo-img {
  height: 45px;
}

.mobile-menu-btn {
  display: none;
  background: transparent;
  border: none;
  cursor: pointer;
  color: var(--primary-dark);
  z-index: 1001;
  padding: 8px;
}

.mobile-icon {
  width: 32px;
  height: 32px;
}

.nav-list {
  display: flex;
  gap: 3rem;
  list-style: none;
  align-items: center;
  margin: 0;
  padding: 0;
}

.nav-link-item {
  text-decoration: none;
  color: var(--primary-dark);
  font-weight: 600;
  font-size: 1.1rem;
  transition: color 0.3s;
  display: block;
  padding: 0.5rem 0;
  position: relative;
}

.nav-link-item::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--primary);
  transition: width 0.3s;
}

.nav-link-item:hover {
  color: var(--primary);
}

.nav-link-item:hover::after {
  width: 100%;
}

.router-link-exact-active.nav-link-item {
  color: var(--primary);
}
.router-link-exact-active.nav-link-item::after {
  width: 100%;
}

/* Lang Switcher Styles */
.lang-switcher-li {
  position: relative;
}

.lang-switcher {
  position: relative;
  display: inline-block;
  z-index: 1010;
}

.lang-btn {
  background: rgba(0, 71, 255, 0.05);
  border: 1px solid rgba(0, 71, 255, 0.1);
  padding: 0.6rem 1.2rem;
  border-radius: 99px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--primary-dark);
  font-weight: 600;
  font-size: 0.95rem;
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.lang-btn:hover {
  background: rgba(0, 71, 255, 0.1);
  border-color: rgba(0, 71, 255, 0.25);
  transform: translateY(-2px);
}

.lang-globe-icon {
  width: 16px;
  height: 16px;
}

.lang-current {
  font-size: 0.95rem;
}

.lang-chevron-icon {
  width: 14px;
  height: 14px;
  transition: transform 0.3s;
}

.lang-dropdown {
  display: flex;
  position: absolute;
  top: calc(100% + 10px);
  right: 0;
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(0, 71, 255, 0.08);
  border-radius: 20px;
  box-shadow: var(--shadow-premium);
  min-width: 185px;
  z-index: 1000;
  overflow: hidden;
  padding: 0.5rem;
  flex-direction: column;
  gap: 4px;
}

.lang-option {
  background: transparent;
  border: none;
  padding: 0.8rem 1rem;
  text-align: left;
  cursor: pointer;
  border-radius: 12px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.9rem;
  color: var(--primary-dark);
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  width: 100%;
}

.lang-option:hover {
  background: rgba(0, 71, 255, 0.05);
  color: var(--primary);
  transform: translateX(4px);
}

.lang-option.selected {
  background: rgba(0, 71, 255, 0.08);
  color: var(--primary);
}

.lang-option-flag {
  font-size: 1.1rem;
}

.menu-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background: rgba(0, 18, 51, 0.4);
  backdrop-filter: blur(8px);
  z-index: 998;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.4s;
}

.menu-overlay.active {
  opacity: 1;
  pointer-events: auto;
}

/* Fade Slide Transition for dropdown */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

/* Responsive Menu styles for Mobile */
@media (max-width: 992px) {
  .mobile-menu-btn {
    display: block;
  }

  .nav-list {
    position: fixed;
    top: 80px;
    right: -100%;
    width: 280px;
    height: calc(100vh - 80px);
    background: white;
    box-shadow: -10px 0 30px rgba(0, 0, 0, 0.05);
    flex-direction: column;
    align-items: flex-start;
    padding: 3rem 2rem;
    gap: 2rem;
    transition: right 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    z-index: 999;
  }

  .nav-list.active {
    right: 0;
  }

  .nav-link-item {
    font-size: 1.2rem;
    width: 100%;
  }

  .lang-switcher-li {
    width: 100%;
    margin-top: 1rem;
  }
  
  .lang-switcher {
    width: 100%;
  }
  
  .lang-btn {
    width: 100%;
    justify-content: space-between;
  }
  
  .lang-dropdown {
    width: 100%;
    position: static;
    margin-top: 0.5rem;
    box-shadow: none;
    background: rgba(0, 71, 255, 0.02);
    border-radius: 12px;
  }
}
</style>

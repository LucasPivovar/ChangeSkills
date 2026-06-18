<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { MessageCircle, Mail, X } from '@lucide/vue'
import { t } from '@/i18n'

const isOpen = ref(false)
const containerRef = ref(null)

const toggleMenu = () => {
  isOpen.value = !isOpen.value
}

const closeMenu = () => {
  isOpen.value = false
}

const handleClickOutside = (event) => {
  if (containerRef.value && !containerRef.value.contains(event.target)) {
    closeMenu()
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

<template>
  <div ref="containerRef" class="contact-float-container">
    <!-- Options List (expands upwards) -->
    <div class="contact-options" :class="{ 'active': isOpen }">
      <!-- Email Option (higher up) -->
      <a 
        href="mailto:contato@changeskills.com.br" 
        class="contact-option-btn mail-btn" 
        :class="{ 'visible': isOpen }"
        aria-label="Enviar E-mail"
        @click="closeMenu"
      >
        <span class="option-tooltip">{{ t('emailOpt', 'global') }}</span>
        <div class="icon-wrapper">
          <Mail class="option-icon" />
        </div>
      </a>

      <!-- WhatsApp Option (closer to trigger) -->
      <a 
        href="https://wa.me/555481223965" 
        target="_blank" 
        rel="noopener" 
        class="contact-option-btn wa-btn" 
        :class="{ 'visible': isOpen }"
        aria-label="Conversar no WhatsApp"
        @click="closeMenu"
      >
        <span class="option-tooltip">{{ t('whatsappOpt', 'global') }}</span>
        <div class="icon-wrapper">
          <MessageCircle class="option-icon" />
        </div>
      </a>
    </div>

    <!-- Main Floating Button (Trigger) -->
    <button 
      class="contact-trigger-btn" 
      :class="{ 'active': isOpen }" 
      @click="toggleMenu"
      :aria-label="t('contact', 'global')"
    >
      <div class="trigger-icons-container">
        <!-- Close icon when menu is open, chat icon when closed -->
        <transition name="fade-rotate" mode="out-in">
          <X v-if="isOpen" key="close" class="trigger-icon" />
          <MessageCircle v-else key="chat" class="trigger-icon" />
        </transition>
      </div>
      <!-- Floating tooltip when closed and hovered -->
      <span class="trigger-tooltip" v-if="!isOpen">{{ t('contact', 'global') }}</span>
    </button>
  </div>
</template>

<style scoped>
.contact-float-container {
  position: fixed;
  bottom: 30px;
  right: 30px;
  z-index: 1000;
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* Main Trigger Button */
.contact-trigger-btn {
  width: 65px;
  height: 65px;
  border-radius: 50%;
  background: var(--primary);
  color: white;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 15px 35px rgba(0, 71, 255, 0.3);
  transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  position: relative;
  outline: none;
}

.contact-trigger-btn:hover {
  transform: scale(1.08) translateY(-5px);
  box-shadow: 0 25px 45px rgba(0, 71, 255, 0.4);
}

.contact-trigger-btn.active {
  transform: scale(1) rotate(0deg);
  background: var(--primary-dark);
  box-shadow: 0 10px 25px rgba(0, 18, 51, 0.2);
}

.trigger-icons-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
}

.trigger-icon {
  width: 30px;
  height: 30px;
}

/* Options Container */
.contact-options {
  position: absolute;
  bottom: 75px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  align-items: center;
  pointer-events: none;
  opacity: 0;
  transform: translateY(20px) scale(0.85);
  transition: opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1),
              transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  width: 100%;
}

.contact-options.active {
  pointer-events: auto;
  opacity: 1;
  transform: translateY(0) scale(1);
}

/* Individual Option Button */
.contact-option-btn {
  width: 55px;
  height: 55px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  text-decoration: none;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
  position: relative;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.15),
              opacity 0.3s ease,
              transform 0.3s ease;
  opacity: 0;
  transform: translateY(15px);
}

/* Stagger transitions when opening */
.contact-options.active .contact-option-btn:nth-child(1) {
  opacity: 1;
  transform: translateY(0);
  transition-delay: 0.1s;
}

.contact-options.active .contact-option-btn:nth-child(2) {
  opacity: 1;
  transform: translateY(0);
  transition-delay: 0.05s;
}

/* WhatsApp Option Colors */
.wa-btn {
  background: #25D366;
  box-shadow: 0 10px 25px rgba(37, 211, 102, 0.3);
}

.wa-btn:hover {
  transform: scale(1.1) translateY(-4px);
  box-shadow: 0 15px 30px rgba(37, 211, 102, 0.45);
}

/* Email Option Colors */
.mail-btn {
  background: var(--primary);
  box-shadow: 0 10px 25px rgba(0, 71, 255, 0.3);
}

.mail-btn:hover {
  transform: scale(1.1) translateY(-4px);
  box-shadow: 0 15px 30px rgba(0, 71, 255, 0.45);
}

.icon-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
}

.option-icon {
  width: 25px;
  height: 25px;
}

/* Tooltips */
.trigger-tooltip,
.option-tooltip {
  position: absolute;
  right: 75px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(0, 0, 0, 0.05);
  color: var(--primary-dark);
  padding: 0.7rem 1.2rem;
  border-radius: 12px;
  font-weight: 500;
  font-size: 0.88rem;
  white-space: nowrap;
  box-shadow: 0 8px 20px rgba(0, 18, 51, 0.08);
  pointer-events: none;
  opacity: 0;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

/* Trigger Button Tooltip */
.trigger-tooltip {
  transform: translateX(15px);
  font-weight: 500;
  font-size: 0.92rem;
  right: 80px;
}

.contact-trigger-btn:hover .trigger-tooltip {
  opacity: 1;
  transform: translateX(0);
}

/* Option Buttons Tooltips */
.option-tooltip {
  transform: translateX(10px);
}

.contact-option-btn:hover .option-tooltip {
  opacity: 1;
  transform: translateX(0);
}

/* Icon swap transition animation (trigger button) */
.fade-rotate-enter-active,
.fade-rotate-leave-active {
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

.fade-rotate-enter-from {
  opacity: 0;
  transform: scale(0.6) rotate(-45deg);
}

.fade-rotate-leave-to {
  opacity: 0;
  transform: scale(0.6) rotate(45deg);
}
</style>

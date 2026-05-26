<script setup>
import { MessageCircle } from '@lucide/vue'
</script>

<template>
  <a href="https://wa.me/555481223965" target="_blank" rel="noopener" class="wa-float-btn" aria-label="Fale Conosco no WhatsApp">
    <MessageCircle class="wa-icon" />
    <span class="wa-tooltip">Fale Conosco</span>
  </a>
</template>

<style scoped>
.wa-float-btn {
  position: fixed;
  bottom: 30px;
  right: 30px;
  width: 65px;
  height: 65px;
  background: #25D366;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  box-shadow: 0 15px 35px rgba(37, 211, 102, 0.3);
  z-index: 1000;
  transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.wa-float-btn:hover {
  transform: scale(1.1) translateY(-10px);
  box-shadow: 0 25px 45px rgba(37, 211, 102, 0.4);
}

.wa-icon {
  width: 32px;
  height: 32px;
}

.wa-tooltip {
  position: absolute;
  right: 80px;
  background: white;
  color: var(--primary-dark);
  padding: 0.8rem 1.5rem;
  border-radius: 12px;
  font-weight: 700;
  font-size: 0.9rem;
  white-space: nowrap;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  opacity: 0;
  transform: translateX(20px);
  transition: all 0.3s;
  pointer-events: none;
}

.wa-float-btn:hover .wa-tooltip {
  opacity: 1;
  transform: translateX(0);
}
</style>

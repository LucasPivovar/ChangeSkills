<script setup>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import WhatsAppButton from '@/components/WhatsAppButton.vue'
</script>

<template>
  <Header />
  
  <main class="main-content">
    <router-view />
  </main>
  
  <WhatsAppButton />
  <Footer />
</template>

<style>
/* Reset and adjustments for standard header offset */
.main-content {
  min-height: 80vh;
}
</style>

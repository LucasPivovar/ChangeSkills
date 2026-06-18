<script setup>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import FloatingContactButton from '@/components/FloatingContactButton.vue'
</script>

<template>
  <Header />
  
  <main class="main-content">
    <router-view v-slot="{ Component }">
      <transition name="page-fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
  </main>
  
  <FloatingContactButton />
  <Footer />
</template>

<style>
/* Reset and adjustments for standard header offset */
.main-content {
  min-height: 80vh;
}
</style>

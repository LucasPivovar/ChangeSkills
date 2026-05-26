<script setup>
import { onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { Book, Layers } from '@lucide/vue'
import { t } from '@/i18n'

onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active')
      }
    })
  }, { threshold: 0.1 })
  
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el))
})
</script>

<template>
  <div class="curso-espanhol-view">
    <!-- Hero Section -->
    <section class="course-hero">
      <img src="/assets/img/banners/es.webp" alt="Espanhol Hero" class="hero-bg-img">
      <div class="hero-overlay"></div>
      <div class="container reveal active hero-content">
        <span class="hero-tag">{{ t('espanhol.heroTag', 'courses') }}</span>
        <h1 class="hero-title">{{ t('espanhol.heroTitle', 'courses') }} <span class="highlight">{{ t('espanhol.heroHighlight', 'courses') }}</span></h1>
        <p class="hero-desc">
          {{ t('espanhol.heroDesc', 'courses') }}
        </p>
      </div>
    </section>

    <!-- Modality Grid -->
    <section id="cursos" class="container courses-section">
      <div class="courses-grid">
        <!-- 1. JOVENS -->
        <div class="course-card reveal">
          <img src="/assets/img/espanol card1.jpeg" alt="Espanhol para Jovens — Change Skills" class="card-img">
          <div class="course-card-content">
            <h3>{{ t('espanhol.jovensTitle', 'courses') }}</h3>
            <div class="course-info"><Book class="info-icon" /> <strong>{{ t('materialLabel', 'courses') }}</strong> {{ t('espanhol.jovensMaterial', 'courses') }}</div>
            <div class="course-info"><Layers class="info-icon" /> <strong>{{ t('programLabel', 'courses') }}</strong> {{ t('espanhol.jovensProgram', 'courses') }}</div>
            <p class="course-description">{{ t('espanhol.jovensDesc', 'courses') }}</p>
            <RouterLink to="/cursos/modalidades/espanhol-jovens" class="btn-course">{{ t('learnMore', 'courses') }}</RouterLink>
          </div>
        </div>

        <!-- 2. ADULTOS -->
        <div class="course-card reveal">
          <img src="/assets/img/adult espanol.jpeg" alt="Espanhol para Adultos — Change Skills" class="card-img">
          <div class="course-card-content">
            <h3>{{ t('espanhol.adultosTitle', 'courses') }}</h3>
            <div class="course-info"><Book class="info-icon" /> <strong>{{ t('materialLabel', 'courses') }}</strong> {{ t('espanhol.adultosMaterial', 'courses') }}</div>
            <div class="course-info"><Layers class="info-icon" /> <strong>{{ t('programLabel', 'courses') }}</strong> {{ t('espanhol.adultosProgram', 'courses') }}</div>
            <p class="course-description">{{ t('espanhol.adultosDesc', 'courses') }}</p>
            <RouterLink to="/cursos/modalidades/espanhol-adultos" class="btn-course">{{ t('learnMore', 'courses') }}</RouterLink>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.curso-espanhol-view {
  width: 100%;
}

.course-hero {
  position: relative;
  padding: 250px 0 160px 0;
  min-height: 85vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  overflow: hidden;
  background: #001233;
  box-sizing: border-box;
}

.hero-bg-img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 0;
  opacity: 0.6;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, var(--primary-dark), transparent);
  z-index: 1;
}

.hero-content {
  position: relative;
  z-index: 2;
}

.hero-tag {
  color: var(--accent);
  font-weight: 800;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  display: inline-block;
  margin-bottom: 2rem;
  font-size: 0.95rem;
}

.hero-title {
  font-size: 5rem;
  color: white;
  margin-bottom: 2rem;
  line-height: 1;
  font-weight: 800;
  margin-top: 0;
}

.hero-title .highlight {
  color: var(--accent);
}

.hero-desc {
  font-size: 1.4rem;
  color: rgba(255, 255, 255, 0.9);
  font-weight: 300;
  max-width: 800px;
  margin: 0 auto;
  line-height: 1.6;
}

.courses-section {
  padding: 100px 0;
}

.courses-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2.5rem;
  max-width: 900px;
  margin: 0 auto;
  text-align: left;
}

.course-card {
  background: white;
  border-radius: 25px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  transition: var(--transition);
  display: flex;
  flex-direction: column;
  border: 1px solid rgba(0, 0, 0, 0.03);
}

.course-card:hover {
  transform: translateY(-10px);
  box-shadow: var(--shadow-premium);
}

.card-img {
  width: 100%;
  height: 220px;
  object-fit: cover;
  display: block;
}

.course-card-content {
  padding: 2.5rem 2rem;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
}

.course-card-content h3 {
  color: var(--primary-dark);
  font-size: 1.5rem;
  margin-bottom: 1.5rem;
  margin-top: 0;
  font-weight: 800;
}

.course-info {
  font-size: 0.95rem;
  color: var(--gray);
  margin-bottom: 0.8rem;
  display: flex;
  align-items: center;
  gap: 8px;
}

.course-info strong {
  color: var(--primary-dark);
}

.info-icon {
  width: 16px;
  height: 16px;
  color: var(--primary);
}

.course-description {
  font-size: 1rem;
  line-height: 1.7;
  color: var(--gray);
  margin: 1.5rem 0;
  flex-grow: 1;
}

.btn-course {
  background: var(--primary);
  color: white;
  text-decoration: none;
  padding: 1.1rem;
  border-radius: 12px;
  text-align: center;
  font-weight: 700;
  transition: var(--transition);
  display: block;
}

.btn-course:hover {
  background: var(--primary-dark);
  transform: scale(1.02);
}

@media (max-width: 992px) {
  .courses-grid {
    grid-template-columns: 1fr;
    max-width: 480px;
  }
}
</style>

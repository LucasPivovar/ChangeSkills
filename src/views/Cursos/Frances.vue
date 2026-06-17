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
  <div class="curso-frances-view">
    <!-- Hero Section -->
    <section class="course-hero">
      <img src="/assets/img/banners/fr.webp" alt="Frances Hero" class="hero-bg-img">
      <div class="hero-overlay"></div>
      <div class="container reveal active hero-content">
        <span class="hero-tag">{{ t('frances.heroTag', 'courses') }}</span>
        <h1 class="hero-title">{{ t('frances.heroTitle', 'courses') }} <span class="highlight">{{ t('frances.heroHighlight', 'courses') }}</span></h1>
        <p class="hero-desc">
          {{ t('frances.heroDesc', 'courses') }}
        </p>
      </div>
    </section>

    <!-- Modality Grid -->
    <section id="cursos" class="container courses-section">
      <div class="courses-grid">
        <!-- 1. ENFANTS -->
        <div class="course-card reveal reveal-delay-1">
          <img src="/assets/img/capa/FRA KIDS.webp" alt="Hourra! — Français pour Enfants" class="card-img">
          <div class="course-card-content">
            <h3>{{ t('frances.enfantsTitle', 'courses') }}</h3>
            <div class="course-info"><Book class="info-icon" /> <strong>{{ t('materialLabel', 'courses') }}</strong> {{ t('frances.enfantsMaterial', 'courses') }}</div>
            <div class="course-info"><Layers class="info-icon" /> <strong>{{ t('programLabel', 'courses') }}</strong> {{ t('frances.enfantsProgram', 'courses') }}</div>
            <p class="course-description">{{ t('frances.enfantsDesc', 'courses') }}</p>
            <RouterLink to="/cursos/modalidades/frances-enfants" class="btn-course">{{ t('learnMore', 'courses') }}</RouterLink>
          </div>
        </div>

        <!-- 2. ADOLESCENTS -->
        <div class="course-card reveal reveal-delay-2">
          <img src="/assets/img/capa/FRA TEEN.webp" alt="Français pour Adolescents" class="card-img">
          <div class="course-card-content">
            <h3>{{ t('frances.adosTitle', 'courses') }}</h3>
            <div class="course-info"><Book class="info-icon" /> <strong>{{ t('materialLabel', 'courses') }}</strong> {{ t('frances.adosMaterial', 'courses') }}</div>
            <div class="course-info"><Layers class="info-icon" /> <strong>{{ t('programLabel', 'courses') }}</strong> {{ t('frances.adosProgram', 'courses') }}</div>
            <p class="course-description">{{ t('frances.adosDesc', 'courses') }}</p>
            <RouterLink to="/cursos/modalidades/frances-ados" class="btn-course">{{ t('learnMore', 'courses') }}</RouterLink>
          </div>
        </div>

        <!-- 3. ADULTES -->
        <div class="course-card reveal reveal-delay-3">
          <img src="/assets/img/capa/FRA ADULT.webp" alt="Français pour Adultes" class="card-img">
          <div class="course-card-content">
            <h3>{{ t('frances.adultesTitle', 'courses') }}</h3>
            <div class="course-info"><Book class="info-icon" /> <strong>{{ t('materialLabel', 'courses') }}</strong> {{ t('frances.adultesMaterial', 'courses') }}</div>
            <div class="course-info"><Layers class="info-icon" /> <strong>{{ t('programLabel', 'courses') }}</strong> {{ t('frances.adultesProgram', 'courses') }}</div>
            <p class="course-description">{{ t('frances.adultesDesc', 'courses') }}</p>
            <RouterLink to="/cursos/modalidades/frances-adultes" class="btn-course">{{ t('learnMore', 'courses') }}</RouterLink>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.curso-frances-view {
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
  opacity: 1;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.45);
  z-index: 1;
}

.hero-content {
  position: relative;
  z-index: 2;
}

.hero-tag {
  color: #ffffff;
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
  color: #ffffff;
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
  grid-template-columns: repeat(3, 1fr);
  gap: 2.5rem;
  max-width: 1200px;
  margin: 0 auto;
  text-align: left;
}

.course-card {
  background: white;
  border-radius: 25px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
  border: 1px solid rgba(0, 0, 0, 0.03);
}

.course-card:hover {
  transform: translateY(-10px) scale(1.05);
  border: 1px solid #000000 !important;
  box-shadow: 0 30px 60px rgba(0, 0, 0, 0.12) !important;
}

.course-card:hover .info-icon {
  transform: scale(1.1) rotate(5deg);
}

.card-img {
  width: 100%;
  height: 380px;
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
  transition: transform 0.3s ease;
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
    grid-template-columns: repeat(2, 1fr);
    max-width: 800px;
  }
}

@media (max-width: 768px) {
  .courses-grid {
    grid-template-columns: 1fr;
    max-width: 480px;
  }
}
</style>

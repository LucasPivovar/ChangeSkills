<script setup>
import { onMounted, computed } from 'vue'
import { RouterLink } from 'vue-router'
import { Book, User } from '@lucide/vue'
import { t } from '@/i18n'

const modalities = computed(() => [
  {
    title: t('ingles.kidsTitle', 'courses'),
    material: t('ingles.kidsMaterial', 'courses'),
    detailLabel: t('ageLabel', 'courses'),
    detailValue: t('ingles.kidsAgeValue', 'courses'),
    image: '/assets/img/capa/ENG KID.webp',
    desc: t('ingles.kidsDesc', 'courses'),
    to: '/cursos/modalidades/kids',
    hasAge: true
  },
  {
    title: t('ingles.teensTitle', 'courses'),
    material: t('ingles.teensMaterial', 'courses'),
    detailLabel: t('ageLabel', 'courses'),
    detailValue: t('ingles.teensAgeValue', 'courses'),
    image: '/assets/img/capa/ENG TEEN.webp',
    desc: t('ingles.teensDesc', 'courses'),
    to: '/cursos/modalidades/teens',
    hasAge: true
  },
  {
    title: t('ingles.fastTrackTitle', 'courses'),
    material: t('ingles.fastTrackMaterial', 'courses'),
    image: '/assets/img/capa/FAST ENG.webp',
    desc: t('ingles.fastTrackDesc', 'courses'),
    to: '/cursos/modalidades/fast-track',
    hasAge: false
  },
  {
    title: t('ingles.excellenceTitle', 'courses'),
    material: t('ingles.excellenceMaterial', 'courses'),
    image: '/assets/img/capa/ENG ADULT.webp',
    desc: t('ingles.excellenceDesc', 'courses'),
    to: '/cursos/modalidades/excellence',
    hasAge: false
  },
  {
    title: t('ingles.businessTitle', 'courses'),
    material: t('ingles.businessMaterial', 'courses'),
    image: '/assets/img/capa/ENG BUSINESS.webp',
    desc: t('ingles.businessDesc', 'courses'),
    to: '/cursos/modalidades/business',
    hasAge: false
  },
  {
    title: t('ingles.scientificTitle', 'courses'),
    material: t('ingles.scientificMaterial', 'courses'),
    image: '/assets/img/capa/ENG RESEARCHERS.webp',
    desc: t('ingles.scientificDesc', 'courses'),
    to: '/cursos/modalidades/scientific',
    hasAge: false
  },
  {
    title: t('ingles.ingles50Title', 'courses'),
    material: t('ingles.ingles50Material', 'courses'),
    image: '/assets/img/card-ingles-50.png',
    desc: t('ingles.ingles50Desc', 'courses'),
    to: '/cursos/modalidades/ingles-50-plus',
    hasAge: false
  }
])

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
  <div class="curso-ingles-view">
    <!-- Hero Section -->
    <section class="course-hero">
      <img src="/assets/img/banners/ing.webp" alt="Inglês Hero" class="hero-bg-img">
      <div class="hero-overlay"></div>
      <div class="container reveal active hero-content">
        <span class="hero-tag">{{ t('ingles.heroTag', 'courses') }}</span>
        <h1 class="hero-title">{{ t('ingles.heroTitle', 'courses') }} <span class="highlight">{{ t('ingles.heroHighlight', 'courses') }}</span></h1>
        <p class="hero-desc">
          {{ t('ingles.heroDesc', 'courses') }}
        </p>
      </div>
    </section>

    <!-- Modality Grid -->
    <section id="cursos" class="container courses-section">
      <div class="courses-grid">
        <div 
          v-for="(mod, idx) in modalities" 
          :key="idx" 
          class="course-card reveal"
        >
          <img :src="mod.image" :alt="mod.title" class="card-img">
          <div class="course-card-content">
            <h3>{{ mod.title }}</h3>
            <div class="course-info">
              <Book class="info-icon" /> 
              <strong>{{ t('materialLabel', 'courses') }}</strong> {{ mod.material }}
            </div>
            <div v-if="mod.hasAge" class="course-info">
              <User class="info-icon" /> 
              <strong>{{ mod.detailLabel }}</strong> {{ mod.detailValue }}
            </div>
            <p class="course-description">{{ mod.desc }}</p>
            <RouterLink :to="mod.to" class="btn-course">{{ t('learnMore', 'courses') }}</RouterLink>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.curso-ingles-view {
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
  background: rgba(0, 0, 0, 0.2);
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
  font-size: 1.4rem;
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
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--gray);
  margin: 1.2rem 0;
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
  margin-top: auto;
}

.btn-course:hover {
  background: var(--primary-dark);
  transform: scale(1.02);
}

@media (max-width: 992px) {
  .courses-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 600px) {
  .courses-grid {
    grid-template-columns: 1fr;
  }
}
</style>

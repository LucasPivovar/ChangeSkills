<script setup>
import { ref, onMounted, computed } from 'vue'
import { RouterLink } from 'vue-router'
import { ArrowRight, ChevronRight, ChevronDown, Quote, FileText, MessagesSquare } from '@lucide/vue'
import { t } from '@/i18n'

const faqs = computed(() => [
  {
    question: t('faqQ1', 'home'),
    answer: t('faqA1', 'home')
  },
  {
    question: t('faqQ2', 'home'),
    answer: t('faqA2', 'home')
  },
  {
    question: t('faqQ3', 'home'),
    answer: t('faqA3', 'home')
  },
  {
    question: t('faqQ4', 'home'),
    answer: t('faqA4', 'home')
  },
  {
    question: t('faqQ5', 'home'),
    answer: t('faqA5', 'home')
  }
])

const isFaqOpen = ref([false, false, false, false, false])

function toggleFaq(index) {
  isFaqOpen.value[index] = !isFaqOpen.value[index]
}

onMounted(() => {
  // Load Swiper CSS dynamically
  if (!document.getElementById('swiper-css')) {
    const link = document.createElement('link')
    link.id = 'swiper-css'
    link.rel = 'stylesheet'
    link.href = 'https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css'
    document.head.appendChild(link)
  }

  // Load Swiper JS dynamically
  if (window.Swiper) {
    initSwiper()
  } else {
    const script = document.createElement('script')
    script.src = 'https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js'
    script.onload = () => {
      initSwiper()
    }
    document.body.appendChild(script)
  }

  // Setup reveal observer
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active')
      }
    })
  }, { threshold: 0.1 })
  
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el))

  // Staggered trigger for course cards
  const cursosSection = document.getElementById('cursos-swiper-section')
  if (cursosSection) {
    const cardsObserver = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('cards-visible')
          obs.disconnect()
        }
      })
    }, { threshold: 0.15 })
    cardsObserver.observe(cursosSection)
  }
})

function initSwiper() {
  new window.Swiper('.hero-swiper', {
    direction: 'horizontal',
    loop: true,
    speed: 800,
    parallax: true,
    grabCursor: true,
    autoplay: {
      delay: 6000,
      disableOnInteraction: false,
    }
  })

  new window.Swiper('.cursos-swiper', {
    slidesPerView: 4,
    spaceBetween: 30,
    autoplay: {
      delay: 3000,
      disableOnInteraction: false,
    },
    loop: true,
    breakpoints: {
      320: { slidesPerView: 1 },
      768: { slidesPerView: 2 },
      1024: { slidesPerView: 4 }
    }
  })
}
</script>

<template>
  <div class="home-view">
    <!-- 1. Hero Slider Section -->
    <section class="hero-slider-container">
      <div class="swiper hero-swiper">
        <div class="swiper-wrapper">
          
          <!-- SLIDE 1: General Welcome -->
          <div class="swiper-slide mesh-bg slide-flex">
            <div class="container hero-grid">
              <div class="reveal active" data-swiper-parallax="-300">
                <div class="subheading-container">
                  <span class="subheading-text">{{ t('heroTag', 'home') }}</span>
                </div>
                <h1 class="hero-title">{{ t('heroTitle', 'home') }} <span class="highlight-text">{{ t('heroHighlight', 'home') }}</span></h1>
                <p class="hero-desc">{{ t('heroDesc', 'home') }}</p>
                <div class="btn-group">
                  <a href="#cursos" class="btn-vip">{{ t('heroExplore', 'home') }} <ArrowRight class="btn-icon" /></a>
                  <RouterLink to="/services/agendamento-nivelamento" class="btn-vip btn-secondary">{{ t('heroNivelamento', 'home') }}</RouterLink>
                </div>
              </div>
              <div class="mascot-container" data-swiper-parallax="-100">
                <div class="mascot-wrapper">
                  <img src="/assets/img/mascot.png" alt="Change Skills Mascot" class="mascot-img">
                  <div class="mascot-glow"></div>
                  <div class="mascot-shadow"></div>
                </div>
              </div>
            </div>
          </div>

          <!-- SLIDE 2: Global Excellence -->
          <div class="swiper-slide slide-bg-2">
            <div class="slide2-overlay"></div>
            <div class="reveal active slide2-content" data-swiper-parallax="-400">
              <div class="subheading-container">
                <span class="subheading-text accent-color">{{ t('heroTag2', 'home') }}</span>
              </div>
              <h2 class="slide2-title">{{ t('heroTitle2', 'home') }} <span class="accent-color">{{ t('heroHighlight2', 'home') }}</span></h2>
              <p class="slide2-desc">{{ t('heroDesc2', 'home') }}</p>
              <RouterLink to="/nossa-escola" class="btn-vip btn-accent">{{ t('heroMore', 'home') }} <ChevronRight class="btn-icon" /></RouterLink>
            </div>
          </div>

        </div>
        
        <!-- Scroll Indicator -->
        <div class="hero-scroll-indicator">
          <div class="scroll-mouse">
            <div class="scroll-wheel"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 2. Nossa Escola (Overview) -->
    <section id="escola" class="escola-section">
      <div class="container">
        <div class="text-center reveal header-margin">
          <span class="section-tag">{{ t('historiaTag', 'home') }}</span>
          <h2 class="section-title">{{ t('historiaTitle', 'home') }}</h2>
        </div>

        <div class="escola-grid">
          <div class="reveal escola-info">
            <div class="escola-card">
              <h3 class="card-heading">{{ t('historiaCardTitle', 'home') }}</h3>
              <p class="card-text">
                {{ t('historiaCardText', 'home') }}
              </p>
            </div>
            <div class="escola-card">
              <h3 class="card-heading">{{ t('metodologiaCardTitle', 'home') }}</h3>
              <p class="card-text">
                {{ t('metodologiaCardText', 'home') }}
              </p>
            </div>
          </div>
          
          <div class="reveal photo-reveal">
            <div class="founders-photo-card">
              <img src="/assets/img/image.png" alt="Tay & Wagner" class="founders-img">
              <div class="founders-overlay"></div>
              <div class="founders-caption">
                <p class="founders-names">{{ t('foundersNames', 'home') }}</p>
                <p class="founders-subtitle">{{ t('foundersSubtitle', 'home') }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. Cursos (Choose Language) -->
    <section id="cursos" class="cursos-section mesh-bg">
      <div class="container">
        <div class="text-center reveal subheading-gap">
          <span class="section-tag">{{ t('escolhaTag', 'home') }}</span>
          <h2 class="section-title">{{ t('escolhaTitle', 'home') }}</h2>
        </div>
        
        <!-- Swiper Slider para Cursos -->
        <div class="swiper cursos-swiper" id="cursos-swiper-section">
          <div class="swiper-wrapper">
            <!-- Inglês -->
            <div class="swiper-slide curso-card" style="--card-delay: 0.05s;">
              <RouterLink to="/cursos/ingles" class="curso-link">
                <img src="/assets/englishcard.jpeg" alt="Inglês Card" class="curso-img">
                <div class="curso-overlay"></div>
                <div class="curso-content">
                  <h3 class="curso-title">{{ t('ingles', 'home') }}</h3>
                  <span class="curso-action" v-html="t('cursoAction', 'home')"></span>
                </div>
              </RouterLink>
            </div>
            
            <!-- Espanhol -->
            <div class="swiper-slide curso-card" style="--card-delay: 0.25s;">
              <RouterLink to="/cursos/espanhol" class="curso-link">
                <img src="/assets/espanolcard.jpeg" alt="Espanhol Card" class="curso-img">
                <div class="curso-overlay"></div>
                <div class="curso-content">
                  <h3 class="curso-title">{{ t('espanhol', 'home') }}</h3>
                  <span class="curso-action" v-html="t('cursoAction', 'home')"></span>
                </div>
              </RouterLink>
            </div>
            
            <!-- Francês -->
            <div class="swiper-slide curso-card" style="--card-delay: 0.45s;">
              <RouterLink to="/cursos/frances" class="curso-link">
                <img src="/assets/francescard.jpeg" alt="Francês Card" class="curso-img">
                <div class="curso-overlay"></div>
                <div class="curso-content">
                  <h3 class="curso-title">{{ t('frances', 'home') }}</h3>
                  <span class="curso-action" v-html="t('cursoAction', 'home')"></span>
                </div>
              </RouterLink>
            </div>
            
            <!-- Português -->
            <div class="swiper-slide curso-card" style="--card-delay: 0.65s;">
              <RouterLink to="/cursos/portugues" class="curso-link">
                <img src="/assets/portuguesecard.jpeg" alt="Português Card" class="curso-img">
                <div class="curso-overlay"></div>
                <div class="curso-content">
                  <h3 class="curso-title">{{ t('portugues', 'home') }}</h3>
                  <span class="curso-action" v-html="t('cursoAction', 'home')"></span>
                </div>
              </RouterLink>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. Depoimentos (Testimonials) -->
    <section id="depoimentos" class="testimonials-section">
      <div class="testimonials-glow"></div>
      <div class="container testimonials-content">
        <div class="text-center reveal subheading-gap">
          <span class="section-tag accent-color">{{ t('comunidadeTag', 'home') }}</span>
          <h2 class="section-title text-white">{{ t('comunidadeTitle', 'home') }}</h2>
        </div>
        <div class="testimonials-grid">
          <div class="glass-card reveal">
            <Quote class="quote-icon" />
            <p class="quote-text">{{ t('testimonial1', 'home') }}</p>
            <p class="quote-author">{{ t('testimonialAuthor1', 'home') }}</p>
          </div>
          <div class="glass-card reveal">
            <Quote class="quote-icon" />
            <p class="quote-text">{{ t('testimonial2', 'home') }}</p>
            <p class="quote-author">{{ t('testimonialAuthor2', 'home') }}</p>
          </div>
          <div class="glass-card reveal">
            <Quote class="quote-icon" />
            <p class="quote-text">{{ t('testimonial3', 'home') }}</p>
            <p class="quote-author">{{ t('testimonialAuthor3', 'home') }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 5. Serviços Extras -->
    <section id="servicos" class="servicos-section">
      <div class="container">
        <div class="text-center reveal subheading-gap">
          <span class="section-tag">{{ t('servicosTag', 'home') }}</span>
          <h2 class="section-title">{{ t('servicosTitle', 'home') }}</h2>
          <p class="section-desc">{{ t('servicosSubtitle', 'home') }}</p>
        </div>
        <div class="servicos-grid">
          <!-- Serviço 1: Traduções -->
          <RouterLink to="/services/traducoes" class="glass-card-btn reveal">
            <div class="servico-icon-container">
              <FileText class="servico-icon" />
            </div>
            <h3 class="servico-title">{{ t('servicoCardTitle1', 'home') }}</h3>
            <p class="servico-desc">{{ t('servicoCardDesc1', 'home') }}</p>
          </RouterLink>

          <!-- Serviço 2: Aulas de Conversação -->
          <RouterLink to="/services/aulas-conversacao" class="glass-card-btn reveal">
            <div class="servico-icon-container">
              <MessagesSquare class="servico-icon" />
            </div>
            <h3 class="servico-title">{{ t('servicoCardTitle2', 'home') }}</h3>
            <p class="servico-desc">{{ t('servicoCardDesc2', 'home') }}</p>
          </RouterLink>
        </div>
      </div>
    </section>

    <!-- 6. FAQ Section -->
    <section id="faq" class="faq-section">
      <div class="container faq-container">
        <div class="text-center reveal header-margin">
          <span class="section-tag">{{ t('faqTag', 'home') }}</span>
          <h2 class="section-title">{{ t('faqTitle', 'home') }}</h2>
        </div>
        
        <div class="reveal faq-list">
          <div v-for="(item, idx) in faqs" :key="idx" class="faq-vip-item">
            <button class="faq-vip-toggle" @click="toggleFaq(idx)">
              <span>{{ item.question }}</span>
              <ChevronDown class="faq-chevron" :class="{ 'rotated': isFaqOpen[idx] }" />
            </button>
            <transition name="expand">
              <div v-if="isFaqOpen[idx]" class="faq-vip-content">
                {{ item.answer }}
              </div>
            </transition>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.home-view {
  width: 100%;
}

.hero-slider-container {
  padding: 0;
  position: relative;
  overflow: hidden;
  background: #f0f4ff;
  margin-top: -80px;
  z-index: 1;
}

.hero-swiper {
  height: 100vh;
  touch-action: pan-y !important;
  cursor: grab;
}

.hero-swiper:active {
  cursor: grabbing;
}

.slide-flex {
  min-height: 85vh;
  display: flex;
  align-items: center;
}

.hero-grid {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 4rem;
  align-items: center;
  padding-top: 100px;
}

.subheading-container {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 2rem;
}

.subheading-text {
  color: var(--primary);
  font-weight: 800;
  letter-spacing: 0.2em;
  font-size: 0.9rem;
}

.subheading-text.accent-color {
  color: var(--accent);
}

.accent-color {
  color: var(--accent) !important;
}

.hero-title {
  margin-bottom: 2rem;
  font-size: clamp(3rem, 5vw, 4.5rem);
  line-height: 1.15;
  color: var(--primary-dark);
  font-weight: 800;
}

.highlight-text {
  color: var(--primary);
}

.hero-desc {
  font-size: 1.2rem;
  color: var(--gray);
  line-height: 1.8;
  margin-bottom: 3.5rem;
  max-width: 600px;
}

.btn-group {
  display: flex;
  gap: 1.5rem;
  flex-wrap: wrap;
}

.btn-secondary {
  background: white !important;
  color: var(--primary-dark) !important;
  border: 1px solid rgba(0, 0, 0, 0.1) !important;
}

.btn-secondary:hover {
  background: var(--primary-dark) !important;
  color: white !important;
}

.mascot-container {
  text-align: center;
}

.mascot-wrapper {
  position: relative;
  display: inline-block;
}

.mascot-img {
  width: 100%;
  max-width: 480px;
  position: relative;
  z-index: 2;
}

.mascot-glow {
  position: absolute;
  top: 10%;
  left: 10%;
  width: 80%;
  height: 80%;
  background: radial-gradient(circle, var(--primary), transparent 70%);
  opacity: 0.1;
  filter: blur(40px);
  z-index: 1;
}

.mascot-shadow {
  width: 60%;
  height: 20px;
  background: rgba(0, 0, 0, 0.12);
  border-radius: 50%;
  filter: blur(12px);
  margin: -20px auto 0 auto;
}

/* Slide 2 */
.slide-bg-2 {
  min-height: 85vh;
  position: relative;
  background: url('https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=1920&q=80') center/cover no-repeat;
}

.slide2-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to left, var(--primary-dark) 45%, transparent 80%);
  z-index: 1;
}

.slide2-content {
  position: absolute;
  top: 32%;
  transform: translateY(-50%);
  right: 10%;
  width: 100%;
  max-width: 580px;
  text-align: left;
  z-index: 10;
  padding: 0;
  margin: 0;
}

.slide2-title {
  margin-bottom: 1.5rem;
  font-size: clamp(2.5rem, 6vw, 4.2rem);
  color: white;
  line-height: 1.05;
  font-weight: 900;
  letter-spacing: -0.02em;
}

.slide2-desc {
  font-size: 1.25rem;
  color: rgba(255, 255, 255, 0.85);
  line-height: 1.7;
  margin-bottom: 3rem;
  font-weight: 400;
}

.btn-accent {
  background: var(--accent) !important;
  color: var(--primary-dark) !important;
  border: none !important;
  padding: 1.3rem 3.5rem !important;
  display: inline-flex !important;
  font-weight: 800 !important;
}

.btn-accent:hover {
  background: white !important;
}

/* Scroll indicator animation */
.hero-scroll-indicator {
  position: absolute;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 10;
  opacity: 0.5;
}

.scroll-mouse {
  width: 24px;
  height: 40px;
  border: 2px solid var(--primary-dark);
  border-radius: 20px;
  position: relative;
}

.scroll-wheel {
  width: 4px;
  height: 8px;
  background: var(--primary);
  border-radius: 2px;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  top: 8px;
  animation: mouseScroll 2s infinite ease-in-out;
}

@keyframes mouseScroll {
  0% { transform: translate(-50%, 0); opacity: 0; }
  50% { transform: translate(-50%, 8px); opacity: 1; }
  100% { transform: translate(-50%, 16px); opacity: 0; }
}

/* Institutional segment */
.escola-section {
  background: var(--bg-light);
  position: relative;
  overflow: hidden;
  padding-bottom: 80px;
  padding-top: 120px;
}

.section-tag {
  color: var(--primary);
  font-weight: 800;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  font-size: 0.9rem;
  display: inline-block;
  margin-bottom: 1rem;
}

.section-title {
  font-size: 3rem;
  color: var(--primary-dark);
  font-weight: 800;
  margin: 0;
}

.text-white {
  color: white !important;
}

.escola-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6rem;
  align-items: start;
  margin-top: 5rem;
}

.escola-info {
  display: flex;
  flex-direction: column;
  gap: 4rem;
}

.escola-card h3 {
  color: var(--primary-dark);
  font-size: 1.8rem;
  margin-bottom: 1.5rem;
  margin-top: 0;
  font-weight: 700;
}

.card-text {
  font-size: 1.15rem;
  color: var(--gray);
  line-height: 1.8;
  margin: 0;
}

.founders-photo-card {
  position: relative;
  border-radius: 40px;
  overflow: hidden;
  box-shadow: var(--shadow-premium);
}

.founders-img {
  width: 100%;
  height: 480px;
  object-fit: cover;
  object-position: center 85%;
  display: block;
}

.founders-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0, 18, 51, 0.8) 0%, rgba(0, 18, 51, 0) 60%);
}

.founders-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 2.5rem 2rem;
  z-index: 2;
  text-align: center;
}

.founders-names {
  color: white;
  font-weight: 700;
  font-size: 1.25rem;
  margin: 0;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.founders-subtitle {
  color: rgba(255, 255, 255, 0.85);
  font-size: 0.95rem;
  margin: 5px 0 0 0;
  font-weight: 500;
}

/* Course cards staggered */
@keyframes courseCardIn {
  0%   { opacity: 0; transform: translateY(50px) scale(0.95); }
  60%  { opacity: 1; transform: translateY(-6px) scale(1.01); }
  100% { opacity: 1; transform: translateY(0)   scale(1); }
}

.curso-card {
  opacity: 0;
  transform: translateY(50px) scale(0.95);
}

.cursos-swiper.cards-visible .curso-card {
  animation: courseCardIn 0.75s cubic-bezier(0.22, 1, 0.36, 1) both;
  animation-delay: var(--card-delay, 0s);
}

.cursos-section {
  padding: 120px 0;
}

.subheading-gap {
  margin-bottom: 5rem;
}

.cursos-swiper {
  padding: 15px 0;
}

.curso-link {
  display: block;
  position: relative;
  height: 350px;
  border-radius: 40px;
  overflow: hidden;
  text-decoration: none;
}

.curso-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 0;
  transition: transform 0.6s ease;
}

.curso-link:hover .curso-img {
  transform: scale(1.05);
}

.curso-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(5, 5, 68, 0.9), transparent);
  z-index: 1;
  opacity: 0;
  transition: opacity 0.5s ease;
}

.curso-content {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 3rem;
  z-index: 2;
  text-align: left;
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.5s ease, transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.curso-link:hover .curso-overlay {
  opacity: 1;
}

.curso-link:hover .curso-content {
  opacity: 1;
  transform: translateY(0);
}

.curso-title {
  color: white;
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
  margin-top: 0;
  font-weight: 700;
}

.curso-action {
  color: var(--accent);
  font-weight: 600;
}

/* Testimonials / Community segment */
.testimonials-section {
  background: var(--primary-dark);
  color: white;
  position: relative;
  overflow: hidden;
  padding: 120px 0;
}

.testimonials-glow {
  position: absolute;
  top: -20%;
  right: -10%;
  width: 800px;
  height: 800px;
  background: var(--primary);
  filter: blur(250px);
  opacity: 0.4;
  border-radius: 50%;
  z-index: 0;
}

.testimonials-content {
  position: relative;
  z-index: 1;
}

.testimonials-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 3rem;
  text-align: left;
}

.testimonials-grid .glass-card {
  background: rgba(255, 255, 255, 0.05);
  border-color: rgba(255, 255, 255, 0.1);
  padding: 3rem;
  border-radius: 24px;
  border-width: 1px;
  border-style: solid;
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.testimonials-grid .glass-card:hover {
  transform: translateY(-10px);
  background: rgba(255, 255, 255, 0.12) !important;
  border-color: rgba(0, 209, 255, 0.5) !important;
  box-shadow: 0 20px 50px rgba(0, 209, 255, 0.25) !important;
}

.quote-icon {
  color: var(--accent);
  width: 40px;
  height: 40px;
  margin-bottom: 2rem;
  opacity: 0.5;
}

.quote-text {
  font-size: 1.2rem;
  color: white;
  font-weight: 600;
  line-height: 1.6;
  margin-bottom: 2rem;
  margin-top: 0;
}

.quote-author {
  color: rgba(255, 255, 255, 0.7);
  font-size: 1.1rem;
  margin: 0;
}

/* Services Extra styling */
.servicos-section {
  padding: 120px 0;
}

.section-desc {
  color: var(--gray);
  font-size: 1.2rem;
  margin-top: 1rem;
  margin-bottom: 0;
}

.servicos-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2.5rem;
  margin-top: 4rem;
}

.glass-card-btn {
  text-decoration: none;
  text-align: center;
  padding: 3rem 2rem;
  background: white;
  border: 1px solid rgba(0, 71, 255, 0.05);
  border-radius: 24px;
  box-shadow: var(--shadow-premium);
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  display: block;
}

.glass-card-btn:hover {
  transform: translateY(-10px);
  border-color: rgba(0, 71, 255, 0.25) !important;
  box-shadow: 0 30px 60px rgba(0, 71, 255, 0.1) !important;
}

.servico-icon-container {
  width: 60px;
  height: 60px;
  background: rgba(0, 71, 255, 0.06);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1.5rem auto;
  transition: transform 0.3s ease;
}

.glass-card-btn:hover .servico-icon-container {
  transform: scale(1.1) rotate(5deg);
}

.servico-icon {
  color: var(--primary);
  width: 28px;
  height: 28px;
}

.servico-title {
  color: var(--primary-dark);
  font-size: 1.4rem;
  margin-bottom: 1rem;
  margin-top: 0;
  font-weight: 700;
}

.servico-desc {
  color: var(--gray);
  font-size: 1.05rem;
  line-height: 1.6;
  margin: 0;
}

/* FAQ segment styling */
.faq-section {
  background: var(--bg-light);
  padding: 120px 0;
}

.faq-container {
  max-width: 900px;
}

.faq-list {
  margin-top: 5rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.faq-vip-item {
  background: white;
  border-radius: 20px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.02);
  overflow: hidden;
  border: 1px solid rgba(0,0,0,0.02);
  transition: all 0.3s ease;
}

.faq-vip-toggle {
  width: 100%;
  padding: 2rem 2.5rem;
  background: transparent;
  border: none;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--primary-dark);
  text-align: left;
  gap: 1.5rem;
}

.faq-chevron {
  color: var(--primary);
  width: 20px;
  height: 20px;
  transition: transform 0.3s ease;
}

.faq-chevron.rotated {
  transform: rotate(180deg);
}

.faq-vip-content {
  padding: 0 2.5rem 2.5rem 2.5rem;
  font-size: 1.1rem;
  color: var(--gray);
  line-height: 1.8;
  border-top: 1px solid rgba(0,0,0,0.01);
}

/* Expand Animation */
.expand-enter-active,
.expand-leave-active {
  transition: all 0.3s ease-out;
  max-height: 200px;
  opacity: 1;
  overflow: hidden;
}

.expand-enter-from,
.expand-leave-to {
  max-height: 0;
  opacity: 0;
  padding-bottom: 0;
}

/* Responsive Overrides */
@media (max-width: 992px) {
  .hero-swiper {
    height: auto !important;
    min-height: 112vh !important;
  }

  .slide-flex {
    min-height: 112vh !important;
    padding-bottom: 80px !important;
    box-sizing: border-box;
  }

  .slide-bg-2 {
    min-height: 112vh !important;
    padding-bottom: 80px !important;
    box-sizing: border-box;
  }

  .hero-grid {
    grid-template-columns: 1fr;
    text-align: center;
    padding-top: 170px;
    gap: 2rem;
  }
  
  .subheading-container {
    justify-content: center;
    margin-bottom: 0.8rem;
  }
  
  .hero-title {
    font-size: clamp(2rem, 7vw, 2.6rem);
    margin-bottom: 1rem;
    line-height: 1.2;
  }

  .hero-desc {
    margin: 0 auto 1.5rem auto;
    font-size: 1.05rem;
    line-height: 1.6;
    max-width: 90%;
  }
  
  .btn-group {
    justify-content: center;
    gap: 1rem;
  }

  .mascot-img {
    max-width: 160px;
    margin: 0 auto;
  }

  .mascot-shadow {
    width: 100px;
    height: 10px;
    margin: -10px auto 0 auto;
  }

  .escola-grid {
    grid-template-columns: 1fr;
    gap: 4rem;
  }
  
  .founders-img {
    height: 380px;
  }

  .testimonials-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .servicos-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
}

@media (max-width: 768px) {
  .hero-scroll-indicator {
    display: none !important;
  }
  
  .slide2-content {
    top: 35% !important;
    transform: none !important;
    right: 5% !important;
    left: 5% !important;
    width: 90% !important;
    max-width: 100% !important;
    text-align: center !important;
  }
  
  .slide2-title {
    font-size: clamp(1.8rem, 5vw, 2.4rem) !important;
    text-shadow: 0 4px 12px rgba(0,0,0,0.5);
  }
  
  .slide2-desc {
    font-size: 1rem !important;
    margin-bottom: 1.8rem !important;
    text-shadow: 0 2px 6px rgba(0,0,0,0.5);
  }
}
</style>

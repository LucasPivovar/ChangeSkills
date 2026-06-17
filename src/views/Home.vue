<script setup>
import { ref, onMounted, computed } from 'vue'
import { RouterLink, useRoute } from 'vue-router'
import { ArrowRight, ChevronRight, ChevronDown, Quote, FileText, MessagesSquare, Languages, Bot, Zap } from '@lucide/vue'
import { t } from '@/i18n'
import videoPlayback from '@/assets/cinematic 3.mp4'

// Local testimonials avatar imports
import avatarJosef from '@/assets/depoimentos/depoimentos/front-view-man-posing-outdoors.jpg.jpeg'
import avatarChantal from '@/assets/depoimentos/depoimentos/medium-shot-beautiful-woman-with-braids.jpg.jpeg'
import avatarChloe from '@/assets/depoimentos/depoimentos/medium-shot-woman-having-fun-outdoors.jpg.jpeg'
import avatarJasmine from '@/assets/depoimentos/depoimentos/medium-shot-woman-living-healthy-life.jpg.jpeg'
import avatarArielle from '@/assets/depoimentos/depoimentos/portrait-millennial-woman-living-country-side-after-moving-from-city.jpg.jpeg'
import avatarBenjamin from '@/assets/depoimentos/depoimentos/portrait-handsome-man.jpg.jpeg'
import avatarMaria from '@/assets/depoimentos/depoimentos/portrait-woman-showing-strong-emotions-mental-health-awareness.jpg.jpeg'
import avatarAdrian from '@/assets/depoimentos/depoimentos/front-view-man-posing-outdoors (1).jpg.jpeg'
import avatarPierre from '@/assets/depoimentos/depoimentos/front-view-man-posing-outdoors (2).jpg.jpeg'
import avatarAlan from '@/assets/depoimentos/depoimentos/portrt-smiling-black-man.jpg.jpeg'
import avatarEmilio from '@/assets/depoimentos/depoimentos/young-hispanic-man-smiling-confident-park.jpg.jpeg'
import avatarLucas from '@/assets/depoimentos/depoimentos/close-up-excited-person-portrait.jpg.jpeg'

const route = useRoute()

const row1Testimonials = computed(() => [
  {
    id: 1,
    name: "Josef, ES",
    text: t('testimonialJosefText', 'home'),
    avatar: avatarJosef,
    flag: "https://flagcdn.com/w40/es.png",
    bgColor: "#1c5bf0",
    textColor: "#ffffff",
    trustpilot: false
  },
  {
    id: 2,
    name: "Chantal, FR",
    text: t('testimonialChantalText', 'home'),
    avatar: avatarChantal,
    flag: "https://flagcdn.com/w40/fr.png",
    bgColor: "#1243c2",
    textColor: "#ffffff",
    trustpilot: false
  },
  {
    id: 3,
    name: "Chloe, US",
    text: t('testimonialChloeText', 'home'),
    avatar: avatarChloe,
    flag: "https://flagcdn.com/w40/us.png",
    bgColor: "#2b60e6",
    textColor: "#ffffff",
    trustpilot: false
  }
])

const row2Testimonials = computed(() => [
  {
    id: 4,
    name: "Jasmine, CA",
    text: t('testimonialJasmineText', 'home'),
    avatar: avatarJasmine,
    flag: "https://flagcdn.com/w40/ca.png",
    bgColor: "#4a7cf2",
    textColor: "#ffffff",
    trustpilot: true
  },
  {
    id: 5,
    name: "Arielle, US",
    text: t('testimonialArielleText', 'home'),
    avatar: avatarArielle,
    flag: "https://flagcdn.com/w40/us.png",
    bgColor: "#0d2d85",
    textColor: "#ffffff",
    trustpilot: true
  },
  {
    id: 6,
    name: "Benjamin, US",
    text: t('testimonialBenjaminText', 'home'),
    avatar: avatarBenjamin,
    flag: "https://flagcdn.com/w40/us.png",
    bgColor: "#1c5bf0",
    textColor: "#ffffff",
    trustpilot: true
  }
])

const row3Testimonials = computed(() => [
  {
    id: 7,
    name: "Maria, PT",
    text: t('testimonialMariaText', 'home'),
    avatar: avatarMaria,
    flag: "https://flagcdn.com/w40/pt.png",
    bgColor: "#1243c2",
    textColor: "#ffffff",
    trustpilot: true
  },
  {
    id: 8,
    name: "Adrian, CA",
    text: t('testimonialAdrianText', 'home'),
    avatar: avatarAdrian,
    flag: "https://flagcdn.com/w40/ca.png",
    bgColor: "#2b60e6",
    textColor: "#ffffff",
    trustpilot: false
  },
  {
    id: 9,
    name: "Pierre, FR",
    text: t('testimonialPierreText', 'home'),
    avatar: avatarPierre,
    flag: "https://flagcdn.com/w40/fr.png",
    bgColor: "#4a7cf2",
    textColor: "#ffffff",
    trustpilot: false
  }
])

const row4Testimonials = computed(() => [
  {
    id: 10,
    name: "Alan, BR",
    text: t('testimonialAlanText', 'home'),
    avatar: avatarAlan,
    flag: "https://flagcdn.com/w40/br.png",
    bgColor: "#0d2d85",
    textColor: "#ffffff",
    trustpilot: true
  },
  {
    id: 11,
    name: "Emilio, IT",
    text: t('testimonialEmilioText', 'home'),
    avatar: avatarEmilio,
    flag: "https://flagcdn.com/w40/it.png",
    bgColor: "#1c5bf0",
    textColor: "#ffffff",
    trustpilot: false
  },
  {
    id: 12,
    name: "Lucas, US",
    text: t('testimonialLucasText', 'home'),
    avatar: avatarLucas,
    flag: "https://flagcdn.com/w40/us.png",
    bgColor: "#1243c2",
    textColor: "#ffffff",
    trustpilot: false
  }
])

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

  if (route.hash) {
    setTimeout(() => {
      const element = document.querySelector(route.hash)
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' })
      }
    }, 500)
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
            <video 
              autoplay 
              muted 
              loop 
              playsinline 
              class="hero-video-bg"
            >
              <source :src="videoPlayback" type="video/mp4">
            </video>
            <div class="hero-overlay"></div>
            <div class="slide2-content-wrapper" data-swiper-parallax="-400">
              <div class="reveal active slide2-content">
                <div class="subheading-container">
                  <span class="subheading-text accent-color">{{ t('heroTag2', 'home') }}</span>
                </div>
                <h2 class="slide2-title">{{ t('heroTitle2', 'home') }} <span class="accent-color">{{ t('heroHighlight2', 'home') }}</span></h2>
                <p class="slide2-desc">{{ t('heroDesc2', 'home') }}</p>
                <RouterLink to="/nossa-escola" class="btn-vip btn-accent">{{ t('heroMore', 'home') }} <ChevronRight class="btn-icon" /></RouterLink>
              </div>
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
          <div class="reveal reveal-left escola-info">
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
          
          <div class="reveal reveal-right photo-reveal">
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
                <div class="flag-circle">
                  <img src="https://flagcdn.com/w40/gb.png" alt="UK Flag">
                </div>
                <div class="card-label" style="background-color: rgb(33, 68, 139);">{{ t('ingles', 'home') }}</div>
              </RouterLink>
            </div>
            
            <!-- Espanhol -->
            <div class="swiper-slide curso-card" style="--card-delay: 0.25s;">
              <RouterLink to="/cursos/espanhol" class="curso-link">
                <img src="/assets/espanolcard.jpeg" alt="Espanhol Card" class="curso-img">
                <div class="flag-circle">
                  <img src="https://flagcdn.com/w40/es.png" alt="Spain Flag">
                </div>
                <div class="card-label" style="background-color: rgb(176, 87, 22);">{{ t('espanhol', 'home') }}</div>
              </RouterLink>
            </div>
            
            <!-- Francês -->
            <div class="swiper-slide curso-card" style="--card-delay: 0.45s;">
              <RouterLink to="/cursos/frances" class="curso-link">
                <img src="/assets/francescard.jpeg" alt="Francês Card" class="curso-img">
                <div class="flag-circle">
                  <img src="https://flagcdn.com/w40/fr.png" alt="France Flag">
                </div>
                <div class="card-label" style="background-color: rgb(40, 68, 107);">{{ t('frances', 'home') }}</div>
              </RouterLink>
            </div>
            
            <!-- Português -->
            <div class="swiper-slide curso-card" style="--card-delay: 0.65s;">
              <RouterLink to="/cursos/portugues" class="curso-link">
                <img src="/assets/portuguesecard.jpeg" alt="Português Card" class="curso-img">
                <div class="flag-circle">
                  <img src="https://flagcdn.com/w40/br.png" alt="Brazil Flag">
                </div>
                <div class="card-label" style="background-color: rgb(11, 94, 40);">{{ t('portugues', 'home') }}</div>
              </RouterLink>
            </div>
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
          <RouterLink to="/services/traducoes" class="glass-card-btn reveal reveal-left reveal-delay-1">
            <div class="servico-icon-container">
              <FileText class="servico-icon" />
            </div>
            <h3 class="servico-title">{{ t('servicoCardTitle1', 'home') }}</h3>
            <p class="servico-desc">{{ t('servicoCardDesc1', 'home') }}</p>
          </RouterLink>

          <!-- Serviço 2: Aulas de Conversação -->
          <RouterLink to="/services/aulas-conversacao" class="glass-card-btn reveal reveal-right reveal-delay-2">
            <div class="servico-icon-container">
              <MessagesSquare class="servico-icon" />
            </div>
            <h3 class="servico-title">{{ t('servicoCardTitle2', 'home') }}</h3>
            <p class="servico-desc">{{ t('servicoCardDesc2', 'home') }}</p>
          </RouterLink>
        </div>
      </div>
    </section>

    <!-- App Promo Banner Section -->
    <section class="app-banner-section container">
      <div class="app-banner-card">
        <div class="app-banner-content reveal reveal-left reveal-delay-1">
          <span class="app-banner-tag">{{ t('appBannerTag', 'home') }}</span>
          <h2 class="app-banner-title">{{ t('appBannerTitle', 'home') }}</h2>
          <p class="app-banner-desc">
            {{ t('appBannerDesc', 'home') }}
          </p>
          <div class="app-banner-buttons">
            <a href="https://changeskills.com.br" target="_blank" class="btn-app-download">
              {{ t('appBannerBtn', 'home') }}
            </a>
          </div>
        </div>
        <div class="app-banner-mockup reveal reveal-right reveal-delay-2">
          <!-- Glow background -->
          <div class="mockup-glow"></div>

          <!-- CSS Phone Frame -->
          <div class="phone-mockup-frame">
            <div class="phone-screen">
              <img src="/assets/img/camaleao_chat.png" alt="Change Skills App Screenshot" class="app-mockup-img">
            </div>
          </div>

          <!-- Floating Interactive Badges -->
          <div class="floating-element badge-en">
            <span class="badge-icon-wrap"><Languages class="badge-icon" /></span>
            <span class="badge-text">Speak English</span>
          </div>
          <div class="floating-element badge-ai">
            <span class="badge-icon-wrap"><Bot class="badge-icon" /></span>
            <span class="badge-text">Camaleão IA</span>
          </div>
          <div class="floating-element badge-xp">
            <span class="badge-icon-wrap"><Zap class="badge-icon" /></span>
            <span class="badge-text">Daily Practice</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. Depoimentos (Testimonials Carousel) -->
    <section id="depoimentos" class="new-testimonials-section reveal">
      <!-- Row 1: scrolls left -->
      <div class="marquee-wrapper">
        <div class="marquee-track marquee-left marquee-row-1">
          <!-- Main items -->
          <div v-for="item in row1Testimonials" :key="item.id" class="testimonial-bubble-card">
            <div class="bubble-layout">
              <div class="avatar-container">
                <img :src="item.avatar" class="avatar-img" alt="User Avatar" />
                <div class="flag-badge">
                  <img :src="item.flag" class="flag-img" alt="Country Flag" />
                </div>
              </div>
              <div class="bubble-speech" :style="{ backgroundColor: item.bgColor }">
                <div class="bubble-arrow" :style="{ borderRightColor: item.bgColor }"></div>
                <p class="bubble-text">{{ item.text }}</p>
                <div class="bubble-footer">
                  <span class="user-name">{{ item.name }}</span>
                  <div v-if="item.trustpilot" class="trustpilot-rating">
                    <span class="star-icon">★</span>
                    <span class="trustpilot-text">Trustpilot</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- Duplicate items for infinite scrolling loop -->
          <div v-for="item in row1Testimonials" :key="'dup1-' + item.id" class="testimonial-bubble-card">
            <div class="bubble-layout">
              <div class="avatar-container">
                <img :src="item.avatar" class="avatar-img" alt="User Avatar" />
                <div class="flag-badge">
                  <img :src="item.flag" class="flag-img" alt="Country Flag" />
                </div>
              </div>
              <div class="bubble-speech" :style="{ backgroundColor: item.bgColor }">
                <div class="bubble-arrow" :style="{ borderRightColor: item.bgColor }"></div>
                <p class="bubble-text">{{ item.text }}</p>
                <div class="bubble-footer">
                  <span class="user-name">{{ item.name }}</span>
                  <div v-if="item.trustpilot" class="trustpilot-rating">
                    <span class="star-icon">★</span>
                    <span class="trustpilot-text">Trustpilot</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Row 2: scrolls right -->
      <div class="marquee-wrapper">
        <div class="marquee-track marquee-right marquee-row-2">
          <!-- Main items -->
          <div v-for="item in row2Testimonials" :key="item.id" class="testimonial-bubble-card">
            <div class="bubble-layout">
              <div class="avatar-container">
                <img :src="item.avatar" class="avatar-img" alt="User Avatar" />
                <div class="flag-badge">
                  <img :src="item.flag" class="flag-img" alt="Country Flag" />
                </div>
              </div>
              <div class="bubble-speech" :style="{ backgroundColor: item.bgColor }">
                <div class="bubble-arrow" :style="{ borderRightColor: item.bgColor }"></div>
                <p class="bubble-text">{{ item.text }}</p>
                <div class="bubble-footer">
                  <span class="user-name">{{ item.name }}</span>
                  <div v-if="item.trustpilot" class="trustpilot-rating">
                    <span class="star-icon">★</span>
                    <span class="trustpilot-text">Trustpilot</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- Duplicate items for infinite scrolling loop -->
          <div v-for="item in row2Testimonials" :key="'dup2-' + item.id" class="testimonial-bubble-card">
            <div class="bubble-layout">
              <div class="avatar-container">
                <img :src="item.avatar" class="avatar-img" alt="User Avatar" />
                <div class="flag-badge">
                  <img :src="item.flag" class="flag-img" alt="Country Flag" />
                </div>
              </div>
              <div class="bubble-speech" :style="{ backgroundColor: item.bgColor }">
                <div class="bubble-arrow" :style="{ borderRightColor: item.bgColor }"></div>
                <p class="bubble-text">{{ item.text }}</p>
                <div class="bubble-footer">
                  <span class="user-name">{{ item.name }}</span>
                  <div v-if="item.trustpilot" class="trustpilot-rating">
                    <span class="star-icon">★</span>
                    <span class="trustpilot-text">Trustpilot</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Center Title -->
      <div class="testimonials-center-title-container">
        <h2 class="bastidores-title">{{ t('bastidoresTitle', 'home') }}</h2>
      </div>

      <!-- Row 3: scrolls left -->
      <div class="marquee-wrapper">
        <div class="marquee-track marquee-left marquee-row-3">
          <!-- Main items -->
          <div v-for="item in row3Testimonials" :key="item.id" class="testimonial-bubble-card">
            <div class="bubble-layout">
              <div class="avatar-container">
                <img :src="item.avatar" class="avatar-img" alt="User Avatar" />
                <div class="flag-badge">
                  <img :src="item.flag" class="flag-img" alt="Country Flag" />
                </div>
              </div>
              <div class="bubble-speech" :style="{ backgroundColor: item.bgColor }">
                <div class="bubble-arrow" :style="{ borderRightColor: item.bgColor }"></div>
                <p class="bubble-text">{{ item.text }}</p>
                <div class="bubble-footer">
                  <span class="user-name">{{ item.name }}</span>
                  <div v-if="item.trustpilot" class="trustpilot-rating">
                    <span class="star-icon">★</span>
                    <span class="trustpilot-text">Trustpilot</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- Duplicate items for infinite scrolling loop -->
          <div v-for="item in row3Testimonials" :key="'dup3-' + item.id" class="testimonial-bubble-card">
            <div class="bubble-layout">
              <div class="avatar-container">
                <img :src="item.avatar" class="avatar-img" alt="User Avatar" />
                <div class="flag-badge">
                  <img :src="item.flag" class="flag-img" alt="Country Flag" />
                </div>
              </div>
              <div class="bubble-speech" :style="{ backgroundColor: item.bgColor }">
                <div class="bubble-arrow" :style="{ borderRightColor: item.bgColor }"></div>
                <p class="bubble-text">{{ item.text }}</p>
                <div class="bubble-footer">
                  <span class="user-name">{{ item.name }}</span>
                  <div v-if="item.trustpilot" class="trustpilot-rating">
                    <span class="star-icon">★</span>
                    <span class="trustpilot-text">Trustpilot</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Row 4: scrolls right -->
      <div class="marquee-wrapper">
        <div class="marquee-track marquee-right marquee-row-4">
          <!-- Main items -->
          <div v-for="item in row4Testimonials" :key="item.id" class="testimonial-bubble-card">
            <div class="bubble-layout">
              <div class="avatar-container">
                <img :src="item.avatar" class="avatar-img" alt="User Avatar" />
                <div class="flag-badge">
                  <img :src="item.flag" class="flag-img" alt="Country Flag" />
                </div>
              </div>
              <div class="bubble-speech" :style="{ backgroundColor: item.bgColor }">
                <div class="bubble-arrow" :style="{ borderRightColor: item.bgColor }"></div>
                <p class="bubble-text">{{ item.text }}</p>
                <div class="bubble-footer">
                  <span class="user-name">{{ item.name }}</span>
                  <div v-if="item.trustpilot" class="trustpilot-rating">
                    <span class="star-icon">★</span>
                    <span class="trustpilot-text">Trustpilot</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- Duplicate items for infinite scrolling loop -->
          <div v-for="item in row4Testimonials" :key="'dup4-' + item.id" class="testimonial-bubble-card">
            <div class="bubble-layout">
              <div class="avatar-container">
                <img :src="item.avatar" class="avatar-img" alt="User Avatar" />
                <div class="flag-badge">
                  <img :src="item.flag" class="flag-img" alt="Country Flag" />
                </div>
              </div>
              <div class="bubble-speech" :style="{ backgroundColor: item.bgColor }">
                <div class="bubble-arrow" :style="{ borderRightColor: item.bgColor }"></div>
                <p class="bubble-text">{{ item.text }}</p>
                <div class="bubble-footer">
                  <span class="user-name">{{ item.name }}</span>
                  <div v-if="item.trustpilot" class="trustpilot-rating">
                    <span class="star-icon">★</span>
                    <span class="trustpilot-text">Trustpilot</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
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
          <div v-for="(item, idx) in faqs" :key="idx" class="faq-vip-item" :class="{ 'active': isFaqOpen[idx] }">
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
  background: #001233;
  overflow: hidden;
}

.hero-video-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 0;
  opacity: 1;
  pointer-events: none;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.45);
  z-index: 1;
}

.slide2-content-wrapper {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  padding-bottom: 240px; /* Shift content slightly higher up from the bottom */
  z-index: 10;
  pointer-events: none;
}

.slide2-content {
  width: 100%;
  max-width: 800px;
  text-align: center;
  padding: 0 20px;
  margin: 0 auto;
  pointer-events: auto;
}

.slide2-content .subheading-container {
  justify-content: center;
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
  margin: 0 auto 3rem auto;
  max-width: 700px;
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
  height: 400px;
  border-radius: 40px;
  overflow: hidden;
  text-decoration: none;
  transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.4s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
}

.curso-link:hover {
  transform: translateY(-12px) scale(1.02);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
}

/* Subtle dark gradient overlay to highlight text */
.curso-link::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.35) 0%, rgba(0, 0, 0, 0.05) 50%, rgba(0, 0, 0, 0) 100%);
  z-index: 1;
  pointer-events: none;
  transition: background-image 0.4s ease;
}

.curso-link:hover::before {
  background: linear-gradient(to top, rgba(0, 0, 0, 0.45) 0%, rgba(0, 0, 0, 0.1) 50%, rgba(0, 0, 0, 0) 100%);
}

/* Card Glare Shine Effect */
.curso-link::after {
  content: '';
  position: absolute;
  top: 0;
  left: -150%;
  width: 125%;
  height: 100%;
  background: linear-gradient(
    to right,
    rgba(255, 255, 255, 0) 0%,
    rgba(255, 255, 255, 0.3) 50%,
    rgba(255, 255, 255, 0) 100%
  );
  transform: skewX(-25deg);
  transition: 0.75s;
  z-index: 3;
}

.curso-link:hover::after {
  left: 150%;
}

.curso-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 0;
  transition: transform 0.6s cubic-bezier(0.25, 1, 0.5, 1);
}

.curso-link:hover .curso-img {
  transform: scale(1.08);
}

.flag-circle {
  position: absolute;
  top: 18px;
  left: 18px;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  z-index: 2;
  overflow: hidden;
  background: white;
  border: 3px solid white;
  transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.curso-link:hover .flag-circle {
  transform: scale(1.15) rotate(8deg);
}

.flag-circle img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.card-label {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 16px;
  color: white;
  font-weight: 800;
  font-size: 20px;
  text-align: center;
  transition: padding-bottom 0.3s ease, font-size 0.3s ease;
  z-index: 2;
}

.curso-link:hover .card-label {
  padding-bottom: 22px;
  font-size: 22px;
}

/* Testimonials Carousel (New) */
.new-testimonials-section {
  background-color: #ffffff;
  padding: 80px 0;
  overflow: hidden;
  position: relative;
  width: 100%;
}

.marquee-wrapper {
  overflow: hidden;
  width: 100%;
  display: flex;
  align-items: center;
  margin: 1.5rem 0;
  /* Premium fade effect on left and right sides */
  mask-image: linear-gradient(to right, transparent, white 15%, white 85%, transparent);
  -webkit-mask-image: linear-gradient(to right, transparent, white 15%, white 85%, transparent);
}

.marquee-track {
  display: flex;
  gap: 2rem;
  width: max-content;
}

.marquee-row-1 {
  animation: scrollLeft 38s linear infinite;
}

.marquee-row-2 {
  animation: scrollRight 46s linear infinite;
}

.marquee-row-3 {
  animation: scrollLeft 42s linear infinite;
}

.marquee-row-4 {
  animation: scrollRight 34s linear infinite;
}

.marquee-track:hover {
  animation-play-state: paused;
}

@keyframes scrollLeft {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-50%);
  }
}

@keyframes scrollRight {
  0% {
    transform: translateX(-50%);
  }
  100% {
    transform: translateX(0);
  }
}

.testimonial-bubble-card {
  flex-shrink: 0;
  display: flex;
  align-items: center;
}

.bubble-layout {
  display: flex;
  align-items: center;
  gap: 12px;
}

.avatar-container {
  position: relative;
  width: 65px;
  height: 65px;
  flex-shrink: 0;
}

.avatar-img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #ffffff;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
}

.flag-badge {
  position: absolute;
  bottom: -2px;
  right: -2px;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  border: 2px solid #ffffff;
  overflow: hidden;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
  background-color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
}

.flag-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.bubble-speech {
  position: relative;
  border-radius: 24px;
  padding: 1.4rem 1.8rem;
  margin-left: 12px;
  display: flex;
  flex-direction: column;
  color: #ffffff;
  max-width: 400px;
  min-width: 260px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.bubble-arrow {
  position: absolute;
  top: 50%;
  left: -8px;
  transform: translateY(-50%);
  width: 0;
  height: 0;
  border-top: 8px solid transparent;
  border-bottom: 8px solid transparent;
  border-right: 8px solid;
}

.bubble-text {
  font-size: 1.15rem;
  font-weight: 800;
  line-height: 1.35;
  color: #ffffff;
  margin: 0 0 10px 0;
  letter-spacing: -0.01em;
}

.bubble-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 15px;
}

.user-name {
  font-size: 0.9rem;
  font-weight: 700;
  color: rgba(255, 255, 255, 0.85);
}

.trustpilot-rating {
  display: flex;
  align-items: center;
  gap: 3px;
  color: #34d399;
  font-weight: 800;
  font-size: 0.85rem;
}

.trustpilot-rating .star-icon {
  font-size: 1rem;
}

.testimonials-center-title-container {
  padding: 3.5rem 1.5rem;
  text-align: center;
}

.bastidores-title {
  font-size: clamp(2.2rem, 5vw, 3.8rem);
  font-weight: 900;
  color: #000000;
  line-height: 1.15;
  letter-spacing: -0.03em;
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
  transform: translateY(-10px) scale(1.05);
  border: 1px solid #000000 !important;
  box-shadow: 0 30px 60px rgba(0, 0, 0, 0.12) !important;
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
    width: 100% !important;
    max-width: 100% !important;
    text-align: center !important;
    padding: 0 15px !important;
  }
  
  .slide2-title {
    font-size: clamp(1.8rem, 5vw, 2.4rem) !important;
    text-shadow: 0 4px 12px rgba(0,0,0,0.5);
    margin-bottom: 1rem !important;
  }
  
  .slide2-desc {
    font-size: 1rem !important;
    margin: 0 auto 1.8rem auto !important;
    max-width: 90% !important;
    text-shadow: 0 2px 6px rgba(0,0,0,0.5);
  }
}

/* App Banner Section */
.app-banner-section {
  padding-top: 80px;
  padding-bottom: 80px;
}

.app-banner-card {
  background: linear-gradient(135deg, #1c5bf0 0%, #0c3da6 100%);
  border-radius: 40px;
  display: grid;
  grid-template-columns: 1.25fr 0.75fr;
  align-items: center;
  position: relative;
  overflow: hidden;
  box-shadow: 0 30px 60px rgba(28, 91, 240, 0.25);
  padding: 0;
}

.app-banner-content {
  padding: 5rem 6rem;
  color: white;
  text-align: left;
}

.app-banner-tag {
  color: var(--accent);
  font-weight: 800;
  letter-spacing: 0.2em;
  font-size: 0.9rem;
  text-transform: uppercase;
  display: inline-block;
  margin-bottom: 1.5rem;
}

.app-banner-title {
  font-size: clamp(2.2rem, 4vw, 3.2rem);
  font-weight: 900;
  color: white;
  line-height: 1.2;
  margin: 0 0 1.5rem 0;
  letter-spacing: -0.02em;
}

.app-banner-desc {
  color: rgba(255, 255, 255, 0.9);
  font-size: 1.15rem;
  line-height: 1.8;
  margin: 0 0 3rem 0;
  max-width: 550px;
}

.btn-app-download {
  display: inline-flex;
  align-items: center;
  background: white;
  color: #1c5bf0;
  text-decoration: none;
  padding: 1.2rem 3rem;
  border-radius: 99px;
  font-weight: 850;
  font-size: 1.1rem;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.btn-app-download:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.25);
  background: var(--primary-dark);
  color: white;
}

.app-banner-mockup {
  position: relative;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 3rem 0;
  left: -40px; /* Shifts the mockup and badges 40px to the left on desktop layout */
}

.mockup-glow {
  position: absolute;
  width: 280px;
  height: 280px;
  background: radial-gradient(circle, rgba(0, 209, 255, 0.35) 0%, transparent 70%);
  z-index: 1;
  pointer-events: none;
  filter: blur(30px);
}

.phone-mockup-frame {
  border: 10px solid #1e293b;
  border-radius: 38px;
  background: #1e293b;
  box-shadow: 0 30px 60px -15px rgba(0, 0, 0, 0.5);
  position: relative;
  width: 250px;
  height: 530px; /* Increased height to 530px to prevent cropping of top/bottom details */
  overflow: hidden;
  transform: translateY(10px) rotate(-3deg);
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
  z-index: 2;
}

.phone-mockup-frame::after {
  content: '';
  position: absolute;
  top: 10px;
  left: 50%;
  transform: translateX(-50%);
  width: 65px;
  height: 16px;
  background: #000000;
  border-radius: 20px;
  z-index: 10;
}

.phone-screen {
  width: 100%;
  height: 100%;
  background: #f3f6fc; /* Matches app background */
  overflow: hidden;
  position: relative;
  border-radius: 28px;
}

.app-mockup-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: top;
  display: block;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.app-banner-card:hover .phone-mockup-frame {
  transform: translateY(-10px) rotate(0deg) scale(1.05);
}

/* Floating Badges */
.floating-element {
  position: absolute;
  background: rgba(255, 255, 255, 0.94);
  backdrop-filter: blur(12px);
  padding: 0.65rem 1.1rem;
  border-radius: 20px;
  box-shadow: 0 15px 35px rgba(0, 0, 100, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.3);
  display: flex;
  align-items: center;
  gap: 10px;
  z-index: 5;
  font-weight: 800;
  color: var(--primary-dark);
  font-size: 0.85rem;
  pointer-events: none;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.badge-icon-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 8px;
  flex-shrink: 0;
}

.badge-en .badge-icon-wrap {
  background: rgba(0, 71, 255, 0.1);
  color: var(--primary);
}

.badge-ai .badge-icon-wrap {
  background: rgba(168, 85, 247, 0.15);
  color: #a855f7;
}

.badge-xp .badge-icon-wrap {
  background: rgba(245, 158, 11, 0.15);
  color: #f59e0b;
}

.badge-icon {
  width: 15px;
  height: 15px;
}

.badge-en {
  top: 15%;
  left: -15px;
  transform: rotate(-8deg);
}

.badge-ai {
  top: 45%;
  right: -5px; /* Shipped inwards to prevent cropping */
  transform: rotate(6deg);
}

.badge-xp {
  bottom: 15%;
  left: -5px;
  transform: rotate(4deg);
}

/* Hover dynamics for floating elements */
.app-banner-card:hover .badge-en {
  transform: translate(-15px, -12px) rotate(-12deg) scale(1.08);
}

.app-banner-card:hover .badge-ai {
  transform: translate(6px, -5px) rotate(10deg) scale(1.08); /* Safer translate value */
}

.app-banner-card:hover .badge-xp {
  transform: translate(-10px, 12px) rotate(2deg) scale(1.08);
}

@media (max-width: 1024px) {
  .app-banner-card {
    grid-template-columns: 1fr;
    text-align: center;
  }
  .app-banner-content {
    padding: 4rem 3rem 2rem 3rem;
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .app-banner-desc {
    margin-left: auto;
    margin-right: auto;
  }
  .app-banner-mockup {
    padding-top: 2rem;
    overflow: hidden;
    left: 0; /* Reset left offset on mobile layout to keep it centered */
  }
  .phone-mockup-frame {
    width: 220px;
    height: 470px;
    border-radius: 34px;
    border-width: 8px;
    transform: translateY(10px) rotate(0deg);
  }
  .phone-screen {
    border-radius: 26px;
  }
  .app-banner-card:hover .phone-mockup-frame {
    transform: translateY(0) scale(1.03);
  }
  .badge-en {
    left: 10px;
    top: 20%;
  }
  .badge-ai {
    right: 10px;
    top: 50%;
  }
  .badge-xp {
    left: 15px;
    bottom: 20%;
  }
}

/* Responsive design for smaller desktop screens (widths) */
@media (max-width: 1680px) {
  .hero-grid {
    gap: 3rem;
  }
  .hero-title {
    font-size: clamp(2.5rem, 4vw, 3.8rem);
  }
  .hero-desc {
    font-size: 1.15rem;
    margin-bottom: 2.5rem;
  }
  .mascot-img {
    max-width: 420px;
  }
  .slide2-title {
    font-size: clamp(2.2rem, 4.5vw, 3.5rem);
  }
  .slide2-desc {
    font-size: 1.15rem;
    margin-bottom: 2rem;
    max-width: 650px;
  }
  .slide2-content-wrapper {
    padding-bottom: 210px;
  }
}

@media (max-width: 1440px) {
  .hero-grid {
    gap: 2.5rem;
  }
  .hero-title {
    font-size: clamp(2.2rem, 3.8vw, 3.2rem);
  }
  .hero-desc {
    font-size: 1.1rem;
    margin-bottom: 2rem;
  }
  .mascot-img {
    max-width: 360px;
  }
  .slide2-title {
    font-size: clamp(2rem, 4.2vw, 3rem);
  }
  .slide2-desc {
    font-size: 1.1rem;
    margin-bottom: 1.8rem;
    max-width: 600px;
  }
  .slide2-content-wrapper {
    padding-bottom: 170px;
  }
}

@media (max-width: 1280px) {
  .hero-grid {
    gap: 1.5rem;
  }
  .hero-title {
    font-size: clamp(2rem, 3.5vw, 2.8rem);
  }
  .hero-desc {
    font-size: 1.05rem;
    margin-bottom: 1.5rem;
  }
  .mascot-img {
    max-width: 300px;
  }
  .slide2-title {
    font-size: clamp(1.8rem, 4vw, 2.6rem);
  }
  .slide2-desc {
    font-size: 1.05rem;
    margin-bottom: 1.5rem;
    max-width: 550px;
  }
  .slide2-content-wrapper {
    padding-bottom: 140px;
  }
}

/* Responsive design for smaller desktop screens (heights) */
@media (max-height: 900px) {
  .hero-grid {
    padding-top: 80px;
    gap: 2.5rem;
  }
  .hero-title {
    font-size: clamp(2.5rem, 4vw, 3.5rem);
    margin-bottom: 1.5rem;
  }
  .hero-desc {
    margin-bottom: 2rem;
    font-size: 1.1rem;
  }
  .mascot-img {
    max-width: 380px;
  }
  .slide2-title {
    font-size: clamp(2.2rem, 4.5vw, 3.2rem);
    margin-bottom: 1.2rem;
  }
  .slide2-desc {
    margin-bottom: 1.8rem;
    font-size: 1.1rem;
  }
  .slide2-content-wrapper {
    padding-bottom: 180px;
  }
  .subheading-container {
    margin-bottom: 1.2rem;
  }
}

@media (max-height: 800px) {
  .hero-grid {
    padding-top: 60px;
    gap: 2rem;
  }
  .hero-title {
    font-size: clamp(2.2rem, 3.8vw, 3rem);
    margin-bottom: 1.2rem;
  }
  .hero-desc {
    margin-bottom: 1.5rem;
    font-size: 1.05rem;
    line-height: 1.7;
  }
  .mascot-img {
    max-width: 320px;
  }
  .slide2-title {
    font-size: clamp(2rem, 4vw, 2.6rem);
    margin-bottom: 1rem;
  }
  .slide2-desc {
    margin-bottom: 1.5rem;
    font-size: 1.05rem;
    line-height: 1.6;
  }
  .slide2-content-wrapper {
    padding-bottom: 140px;
  }
  .btn-accent {
    padding: 1rem 2.8rem !important;
  }
  .subheading-container {
    margin-bottom: 1rem;
  }
}

@media (max-height: 700px) {
  .hero-grid {
    padding-top: 40px;
    gap: 1.5rem;
  }
  .hero-title {
    font-size: clamp(1.8rem, 3.5vw, 2.5rem);
    margin-bottom: 1rem;
  }
  .hero-desc {
    margin-bottom: 1rem;
    font-size: 0.95rem;
    line-height: 1.5;
  }
  .mascot-img {
    max-width: 260px;
  }
  .slide2-title {
    font-size: clamp(1.8rem, 3.5vw, 2.2rem);
    margin-bottom: 0.8rem;
  }
  .slide2-desc {
    margin-bottom: 1.2rem;
    font-size: 0.95rem;
    line-height: 1.5;
  }
  .slide2-content-wrapper {
    padding-bottom: 110px;
  }
  .subheading-container {
    margin-bottom: 0.8rem;
  }
}
</style>

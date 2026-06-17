<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { ArrowRight, ChevronLeft, ChevronRight, X, ExternalLink } from '@lucide/vue'
import { t } from '@/i18n'

const teachers = computed(() => [
  {
    name: t('teacherNames.paula', 'school'),
    language: t('teacherLanguages.ingles', 'school'),
    flags: ["🇺🇸", "🇬🇧"],
    image: "https://changeskills.com.br/wp-content/uploads/2025/11/WhatsApp-Image-2025-11-09-at-08.42.35.jpeg",
    desc: t('teacherDescs.paula', 'school')
  },
  {
    name: t('teacherNames.brenda', 'school'),
    language: t('teacherLanguages.ingles', 'school'),
    flags: ["🇺🇸", "🇬🇧"],
    image: "https://changeskills.com.br/wp-content/uploads/2025/11/WhatsApp-Image-2025-11-09-at-08.45.01.jpeg",
    desc: t('teacherDescs.brenda', 'school')
  },
  {
    name: t('teacherNames.michele', 'school'),
    language: t('teacherLanguages.inglesPort', 'school'),
    flags: ["🇺🇸", "🇬🇧", "🇧🇷"],
    image: "https://changeskills.com.br/wp-content/uploads/2025/11/WhatsApp-Image-2025-11-08-at-20.19.03-1.jpeg",
    desc: t('teacherDescs.michele', 'school')
  },
  {
    name: t('teacherNames.ritchely', 'school'),
    language: t('teacherLanguages.ingles', 'school'),
    flags: ["🇺🇸", "🇬🇧"],
    image: "https://changeskills.com.br/wp-content/uploads/2025/11/WhatsApp-Image-2025-11-08-at-17.46.40-1.jpeg",
    desc: t('teacherDescs.ritchely', 'school')
  },
  {
    name: t('teacherNames.bruna', 'school'),
    language: t('teacherLanguages.ingles', 'school'),
    flags: ["🇺🇸", "🇬🇧"],
    image: "https://changeskills.com.br/wp-content/uploads/2025/11/WhatsApp-Image-2025-11-08-at-11.09.52.jpeg",
    desc: t('teacherDescs.bruna', 'school')
  },
  {
    name: t('teacherNames.wagner', 'school'),
    language: t('teacherLanguages.inglesCientifico', 'school'),
    flags: ["🇺🇸", "🇬🇧"],
    image: "https://changeskills.com.br/wp-content/uploads/2025/11/WhatsApp-Image-2025-11-08-at-11.05.18-1.jpeg",
    desc: t('teacherDescs.wagner', 'school')
  },
  {
    name: t('teacherNames.tayllana', 'school'),
    language: t('teacherLanguages.ingles', 'school'),
    flags: ["🇺🇸", "🇬🇧"],
    image: "https://changeskills.com.br/wp-content/uploads/2025/11/WhatsApp-Image-2025-11-10-at-18.09.59.jpeg",
    desc: t('teacherDescs.tayllana', 'school')
  },
  {
    name: t('teacherNames.adriana', 'school'),
    language: t('teacherLanguages.espanhol', 'school'),
    flags: ["🇪🇸", "🇵🇪"],
    image: "/assets/img/adriana.png",
    desc: t('teacherDescs.adriana', 'school')
  },
  {
    name: t('teacherNames.erika', 'school'),
    language: t('teacherLanguages.espanholFrancesIngles', 'school'),
    flags: ["🇪🇸", "🇫🇷", "🇺🇸", "🇪🇨"],
    image: "/assets/img/erika.png",
    desc: t('teacherDescs.erika', 'school')
  }
])

const isModalOpen = ref(false)
const activeIndex = ref(0)

function openModal(index) {
  activeIndex.value = index
  isModalOpen.value = true
  document.body.style.overflow = 'hidden' // Lock scroll
}

function closeModal() {
  isModalOpen.value = false
  document.body.style.overflow = '' // Restore scroll
}

function nextTeacher() {
  activeIndex.value = (activeIndex.value + 1) % teachers.value.length
}

function prevTeacher() {
  activeIndex.value = (activeIndex.value - 1 + teachers.value.length) % teachers.value.length
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

  // Load GSAP & ScrollTrigger dynamically to animate the timeline
  loadGSAP(() => {
    initTimelineAnimation()
  })
})

function loadGSAP(callback) {
  if (window.gsap && window.ScrollTrigger) {
    callback()
    return
  }

  if (!document.getElementById('gsap-core-js')) {
    const gsapScript = document.createElement('script')
    gsapScript.id = 'gsap-core-js'
    gsapScript.src = 'https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js'
    gsapScript.onload = () => {
      const triggerScript = document.createElement('script')
      triggerScript.id = 'gsap-trigger-js'
      triggerScript.src = 'https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js'
      triggerScript.onload = () => {
        window.gsap.registerPlugin(window.ScrollTrigger)
        callback()
      }
      document.body.appendChild(triggerScript)
    }
    document.body.appendChild(gsapScript)
  } else {
    const interval = setInterval(() => {
      if (window.gsap && window.ScrollTrigger) {
        clearInterval(interval)
        callback()
      }
    }, 100)
  }
}

function initTimelineAnimation() {
  const gsap = window.gsap
  const ScrollTrigger = window.ScrollTrigger

  // Draw active progress line as scroll occurs
  gsap.fromTo('.timeline-progress-line',
    { height: '0%' },
    {
      height: '100%',
      ease: 'none',
      scrollTrigger: {
        trigger: '.timeline-wrapper',
        start: 'top 70%',
        end: 'bottom 70%',
        scrub: true
      }
    }
  )

  // Pop dots and slide timeline content in
  const nodes = document.querySelectorAll('.timeline-node')
  nodes.forEach((node) => {
    const dot = node.querySelector('.timeline-dot')
    const title = node.querySelector('.node-title')
    const desc = node.querySelector('.node-desc')

    // Dot scale pop & background change
    gsap.fromTo(dot,
      { scale: 0.5, backgroundColor: '#cbd5e1', borderColor: '#cbd5e1' },
      {
        scale: 1,
        backgroundColor: '#1c5bf0',
        borderColor: '#ffffff',
        scrollTrigger: {
          trigger: node,
          start: 'top 70%',
          toggleActions: 'play none none reverse'
        }
      }
    )

    // Content fade & slide translation
    gsap.fromTo([title, desc],
      { opacity: 0, x: 40 },
      {
        opacity: 1,
        x: 0,
        stagger: 0.1,
        duration: 0.65,
        ease: 'power2.out',
        scrollTrigger: {
          trigger: node,
          start: 'top 80%',
          toggleActions: 'play none none reverse'
        }
      }
    )
  })
}

function initSwiper() {
  new window.Swiper('.teacher-swiper', {
    slidesPerView: 3,
    spaceBetween: 30,
    speed: 800,
    autoplay: {
      delay: 3500,
      disableOnInteraction: false,
    },
    loop: true,
    pagination: { el: '.swiper-pagination', clickable: true },
    breakpoints: {
      320: { slidesPerView: 1 },
      768: { slidesPerView: 2 },
      1024: { slidesPerView: 3 }
    }
  })
}

onUnmounted(() => {
  if (window.ScrollTrigger) {
    window.ScrollTrigger.getAll().forEach(trigger => trigger.kill())
  }
})
</script>

<template>
  <div class="nossa-escola-view">
    <!-- Hero Header Segment -->
    <section class="nossa-jornada-section">
      <div class="container">
        <div class="jornada-grid">
          <div class="reveal active">
            <span class="segment-tag">{{ t('segmentTag', 'school') }}</span>
            <h2 class="jornada-title">{{ t('jornadaTitle', 'school') }}</h2>
            <p class="jornada-desc">
              {{ t('jornadaDesc', 'school') }}
            </p>
          </div>
          
          <div class="reveal photo-card-reveal">
            <div class="photo-wrapper">
              <img src="/assets/img/image.png" alt="Tay & Wagner - Change Skills" class="photo-img">
              <div class="photo-overlay"></div>
              <div class="photo-caption">
                <p class="photo-names">{{ t('photoCaptionNames', 'school') }}</p>
                <p class="photo-subtitle">{{ t('photoCaptionSubtitle', 'school') }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Timeline of History -->
    <section class="container timeline-section">
      <div class="reveal text-center header-margin">
        <span class="section-tag">{{ t('timelineTag', 'school') }}</span>
        <h2 class="section-title">{{ t('timelineTitle', 'school') }}</h2>
      </div>
      
      <div class="reveal timeline-wrapper">
        <div class="timeline-progress-line"></div>
        <div v-for="(node, idx) in t('timelineNodes', 'school')" :key="idx" class="timeline-node">
          <div class="timeline-dot"></div>
          <h3 class="node-title">{{ node.title }}</h3>
          <p class="node-desc" v-html="node.desc"></p>
        </div>
      </div>
    </section>

    <!-- Teachers Carousel Section -->
    <section id="professores" class="teachers-section mesh-bg">
      <div class="container reveal">
        <span class="section-tag">{{ t('mentoresTag', 'school') }}</span>
        <h2 class="section-title">{{ t('mentoresTitle', 'school') }}</h2>
        <p class="section-desc max-width-desc">{{ t('mentoresDesc', 'school') }}</p>
        
        <div class="swiper teacher-swiper reveal">
          <div class="swiper-wrapper">
            <div v-for="(teacher, idx) in teachers" :key="idx" class="swiper-slide">
              <div class="teacher-card" @click="openModal(idx)">
                <div class="teacher-img-wrapper">
                  <img :src="teacher.image" class="teacher-img" :alt="teacher.name">
                </div>
                <div class="teacher-info">
                  <h3 class="teacher-name">{{ teacher.name }}</h3>
                  <div class="teacher-lang-badges">
                    <span class="teacher-language">{{ teacher.language }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="swiper-pagination"></div>
        </div>
      </div>
    </section>

    <!-- Spotify Playlist Section -->
    <section class="container spotify-section">
      <div class="reveal spotify-wrapper-card">
        <div class="spotify-accent-glow-1"></div>
        <div class="spotify-accent-glow-2"></div>
        
        <div class="spotify-grid">
          <div class="spotify-info">
            <div class="spotify-tag-container">
              <svg viewBox="0 0 24 24" class="spotify-badge-icon">
                <path d="M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm4.586 14.424c-.18.295-.565.387-.86.207-2.377-1.454-5.37-1.783-8.893-.982-.336.075-.668-.135-.744-.47-.077-.337.135-.668.47-.745 3.856-.88 7.15-.503 9.82 1.13.297.182.39.567.207.86zm1.226-2.724c-.226.367-.707.487-1.074.26-2.72-1.672-6.87-2.157-10.075-1.183-.413.127-.85-.106-.977-.52-.127-.414.106-.85.52-.977 3.665-1.11 8.232-.574 11.347 1.34.367.227.487.708.26 1.08zm.107-2.85c-.273.447-.86.593-1.307.32-3.18-1.89-8.413-2.062-11.457-1.137-.502.153-1.026-.135-1.18-.636-.154-.502.136-1.027.637-1.18 3.615-1.1 9.387-.9 13.01 1.25.447.266.593.853.32 1.3z"/>
              </svg>
              <span class="spotify-tag-text">{{ t('spotifyTag', 'school') }}</span>
            </div>
            <h2 class="spotify-title">{{ t('spotifyTitle', 'school') }}</h2>
            <p class="spotify-desc">
              {{ t('spotifyDesc', 'school') }}
            </p>
            <a href="https://open.spotify.com/playlist/41Uf49j61tWGXsnOQ9Is1s" target="_blank" rel="noopener" class="btn-spotify">
              {{ t('spotifyBtn', 'school') }} <ExternalLink class="external-icon" />
            </a>
          </div>
          <div class="spotify-player">
            <iframe style="border-radius:24px" src="https://open.spotify.com/embed/playlist/41Uf49j61tWGXsnOQ9Is1s?utm_source=generator&theme=0" width="100%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
          </div>
        </div>
      </div>
    </section>

    <!-- Reusable profile modal system -->
    <transition name="fade">
      <div v-if="isModalOpen" class="modal-overlay active">
        <!-- Close overlay -->
        <div class="modal-backdrop" @click="closeModal"></div>
        
        <!-- Close Button -->
        <button class="modal-close" @click="closeModal" :aria-label="t('ariaClose', 'school')">
          <X class="close-icon" />
        </button>
        
        <!-- Floating Navigation -->
        <button class="modal-nav-btn modal-nav-prev" @click="prevTeacher" :aria-label="t('ariaPrev', 'school')">
          <ChevronLeft class="nav-arrow" />
        </button>
        <button class="modal-nav-btn modal-nav-next" @click="nextTeacher" :aria-label="t('ariaNext', 'school')">
          <ChevronRight class="nav-arrow" />
        </button>

        <div class="modal-content">
          <div class="modal-left">
            <img :src="teachers[activeIndex].image" :alt="teachers[activeIndex].name" class="modal-profile-img">
          </div>
          <div class="modal-right">
            <h2 class="modal-profile-name">{{ teachers[activeIndex].name }}</h2>
            <div class="modal-profile-lang">
              <span>{{ teachers[activeIndex].language }}</span>
            </div>
            <div class="modal-profile-desc" v-html="teachers[activeIndex].desc"></div>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>


<style scoped>
.nossa-escola-view {
  width: 100%;
}

.nossa-jornada-section {
  background: var(--primary-dark);
  color: white;
  padding: 180px 0 100px 0;
  overflow: hidden;
  position: relative;
}

.segment-tag {
  color: var(--accent);
  font-weight: 800;
  letter-spacing: 0.2em;
  display: inline-block;
  margin-bottom: 1.5rem;
  text-transform: uppercase;
  font-size: 0.9rem;
}

.jornada-title {
  font-size: 4rem;
  color: white;
  margin-top: 0.5rem;
  margin-bottom: 0;
  font-weight: 800;
}

.jornada-desc {
  font-size: 1.2rem;
  color: rgba(255, 255, 255, 0.8);
  margin-top: 3rem;
  line-height: 1.8;
  margin-bottom: 0;
}

.jornada-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8rem;
  align-items: center;
}

.photo-card-reveal {
  text-align: center;
}

.photo-wrapper {
  position: relative;
  border-radius: 40px;
  overflow: hidden;
  box-shadow: 0 30px 60px rgba(0, 0, 0, 0.3);
}

.photo-img {
  width: 100%;
  height: 480px;
  object-fit: cover;
  object-position: center 85%;
  display: block;
}

.photo-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0, 18, 51, 0.8) 0%, rgba(0, 18, 51, 0) 60%);
}

.photo-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 2rem;
  z-index: 2;
  text-align: center;
}

.photo-names {
  color: white;
  font-weight: 700;
  font-size: 1.15rem;
  margin: 0;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.photo-subtitle {
  color: rgba(255, 255, 255, 0.85);
  font-size: 0.9rem;
  margin: 5px 0 0 0;
  font-weight: 500;
}

/* Timeline */
.timeline-section {
  padding-top: 120px;
  padding-bottom: 120px;
}

.section-tag {
  color: var(--primary);
  font-weight: 800;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  font-size: 0.9rem;
  display: inline-block;
}

.section-title {
  font-size: 3rem;
  color: var(--primary-dark);
  margin-top: 1rem;
  font-weight: 800;
  margin-bottom: 0;
}

.header-margin {
  margin-bottom: 5rem;
}

.timeline-wrapper {
  max-width: 800px;
  margin: 0 auto;
  position: relative;
  padding-left: 2rem;
}

.timeline-wrapper::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 4px;
  background: #cbd5e1; /* Gray track background */
  border-radius: 2px;
}

.timeline-progress-line {
  position: absolute;
  left: 0;
  top: 0;
  width: 4px;
  height: 0%;
  background: var(--primary);
  border-radius: 2px;
  z-index: 1;
}

.timeline-node {
  margin-bottom: 3.5rem;
  position: relative;
}

.timeline-node:last-child {
  margin-bottom: 0;
}

.timeline-dot {
  width: 20px;
  height: 20px;
  background: #cbd5e1;
  border-radius: 50%;
  position: absolute;
  left: -2.5rem; /* Centered over the 4px line which is at left: 0 relative to wrapper */
  top: 5px;
  border: 4px solid #cbd5e1;
  box-sizing: border-box;
  z-index: 2;
}

.node-title {
  color: var(--primary-dark);
  font-size: 1.55rem;
  margin-top: 0;
  margin-bottom: 0.5rem;
  font-weight: 800;
}

.node-desc {
  color: var(--gray);
  font-size: 1.1rem;
  margin: 0;
  line-height: 1.7;
}

/* Teachers Segment */
.teachers-section {
  padding: 120px 0;
  text-align: center;
}

.section-desc {
  font-size: 1.2rem;
  color: var(--gray);
  margin-top: 1rem;
  margin-bottom: 0;
}

.max-width-desc {
  max-width: 800px;
  margin: 1rem auto 4rem auto;
}

.teacher-swiper {
  width: 100%;
  padding: 2rem 0 4rem 0;
}

.swiper-slide {
  height: auto;
}

.teacher-card {
  position: relative;
  border-radius: 30px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  cursor: pointer;
  height: 480px;
  max-width: 320px;
  margin: 0 auto;
  display: block;
}

.teacher-card:hover {
  transform: translateY(-10px);
  box-shadow: var(--shadow-premium);
}

.teacher-img-wrapper {
  width: 100%;
  height: 100%;
  overflow: hidden;
  position: relative;
  border-radius: 30px;
}

.teacher-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center top;
  display: block;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.teacher-card:hover .teacher-img {
  transform: scale(1.08);
}

.teacher-info {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0, 18, 51, 0.95) 0%, rgba(0, 18, 51, 0.6) 50%, rgba(0, 18, 51, 0) 100%);
  padding: 2rem;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: center;
  text-align: center;
  opacity: 0;
  transform: translateY(10px);
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  pointer-events: none;
  z-index: 2;
  gap: 0.5rem;
}

.teacher-card:hover .teacher-info {
  opacity: 1;
  transform: translateY(0);
}

.teacher-name {
  color: white;
  font-size: 1.3rem;
  margin: 0;
  font-weight: 800;
  line-height: 1.3;
  text-shadow: 0 2px 4px rgba(0,0,0,0.5);
}

.teacher-lang-badges {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 0.2rem;
}

.teacher-language {
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--accent);
  background: rgba(255, 255, 255, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.25);
  backdrop-filter: blur(5px);
  border-radius: 999px;
  padding: 0.25rem 0.85rem;
  letter-spacing: 0.03em;
}

/* Spotify block */
.spotify-section {
  padding: 120px 0;
}

.spotify-wrapper-card {
  background: linear-gradient(135deg, #020D1A 0%, #082A4D 50%, #0F172A 100%);
  border-radius: 40px;
  padding: 5rem 6rem;
  position: relative;
  overflow: hidden;
  box-shadow: 0 25px 60px rgba(0, 209, 255, 0.15);
}

.spotify-accent-glow-1 {
  position: absolute;
  top: -50%;
  left: -30%;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(0, 209, 255, 0.15) 0%, rgba(0, 209, 255, 0) 70%);
  pointer-events: none;
}

.spotify-accent-glow-2 {
  position: absolute;
  bottom: -50%;
  right: -30%;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(30, 215, 96, 0.1) 0%, rgba(30, 215, 96, 0) 70%);
  pointer-events: none;
}

.spotify-grid {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 6rem;
  align-items: center;
  position: relative;
  z-index: 2;
}

.spotify-tag-container {
  display: inline-flex;
  align-items: center;
  gap: 0.8rem;
  background: rgba(30, 215, 96, 0.15);
  border: 1px solid rgba(30, 215, 96, 0.3);
  padding: 0.6rem 1.2rem;
  border-radius: 50px;
  margin-bottom: 2rem;
  backdrop-filter: blur(10px);
}

.spotify-badge-icon {
  width: 20px;
  height: 20px;
  fill: #1DB954;
}

.spotify-tag-text {
  color: #1DB954;
  font-weight: 700;
  font-size: 0.9rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.spotify-title {
  font-size: 3.2rem;
  color: white;
  line-height: 1.2;
  margin-bottom: 1.5rem;
  font-weight: 800;
  margin-top: 0;
}

.spotify-desc {
  color: rgba(255, 255, 255, 0.75);
  font-size: 1.2rem;
  line-height: 1.8;
  margin-bottom: 3rem;
  margin-top: 0;
}

.btn-spotify {
  display: inline-flex;
  align-items: center;
  gap: 1rem;
  background: #1DB954;
  color: white;
  text-decoration: none;
  padding: 1.2rem 2.5rem;
  border-radius: 50px;
  font-weight: 700;
  font-size: 1.1rem;
  box-shadow: 0 15px 30px rgba(30, 215, 96, 0.3);
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.btn-spotify:hover {
  background: #1ed760 !important;
  transform: translateY(-5px) scale(1.02);
  box-shadow: 0 20px 40px rgba(30, 215, 96, 0.5) !important;
}

.external-icon {
  width: 20px;
  height: 20px;
}

.spotify-player {
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
  line-height: 0;
}

/* Modal Teacher */
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(5, 5, 68, 0.8);
  backdrop-filter: blur(10px);
  z-index: 2000;
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-backdrop {
  position: absolute;
  inset: 0;
  z-index: 2001;
  cursor: pointer;
}

.modal-content {
  background: white;
  width: 92%;
  max-width: 1100px;
  height: 85vh;
  border-radius: 40px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  overflow: hidden;
  position: relative;
  z-index: 2005;
  box-shadow: 0 30px 80px rgba(0, 0, 0, 0.3);
}

.modal-left {
  height: 100%;
  overflow: hidden;
}

.modal-profile-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.modal-right {
  padding: 4rem 3.5rem;
  overflow-y: auto;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  text-align: left;
}

.modal-profile-name {
  font-size: 3rem;
  color: var(--primary-dark);
  margin-bottom: 1rem;
  margin-top: 0;
  font-weight: 800;
}

.modal-profile-lang {
  margin-bottom: 1.5rem;
  font-size: 1.2rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--primary-dark);
}

.modal-flag {
  font-size: 1.3rem;
}

.modal-profile-desc {
  font-size: 1.2rem;
  color: var(--gray);
  line-height: 1.8;
}

.modal-close {
  position: fixed;
  top: 2rem;
  right: 2rem;
  background: white;
  border: none;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
  transition: all 0.3s;
  z-index: 2100;
  color: var(--primary-dark);
}

.modal-close:hover {
  background: var(--primary);
  color: white;
}

.close-icon {
  width: 24px;
  height: 24px;
}

/* Floating Navigation */
.modal-nav-btn {
  position: fixed;
  top: 50%;
  transform: translateY(-50%);
  background: white;
  border: none;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  transition: all 0.3s;
  z-index: 2010;
  color: var(--primary-dark);
}

.modal-nav-btn:hover {
  background: var(--primary);
  color: white;
  transform: translateY(-50%) scale(1.1);
}

.modal-nav-prev { left: 2rem; }
.modal-nav-next { right: 2rem; }

.nav-arrow {
  width: 28px;
  height: 28px;
}

/* Transitions */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
.fade-enter-active .modal-content,
.fade-leave-active .modal-content {
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.fade-enter-from .modal-content,
.fade-leave-to .modal-content {
  transform: scale(0.95);
}

/* Responsive modal and segment queries */
@media (max-width: 991px) {
  .jornada-grid {
    grid-template-columns: 1fr;
    gap: 4rem;
    text-align: center;
  }
  
  .photo-img {
    height: 380px;
  }

  .spotify-wrapper-card {
    padding: 4rem 3rem;
  }
  
  .spotify-grid {
    grid-template-columns: 1fr;
    gap: 3.5rem;
  }
  
  .modal-content {
    grid-template-columns: 1fr;
    height: 90vh;
    overflow: hidden;
  }
  
  .modal-left {
    height: 35vh;
    flex-shrink: 0;
  }
  
  .modal-right {
    padding: 2rem 1.75rem 5rem;
    overflow-y: auto;
    flex: 1;
  }
  
  .modal-nav-btn {
    width: 42px;
    height: 42px;
    top: auto;
    bottom: 1rem;
    transform: none;
  }

  .modal-nav-btn:hover {
    transform: scale(1.05);
  }
  
  .modal-nav-prev { left: 1.5rem; top: auto; bottom: 1rem; }
  .modal-nav-next { right: 1.5rem; top: auto; bottom: 1rem; }

  .teacher-swiper .swiper-slide {
    width: 75vw;
  }
}

@media (max-width: 600px) {
  .teachers-section {
    padding: 80px 0;
  }

  .teacher-img {
    height: 260px;
  }

  .teacher-info {
    padding: 1.25rem 1.25rem 1.5rem;
  }

  .modal-left {
    height: 30vh;
  }

  .modal-right {
    padding: 1.5rem 1.25rem 5rem;
  }

  .modal-profile-name {
    font-size: 1.8rem;
  }

  .modal-close {
    top: 1rem;
    right: 1rem;
    width: 40px;
    height: 40px;
  }
}

</style>

<script setup>
import { onMounted, computed } from 'vue'
import { RouterLink } from 'vue-router'
import { LayoutGrid, BookOpen, UserPlus, Award } from '@lucide/vue'
import { t } from '@/i18n'

const portals = computed(() => [
  {
    type: 'external',
    href: 'https://login.pearson.com/v1/piapi/iesui/signin?client_id=bWPoUiRnLpUhX2rhGeP4AaLCeyQYNYDA&login_success_url=https:%2F%2Fenglish-dashboard.pearson.com%2Fies-session%3FiesCode%3DWn8DsKPPaG',
    title: t('pearsonTitle', 'student'),
    desc: t('pearsonDesc', 'student'),
    icon: LayoutGrid
  },
  {
    type: 'external',
    href: 'https://www.blinklearning.com/v/1778658518/themes/tmpux/launch.php#content/mybooks',
    title: t('blinkTitle', 'student'),
    desc: t('blinkDesc', 'student'),
    icon: BookOpen
  },
  {
    type: 'internal',
    to: '/cadastro-aluno',
    title: t('cadastroTitle', 'student'),
    desc: t('cadastroDesc', 'student'),
    icon: UserPlus
  },
  {
    type: 'internal',
    to: '/services/solicitacao-certificado',
    title: t('certificadoTitle', 'student'),
    desc: t('certificadoDesc', 'student'),
    icon: Award
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
  <div class="area-aluno-view">
    <main class="student-hub-main">
      <!-- Background elements -->
      <div class="glow-bg"></div>
      
      <div class="container reveal active student-hub-content">
        <!-- Section Header -->
        <div class="hub-header">
          <span class="hub-tag">{{ t('hubTag', 'student') }}</span>
          <h1 class="hub-title">{{ t('hubTitle', 'student') }}</h1>
          <p class="hub-desc" v-html="t('hubDesc', 'student')"></p>
        </div>

        <!-- Grid Options -->
        <div class="hub-grid">
          <template v-for="(item, idx) in portals" :key="idx">
            <!-- External portals -->
            <a 
              v-if="item.type === 'external'" 
              :href="item.href" 
              target="_blank" 
              rel="noopener"
              :class="['glass-card', 'hub-card', 'reveal', 'reveal-scale']"
              :style="{ transitionDelay: (idx * 0.15) + 's' }"
            >
              <component :is="item.icon" class="hub-card-icon" />
              <h3 class="hub-card-title">{{ item.title }}</h3>
              <p class="hub-card-desc">{{ item.desc }}</p>
            </a>
            
            <!-- Internal app routes -->
            <RouterLink 
              v-else 
              :to="item.to" 
              :class="['glass-card', 'hub-card', 'reveal', 'reveal-scale']"
              :style="{ transitionDelay: (idx * 0.15) + 's' }"
            >
              <component :is="item.icon" class="hub-card-icon" />
              <h3 class="hub-card-title">{{ item.title }}</h3>
              <p class="hub-card-desc">{{ item.desc }}</p>
            </RouterLink>
          </template>
        </div>
      </div>
    </main>
  </div>
</template>

<style scoped>
.area-aluno-view {
  width: 100%;
}

.student-hub-main {
  background: var(--bg-light);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 220px 0 120px 0; /* visually offset header height and push content down */
  position: relative;
  overflow: hidden;
  box-sizing: border-box;
}

.glow-bg {
  position: absolute;
  top: -10%;
  left: -10%;
  width: 600px;
  height: 600px;
  background: var(--primary);
  filter: blur(250px);
  opacity: 0.1;
  border-radius: 50%;
  z-index: 0;
}

.student-hub-content {
  position: relative;
  z-index: 1;
}

.hub-header {
  text-align: left;
  margin-bottom: 4rem;
}

.hub-tag {
  color: var(--primary);
  font-weight: 800;
  letter-spacing: 0.2em;
  display: block;
  margin-bottom: 0.5rem;
  text-transform: uppercase;
  font-size: 0.9rem;
}

.hub-title {
  color: var(--primary-dark);
  font-size: clamp(3rem, 5vw, 4.5rem);
  margin-bottom: 1.5rem;
  margin-top: 0;
  font-weight: 800;
}

.hub-desc {
  color: var(--gray);
  font-size: 1.2rem;
  max-width: 680px;
  line-height: 1.8;
  margin: 0;
}

.hub-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2.5rem;
}

.hub-card {
  background: white;
  border: 1px solid rgba(0, 0, 0, 0.05);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  border-radius: 24px;
  padding: 3.5rem 2rem;
  text-align: center;
  color: var(--primary-dark);
  text-decoration: none;
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
  align-items: center;
  box-sizing: border-box;
}

.hub-card:hover {
  transform: translateY(-10px) scale(1.05);
  border: 1px solid #000000 !important;
  box-shadow: 0 30px 60px rgba(0, 0, 0, 0.12) !important;
}

.hub-card-icon {
  color: var(--primary);
  width: 48px;
  height: 48px;
  margin-bottom: 1.5rem;
}

.hub-card-title {
  font-size: 1.4rem;
  margin-bottom: 1rem;
  color: var(--primary-dark);
  font-weight: 700;
  margin-top: 0;
}

.hub-card-desc {
  color: var(--gray);
  line-height: 1.6;
  margin: 0;
  font-size: 1rem;
}
</style>

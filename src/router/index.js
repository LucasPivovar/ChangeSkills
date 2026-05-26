import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home.vue')
  },
  {
    path: '/nossa-escola',
    name: 'NossaEscola',
    component: () => import('@/views/NossaEscola.vue')
  },
  {
    path: '/contato',
    name: 'Contato',
    component: () => import('@/views/Contato.vue')
  },
  {
    path: '/area-do-aluno',
    name: 'AreaDoAluno',
    component: () => import('@/views/AreaDoAluno.vue')
  },
  {
    path: '/cadastro-aluno',
    name: 'CadastroAluno',
    component: () => import('@/views/CadastroAluno.vue')
  },
  // Cursos
  {
    path: '/cursos/ingles',
    name: 'Ingles',
    component: () => import('@/views/Cursos/Ingles.vue')
  },
  {
    path: '/cursos/espanhol',
    name: 'Espanhol',
    component: () => import('@/views/Cursos/Espanhol.vue')
  },
  {
    path: '/cursos/frances',
    name: 'Frances',
    component: () => import('@/views/Cursos/Frances.vue')
  },
  {
    path: '/cursos/portugues',
    name: 'Portugues',
    component: () => import('@/views/Cursos/Portugues.vue')
  },
  // Services
  {
    path: '/services/agendamento-nivelamento',
    name: 'AgendamentoNivelamento',
    component: () => import('@/views/Services/AgendamentoNivelamento.vue')
  },
  {
    path: '/services/aulas-conversacao',
    name: 'AulasConversacao',
    component: () => import('@/views/Services/AulasConversacao.vue')
  },
  {
    path: '/services/solicitacao-certificado',
    name: 'SolicitacaoCertificado',
    component: () => import('@/views/Services/SolicitacaoCertificado.vue')
  },
  {
    path: '/services/traducoes',
    name: 'Traducoes',
    component: () => import('@/views/Services/Traducoes.vue')
  },
  {
    path: '/services/verificacao-certificado',
    name: 'VerificacaoCertificado',
    component: () => import('@/views/Services/VerificacaoCertificado.vue')
  },
  // Modalities
  {
    path: '/cursos/modalidades/business',
    name: 'Business',
    component: () => import('@/views/Modalidades/Business.vue')
  },
  {
    path: '/cursos/modalidades/espanhol-adultos',
    name: 'EspanholAdultos',
    component: () => import('@/views/Modalidades/EspanholAdultos.vue')
  },
  {
    path: '/cursos/modalidades/espanhol-jovens',
    name: 'EspanholJovens',
    component: () => import('@/views/Modalidades/EspanholJovens.vue')
  },
  {
    path: '/cursos/modalidades/excellence',
    name: 'Excellence',
    component: () => import('@/views/Modalidades/Excellence.vue')
  },
  {
    path: '/cursos/modalidades/ingles-50-plus',
    name: 'Ingles50Plus',
    component: () => import('@/views/Modalidades/Ingles50Plus.vue')
  },
  {
    path: '/cursos/modalidades/fast-track',
    name: 'FastTrack',
    component: () => import('@/views/Modalidades/FastTrack.vue')
  },
  {
    path: '/cursos/modalidades/frances-ados',
    name: 'FrancesAdos',
    component: () => import('@/views/Modalidades/FrancesAdos.vue')
  },
  {
    path: '/cursos/modalidades/frances-adultes',
    name: 'FrancesAdultes',
    component: () => import('@/views/Modalidades/FrancesAdultes.vue')
  },
  {
    path: '/cursos/modalidades/frances-enfants',
    name: 'FrancesEnfants',
    component: () => import('@/views/Modalidades/FrancesEnfants.vue')
  },
  {
    path: '/cursos/modalidades/kids',
    name: 'Kids',
    component: () => import('@/views/Modalidades/Kids.vue')
  },
  {
    path: '/cursos/modalidades/portugues-adultos',
    name: 'PortuguesAdultos',
    component: () => import('@/views/Modalidades/PortuguesAdultos.vue')
  },
  {
    path: '/cursos/modalidades/portugues-jovens',
    name: 'PortuguesJovens',
    component: () => import('@/views/Modalidades/PortuguesJovens.vue')
  },
  {
    path: '/cursos/modalidades/scientific',
    name: 'Scientific',
    component: () => import('@/views/Modalidades/Scientific.vue')
  },
  {
    path: '/cursos/modalidades/teens',
    name: 'Teens',
    component: () => import('@/views/Modalidades/Teens.vue')
  },
  // Redirect any undefined route back to Home
  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    }
    // Scroll to section if hash exists, else top of page
    if (to.hash) {
      return { el: to.hash, behavior: 'smooth' }
    }
    return { top: 0 }
  }
})

router.afterEach((to, from) => {
  // Wait for the new page view component to mount and render
  setTimeout(() => {
    const storedLang = localStorage.getItem('selectedLanguage') || 'pt'
    const translateSelect = document.querySelector('.goog-te-combo')
    if (translateSelect) {
      // Reset state to pt first to force Google Translate to re-scan
      if (translateSelect.value !== 'pt' && storedLang !== 'pt') {
        translateSelect.value = 'pt'
        translateSelect.dispatchEvent(new Event('change'))
      }
      
      // Apply chosen language
      setTimeout(() => {
        translateSelect.value = storedLang
        translateSelect.dispatchEvent(new Event('change'))
      }, 100)
    }
  }, 450)
})

export default router

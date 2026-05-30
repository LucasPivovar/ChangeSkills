<script setup>
import { ref, computed, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { ArrowLeft, ArrowRight, Check, MessagesSquare, Compass, Clock, Award } from '@lucide/vue'

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

  // Setup reveal IntersectionObserver
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active')
      }
    })
  }, { threshold: 0.1 })
  
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el))
})

function initSwiper() {
  if (window.Swiper) {
    new window.Swiper('.material-swiper', {
      slidesPerView: 4,
      spaceBetween: 20,
      pagination: { el: '.material-swiper .swiper-pagination', clickable: true },
      breakpoints: {
        0:    { slidesPerView: 1 },
        600:  { slidesPerView: 2 },
        900:  { slidesPerView: 3 },
        1200: { slidesPerView: 4 }
      }
    })
  }
}

// Wizard Form Reactive State
const step = ref(1)
const formData = ref({
  nome: '',
  sobrenome: '',
  email: '',
  telefone: '',
  pref_contato: 'whatsapp',
  nivel: '',
  objetivo: ''
})

const isStep1Valid = computed(() => formData.value.nome.trim() !== '')
const isStep2Valid = computed(() => {
  const emailRegex = /^[^s@]+@[^s@]+\.[^s@]+$/
  return emailRegex.test(formData.value.email) && formData.value.telefone.trim() !== ''
})
const isStep3Valid = computed(() => !!formData.value.pref_contato)
const isStep4Valid = computed(() => formData.value.nivel !== '' && formData.value.objetivo !== '')

const progressWidth = computed(() => ((step.value - 1) / 3) * 100 + '%')

function nextStep() {
  if (step.value === 1 && isStep1Valid.value) step.value = 2
  else if (step.value === 2 && isStep2Valid.value) step.value = 3
  else if (step.value === 3 && isStep3Valid.value) step.value = 4
}

function prevStep() {
  if (step.value > 1) step.value--
}

function submitForm() {
  if (isStep4Valid.value) {
    alert('Sua solicitação para o Curso de Inglês 50+ foi recebida com carinho! Entraremos em contato muito em breve.')
    formData.value = {
      nome: '',
      sobrenome: '',
      email: '',
      telefone: '',
      pref_contato: 'whatsapp',
      nivel: '',
      objetivo: ''
    }
    step.value = 1
  }
}
</script>

<template>
  <div class="modality-detail-view">
    <div class="back-nav">
      <div class="container">
        <RouterLink to="/cursos/ingles" class="back-link">
          <ArrowLeft class="btn-icon-svg" /> Voltar para os Cursos
        </RouterLink>
      </div>
    </div>

    <!-- Hero Section -->
    <section class="hero-section">
      <div class="container hero-grid reveal active">
        <div style="text-align: left;">
          <span style="color: var(--primary); font-weight: 800; letter-spacing: 0.2em; display: inline-block; margin-bottom: 1.5rem; text-transform: uppercase;">Change Skills 50+</span>
          <h1 style="font-size: 5rem; margin-bottom: 2rem; line-height: 1.1; color: var(--primary-dark);">Inglês para <span style="color: var(--primary);">50+</span></h1>
          <p style="font-size: 1.6rem; color: var(--primary-dark); font-weight: 600; margin-bottom: 1.5rem;">
            Aprenda inglês para viajar e se comunicar com confiança!
          </p>
          <p style="font-size: 1.2rem; color: var(--gray); margin-bottom: 3rem; line-height: 1.8; max-width: 600px;">
            Na <strong>Change Skills</strong>, oferecemos um curso leve, prático e no seu próprio ritmo. Ideal para quem deseja viajar, fazer amigos e expandir horizontes sem a pressão da gramática tradicional.
          </p>
          <a href="#agendamento" class="btn-vip" style="text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem; padding: 1.1rem 3rem; font-size: 1.2rem;">
            Agende uma aula grátis <ArrowRight style="width: 22px;" class="info-icon" />
          </a>
        </div>
        <div class="hero-image-container">
          <img src="/assets/img/ingles-50-hero.png" alt="Inglês 50+">
        </div>
      </div>
    </section>

    <!-- Como funciona -->
    <section class="container" style="padding: 80px 0;">
      <div class="reveal" style="text-align: center; margin-bottom: 5rem;">
        <h2 style="font-size: 2.8rem; margin-bottom: 1.5rem; color: var(--primary-dark);">Como funciona o curso</h2>
        <p style="font-size: 1.2rem; color: var(--gray); max-width: 900px; margin: auto; line-height: 1.8;">
          O curso 50+ foi desenvolvido especialmente para adultos que buscam praticidade e querem se conectar com o mundo de forma descontraída.
        </p>
      </div>
      
      <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.5rem;">
        <div class="glass-card reveal" style="padding: 3rem 2rem; text-align: center; background: #f8faff; border: none;">
          <MessagesSquare style="color: var(--primary); width: 45px; height: 45px; margin-bottom: 1.5rem;" class="info-icon" />
          <h3 style="color: var(--primary-dark); margin-bottom: 1rem;">Conversação</h3>
          <p style="color: var(--gray); line-height: 1.6;">Prática real focada no vocabulário que você realmente vai usar.</p>
        </div>
        <div class="glass-card reveal" style="padding: 3rem 2rem; text-align: center; background: #f8faff; border: none;">
          <Clock style="color: var(--accent); width: 45px; height: 45px; margin-bottom: 1.5rem;" class="info-icon" />
          <h3 style="color: var(--primary-dark); margin-bottom: 1rem;">Sem Pressão</h3>
          <p style="color: var(--gray); line-height: 1.6;">Aulas dinâmicas e personalizadas que respeitam o seu próprio ritmo.</p>
        </div>
        <div class="glass-card reveal" style="padding: 3rem 2rem; text-align: center; background: #f8faff; border: none;">
          <Compass style="color: var(--primary); width: 45px; height: 45px; margin-bottom: 1.5rem;" class="info-icon" />
          <h3 style="color: var(--primary-dark); margin-bottom: 1rem;">Independência</h3>
          <p style="color: var(--gray); line-height: 1.6;">Conquiste total autonomia para explorar o mundo em suas viagens.</p>
        </div>
      </div>
    </section>

    <!-- Material Section -->
    <section style="background: #f8faff; padding: 100px 0;">
      <div class="container reveal">
        <div style="text-align: center; margin-bottom: 5rem;">
          <h2 style="font-size: 2.8rem; color: var(--primary-dark); margin-bottom: 2rem;">O que você vai aprender</h2>
          <p style="color: var(--gray); font-size: 1.15rem; line-height: 1.8; max-width: 850px; margin: 0 auto;">
            Foco total em situações úteis e reais da vida real, para você aplicar no dia a dia ou em viagens.
          </p>
        </div>

        <div class="material-grid">
          <div class="material-item reveal">
            <img src="/assets/img/ingles-50-viagem.png" alt="Inglês para Viagens">
            <h4>Inglês para Viagens</h4>
            <p>Imigração, aeroportos, hotéis, compras e direções no exterior.</p>
          </div>
          <div class="material-item reveal">
            <img src="/assets/img/ingles-50-viver.png" alt="Conversação Real">
            <h4>Conversação Real</h4>
            <p>Apresentações, preferências pessoais e como fazer novos amigos.</p>
          </div>
          <div class="material-item reveal">
            <img src="/assets/img/ingles-50-mundo.png" alt="Experiências">
            <h4>Experiências de Lazer</h4>
            <p>Aproveite hotéis, cruzeiros, museus e passeios com independência.</p>
          </div>
          <div class="material-item reveal">
            <img src="/assets/img/ingles-50-hero.png" alt="Mente Ativa">
            <h4>Estímulo e Hobbies</h4>
            <p>Mantenha a mente sempre ativa, saudável e aprenda de forma divertida.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Estrutura dos Níveis -->
    <section style="background: white; padding: 100px 0;">
      <div class="container">
        <div class="reveal" style="text-align: left; margin-bottom: 5rem;">
          <span style="color: var(--primary); font-weight: 800; letter-spacing: 0.2em; text-transform: uppercase;">Pilares</span>
          <h2 style="margin-top: 1rem; font-size: 3rem; color: var(--primary-dark);">Nossos Pilares de Ensino</h2>
        </div>
        <div style="display: grid; gap: 2rem;">

          <div class="level-card reveal">
            <div class="level-number">Pilar 1</div>
            <div class="level-title">Comunicação Sem Pressão</div>
            <p style="color: var(--gray); line-height: 1.7; margin-bottom: 1rem;">O foco é a utilidade prática do vocabulário, e não a memorização de regras teóricas cansativas.</p>
            <div class="topic-tags">
              <span class="topic-tag">Viagem</span>
              <span class="topic-tag">Dia-a-dia</span>
              <span class="topic-tag">Praticidade</span>
            </div>
          </div>

          <div class="level-card reveal">
            <div class="level-number">Pilar 2</div>
            <div class="level-title">Repetição Contextualizada</div>
            <p style="color: var(--gray); line-height: 1.7; margin-bottom: 1rem;">Você aprende estruturas gramaticais de forma orgânica e intuitiva, participando de diálogos guiados de uso imediato.</p>
            <div class="topic-tags">
              <span class="topic-tag">Simulação Real</span>
              <span class="topic-tag">Diálogos</span>
              <span class="topic-tag">Pronúncia</span>
            </div>
          </div>

          <div class="level-card reveal">
            <div class="level-number">Pilar 3</div>
            <div class="level-title">Acolhimento e Paciência</div>
            <p style="color: var(--gray); line-height: 1.7; margin-bottom: 1rem;">Um ambiente leve, onde errar faz parte do progresso. As aulas são moldadas exclusivamente aos seus interesses.</p>
            <div class="topic-tags">
              <span class="topic-tag">Seu Tempo</span>
              <span class="topic-tag">Empatia</span>
              <span class="topic-tag">Confiança</span>
            </div>
          </div>

          <div class="level-card reveal">
            <div class="level-number">Pilar 4</div>
            <div class="level-title">Atendimento Exclusivo</div>
            <p style="color: var(--gray); line-height: 1.7; margin-bottom: 1rem;">Acompanhamento próximo, suporte humanizado em todas as etapas e agendamentos flexíveis de acordo com sua rotina.</p>
            <div class="topic-tags">
              <span class="topic-tag">Suporte</span>
              <span class="topic-tag">Flexibilidade</span>
              <span class="topic-tag">Atendimento VIP</span>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- Agendamento Form -->
    <section id="agendamento" class="agendamento-section">
      <div class="container wizard-max-width">
        <h2 class="section-form-title">Agende sua aula experimental</h2>
        <div class="glass-card form-wizard-card">
          <!-- Progress Bar -->
          <div class="wizard-progress-bar">
            <div class="progress-line-bg"></div>
            <div class="progress-line-fill" :style="{ width: progressWidth }"></div>
            <div v-for="i in 4" :key="i" class="step-indicator-dot" :class="{ 'active': step >= i }">
              {{ i }}
            </div>
          </div>

          <form @submit.prevent="submitForm" class="wizard-form-el">
            <!-- STEP 1: Personal Info -->
            <div v-if="step === 1" class="form-step-pane">
              <h3>1. Dados Pessoais</h3>
              <div class="form-grid-2">
                <div class="input-field">
                  <label>Nome *</label>
                  <input v-model="formData.nome" type="text" placeholder="Nome" required class="theme-input">
                </div>
                <div class="input-field">
                  <label>Sobrenome</label>
                  <input v-model="formData.sobrenome" type="text" placeholder="Sobrenome" class="theme-input">
                </div>
              </div>
              <div class="pane-footer-right">
                <button type="button" @click="nextStep" :disabled="!isStep1Valid" class="btn-theme-primary">
                  Próximo <ArrowRight class="btn-icon-svg" />
                </button>
              </div>
            </div>

            <!-- STEP 2: Contact Info -->
            <div v-if="step === 2" class="form-step-pane">
              <h3>2. Dados de Contato</h3>
              <div class="input-field">
                <label>E-mail *</label>
                <input v-model="formData.email" type="email" placeholder="exemplo@email.com" required class="theme-input">
              </div>
              <div class="input-field">
                <label>Telefone / WhatsApp *</label>
                <input v-model="formData.telefone" type="tel" placeholder="(00) 00000-0000" required class="theme-input">
              </div>
              <div class="pane-footer-split">
                <button type="button" @click="prevStep" class="btn-theme-back">
                  <ArrowLeft class="btn-icon-svg" /> Voltar
                </button>
                <button type="button" @click="nextStep" :disabled="!isStep2Valid" class="btn-theme-primary">
                  Próximo <ArrowRight class="btn-icon-svg" />
                </button>
              </div>
            </div>

            <!-- STEP 3: Contact Preference -->
            <div v-if="step === 3" class="form-step-pane">
              <h3>3. Preferência de Contato</h3>
              <label class="group-label">Como prefere que entremos em contato? *</label>
              <div class="radio-group-list">
                <label class="radio-card-option" :class="{ 'selected': formData.pref_contato === 'whatsapp' }">
                  <input v-model="formData.pref_contato" type="radio" value="whatsapp" name="pref_contato" class="radio-box">
                  <span class="radio-txt">💬 Mensagem no WhatsApp</span>
                </label>
                <label class="radio-card-option" :class="{ 'selected': formData.pref_contato === 'email' }">
                  <input v-model="formData.pref_contato" type="radio" value="email" name="pref_contato" class="radio-box">
                  <span class="radio-txt">E-mail</span>
                </label>
                <label class="radio-card-option" :class="{ 'selected': formData.pref_contato === 'ligacao' }">
                  <input v-model="formData.pref_contato" type="radio" value="ligacao" name="pref_contato" class="radio-box">
                  <span class="radio-txt">📞 Receber Ligação</span>
                </label>
              </div>
              <div class="pane-footer-split">
                <button type="button" @click="prevStep" class="btn-theme-back">
                  <ArrowLeft class="btn-icon-svg" /> Voltar
                </button>
                <button type="button" @click="nextStep" :disabled="!isStep3Valid" class="btn-theme-primary">
                  Próximo <ArrowRight class="btn-icon-svg" />
                </button>
              </div>
            </div>

            <!-- STEP 4: Level & Goals -->
            <div v-if="step === 4" class="form-step-pane">
              <h3>4. Nível e Objetivo</h3>
              <div class="input-field">
                <label>Você já estudou inglês alguma vez? *</label>
                <select v-model="formData.nivel" required class="theme-input">
                  <option value="" disabled>Selecione uma opção</option>
                  <option value="nunca">Não, nunca estudei (quero começar do zero)</option>
                  <option value="antigamente">Estudei há muito tempo e esqueci</option>
                  <option value="basico">Tenho noções básicas/consigo ler um pouco</option>
                  <option value="conversacao">Já consigo falar um pouco mas quero destravar</option>
                </select>
              </div>
              <div class="input-field">
                <label>Qual seu maior sonho ou objetivo com o inglês? *</label>
                <select v-model="formData.objetivo" required class="theme-input">
                  <option value="" disabled>Selecione seu objetivo principal</option>
                  <option value="viagem">Viajar para o exterior com independência</option>
                  <option value="familia">Conversar com familiares ou amigos fora do país</option>
                  <option value="mente">Manter a mente ativa e aprender um novo hobby</option>
                  <option value="experiencia">Viver novas experiências em hotéis/cruzeiros</option>
                </select>
              </div>
              <div class="pane-footer-split">
                <button type="button" @click="prevStep" class="btn-theme-back">
                  <ArrowLeft class="btn-icon-svg" /> Voltar
                </button>
                <button type="submit" :disabled="!isStep4Valid" class="btn-theme-submit">
                  Finalizar <Check class="btn-icon-svg" />
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.modality-detail-view {
  width: 100%;
}

.back-nav {
  position: fixed;
  top: 80px;
  left: 0;
  width: 100%;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  z-index: 99;
  padding: 15px 0;
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
}

.back-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: var(--primary);
  text-decoration: none;
  font-weight: 600;
  transition: transform 0.3s;
}

.back-link:hover {
  transform: translateX(-5px);
}

/* Swiper Styles */
.material-swiper {
  margin-top: 4rem;
  padding-bottom: 3rem !important;
}

/* Wizard custom layout styles to keep original aesthetics and responsive behavior */
.agendamento-section {
  padding: 120px 0;
  background: #f8fafc;
}

.wizard-max-width {
  max-width: 800px;
  margin: 0 auto;
}

.section-form-title {
  font-size: 2.5rem;
  color: var(--primary-dark);
  text-align: center;
  margin-bottom: 3rem;
  font-weight: 800;
}

.form-wizard-card {
  background: white;
  padding: 4rem;
  border-radius: 40px;
  box-shadow: 0 30px 60px rgba(0,0,0,0.06);
  border: 1px solid rgba(0,0,0,0.03);
  text-align: left;
}

.wizard-progress-bar {
  display: flex;
  justify-content: space-between;
  position: relative;
  margin-bottom: 3rem;
  max-width: 500px;
  margin-left: auto;
  margin-right: auto;
}

.progress-line-bg {
  position: absolute;
  top: 50%;
  left: 0;
  width: 100%;
  height: 2px;
  background: #e2e8f0;
  z-index: 1;
  transform: translateY(-50%);
}

.progress-line-fill {
  position: absolute;
  top: 50%;
  left: 0;
  height: 2px;
  background: var(--primary);
  z-index: 2;
  transform: translateY(-50%);
  transition: width 0.4s;
}

.step-indicator-dot {
  width: 35px;
  height: 35px;
  background: #e2e8f0;
  color: var(--gray);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  z-index: 3;
  position: relative;
  transition: all 0.4s;
}

.step-indicator-dot.active {
  background: var(--primary);
  color: white;
}

.form-step-pane h3 {
  color: var(--primary-dark);
  font-size: 1.5rem;
  font-weight: 800;
  margin-bottom: 1.5rem;
}

.form-grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

.input-field {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 1.2rem;
}

.input-field label {
  font-weight: 600;
  color: var(--primary-dark);
  font-size: 0.95rem;
}

.theme-input {
  width: 100%;
  padding: 1.1rem 1.5rem;
  border-radius: 12px;
  border: 1px solid rgba(0, 0, 0, 0.08);
  background: #f8fafc;
  font-size: 1rem;
  outline: none;
  transition: border-color 0.3s;
  box-sizing: border-box;
}

.theme-input:focus {
  border-color: var(--primary);
  background: white;
}

.group-label {
  display: block;
  font-weight: 600;
  color: var(--primary-dark);
  margin-bottom: 1rem;
  font-size: 0.95rem;
}

.radio-group-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.radio-card-option {
  background: #f8fafc;
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-radius: 12px;
  padding: 1rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  cursor: pointer;
  transition: all 0.3s;
}

.radio-card-option:hover {
  background: rgba(0, 71, 255, 0.02);
  border-color: rgba(0, 71, 255, 0.2);
}

.radio-card-option.selected {
  background: rgba(0, 71, 255, 0.05);
  border-color: var(--primary);
}

.radio-box {
  accent-color: var(--primary);
  width: 18px;
  height: 18px;
}

.radio-txt {
  font-weight: 600;
  color: var(--primary-dark);
}

.pane-footer-right {
  display: flex;
  justify-content: flex-end;
  margin-top: 2rem;
}

.pane-footer-split {
  display: flex;
  justify-content: space-between;
  margin-top: 2rem;
}

.btn-theme-primary, .btn-theme-submit, .btn-theme-back {
  padding: 1rem 2rem;
  border-radius: 99px;
  font-weight: 700;
  font-size: 1rem;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: all 0.3s;
  border: none;
}

.btn-theme-primary {
  background: var(--primary);
  color: white;
}

.btn-theme-primary:hover:not(:disabled) {
  background: var(--primary-dark);
}

.btn-theme-primary:disabled {
  background: #cbd5e1;
  color: #94a3b8;
  cursor: not-allowed;
}

.btn-theme-back {
  background: #eee;
  color: var(--gray);
}

.btn-theme-back:hover {
  background: #ddd;
}

.btn-theme-submit {
  background: var(--primary-dark);
  color: white;
}

.btn-theme-submit:hover:not(:disabled) {
  background: black;
}

.btn-icon-svg {
  width: 18px;
  height: 18px;
}

@media (max-width: 768px) {
  .form-wizard-card {
    padding: 2.5rem 1.5rem;
  }
  .form-grid-2 {
    grid-template-columns: 1fr;
  }
}
</style>
<!-- HMR trigger comment to force Vite rebuild -->

<script setup>
import { ref, computed, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { ArrowLeft, ArrowRight, Check, PenTool, Mic2, Users } from '@lucide/vue'

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
  const emailRegex = /^[^s@]+@[^s@]+.[^s@]+$/
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
    alert('Solicitação enviada com sucesso!')
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
        <section style="position: relative; padding: 220px 0 150px 0; min-height: 90vh; display: flex; align-items: center; overflow: hidden; background: #001233;">
            <img src="/assets/img/capa/ENG RESEARCHERS.webp" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; z-index: 0; opacity: 0.5;">
            <div style="position: absolute; inset: 0; background: linear-gradient(to right, var(--primary-dark), transparent); z-index: 1;"></div>
            <div class="container" style="position: relative; z-index: 2;">
                <div class="reveal active" style="max-width: 850px; text-align: left;">
                    <span style="color: var(--accent); font-weight: 800; letter-spacing: 0.3em; text-transform: uppercase; margin-bottom: 1.5rem; display: block;">Academic Excellence</span>
                    <h1 style="font-size: 5rem; color: white; margin-bottom: 2rem; line-height: 1.1; font-weight: 800;">English for <span style="color: var(--accent);">Researchers</span></h1>
                    <p style="font-size: 1.4rem; color: rgba(255,255,255,0.9); margin-bottom: 3.5rem; line-height: 1.6; font-weight: 300;">
                        Desenvolva suas habilidades em <strong>inglês acadêmico e científico</strong>. Voltado a pós-graduandos, pesquisadores e profissionais, integrando <strong>Final Draft</strong> com Roadmap e Connectivity.
                    </p>
                    <div style="display: flex; gap: 2rem; align-items: center;">
                        <a href="#agendamento" class="btn-vip">Agendar Aula Grátis <ArrowRight  class="info-icon" /></a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Como Funciona -->
        <section style="background: #f8faff; padding: 120px 0;">
            <div class="container">
                <div class="reveal" style="margin-bottom: 6rem; text-align: left;">
                    <span style="color: var(--primary); font-weight: 800; letter-spacing: 0.2em; text-transform: uppercase;">Metodologia</span>
                    <h2 style="margin-top: 1rem; font-size: 3.5rem; color: var(--primary-dark);">Uma jornada de aperfeiçoamento</h2>
                    <p style="max-width: 900px; margin: 2rem 0; color: var(--gray); font-size: 1.25rem; line-height: 1.8;">
                        Curso desenvolvido para quem deseja elevar sua comunicação acadêmica para o próximo nível. Combinamos aulas estruturadas com foco em <strong>writing científico, academic presentations e leitura crítica</strong> de artigos.
                    </p>
                </div>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem;">
                    <div class="feature-card reveal">
                        <PenTool style="color: var(--primary); width: 40px; height: 40px; margin-bottom: 1.5rem;" class="info-icon" />
                        <h3 style="color: var(--primary-dark); font-size: 1.6rem; margin-bottom: 1rem;">Escrita Estruturada</h3>
                        <p style="color: var(--gray); line-height: 1.6;">Desenvolva textos científicos claros e coesos, praticando abstracts, research papers e proposals com feedback especializado.</p>
                    </div>
                    <div class="feature-card reveal">
                        <Mic2 style="color: var(--accent); width: 40px; height: 40px; margin-bottom: 1.5rem;" class="info-icon" />
                        <h3 style="color: var(--primary-dark); font-size: 1.6rem; margin-bottom: 1rem;">Comunicação Científica</h3>
                        <p style="color: var(--gray); line-height: 1.6;">Pratique apresentações, discussões de resultados e respostas a revisores com simulações reais do ambiente acadêmico.</p>
                    </div>
                    <div class="feature-card reveal">
                        <Users style="color: var(--primary); width: 40px; height: 40px; margin-bottom: 1.5rem;" class="info-icon" />
                        <h3 style="color: var(--primary-dark); font-size: 1.6rem; margin-bottom: 1rem;">Mentoria Individual</h3>
                        <p style="color: var(--gray); line-height: 1.6;">Acompanhamento personalizado para revisar artigos, cartas de motivação e textos acadêmicos em desenvolvimento.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Material Didático -->
        <section id="materiais" style="padding: 120px 0;">
            <div class="container">
                <div class="reveal" style="margin-bottom: 6rem; text-align: left;">
                    <span style="color: var(--primary); font-weight: 800; letter-spacing: 0.2em; text-transform: uppercase;">Materiais e Metodologia</span>
                    <h2 style="margin-top: 1rem; font-size: 3.5rem; color: var(--primary-dark);">Final Draft (Cambridge)</h2>
                    <p style="max-width: 900px; margin: 2rem 0; color: var(--gray); font-size: 1.2rem; line-height: 1.8;">
                        O curso combina <strong>Final Draft (Cambridge University Press)</strong> — referência em escrita acadêmica — com <strong>Roadmap ou Connectivity (Pearson)</strong>, consolidando estrutura e fluência.
                    </p>
                </div>
                <div class="reveal">
                    <div class="material-grid">
                        <div class="material-item reveal">
                            <img src="https://changeskills.com.br/wp-content/uploads/2025/11/81R-k2GjnXL._AC_UF10001000_QL80_.jpg" alt="Final Draft 1">
                            <h4>Final Draft 1</h4>
                        </div>
                        <div class="material-item reveal">
                            <img src="https://changeskills.com.br/wp-content/uploads/2025/11/41ZkJYAFWL._AC_UF10001000_QL80_.jpg" alt="Final Draft 2">
                            <h4>Final Draft 2</h4>
                        </div>
                        <div class="material-item reveal">
                            <img src="https://changeskills.com.br/wp-content/uploads/2025/11/61k9VgA3EeL._AC_UF10001000_QL80_.jpg" alt="Final Draft 3">
                            <h4>Final Draft 3</h4>
                        </div>
                        <div class="material-item reveal">
                            <img src="https://changeskills.com.br/wp-content/uploads/2025/11/41Mzvo7Uw1L._AC_UF10001000_QL80_.jpg" alt="Final Draft 4">
                            <h4>Final Draft 4</h4>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Temas Trabalhados -->
        <section style="padding: 120px 0; background: #001233; color: white;">
            <div class="container">
                <div style="text-align: center; margin-bottom: 60px;" class="reveal">
                    <h2 style="font-size: 3rem; color: var(--accent);">Temas e Competências</h2>
                    <p style="opacity: 0.8; font-size: 1.2rem; margin-top: 1rem;">Desenvolvimento focado na sua produção e performance acadêmica</p>
                </div>
                <div class="grid-competencias">
                    <div class="glass-card reveal" style="padding: 3rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
                        <h3 style="color: var(--accent); font-size: 1.8rem; margin-bottom: 1rem;">Academic Reading</h3>
                        <p style="opacity: 0.8; line-height: 1.7;">Leitura crítica de artigos, identificação de estrutura e vocabulário técnico de áreas científicas diversas.</p>
                    </div>
                    <div class="glass-card reveal" style="padding: 3rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
                        <h3 style="color: var(--accent); font-size: 1.8rem; margin-bottom: 1rem;">Scientific Writing</h3>
                        <p style="opacity: 0.8; line-height: 1.7;">Estrutura de abstracts, papers, resumos, e-mails acadêmicos e cartas de motivação com revisão detalhada.</p>
                    </div>
                    <div class="glass-card reveal" style="padding: 3rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
                        <h3 style="color: var(--accent); font-size: 1.8rem; margin-bottom: 1rem;">Presentations</h3>
                        <p style="opacity: 0.8; line-height: 1.7;">Treino de apresentações orais, defesa de resultados e argumentação em congressos e seminários internacionais.</p>
                    </div>
                    <div class="glass-card reveal" style="padding: 3rem; background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
                        <h3 style="color: var(--accent); font-size: 1.8rem; margin-bottom: 1rem;">Collaboration</h3>
                        <p style="opacity: 0.8; line-height: 1.7;">Comunicação com revisores, coautores e networking acadêmico, incluindo peer-review responses.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Estrutura dos Níveis -->
        <section style="background: white; padding: 100px 0;">
            <div class="container">
                <div class="reveal" style="text-align: left; margin-bottom: 5rem;">
                    <span style="color: var(--primary); font-weight: 800; letter-spacing: 0.2em; text-transform: uppercase;">Programa</span>
                    <h2 style="margin-top: 1rem; font-size: 3rem; color: var(--primary-dark);">Estrutura do Programa</h2>
                </div>
                <div style="display: grid; gap: 2rem;">

                    <div class="level-card reveal">
                        <div class="level-number">Nível 1</div>
                        <div class="level-title">Redação Acadêmica</div>
                        <p style="color: var(--gray); line-height: 1.7; margin-bottom: 1rem;">Fundamentos da escrita científica, estruturação de artigos científicos, redação de abstracts elegantes e coesão textual em inglês acadêmico.</p>
                        <div class="topic-tags">
                            <span class="topic-tag">Abstracts</span>
                            <span class="topic-tag">Introdução</span>
                            <span class="topic-tag">Coesão Textual</span>
                            <span class="topic-tag">Vocabulário Acadêmico</span>
                        </div>
                    </div>

                    <div class="level-card reveal">
                        <div class="level-number">Nível 2</div>
                        <div class="level-title">Apresentações e Pitches</div>
                        <p style="color: var(--gray); line-height: 1.7; margin-bottom: 1rem;">Técnicas de apresentação oral em eventos internacionais, design de slides profissionais de alto impacto e preparação para rodadas de perguntas e respostas (Q&A).</p>
                        <div class="topic-tags">
                            <span class="topic-tag">Slides</span>
                            <span class="topic-tag">Fluência</span>
                            <span class="topic-tag">Congressos</span>
                            <span class="topic-tag">Q&A Sessions</span>
                            <span class="topic-tag">Comunicação Oral</span>
                        </div>
                    </div>

                    <div class="level-card reveal">
                        <div class="level-number">Nível 3</div>
                        <div class="level-title">Leitura e Revisão Crítica</div>
                        <p style="color: var(--gray); line-height: 1.7; margin-bottom: 1rem;">Desenvolvimento de pensamento analítico através do peer review, leitura crítica de literatura científica complexa e debates intelectuais avançados.</p>
                        <div class="topic-tags">
                            <span class="topic-tag">Peer Review</span>
                            <span class="topic-tag">Literatura Científica</span>
                            <span class="topic-tag">Discussões Avançadas</span>
                            <span class="topic-tag">Análise Crítica</span>
                        </div>
                    </div>

                </div>
            </div>
        </section>

        
                <!-- Agendamento Form -->
        
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
                <label>Nível atual no idioma? *</label>
                <select v-model="formData.nivel" required class="theme-input">
                  <option value="" disabled>Selecione seu nível</option>
                  <option value="nunca">Nunca estudei o idioma</option>
                  <option value="iniciante">Iniciante / Básico</option>
                  <option value="intermediario">Intermediário</option>
                  <option value="avancado">Avançado</option>
                </select>
              </div>
              <div class="input-field">
                <label>Qual seu principal objetivo? *</label>
                <select v-model="formData.objetivo" required class="theme-input">
                  <option value="" disabled>Selecione seu objetivo</option>
                  <option value="carreira">Desenvolvimento Profissional / Carreira</option>
                  <option value="viagem">Viagens ou Intercâmbio</option>
                  <option value="academico">Estudos / Fins Acadêmicos</option>
                  <option value="pessoal">Crescimento Pessoal / Hobbies</option>
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

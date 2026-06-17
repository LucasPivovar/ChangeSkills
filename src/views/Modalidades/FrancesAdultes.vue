<script setup>
import { ref, computed, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { ArrowLeft, ArrowRight, Check, MessageCircle, Award, Sliders } from '@lucide/vue'

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
        <RouterLink to="/cursos/frances" class="back-link">
          <ArrowLeft class="btn-icon-svg" /> Voltar para os Cursos
        </RouterLink>
      </div>
    </div>

    <!-- Hero Section -->
        <section class="hero-section">
            <div class="container hero-grid reveal active">
                <div style="text-align: left;">
                    <span style="color: var(--primary); font-weight: 800; letter-spacing: 0.2em; display: inline-block; margin-bottom: 1.5rem; text-transform: uppercase;">🇫🇷 Français pour Adultes</span>
                    <h1 style="font-size: 4.2rem; margin-bottom: 2rem; line-height: 1.1; color: var(--primary-dark);">Francês para <span style="color: var(--primary);">Adultos</span></h1>
                    <p style="font-size: 1.25rem; color: var(--primary-dark); font-weight: 600; margin-bottom: 1.5rem;">
                        Viagens, Carreira, Cultura e Experiências Internacionais
                    </p>
                    <p style="font-size: 1.1rem; color: var(--gray); margin-bottom: 3rem; line-height: 1.8; max-width: 600px;">
                        Ideal para quem deseja aprender francês para viagens, crescimento profissional, estudos, imigração ou interesse cultural. Utilizamos o <strong>Cosmopolite</strong> (Hachette), uma das linhas mais modernas e reconhecidas no ensino de francês para estrangeiros, com 5 níveis do A1 ao C1/C2.
                    </p>
                    <a href="#agendamento" class="btn-vip" style="text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem; padding: 1.1rem 3rem; font-size: 1.2rem;">
                        Agende uma aula experimental <ArrowRight style="width: 22px;" class="info-icon" />
                    </a>
                </div>
                <div class="hero-image-container">
                    <img src="/assets/img/capa/FRA ADULT.webp" alt="Material Cosmopolite Francês para Adultos">
                </div>
            </div>
        </section>

        <!-- Como Funciona -->
        <section style="background: #f8faff; padding: 100px 0;">
            <div class="container">
                <div class="reveal" style="margin-bottom: 5rem; text-align: left;">
                    <span style="color: var(--primary); font-weight: 800; letter-spacing: 0.2em; text-transform: uppercase;">Metodologia</span>
                    <h2 style="margin-top: 1rem; font-size: 3rem; color: var(--primary-dark);">Como funciona o curso</h2>
                    <p style="max-width: 800px; margin: 2rem 0; color: var(--gray); font-size: 1.15rem; line-height: 1.8;">
                        As aulas focam na comunicação real, no desenvolvimento da confiança ao falar e na imersão em diferentes contextos do mundo francófono. Aliada à metodologia personalizada da Change Skills, proporcionam um aprendizado leve, moderno e eficiente.
                    </p>
                </div>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem;">
                    <div class="feature-card reveal">
                        <MessageCircle style="color: var(--primary); width: 40px; height: 40px; margin-bottom: 1.5rem;" class="info-icon" />
                        <h3 style="color: var(--primary-dark); font-size: 1.3rem; margin-bottom: 1rem;">Comunicação Real</h3>
                        <p style="color: var(--gray); line-height: 1.6;">Foco em situações do cotidiano real — restaurantes, trabalho, viagens, negócios e relacionamentos.</p>
                    </div>
                    <div class="feature-card reveal">
                        <Award style="color: var(--accent); width: 40px; height: 40px; margin-bottom: 1.5rem;" class="info-icon" />
                        <h3 style="color: var(--primary-dark); font-size: 1.3rem; margin-bottom: 1rem;">Conteúdo Atual</h3>
                        <p style="color: var(--gray); line-height: 1.6;">Material Cosmopolite com desenvolvimento integrado das 4 habilidades linguísticas e imersão cultural francófona.</p>
                    </div>
                    <div class="feature-card reveal">
                        <Sliders style="color: var(--primary); width: 40px; height: 40px; margin-bottom: 1.5rem;" class="info-icon" />
                        <h3 style="color: var(--primary-dark); font-size: 1.3rem; margin-bottom: 1rem;">Personalizado</h3>
                        <p style="color: var(--gray); line-height: 1.6;">Aulas adaptadas ao seu ritmo, objetivos e nível — seja para viagens, carreira, estudos ou imigração.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Material Cosmopolite -->
        <section style="padding: 100px 0; background: white;" id="material">
            <div class="container reveal">
                <div style="text-align: left; margin-bottom: 5rem;">
                    <span style="color: var(--primary); font-weight: 800; letter-spacing: 0.2em; text-transform: uppercase;">Material Didático</span>
                    <h2 style="margin-top: 1rem; font-size: 3rem; color: var(--primary-dark);">Cosmopolite (Hachette)</h2>
                    <p style="max-width: 900px; margin: 2rem 0; color: var(--gray); font-size: 1.15rem; line-height: 1.8;">
                        O <strong>Cosmopolite</strong> oferece forte foco em comunicação real, conteúdo atual e contextualizado, desenvolvimento integrado das habilidades e aprendizado dinâmico e interativo. 5 volumes do A1 ao C1/C2 para uma jornada completa no francês.
                    </p>
                </div>
                <div class="material-grid-5">
                    <div class="material-item reveal">
                        <img src="/assets/img/Livros - Frances/Livros/WhatsApp Image 2026-05-19 at 17.55.09 (2).jpeg" alt="Cosmopolite 1">
                        <span class="nivel-badge">Nível 1 — A1</span>
                        <h4>Cosmopolite 1</h4>
                        <p>Français Essentiel. Comunicação básica e situações cotidianas.</p>
                    </div>
                    <div class="material-item reveal">
                        <img src="/assets/img/Livros - Frances/Livros/WhatsApp Image 2026-05-19 at 17.55.09 (3).jpeg" alt="Cosmopolite 2">
                        <span class="nivel-badge">Nível 2 — A2</span>
                        <h4>Cosmopolite 2</h4>
                        <p>Communication Quotidienne. Conversação fluida e comunicação social.</p>
                    </div>
                    <div class="material-item reveal">
                        <img src="/assets/img/Livros - Frances/Livros/WhatsApp Image 2026-05-19 at 17.55.09 (4).jpeg" alt="Cosmopolite 3">
                        <span class="nivel-badge">Nível 3 — B1</span>
                        <h4>Cosmopolite 3</h4>
                        <p>Expansion de la Fluidité. Opiniões, diálogos complexos e escuta apurada.</p>
                    </div>
                    <div class="material-item reveal">
                        <img src="/assets/img/Livros - Frances/Livros/WhatsApp Image 2026-05-19 at 17.55.09 (5).jpeg" alt="Cosmopolite 4">
                        <span class="nivel-badge">Nível 4 — B2</span>
                        <h4>Cosmopolite 4</h4>
                        <p>Communication Avancée. Argumentação, debates e contextos profissionais.</p>
                    </div>
                    <div class="material-item reveal">
                        <img src="/assets/img/Livros - Frances/Livros/WhatsApp Image 2026-05-19 at 17.55.08.jpeg" alt="Cosmopolite 5">
                        <span class="nivel-badge">Nível 5 — C1/C2</span>
                        <h4>Cosmopolite 5</h4>
                        <p>Français pour le Monde. Alta autonomia e fluência avançada.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Estrutura dos 5 Níveis -->
        <section style="background: #f8faff; padding: 100px 0;">
            <div class="container">
                <div class="reveal" style="text-align: left; margin-bottom: 5rem;">
                    <span style="color: var(--primary); font-weight: 800; letter-spacing: 0.2em; text-transform: uppercase;">Programa Completo</span>
                    <h2 style="margin-top: 1rem; font-size: 3rem; color: var(--primary-dark);">5 Níveis — Do A1 ao C1/C2</h2>
                </div>
                <div style="display: grid; gap: 2rem;">

                    <div class="level-card reveal">
                        <div class="level-left">
                            <div class="level-number">Nível 1</div>
                            <span class="level-cefr">A1</span>
                            <div class="level-title">Français Essentiel</div>
                            <p class="level-book">📚 Cosmopolite 1</p>
                        </div>
                        <div>
                            <p style="color: var(--gray); line-height: 1.7; margin-bottom: 1rem;">Os alunos aprendem comunicação básica, situações cotidianas, apresentações e interações simples e vocabulário inicial.</p>
                            <div class="topic-tags">
                                <span class="topic-tag">Restaurantes</span>
                                <span class="topic-tag">Transporte</span>
                                <span class="topic-tag">Viagens</span>
                                <span class="topic-tag">Compras</span>
                                <span class="topic-tag">Conversas Sociais</span>
                            </div>
                        </div>
                    </div>

                    <div class="level-card alt reveal">
                        <div class="level-left">
                            <div class="level-number" style="color: var(--accent);">Nível 2</div>
                            <span class="level-cefr">A2</span>
                            <div class="level-title">Communication Quotidienne</div>
                            <p class="level-book">📚 Cosmopolite 2</p>
                        </div>
                        <div>
                            <p style="color: var(--gray); line-height: 1.7; margin-bottom: 1rem;">Os estudantes desenvolvem maior compreensão oral, conversação mais fluida, comunicação social e construção de frases naturais.</p>
                            <div class="topic-tags">
                                <span class="topic-tag">Trabalho e Estudos</span>
                                <span class="topic-tag">Rotina</span>
                                <span class="topic-tag">Cultura e Lazer</span>
                                <span class="topic-tag">Planejamento</span>
                                <span class="topic-tag">Interações Sociais</span>
                            </div>
                        </div>
                    </div>

                    <div class="level-card reveal">
                        <div class="level-left">
                            <div class="level-number">Nível 3</div>
                            <span class="level-cefr">B1</span>
                            <div class="level-title">Expansion de la Fluidité</div>
                            <p class="level-book">📚 Cosmopolite 3</p>
                        </div>
                        <div>
                            <p style="color: var(--gray); line-height: 1.7; margin-bottom: 1rem;">Os alunos passam a expressar opiniões, participar de diálogos mais complexos, melhorar escuta e interpretação e utilizar estruturas mais elaboradas.</p>
                            <div class="topic-tags">
                                <span class="topic-tag">Atualidades</span>
                                <span class="topic-tag">Cultura Francófona</span>
                                <span class="topic-tag">Viagens Internacionais</span>
                                <span class="topic-tag">Situações Reais</span>
                                <span class="topic-tag">Objetivos Profissionais</span>
                            </div>
                        </div>
                    </div>

                    <div class="level-card alt reveal">
                        <div class="level-left">
                            <div class="level-number" style="color: var(--accent);">Nível 4</div>
                            <span class="level-cefr">B2</span>
                            <div class="level-title">Communication Avancée</div>
                            <p class="level-book">📚 Cosmopolite 4</p>
                        </div>
                        <div>
                            <p style="color: var(--gray); line-height: 1.7; margin-bottom: 1rem;">Os estudantes refinam pronúncia, argumentação, naturalidade na comunicação e compreensão de diferentes sotaques do mundo francófono.</p>
                            <div class="topic-tags">
                                <span class="topic-tag">Ambiente Profissional</span>
                                <span class="topic-tag">Cultura e Sociedade</span>
                                <span class="topic-tag">Comunicação Formal</span>
                                <span class="topic-tag">Debates e Apresentações</span>
                                <span class="topic-tag">Contextos Internacionais</span>
                            </div>
                        </div>
                    </div>

                    <div class="level-card reveal">
                        <div class="level-left">
                            <div class="level-number">Nível 5</div>
                            <span class="level-cefr">C1/C2</span>
                            <div class="level-title">Français pour le Monde</div>
                            <p class="level-book">📚 Cosmopolite 5</p>
                        </div>
                        <div>
                            <p style="color: var(--gray); line-height: 1.7; margin-bottom: 1rem;">Os alunos desenvolvem alta autonomia no idioma, fluência avançada, comunicação sofisticada e segurança total em ambientes internacionais.</p>
                            <div class="topic-tags">
                                <span class="topic-tag">Negócios e Networking</span>
                                <span class="topic-tag">Estudos e Imigração</span>
                                <span class="topic-tag">Cultura e Atualidades</span>
                                <span class="topic-tag">Comunicação Acadêmica</span>
                                <span class="topic-tag">Conversação Avançada</span>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </section>

        <!-- Para quem é este curso -->
        <section style="padding: 100px 0; background: white;">
            <div class="container">
                <div class="reveal" style="text-align: center; margin-bottom: 5rem;">
                    <span style="color: var(--primary); font-weight: 800; letter-spacing: 0.2em; text-transform: uppercase;">Público-Alvo</span>
                    <h2 style="margin-top: 1rem; font-size: 3rem; color: var(--primary-dark);">Para quem é este curso?</h2>
                </div>
                <div class="target-grid reveal">
                    <div class="target-item">
                        <span class="target-icon">✈️</span>
                        <h3 style="color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 1.15rem;">Viajantes</h3>
                        <p style="color: var(--gray); font-size: 0.9rem; line-height: 1.6;">Adultos que desejam se comunicar com confiança na França, Bélgica, Canadá e outros países francófonos.</p>
                    </div>
                    <div class="target-item">
                        <span class="target-icon">💼</span>
                        <h3 style="color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 1.15rem;">Profissionais</h3>
                        <p style="color: var(--gray); font-size: 0.9rem; line-height: 1.6;">Profissionais e universitários que precisam do francês para crescimento de carreira e oportunidades internacionais.</p>
                    </div>
                    <div class="target-item">
                        <span class="target-icon">🎓</span>
                        <h3 style="color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 1.15rem;">Estudantes</h3>
                        <p style="color: var(--gray); font-size: 0.9rem; line-height: 1.6;">Quem deseja estudar em universidades francófonas ou obter certificações internacionais como DELF/DALF.</p>
                    </div>
                    <div class="target-item">
                        <span class="target-icon">🌍</span>
                        <h3 style="color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 1.15rem;">Cultura Francófona</h3>
                        <p style="color: var(--gray); font-size: 0.9rem; line-height: 1.6;">Pessoas interessadas em se imergir na riqueza cultural da França, literatura, cinema e gastronomia.</p>
                    </div>
                    <div class="target-item">
                        <span class="target-icon">🏠</span>
                        <h3 style="color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 1.15rem;">Imigração</h3>
                        <p style="color: var(--gray); font-size: 0.9rem; line-height: 1.6;">Adultos que planejam se mudar para países francófonos e precisam de fluência no idioma para se integrar.</p>
                    </div>
                    <div class="target-item">
                        <span class="target-icon">💬</span>
                        <h3 style="color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 1.15rem;">Aprendizado Comunicativo</h3>
                        <p style="color: var(--gray); font-size: 0.9rem; line-height: 1.6;">Quem busca aprender de forma prática, personalizada e conectada à vida real — no seu ritmo.</p>
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

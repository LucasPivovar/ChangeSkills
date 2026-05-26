<script setup>
import { ref, computed, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { ArrowLeft, ArrowRight, Check, Compass, MessagesSquare, Award, Clock } from '@lucide/vue'

onMounted(() => {
  // Load Swiper CSS dynamically
  if (!document.getElementById('swiper-css')) {
    const link = document.createElement('link')
    link.id = 'swiper-css'
    link.rel = 'stylesheet'
    link.href = 'https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css'
    document.head.appendChild(link)
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

// Wizard Form Reactive State
const step = ref(1)
const formData = ref({
  nome: '',
  sobrenome: '',
  email: '',
  telefone: '',
  pref_contato: 'whatsapp',
  experiencia: '',
  objetivo: ''
})

const isStep1Valid = computed(() => formData.value.nome.trim() !== '')
const isStep2Valid = computed(() => {
  const emailRegex = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/
  return emailRegex.test(formData.value.email) && formData.value.telefone.trim() !== ''
})
const isStep3Valid = computed(() => !!formData.value.pref_contato)
const isStep4Valid = computed(() => formData.value.experiencia !== '' && formData.value.objetivo !== '')

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
      experiencia: '',
      objetivo: ''
    }
    step.value = 1
  }
}
</script>

<template>
  <div class="modality-detail-view">
    <!-- Back to Cursos Link -->
    <div class="back-nav">
      <div class="container">
        <RouterLink to="/cursos/ingles" class="back-link">
          <ArrowLeft class="btn-icon-svg" /> Voltar para Cursos de Inglês
        </RouterLink>
      </div>
    </div>

    <!-- Hero Section -->
    <section class="modality-hero">
      <img src="/assets/img/ingles-50-hero.png" alt="Curso de Inglês 50+" class="hero-bg-img">
      <div class="hero-overlay"></div>
      <div class="container hero-content">
        <div class="reveal active hero-text-wrapper">
          <span class="hero-category-tag">Inglês Sênior</span>
          <h1 class="hero-title-h1">Curso de Inglês <span class="highlight-text">50+</span></h1>
          <p class="hero-desc-p">
            Aprenda Inglês para Viver Experiências, Viajar e se Comunicar com Confiança. Nunca é tarde para expandir seus horizontes e conquistar sua independência no exterior.
          </p>
          <div class="hero-cta-btn">
            <a href="#agendamento" class="btn-vip">Solicitar Aula Experimental <ArrowRight class="btn-icon-svg" /></a>
          </div>
        </div>
      </div>
    </section>

    <!-- Apresentação & Como Funciona -->
    <section class="section-presentation">
      <div class="container">
        <div class="grid-2-col">
          <div class="reveal left-info">
            <span class="section-tag-small">Nova Perspectiva</span>
            <h2 class="section-title-h2">Aprenda de forma leve e prática</h2>
            <p class="section-desc-p">
              Na <strong>Change Skills Idiomas</strong> acreditamos que nunca é tarde para aprender inglês, principalmente quando o objetivo é viver novas experiências, viajar pelo mundo e se comunicar com segurança no dia-a-dia.
            </p>
            <p class="section-desc-p">
              Nosso curso 50+ foi desenvolvido especialmente para adultos que desejam aprender inglês de forma leve, prática e personalizada, <strong>sem pressão e sem foco excessivo em gramática tradicional</strong>. Aqui, o aprendizado acontece por meio de situações reais da vida cotidiana, respeitando o ritmo, os interesses e os objetivos de cada aluno.
            </p>
          </div>
          
          <div class="reveal right-checklist">
            <div class="checklist-card">
              <h3 class="checklist-title">Como Funciona o Curso</h3>
              <ul class="checklist-ul">
                <li><span class="check-icon">✔</span> Aulas totalmente personalizadas</li>
                <li><span class="check-icon">✔</span> Foco em conversação e compreensão</li>
                <li><span class="check-icon">✔</span> Situações reais de viagem e cotidiano</li>
                <li><span class="check-icon">✔</span> Sem necessidade de seguir livro didático tradicional</li>
                <li><span class="check-icon">✔</span> Aulas online ao vivo e dinâmicas</li>
                <li><span class="check-icon">✔</span> Aprendizado no seu ritmo</li>
                <li><span class="check-icon">✔</span> Professores pacientes e preparados para o público adulto</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- O Que Você Vai Aprender (3 Cards utilizando Assets Oficiais) -->
    <section class="section-learning bg-light-gray">
      <div class="container">
        <div class="text-center reveal header-margin">
          <span class="section-tag-small">Jornada Prática</span>
          <h2 class="section-title-h2">O que você vai aprender com a gente</h2>
          <p class="section-subtitle-p">Foco total em situações úteis e reais da vida real</p>
        </div>

        <div class="learning-grid">
          <!-- Card 1: Viagens -->
          <div class="learning-card reveal">
            <div class="learning-card-img-wrapper">
              <img src="/assets/img/ingles-50-viagem.png" alt="Inglês para Viagens" class="learning-card-img">
              <div class="learning-card-overlay"></div>
              <span class="learning-card-tag">✈️ Viagens</span>
            </div>
            <div class="learning-card-content">
              <h3>Inglês para Viagens</h3>
              <p>Aprenda a se comunicar com segurança em todas as etapas de suas viagens internacionais:</p>
              <ul class="learning-sub-ul">
                <li>Vocabulário essencial de viagem</li>
                <li>Passagem por aeroporto e imigração</li>
                <li>Check-in em hotéis e resorts</li>
                <li>Pedidos em restaurantes e cafés</li>
                <li>Compras, lojas e negociações</li>
                <li>Uso de transportes (Uber, táxi, metrô, etc.)</li>
                <li>Pedir direções e ajuda em emergências</li>
              </ul>
            </div>
          </div>

          <!-- Card 2: Conversação -->
          <div class="learning-card reveal">
            <div class="learning-card-img-wrapper">
              <img src="/assets/img/ingles-50-viver.png" alt="Conversação" class="learning-card-img">
              <div class="learning-card-overlay"></div>
              <span class="learning-card-tag">🗣 Conversação</span>
            </div>
            <div class="learning-card-content">
              <h3>Conversação do Dia-a-Dia</h3>
              <p>Desenvolva a habilidade de conversar naturalmente em inglês e criar conexões reais:</p>
              <ul class="learning-sub-ul">
                <li>Apresentações pessoais e socialização</li>
                <li>Falar sobre família, rotina e planos</li>
                <li>Como fazer novas amizades e contatos</li>
                <li>Hobbies, preferências e interesses</li>
                <li>Cultura, entretenimento e lazer</li>
                <li>Pequenas conversas cotidianas ("small talk")</li>
                <li>Expressões comuns e pronúncia natural</li>
              </ul>
            </div>
          </div>

          <!-- Card 3: Experiências -->
          <div class="learning-card reveal">
            <div class="learning-card-img-wrapper">
              <img src="/assets/img/ingles-50-mundo.png" alt="Experiências" class="learning-card-img">
              <div class="learning-card-overlay"></div>
              <span class="learning-card-tag">🌎 Experiências</span>
            </div>
            <div class="learning-card-content">
              <h3>Experiências Internacionais</h3>
              <p>Ideal para quem deseja aproveitar ao máximo momentos únicos no exterior com independência:</p>
              <ul class="learning-sub-ul">
                <li>Vivência em resorts, spas e cruzeiros</li>
                <li>Passeios em museus e pontos turísticos</li>
                <li>Participação em eventos internacionais</li>
                <li>Reservas em restaurantes sofisticados</li>
                <li>Comunicação com atendimento ao cliente</li>
                <li>Contorno de situações inesperadas</li>
                <li>Autonomia e liberdade para explorar</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Escuta e Metodologia -->
    <section class="section-methodology">
      <div class="container">
        <div class="grid-2-col">
          <div class="reveal flex-center">
            <div class="methodology-visual-card">
              <Compass class="methodology-icon" />
              <h3>Desenvolvimento da Escuta e Confiança</h3>
              <p>Trabalhamos constantemente na melhora da compreensão auditiva, pronúncia natural e, principalmente, na sua segurança ao falar, reduzindo qualquer ansiedade.</p>
              <p class="small-info">Utilizamos vídeos dinâmicos, diálogos cotidianos simulados, músicas clássicas, situações de simulação real e materiais personalizados para o ritmo de cada aluno.</p>
            </div>
          </div>

          <div class="reveal flex-column-start">
            <span class="section-tag-small">Sem Pressão</span>
            <h2 class="section-title-h2">Metodologia Change Skills 50+</h2>
            <p class="section-desc-p">Nossa metodologia é baseada em pilares acolhedores:</p>
            
            <div class="pilar-item">
              <h4>💬 Comunicação Prática</h4>
              <p>O foco é a utilidade prática do vocabulário, e não a memorização de regras teóricas cansativas.</p>
            </div>
            
            <div class="pilar-item">
              <h4>🔄 Repetição Contextualizada</h4>
              <p>Você aprende estruturas gramaticais de forma orgânica e intuitiva, participando de diálogos guiados.</p>
            </div>

            <div class="pilar-item">
              <h4>❤️ Acolhimento e Paciência</h4>
              <p>Um ambiente leve, onde errar faz parte do progresso. As aulas são moldadas exclusivamente aos seus interesses.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Para Quem e Diferenciais -->
    <section class="section-target bg-dark-blue text-white">
      <div class="container">
        <div class="grid-2-col">
          <div class="reveal">
            <h2 class="section-title-h2 text-white">Para quem é este curso?</h2>
            <ul class="target-ul">
              <li>✨ Pessoas que querem viajar com mais independência</li>
              <li>✨ Quem sempre sonhou em aprender inglês mas não se adaptou a escolas tradicionais</li>
              <li>✨ Adultos que buscam aprender sem pressão de notas ou provas</li>
              <li>✨ Estudantes que procuram aulas mais leves, humanas e dinâmicas</li>
              <li>✨ Quem deseja conversar em inglês e se manter ativo cognitivamente</li>
              <li>✨ Pessoas que preferem aulas personalizadas adaptadas ao seu próprio ritmo</li>
            </ul>
          </div>

          <div class="reveal">
            <h2 class="section-title-h2 text-white">Nossos Diferenciais</h2>
            <div class="diferenciais-grid">
              <div class="diferencial-card-glass">
                <Award class="dif-icon" />
                <h4>Atendimento VIP</h4>
                <p>Acompanhamento próximo e suporte humanizado em todas as etapas.</p>
              </div>
              <div class="diferencial-card-glass">
                <Clock class="dif-icon" />
                <h4>Flexibilidade Total</h4>
                <p>Agendamentos flexíveis de acordo com sua rotina de vida e viagens.</p>
              </div>
              <div class="diferencial-card-glass">
                <MessagesSquare class="dif-icon" />
                <h4>Professores Especializados</h4>
                <p>Docentes extremamente pacientes e treinados especificamente para o público maduro.</p>
              </div>
            </div>
          </div>
        </div>

        <div class="reveal tagline-footer-box">
          <p class="tagline-bold">Viva novas experiências com mais liberdade e confiança.</p>
          <p class="tagline-sub">Inglês para a vida real. No seu ritmo. Do seu jeito.</p>
        </div>
      </div>
    </section>

    <!-- Wizard Form Experimental -->
    <section id="agendamento" class="agendamento-section">
      <div class="container wizard-max-width">
        <h2 class="section-form-title">Solicite sua Aula Experimental Grátis</h2>
        <p class="section-form-subtitle">Preencha as informações abaixo e nossa equipe entrará em contato de forma carinhosa.</p>
        
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
              <h3>1. Como podemos chamar você?</h3>
              <div class="form-grid-2">
                <div class="input-field">
                  <label>Nome *</label>
                  <input v-model="formData.nome" type="text" placeholder="Seu nome" required class="theme-input">
                </div>
                <div class="input-field">
                  <label>Sobrenome</label>
                  <input v-model="formData.sobrenome" type="text" placeholder="Seu sobrenome" class="theme-input">
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
                <input v-model="formData.email" type="email" placeholder="seuemail@provedor.com" required class="theme-input">
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
              <h3>3. Canal de Preferência</h3>
              <label class="group-label">Como você prefere receber nosso contato inicial? *</label>
              <div class="radio-group-list">
                <label class="radio-card-option" :class="{ 'selected': formData.pref_contato === 'whatsapp' }">
                  <input v-model="formData.pref_contato" type="radio" value="whatsapp" name="pref_contato" class="radio-box">
                  <span class="radio-txt">💬 Mensagem no meu WhatsApp</span>
                </label>
                <label class="radio-card-option" :class="{ 'selected': formData.pref_contato === 'email' }">
                  <input v-model="formData.pref_contato" type="radio" value="email" name="pref_contato" class="radio-box">
                  <span class="radio-txt">📩 Por e-mail</span>
                </label>
                <label class="radio-card-option" :class="{ 'selected': formData.pref_contato === 'ligacao' }">
                  <input v-model="formData.pref_contato" type="radio" value="ligacao" name="pref_contato" class="radio-box">
                  <span class="radio-txt">📞 Receber uma ligação carinhosa</span>
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

            <!-- STEP 4: Experience & Objectives -->
            <div v-if="step === 4" class="form-step-pane">
              <h3>4. Seu Perfil e Objetivos</h3>
              <div class="input-field">
                <label>Você já estudou inglês alguma vez? *</label>
                <select v-model="formData.experiencia" required class="theme-input">
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
                  Finalizar Cadastro <Check class="btn-icon-svg" />
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

/* Hero Section */
.modality-hero {
  position: relative;
  padding: 220px 0 150px 0;
  min-height: 80vh;
  display: flex;
  align-items: center;
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
  opacity: 0.55;
  transform: scale(1.02);
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to right, rgba(0, 18, 51, 0.9) 35%, rgba(0, 18, 51, 0.3) 100%);
  z-index: 1;
}

.hero-text-wrapper {
  max-width: 800px;
  text-align: left;
  position: relative;
  z-index: 2;
}

.hero-category-tag {
  color: var(--accent);
  font-weight: 800;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  margin-bottom: 1.5rem;
  display: block;
}

.hero-title-h1 {
  font-size: clamp(3rem, 6vw, 5rem);
  color: white;
  margin-bottom: 2rem;
  line-height: 1.1;
  font-weight: 800;
}

.hero-title-h1 .highlight-text {
  color: var(--accent);
}

.hero-desc-p {
  font-size: clamp(1.1rem, 2vw, 1.35rem);
  color: rgba(255, 255, 255, 0.95);
  margin-bottom: 3.5rem;
  line-height: 1.7;
  font-weight: 300;
}

/* Sections Base */
.section-presentation {
  padding: 120px 0;
  background: white;
}

.grid-2-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5rem;
  align-items: start;
  text-align: left;
}

.section-tag-small {
  color: var(--primary);
  font-weight: 800;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  font-size: 0.9rem;
  display: inline-block;
  margin-bottom: 1rem;
}

.section-title-h2 {
  font-size: clamp(2rem, 4vw, 3rem);
  color: var(--primary-dark);
  font-weight: 800;
  margin-top: 0;
  margin-bottom: 2rem;
}

.section-desc-p {
  font-size: 1.15rem;
  color: var(--gray);
  line-height: 1.8;
  margin-bottom: 1.5rem;
}

.bg-light-gray {
  background: #f8fafc;
}

/* Checklist Card */
.checklist-card {
  background: #f1f5f9;
  border-radius: 30px;
  padding: 3rem;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.02);
  border: 1px solid rgba(0, 0, 0, 0.03);
}

.checklist-title {
  color: var(--primary-dark);
  font-size: 1.6rem;
  margin-bottom: 2rem;
  margin-top: 0;
  font-weight: 800;
}

.checklist-ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}

.checklist-ul li {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 1.1rem;
  color: var(--primary-dark);
  font-weight: 600;
}

.check-icon {
  color: #10b981;
  font-weight: bold;
  font-size: 1.2rem;
}

/* Learning grid */
.section-learning {
  padding: 120px 0;
}

.header-margin {
  margin-bottom: 6rem;
  text-align: left;
}

.section-subtitle-p {
  color: var(--gray);
  font-size: 1.2rem;
  margin-top: 0.5rem;
}

.learning-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2.5rem;
  text-align: left;
}

.learning-card {
  background: white;
  border-radius: 30px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0,0,0,0.03);
  border: 1px solid rgba(0,0,0,0.02);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.learning-card:hover {
  transform: translateY(-8px);
  box-shadow: var(--shadow-premium);
}

.learning-card-img-wrapper {
  position: relative;
  height: 200px;
  overflow: hidden;
}

.learning-card-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.learning-card-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0, 18, 51, 0.4), transparent);
}

.learning-card-tag {
  position: absolute;
  top: 15px;
  left: 15px;
  background: rgba(255, 255, 255, 0.95);
  color: var(--primary-dark);
  font-weight: 800;
  font-size: 0.85rem;
  padding: 0.5rem 1rem;
  border-radius: 99px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

.learning-card-content {
  padding: 2.5rem 2rem;
}

.learning-card-content h3 {
  color: var(--primary-dark);
  font-size: 1.45rem;
  margin-top: 0;
  margin-bottom: 1rem;
  font-weight: 800;
}

.learning-card-content p {
  color: var(--gray);
  font-size: 1.05rem;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.learning-sub-ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.learning-sub-ul li {
  position: relative;
  padding-left: 20px;
  font-size: 0.95rem;
  color: var(--primary-dark);
  font-weight: 600;
}

.learning-sub-ul li::before {
  content: '✦';
  position: absolute;
  left: 0;
  color: var(--accent);
}

/* Methodology */
.section-methodology {
  padding: 120px 0;
  background: white;
}

.flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}

.methodology-visual-card {
  background: linear-gradient(135deg, var(--primary-dark), #002b80);
  border-radius: 35px;
  padding: 4rem 3rem;
  color: white;
  box-shadow: var(--shadow-premium);
  max-width: 480px;
}

.methodology-icon {
  width: 50px;
  height: 50px;
  color: var(--accent);
  margin-bottom: 2rem;
}

.methodology-visual-card h3 {
  font-size: 1.8rem;
  margin-bottom: 1.5rem;
  margin-top: 0;
  font-weight: 800;
  color: var(--accent);
}

.methodology-visual-card p {
  opacity: 0.95;
  line-height: 1.7;
  font-size: 1.1rem;
  margin-bottom: 1.5rem;
}

.methodology-visual-card .small-info {
  opacity: 0.75;
  font-size: 0.95rem;
  margin-bottom: 0;
  border-top: 1px solid rgba(255, 255, 255, 0.15);
  padding-top: 1.5rem;
}

.flex-column-start {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
}

.pilar-item {
  margin-bottom: 1.8rem;
  border-left: 3px solid var(--accent);
  padding-left: 1.5rem;
}

.pilar-item h4 {
  font-size: 1.25rem;
  color: var(--primary-dark);
  margin-top: 0;
  margin-bottom: 0.5rem;
  font-weight: 700;
}

.pilar-item p {
  color: var(--gray);
  line-height: 1.6;
  margin: 0;
  font-size: 1.05rem;
}

/* Target & Differentials */
.section-target {
  padding: 120px 0;
}

.bg-dark-blue {
  background: var(--primary-dark);
}

.target-ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.target-ul li {
  font-size: 1.15rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.9);
}

.diferenciais-grid {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.diferencial-card-glass {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 20px;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.dif-icon {
  width: 32px;
  height: 32px;
  color: var(--accent);
}

.diferencial-card-glass h4 {
  font-size: 1.25rem;
  color: var(--accent);
  margin: 0;
  font-weight: 700;
}

.diferencial-card-glass p {
  margin: 0;
  opacity: 0.8;
  line-height: 1.6;
  font-size: 1rem;
}

.tagline-footer-box {
  text-align: center;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  margin-top: 6rem;
  padding-top: 4rem;
}

.tagline-bold {
  font-size: 1.6rem;
  font-weight: 700;
  color: var(--accent);
  margin-bottom: 0.5rem;
  margin-top: 0;
}

.tagline-sub {
  font-size: 1.15rem;
  opacity: 0.85;
  margin: 0;
}

/* Wizard custom styles */
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
  margin-bottom: 0.5rem;
  font-weight: 800;
}

.section-form-subtitle {
  color: var(--gray);
  text-align: center;
  margin-bottom: 4rem;
  font-size: 1.15rem;
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
  margin-bottom: 4rem;
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
  margin-bottom: 1.5rem;
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
  margin-bottom: 2rem;
}

.radio-card-option {
  background: #f8fafc;
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-radius: 12px;
  padding: 1.2rem;
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
  padding: 1.1rem 2.2rem;
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

@media (max-width: 992px) {
  .grid-2-col {
    grid-template-columns: 1fr;
    gap: 3.5rem;
  }
  .learning-grid {
    grid-template-columns: 1fr;
    gap: 2.5rem;
  }
  .methodology-visual-card {
    max-width: 100%;
  }
}

@media (max-width: 768px) {
  .modality-hero {
    padding: 180px 0 100px 0;
  }
  .form-wizard-card {
    padding: 2.5rem 1.5rem;
  }
  .form-grid-2 {
    grid-template-columns: 1fr;
  }
}
</style>

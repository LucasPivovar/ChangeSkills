<script setup>
import { ref, computed, onMounted } from 'vue'
import { Mic, Brain, Volume2, MessageCircle, Target, UserCheck, ArrowLeft, ArrowRight, Check } from '@lucide/vue'

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

const step = ref(1)

const formData = ref({
  nome: '',
  sobrenome: '',
  email: '',
  telefone: '',
  pref_contato: 'whatsapp',
  nivel_ingles: '',
  foco: ''
})

const isStep1Valid = computed(() => {
  return formData.value.nome.trim() !== ''
})

const isStep2Valid = computed(() => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return emailRegex.test(formData.value.email) && formData.value.telefone.trim() !== ''
})

const isStep3Valid = computed(() => {
  return !!formData.value.pref_contato
})

const isStep4Valid = computed(() => {
  return formData.value.nivel_ingles !== ''
})

const progressWidth = computed(() => {
  return ((step.value - 1) / 3) * 100 + '%'
})

function nextStep() {
  if (step.value === 1 && isStep1Valid.value) {
    step.value = 2
  } else if (step.value === 2 && isStep2Valid.value) {
    step.value = 3
  } else if (step.value === 3 && isStep3Valid.value) {
    step.value = 4
  }
}

function prevStep() {
  if (step.value > 1) {
    step.value--
  }
}

function submitForm() {
  if (isStep4Valid.value) {
    alert('Solicitação enviada com sucesso!')
    // Reset form
    formData.value = {
      nome: '',
      sobrenome: '',
      email: '',
      telefone: '',
      pref_contato: 'whatsapp',
      nivel_ingles: '',
      foco: ''
    }
    step.value = 1
  }
}
</script>

<template>
  <div class="aulas-conversacao-view">
    <!-- Hero -->
    <section class="mesh-bg hero-section">
      <div class="container reveal active hero-content">
        <span class="hero-tag">AULAS DE CONVERSAÇÃO</span>
        <h1 class="hero-title">Desenvolva sua fluência <br><span class="gradient-text">e confiança</span></h1>
        <p class="hero-desc">
          Aulas 100% focadas em fala, escuta e interação em qualquer idioma (como Inglês, Espanhol, Francês e Português), com temas do dia a dia e do ambiente profissional. Ideal para quem já tem base no idioma e deseja alcançar uma comunicação natural, espontânea e se expressar com confiança.
        </p>
      </div>
    </section>

    <!-- Info & Benefits -->
    <section class="container info-section">
      <div class="info-grid">
        <div class="info-left">
          <div class="glass-card reveal">
            <h2>Sobre o Curso</h2>
            <p>
              Projetado para quem deseja aprimorar sua comunicação oral e se expressar com mais segurança em qualquer idioma. Trabalhamos com material próprio, tópicos dinâmicos, vocabulário prático e correções personalizadas.
            </p>
          </div>

          <div class="glass-card reveal">
            <h2>Material Utilizado</h2>
            <p>
              Utilizamos materiais próprios desenvolvidos para a sua necessidade. Trazemos temas atuais, aulas interativas, vídeos, podcasts e debates. O conteúdo é adaptado ao nível do aluno, garantindo aprendizado constante e eficiente.
            </p>
          </div>
        </div>

        <div class="glass-card benefits-card reveal">
          <h2>Benefícios do Curso</h2>
          <div class="check-item"><Mic class="check-icon" /> Prática de fala com feedback em tempo real</div>
          <div class="check-item"><Brain class="check-icon" /> Ampliação de vocabulário para o dia a dia</div>
          <div class="check-item"><Volume2 class="check-icon" /> Correção de pronúncia e entonação</div>
          <div class="check-item"><MessageCircle class="check-icon" /> Simulações de conversas reais</div>
          <div class="check-item"><Target class="check-icon" /> Ambiente dinâmico e colaborativo</div>
          <div class="check-item"><UserCheck class="check-icon" /> Professores experientes e motivadores</div>
        </div>
      </div>
    </section>

    <!-- Wizard Form -->
    <section class="container form-section">
      <div class="glass-card wizard-container reveal">
        <div class="wizard-header">
          <h2>Agende sua aula experimental gratuita</h2>
          <p>Preencha seus dados e receba mais informações sobre o curso.</p>
        </div>
        
        <!-- Progress Bar -->
        <div class="progress-bar-container">
          <div class="progress-bg-line"></div>
          <div class="progress-line" :style="{ width: progressWidth }"></div>
          
          <div 
            v-for="i in 4" 
            :key="i"
            class="step-indicator" 
            :class="{ 'active': step >= i }"
          >
            {{ i }}
          </div>
        </div>

        <form @submit.prevent="submitForm" class="wizard-form">
          <!-- STEP 1: Personal Info -->
          <div v-if="step === 1" class="form-step">
            <h3>1. Seus Dados</h3>
            <div class="form-grid">
              <div class="input-group">
                <label>Nome *</label>
                <input v-model="formData.nome" type="text" placeholder="Nome" required class="form-input">
              </div>
              <div class="input-group">
                <label>Sobrenome</label>
                <input v-model="formData.sobrenome" type="text" placeholder="Sobrenome" class="form-input">
              </div>
            </div>
            <div class="step-footer">
              <button 
                type="button" 
                @click="nextStep" 
                :disabled="!isStep1Valid" 
                class="btn-next btn-primary-theme"
              >
                Próximo <ArrowRight class="btn-icon" />
              </button>
            </div>
          </div>

          <!-- STEP 2: Contact Info -->
          <div v-if="step === 2" class="form-step">
            <h3>2. Dados de Contato</h3>
            <div class="input-group">
              <label>E-mail *</label>
              <input v-model="formData.email" type="email" placeholder="exemplo@email.com" required class="form-input">
            </div>
            <div class="input-group">
              <label>Telefone / WhatsApp *</label>
              <input v-model="formData.telefone" type="tel" placeholder="(00) 00000-0000" required class="form-input">
            </div>
            <div class="step-footer split">
              <button type="button" @click="prevStep" class="btn-back">
                <ArrowLeft class="btn-icon" /> Voltar
              </button>
              <button 
                type="button" 
                @click="nextStep" 
                :disabled="!isStep2Valid" 
                class="btn-next btn-primary-theme"
              >
                Próximo <ArrowRight class="btn-icon" />
              </button>
            </div>
          </div>

          <!-- STEP 3: Preferences -->
          <div v-if="step === 3" class="form-step">
            <h3>3. Preferência de Contato</h3>
            <label class="section-label">Como prefere que entremos em contato? *</label>
            <div class="radio-options">
              <label class="radio-card" :class="{ 'selected': formData.pref_contato === 'whatsapp' }">
                <input v-model="formData.pref_contato" type="radio" name="pref_contato" value="whatsapp" class="radio-input">
                <span class="radio-label">💬 Mensagem no WhatsApp</span>
              </label>
              <label class="radio-card" :class="{ 'selected': formData.pref_contato === 'email' }">
                <input v-model="formData.pref_contato" type="radio" name="pref_contato" value="email" class="radio-input">
                <span class="radio-label">📧 Enviar E-mail</span>
              </label>
              <label class="radio-card" :class="{ 'selected': formData.pref_contato === 'ligacao' }">
                <input v-model="formData.pref_contato" type="radio" name="pref_contato" value="ligacao" class="radio-input">
                <span class="radio-label">📞 Receber Ligação</span>
              </label>
            </div>
            <div class="step-footer split">
              <button type="button" @click="prevStep" class="btn-back">
                <ArrowLeft class="btn-icon" /> Voltar
              </button>
              <button 
                type="button" 
                @click="nextStep" 
                :disabled="!isStep3Valid" 
                class="btn-next btn-primary-theme"
              >
                Próximo <ArrowRight class="btn-icon" />
              </button>
            </div>
          </div>

          <!-- STEP 4: Level & Goals -->
          <div v-if="step === 4" class="form-step">
            <h3>4. Sobre Você</h3>
            <div class="input-group">
              <label>Qual seu nível atual no idioma?</label>
              <select v-model="formData.nivel_ingles" required class="form-input">
                <option value="" disabled>Selecione</option>
                <option value="nunca">Nunca fiz curso</option>
                <option value="iniciante">Sei um pouco</option>
                <option value="intermediario">Sei moderadamente</option>
                <option value="avancado">Sou fluente mas preciso praticar!</option>
              </select>
            </div>
            <div class="input-group">
              <label>Qual é o foco da sua conversação?</label>
              <textarea v-model="formData.foco" rows="4" placeholder="Ex: Preciso de inglês para o trabalho, viagens, entrevistas..." class="form-input textarea-input"></textarea>
            </div>
            <div class="step-footer split">
              <button type="button" @click="prevStep" class="btn-back">
                <ArrowLeft class="btn-icon" /> Voltar
              </button>
              <button 
                type="submit" 
                :disabled="!isStep4Valid" 
                class="btn-submit"
              >
                Finalizar e Enviar <Check class="btn-icon" />
              </button>
            </div>
          </div>
        </form>
      </div>
    </section>
  </div>
</template>

<style scoped>
.aulas-conversacao-view {
  width: 100%;
}

.hero-section {
  padding: 240px 0 120px 0;
  text-align: center;
  background: linear-gradient(135deg, #f5f7ff 0%, #eef2ff 100%);
}

.hero-tag {
  color: var(--primary);
  font-weight: 800;
  letter-spacing: 0.25em;
  font-size: 0.9rem;
  text-transform: uppercase;
  display: inline-block;
  margin-bottom: 1.5rem;
}

.hero-title {
  font-size: 4.5rem;
  margin: 1.5rem 0;
  font-weight: 800;
  line-height: 1.1;
  color: var(--primary-dark);
}

.gradient-text {
  background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-desc {
  font-size: 1.3rem;
  color: var(--gray);
  max-width: 800px;
  margin: 0 auto;
  font-weight: 400;
  line-height: 1.6;
}

.info-section {
  padding: 80px 0;
}

.info-grid {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 3rem;
}

.info-left {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.glass-card {
  background: white;
  border-radius: 30px;
  padding: 3rem;
  box-shadow: var(--shadow-premium);
  border: 1px solid rgba(0, 0, 0, 0.03);
  text-align: left;
}

.glass-card h2 {
  font-size: 1.8rem;
  color: var(--primary-dark);
  margin-bottom: 1.5rem;
  font-weight: 800;
}

.glass-card p {
  color: var(--gray);
  font-size: 1.1rem;
  line-height: 1.8;
  margin: 0;
}

.benefits-card {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.check-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  font-size: 1.1rem;
  color: var(--gray);
  line-height: 1.6;
}

.check-icon {
  color: var(--primary);
  flex-shrink: 0;
  margin-top: 3px;
  width: 20px;
  height: 20px;
}

.form-section {
  padding-bottom: 120px;
}

.wizard-container {
  max-width: 850px;
  margin: 0 auto;
  padding: 4rem;
  border-radius: 40px;
}

.wizard-header {
  text-align: center;
  margin-bottom: 3rem;
}

.wizard-header h2 {
  font-size: 2.3rem;
  color: var(--primary-dark);
  margin-bottom: 1rem;
}

.wizard-header p {
  color: var(--gray);
  font-size: 1.1rem;
}

.progress-bar-container {
  display: flex;
  justify-content: space-between;
  position: relative;
  margin-bottom: 3rem;
  max-width: 500px;
  margin-left: auto;
  margin-right: auto;
}

.progress-bg-line {
  position: absolute;
  top: 50%;
  left: 0;
  width: 100%;
  height: 2px;
  background: #e2e8f0;
  z-index: 1;
  transform: translateY(-50%);
}

.progress-line {
  position: absolute;
  top: 50%;
  left: 0;
  height: 2px;
  background: var(--primary);
  z-index: 2;
  transform: translateY(-50%);
  transition: width 0.4s;
}

.step-indicator {
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

.step-indicator.active {
  background: var(--primary);
  color: white;
}

.wizard-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-step h3 {
  color: var(--primary-dark);
  font-size: 1.5rem;
  font-weight: 800;
  margin-bottom: 1.5rem;
  text-align: left;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

.input-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  text-align: left;
  margin-bottom: 1.2rem;
}

.input-group label {
  font-weight: 600;
  color: var(--primary-dark);
  font-size: 0.95rem;
}

.form-input {
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

.form-input:focus {
  border-color: var(--primary);
  background: white;
}

.textarea-input {
  resize: vertical;
}

.section-label {
  display: block;
  font-weight: 600;
  color: var(--primary-dark);
  margin-bottom: 1rem;
  font-size: 0.95rem;
  text-align: left;
}

.radio-options {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.radio-card {
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

.radio-card:hover {
  background: rgba(0, 71, 255, 0.02);
  border-color: rgba(0, 71, 255, 0.2);
}

.radio-card.selected {
  background: rgba(0, 71, 255, 0.05);
  border-color: var(--primary);
}

.radio-input {
  accent-color: var(--primary);
  width: 18px;
  height: 18px;
}

.radio-label {
  font-weight: 600;
  color: var(--primary-dark);
}

.step-footer {
  display: flex;
  justify-content: flex-end;
  margin-top: 2rem;
}

.step-footer.split {
  justify-content: space-between;
}

.btn-next, .btn-submit, .btn-back {
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

.btn-primary-theme {
  background: var(--primary);
  color: white;
}

.btn-primary-theme:hover:not(:disabled) {
  background: var(--primary-dark);
}

.btn-primary-theme:disabled {
  background: #cbd5e1;
  color: #94a3b8;
  cursor: not-allowed;
}

.btn-back {
  background: transparent;
  color: var(--primary);
  border: 2px solid var(--primary);
}

.btn-back:hover {
  background: rgba(0, 71, 255, 0.05);
}

.btn-submit {
  background: var(--primary-dark);
  color: white;
}

.btn-submit:hover:not(:disabled) {
  background: black;
}

.btn-submit:disabled {
  background: #cbd5e1;
  color: #94a3b8;
  cursor: not-allowed;
}

.btn-icon {
  width: 18px;
  height: 18px;
}

@media (max-width: 992px) {
  .info-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 3rem;
  }
  .hero-desc {
    font-size: 1.1rem;
  }
  .wizard-container {
    padding: 2.5rem 1.5rem;
  }
  .form-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { CheckCircle2, ArrowRight, ArrowLeft, Check } from '@lucide/vue'

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
  nome_completo: '',
  documento: '',
  email: '',
  telefone: '',
  modulo_concluido: '',
  data_conclusao: ''
})

const isStep1Valid = computed(() => {
  return formData.value.nome_completo.trim() !== '' && formData.value.documento.trim() !== ''
})

const isStep2Valid = computed(() => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return emailRegex.test(formData.value.email) && formData.value.telefone.trim() !== ''
})

const isStep3Valid = computed(() => {
  return formData.value.modulo_concluido.trim() !== '' && formData.value.data_conclusao !== ''
})

const progressWidth = computed(() => {
  return ((step.value - 1) / 2) * 100 + '%'
})

function nextStep() {
  if (step.value === 1 && isStep1Valid.value) {
    step.value = 2
  } else if (step.value === 2 && isStep2Valid.value) {
    step.value = 3
  }
}

function prevStep() {
  if (step.value > 1) {
    step.value--
  }
}

function submitForm() {
  if (isStep3Valid.value) {
    alert('Solicitação de certificado enviada com sucesso!')
    // Reset form
    formData.value = {
      nome_completo: '',
      documento: '',
      email: '',
      telefone: '',
      modulo_concluido: '',
      data_conclusao: ''
    }
    step.value = 1
  }
}
</script>

<template>
  <div class="solicitacao-certificado-view">
    <!-- Hero -->
    <section class="mesh-bg hero-section">
      <div class="container reveal active hero-content">
        <span class="hero-tag">PARABÉNS PELA CONQUISTA</span>
        <h1 class="hero-title">Concluiu o curso <br><span class="gradient-text">conosco?</span></h1>
        <p class="hero-desc">
          Este é o canal oficial para solicitar seu certificado de conclusão.<br>
          Preencha o formulário para que possamos emitir seu certificado de forma rápida e segura.
        </p>
      </div>
    </section>

    <!-- Info & Requirements -->
    <section class="container info-section">
      <div class="info-grid">
        <!-- Requisitos -->
        <div class="glass-card reveal">
          <h2>Requisitos para Solicitar</h2>
          <div class="check-item"><CheckCircle2 class="check-icon" /> Ter concluído todos os módulos do curso</div>
          <div class="check-item"><CheckCircle2 class="check-icon" /> Ter atingido a frequência mínima exigida</div>
          <div class="check-item"><CheckCircle2 class="check-icon" /> Ter alcançado 75% de aprovação no seu módulo</div>
          <div class="check-item"><CheckCircle2 class="check-icon" /> Estar com as mensalidades regularizadas</div>
          
          <div class="alert-box">
            <p>
              Solicitações que não atendam aos requisitos não serão processadas! Se você não tem certeza se atende a todos os pré-requisitos, entre em contato com nossa equipe.
            </p>
          </div>
        </div>

        <!-- Info e Prazos -->
        <div class="info-right-column">
          <div class="glass-card reveal">
            <h2>Informações Necessárias</h2>
            <ul class="arrow-list">
              <li><ArrowRight class="list-arrow" /> Nome completo (como deve aparecer no certificado)</li>
              <li><ArrowRight class="list-arrow" /> CPF ou documento de identificação</li>
              <li><ArrowRight class="list-arrow" /> Nome do módulo e detalhes do curso concluído</li>
              <li><ArrowRight class="list-arrow" /> Data de conclusão do curso</li>
              <li><ArrowRight class="list-arrow" /> E-mail para envio do certificado</li>
              <li><ArrowRight class="list-arrow" /> Telefone para contato</li>
            </ul>
          </div>

          <div class="glass-card reveal">
            <h2>Prazos e Importante</h2>
            <p class="deadline-text">O prazo para emissão do certificado é de até <strong>14 dias úteis</strong> após o recebimento da solicitação completa. Ele será enviado em formato PDF.</p>
            <ul class="bullet-list">
              <li>A emissão da 1ª via é gratuita.</li>
              <li>A 2ª via pode ter cobrança de taxa administrativa.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Wizard Form -->
    <section class="container form-section">
      <div class="glass-card wizard-container reveal">
        <div class="wizard-header">
          <h2>Solicite seu Certificado Aqui</h2>
          <p>Se você já tem as informações e atende aos pré-requisitos, preencha abaixo:</p>
        </div>
        
        <!-- Progress Bar -->
        <div class="progress-bar-container">
          <div class="progress-bg-line"></div>
          <div class="progress-line" :style="{ width: progressWidth }"></div>
          
          <div 
            v-for="i in 3" 
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
            <h3>1. Dados do Aluno</h3>
            <div class="form-grid">
              <div class="input-group">
                <label>Nome Completo *</label>
                <input v-model="formData.nome_completo" type="text" placeholder="Como deve aparecer no certificado" required class="form-input">
              </div>
              <div class="input-group">
                <label>CPF ou RG *</label>
                <input v-model="formData.documento" type="text" placeholder="Documento de identificação" required class="form-input">
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
              <label>E-mail para Envio *</label>
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

          <!-- STEP 3: Course Info -->
          <div v-if="step === 3" class="form-step">
            <h3>3. Informações do Curso</h3>
            <div class="input-group">
              <label>Módulo / Curso Concluído *</label>
              <input v-model="formData.modulo_concluido" type="text" placeholder="Ex: Adult Fast Track - Nível B2" required class="form-input">
            </div>
            <div class="input-group">
              <label>Data de Conclusão *</label>
              <input v-model="formData.data_conclusao" type="date" required class="form-input">
            </div>
            <div class="step-footer split">
              <button type="button" @click="prevStep" class="btn-back">
                <ArrowLeft class="btn-icon" /> Voltar
              </button>
              <button 
                type="submit" 
                :disabled="!isStep3Valid" 
                class="btn-submit"
              >
                Solicitar Certificado <Check class="btn-icon" />
              </button>
            </div>
          </div>
        </form>
      </div>
    </section>
  </div>
</template>

<style scoped>
.solicitacao-certificado-view {
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
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 3rem;
}

.info-right-column {
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

.check-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  font-size: 1.15rem;
  color: var(--gray);
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.check-icon {
  color: #22c55e;
  flex-shrink: 0;
  margin-top: 3px;
  width: 22px;
  height: 22px;
}

.alert-box {
  margin-top: 2rem;
  padding: 1.5rem;
  background: rgba(239, 68, 68, 0.08);
  border-left: 4px solid #EF4444;
  border-radius: 0 15px 15px 0;
}

.alert-box p {
  color: #991b1b;
  font-weight: 600;
  font-size: 1rem;
  line-height: 1.6;
  margin: 0;
}

.arrow-list {
  list-style: none;
  color: var(--gray);
  font-size: 1.1rem;
  line-height: 1.8;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 0;
  margin: 0;
}

.list-arrow {
  width: 16px;
  height: 16px;
  color: var(--primary);
  display: inline-block;
  margin-right: 10px;
  vertical-align: middle;
}

.deadline-text {
  color: var(--gray);
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.bullet-list {
  list-style: none;
  color: var(--gray);
  font-size: 1.1rem;
  line-height: 1.8;
  padding: 0;
  margin: 0;
}

.bullet-list li {
  position: relative;
  padding-left: 1.5rem;
}

.bullet-list li::before {
  content: "•";
  color: var(--primary);
  font-size: 1.5rem;
  position: absolute;
  left: 0;
  top: -3px;
}

.form-section {
  padding-bottom: 120px;
}

.wizard-container {
  max-width: 850px;
  margin: 0 auto;
  padding: 4rem;
  border-radius: 40px;
  text-align: center;
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
  max-width: 400px;
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

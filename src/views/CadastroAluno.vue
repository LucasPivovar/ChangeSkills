<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ArrowLeft, ArrowRight, Check } from '@lucide/vue'

const router = useRouter()
const currentStep = ref(1)

// Form fields reactive model
const form = ref({
  nome: '',
  cpf: '',
  dataNascimento: '',
  email: '',
  whatsapp: '',
  endereco: '',
  idioma: '',
  modalidade: '',
  ondeConheceu: '',
  concordaTermos: false
})

const progressPercentage = computed(() => {
  return ((currentStep.value - 1) / 3) * 100
})

function nextStep() {
  if (currentStep.value < 4) {
    currentStep.value++
  }
}

function prevStep() {
  if (currentStep.value > 1) {
    currentStep.value--
  }
}

function handleSubmit() {
  alert('Cadastro enviado com sucesso!')
  router.push('/area-do-aluno')
}

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
  <div class="cadastro-view">
    <main class="cadastro-main">
      <!-- Background mesh effects -->
      <section class="cadastro-hero mesh-bg">
        <div class="hero-glow"></div>
        <div class="container reveal active hero-content">
          <span class="hero-tag">MATRÍCULAS ABERTAS</span>
          <h1 class="hero-title">Cadastro de<br>Novos Alunos</h1>
          <p class="hero-desc">
            Preencha o formulário abaixo para realizar seu cadastro e iniciar sua jornada de aprendizado conosco.
          </p>
        </div>
      </section>

      <!-- Step Wizard Form Container -->
      <section class="container form-section">
        <div class="glass-card reveal form-wrapper-card">
          
          <!-- Progress Bar Indicators -->
          <div class="progress-bar-container">
            <div class="progress-bg-line"></div>
            <div class="progress-fill-line" :style="{ width: progressPercentage + '%' }"></div>
            
            <div 
              v-for="step in 4" 
              :key="step"
              class="step-indicator" 
              :class="{ 'active': currentStep >= step }"
            >
              {{ step }}
            </div>
          </div>

          <form @submit.prevent="handleSubmit" class="wizard-form">
            
            <!-- STEP 1: Personal Info -->
            <div v-if="currentStep === 1" class="form-step">
              <h3 class="step-title">1. Dados Pessoais</h3>
              <div class="form-grid">
                <div class="form-group">
                  <label for="fullName">Nome Completo *</label>
                  <input 
                    id="fullName"
                    v-model="form.nome" 
                    type="text" 
                    placeholder="Seu nome" 
                    class="form-control"
                    required
                  >
                </div>
                <div class="form-group">
                  <label for="cpf">CPF *</label>
                  <input 
                    id="cpf"
                    v-model="form.cpf" 
                    type="text" 
                    placeholder="000.000.000-00" 
                    class="form-control"
                    required
                  >
                </div>
              </div>
              <div class="form-group mt-large">
                <label for="birthdate">Data de Nascimento *</label>
                <input 
                  id="birthdate"
                  v-model="form.dataNascimento" 
                  type="date" 
                  class="form-control"
                  required
                >
              </div>
              
              <div class="form-actions-right">
                <button type="button" @click="nextStep" class="btn-vip">
                  Próximo <ArrowRight class="btn-arrow" />
                </button>
              </div>
            </div>

            <!-- STEP 2: Address and contact info -->
            <div v-if="currentStep === 2" class="form-step">
              <h3 class="step-title">2. Dados de Contato e Endereço</h3>
              <div class="form-grid">
                <div class="form-group">
                  <label for="email">E-mail *</label>
                  <input 
                    id="email"
                    v-model="form.email" 
                    type="email" 
                    placeholder="exemplo@email.com" 
                    class="form-control"
                    required
                  >
                </div>
                <div class="form-group">
                  <label for="whatsapp">WhatsApp / Telefone *</label>
                  <input 
                    id="whatsapp"
                    v-model="form.whatsapp" 
                    type="tel" 
                    placeholder="(00) 00000-0000" 
                    class="form-control"
                    required
                  >
                </div>
              </div>
              <div class="form-group mt-large">
                <label for="address">Endereço Completo</label>
                <input 
                  id="address"
                  v-model="form.endereco" 
                  type="text" 
                  placeholder="Rua, Número, Bairro, Cidade - UF" 
                  class="form-control"
                >
              </div>
              
              <div class="form-actions-split">
                <button type="button" @click="prevStep" class="btn-back">
                  <ArrowLeft class="btn-arrow-left" /> Voltar
                </button>
                <button type="button" @click="nextStep" class="btn-vip">
                  Próximo <ArrowRight class="btn-arrow" />
                </button>
              </div>
            </div>

            <!-- STEP 3: Course Selection -->
            <div v-if="currentStep === 3" class="form-step">
              <h3 class="step-title">3. Curso de Interesse</h3>
              <div class="form-group">
                <label for="language">Idioma Desejado *</label>
                <select 
                  id="language"
                  v-model="form.idioma"
                  class="form-control"
                  required
                >
                  <option value="" disabled selected>Selecione um idioma</option>
                  <option value="ingles">Inglês</option>
                  <option value="espanhol">Español</option>
                  <option value="frances">Français</option>
                  <option value="portugues">Português para Estrangeiros</option>
                </select>
              </div>
              
              <div class="form-group mt-large">
                <label for="modality">Modalidade *</label>
                <select 
                  id="modality"
                  v-model="form.modalidade"
                  class="form-control"
                  required
                >
                  <option value="" disabled selected>Selecione a modalidade</option>
                  <option value="online">Online Ao Vivo</option>
                  <option value="presencial">Presencial</option>
                  <option value="hibrido">Híbrido</option>
                </select>
              </div>
              
              <div class="form-actions-split">
                <button type="button" @click="prevStep" class="btn-back">
                  <ArrowLeft class="btn-arrow-left" /> Voltar
                </button>
                <button type="button" @click="nextStep" class="btn-vip">
                  Próximo <ArrowRight class="btn-arrow" />
                </button>
              </div>
            </div>

            <!-- STEP 4: Privacy & Completion -->
            <div v-if="currentStep === 4" class="form-step">
              <h3 class="step-title">4. Preferências Adicionais</h3>
              <div class="form-group">
                <label for="source">Como conheceu a Change Skills?</label>
                <select 
                  id="source"
                  v-model="form.ondeConheceu"
                  class="form-control"
                >
                  <option value="" disabled selected>Selecione uma opção</option>
                  <option value="instagram">Instagram / Facebook</option>
                  <option value="google">Busca no Google</option>
                  <option value="indicacao">Indicação de amigo/aluno</option>
                  <option value="outros">Outros</option>
                </select>
              </div>
              
              <div class="form-group mt-large">
                <label class="checkbox-container">
                  <input 
                    v-model="form.concordaTermos" 
                    type="checkbox" 
                    class="checkbox-input"
                    required
                  >
                  <span class="checkbox-text">
                    Li e concordo com os Termos de Uso e Política de Privacidade da Change Skills Idiomas. Declaro que as informações fornecidas são verdadeiras.
                  </span>
                </label>
              </div>
              
              <div class="form-actions-split">
                <button type="button" @click="prevStep" class="btn-back">
                  <ArrowLeft class="btn-arrow-left" /> Voltar
                </button>
                <button type="submit" class="btn-vip btn-submit">
                  Finalizar Cadastro <Check class="btn-arrow" />
                </button>
              </div>
            </div>

          </form>
        </div>
      </section>
    </main>
  </div>
</template>

<style scoped>
.cadastro-view {
  width: 100%;
  background: var(--bg-light);
}

.cadastro-main {
  min-height: 100vh;
  position: relative;
  overflow: hidden;
  box-sizing: border-box;
}

.cadastro-hero {
  padding-top: 180px;
  text-align: center;
  padding-bottom: 80px;
  position: relative;
}

.hero-glow {
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

.hero-content {
  position: relative;
  z-index: 1;
}

.hero-tag {
  color: var(--primary);
  font-weight: 800;
  letter-spacing: 0.2em;
  font-size: 0.9rem;
  display: inline-block;
}

.hero-title {
  font-size: clamp(2.5rem, 5vw, 4rem);
  margin-bottom: 2rem;
  margin-top: 1rem;
  color: var(--primary-dark);
  font-weight: 800;
  line-height: 1.15;
}

.hero-desc {
  font-size: 1.2rem;
  color: var(--gray);
  max-width: 800px;
  margin: auto;
  line-height: 1.6;
}

.form-section {
  padding-top: 50px;
  padding-bottom: 200px;
  position: relative;
  z-index: 1;
}

.form-wrapper-card {
  margin: auto;
  max-width: 800px;
  background: white;
  padding: clamp(2rem, 5vw, 4rem);
  border-radius: 40px;
  box-shadow: 0 30px 60px rgba(0, 0, 0, 0.08);
  border: 1px solid rgba(0, 0, 0, 0.03);
  box-sizing: border-box;
  text-align: left;
}

/* Wizard progress bars */
.progress-bar-container {
  display: flex;
  justify-content: space-between;
  position: relative;
  margin-bottom: 3.5rem;
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

.progress-fill-line {
  position: absolute;
  top: 50%;
  left: 0;
  height: 2px;
  background: var(--primary);
  z-index: 2;
  transform: translateY(-50%);
  transition: width 0.4s ease;
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
  transition: all 0.4s ease;
}

.step-indicator.active {
  background: var(--primary);
  color: white;
}

.wizard-form {
  box-sizing: border-box;
}

.form-step {
  box-sizing: border-box;
}

.step-title {
  color: var(--primary-dark);
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 2rem;
  margin-top: 0;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group label {
  display: block;
  font-weight: 600;
  color: var(--primary-dark);
  margin-bottom: 0.5rem;
  font-size: 0.95rem;
}

.form-control {
  width: 100%;
  padding: 1.1rem 1.5rem;
  border-radius: 12px;
  border: 1px solid rgba(0, 0, 0, 0.08);
  background: #f8fafc;
  font-size: 1rem;
  outline: none;
  transition: border-color 0.3s;
  box-sizing: border-box;
  font-family: inherit;
}

.form-control:focus {
  border-color: var(--primary);
  background: white;
}

select.form-control {
  appearance: none;
  background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2364748b' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 1.5rem center;
  background-size: 1.2rem;
}

.mt-large {
  margin-top: 1.5rem;
}

.form-actions-right {
  text-align: right;
  margin-top: 2.5rem;
}

.form-actions-split {
  display: flex;
  justify-content: space-between;
  margin-top: 2.5rem;
}

.btn-back {
  background: transparent;
  color: var(--primary);
  border: 2px solid var(--primary);
  cursor: pointer;
  padding: 1rem 2rem;
  border-radius: 99px;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 1rem;
  transition: var(--transition);
}

.btn-back:hover {
  background: var(--primary);
  color: white;
  transform: translateY(-2px);
}

.btn-arrow-left {
  width: 18px;
  height: 18px;
}

.btn-arrow {
  width: 18px;
  height: 18px;
  vertical-align: middle;
}

.btn-submit {
  background: var(--primary-dark) !important;
}

.btn-submit:hover {
  background: var(--primary) !important;
}

/* Checkbox alignment */
.checkbox-container {
  background: #f8fafc;
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-radius: 12px;
  padding: 1.2rem;
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  cursor: pointer;
  box-sizing: border-box;
}

.checkbox-input {
  accent-color: var(--primary);
  width: 18px;
  height: 18px;
  margin-top: 3px;
  flex-shrink: 0;
}

.checkbox-text {
  font-weight: 400;
  color: var(--gray);
  font-size: 0.9rem;
  line-height: 1.5;
}

@media (max-width: 768px) {
  .form-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
}
</style>

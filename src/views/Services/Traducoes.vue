<script setup>
import { ref, computed, onMounted } from 'vue'
import { Clock, CalendarCheck, Check, UploadCloud, Quote, ArrowLeft, ArrowRight } from '@lucide/vue'

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
  titulo_documento: '',
  idioma_original: 'Português',
  idioma_destino: 'Inglês',
  observacoes: ''
})

const fileName = ref('')
const fileInput = ref(null)

function triggerFileInput() {
  fileInput.value.click()
}

function handleFileChange(event) {
  const files = event.target.files
  if (files.length > 0) {
    fileName.value = files[0].name
  }
}

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
  return formData.value.titulo_documento.trim() !== ''
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
      titulo_documento: '',
      idioma_original: 'Português',
      idioma_destino: 'Inglês',
      observacoes: ''
    }
    fileName.value = ''
    step.value = 1
  }
}
</script>

<template>
  <div class="traducoes-view">
    <!-- Hero -->
    <section class="mesh-bg hero-section">
      <div class="container reveal active hero-content">
        <span class="hero-tag">TRADUÇÃO TÉCNICA E CIENTÍFICA</span>
        <h1 class="hero-title">Traduções Profissionais para<br><span class="gradient-text">Documentos Científicos</span></h1>
        <p class="hero-desc">
          Artigos, papers, teses, relatórios e apresentações com precisão terminológica, sigilo e alto padrão acadêmico.
        </p>
        <div class="meta-badges">
          <span class="badge"><Clock class="badge-icon" /> Orçamento em até 24h</span>
          <span class="badge"><CalendarCheck class="badge-icon" /> Prazo típico: 7–14 dias</span>
        </div>
      </div>
    </section>

    <!-- Info & How it Works -->
    <section class="container info-section">
      <div class="info-grid">
        <div class="glass-card reveal benefit-card">
          <h2>Por que escolher nossas traduções?</h2>
          <div class="check-item"><Check class="check-icon" /> Equipe especializada em produção científica</div>
          <div class="check-item"><Check class="check-icon" /> Sigilo absoluto e NDA sempre disponível</div>
          <div class="check-item"><Check class="check-icon" /> Entrega dentro do prazo e total transparência</div>
          <div class="check-item"><Check class="check-icon" /> Revisão técnica incluída</div>
        </div>

        <div class="reveal steps-container">
          <h2>Como Funciona</h2>
          <div class="steps-grid">
            <div class="step-box">
              <div class="step-number">1</div>
              <p>Você preenche o formulário abaixo (sem anexar arquivo obrigatório).</p>
            </div>
            <div class="step-box">
              <div class="step-number">2</div>
              <p>Avaliamos e enviamos o orçamento em até 24h úteis.</p>
            </div>
            <div class="step-box">
              <div class="step-number">3</div>
              <p>Após aprovação, solicitamos o arquivo final e iniciamos a tradução.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Wizard Form -->
    <section class="container form-section">
      <div class="glass-card wizard-container reveal">
        <div class="wizard-header">
          <h2>Solicite seu Orçamento</h2>
          <p>Preencha os campos abaixo e entraremos em contato rapidamente.</p>
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

          <!-- STEP 4: Document Info -->
          <div v-if="step === 4" class="form-step">
            <h3>4. Detalhes do Documento</h3>
            
            <div class="input-group">
              <label>Título ou Área do Documento *</label>
              <input v-model="formData.titulo_documento" type="text" placeholder="Ex: Nutrição Animal / Artigo Científico" required class="form-input">
            </div>

            <div class="form-grid">
              <div class="input-group">
                <label>Idioma Original</label>
                <select v-model="formData.idioma_original" class="form-input">
                  <option>Português</option>
                  <option>Inglês</option>
                  <option>Espanhol</option>
                  <option>Francês</option>
                </select>
              </div>
              <div class="input-group">
                <label>Traduzir para</label>
                <select v-model="formData.idioma_destino" class="form-input">
                  <option>Inglês</option>
                  <option>Português</option>
                  <option>Espanhol</option>
                  <option>Francês</option>
                </select>
              </div>
            </div>

            <div class="input-group">
              <label>Anexar Documento (Opcional)</label>
              <div 
                class="upload-box" 
                @click="triggerFileInput"
              >
                <UploadCloud class="upload-icon" />
                <p v-if="!fileName" class="upload-placeholder">Clique para escolher o arquivo (.pdf, .doc, .docx)</p>
                <p v-else class="upload-filename">📁 {{ fileName }}</p>
                <input 
                  ref="fileInput" 
                  type="file" 
                  accept=".pdf,.doc,.docx" 
                  style="display: none;" 
                  @change="handleFileChange"
                >
              </div>
            </div>

            <div class="input-group">
              <label>Observações</label>
              <textarea v-model="formData.observacoes" rows="3" placeholder="Informações adicionais..." class="form-input textarea-input"></textarea>
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

    <!-- Testimonials -->
    <section class="testimonials-section">
      <div class="container text-center reveal">
        <span class="testimonials-tag">FEEDBACK</span>
        <h2 class="testimonials-title">O que nossos clientes dizem</h2>
        
        <div class="testimonials-grid">
          <div class="glass-card testimonial-card">
            <Quote class="quote-icon" />
            <p class="testimonial-text">
              "Utilizo o serviço de revisão de inglês da Change Skills Idiomas há alguns anos e reconheço a excelência do trabalho realizado. As revisões elevam significativamente a qualidade textual dos nossos manuscritos. Sou muito grata pelo cuidado, profissionalismo e consistência do serviço."
            </p>
            <div class="testimonial-author">
              <strong>Dra. Aline Pompermaier</strong>
              <span>Professora e Pesquisadora Universitária</span>
            </div>
          </div>

          <div class="glass-card testimonial-card">
            <Quote class="quote-icon" />
            <p class="testimonial-text">
              "Usei o serviço da Change Skills Idiomas para tradução de documentos para solicitação do visto americano e fiquei muito satisfeita. Atendimento rápido, claro e profissional. As traduções ficaram precisas e de acordo com o exigido no processo oficial! Agradeço muito e super recomendo!"
            </p>
            <div class="testimonial-author">
              <strong>Dra. Tatiana Benedetti</strong>
              <span>Pós-Doc at Oregon State University</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.traducoes-view {
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
  margin-bottom: 3rem;
}

.meta-badges {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
}

.badge {
  background: rgba(0, 71, 255, 0.05);
  color: var(--primary-dark);
  padding: 0.8rem 1.8rem;
  border-radius: 100px;
  font-weight: 600;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.badge-icon {
  width: 18px;
  height: 18px;
  color: var(--primary);
}

.info-section {
  padding: 100px 0 60px 0;
}

.info-grid {
  display: grid;
  grid-template-columns: 1fr 1.5fr;
  gap: 3rem;
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
  margin-bottom: 2rem;
  font-weight: 800;
}

.check-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  font-size: 1.1rem;
  color: var(--gray);
  line-height: 1.6;
  margin-bottom: 1.2rem;
}

.check-icon {
  color: var(--primary);
  flex-shrink: 0;
  margin-top: 3px;
  width: 20px;
  height: 20px;
}

.steps-container h2 {
  font-size: 2.2rem;
  color: var(--primary-dark);
  margin-bottom: 2rem;
  text-align: center;
  font-weight: 800;
}

.steps-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.step-box {
  background: white;
  padding: 2.5rem 1.5rem;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
  text-align: center;
  border: 1px solid rgba(0, 0, 0, 0.02);
}

.step-number {
  width: 45px;
  height: 45px;
  background: var(--primary-dark);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
  font-weight: 800;
  margin: 0 auto 1.5rem auto;
}

.step-box p {
  color: var(--gray);
  font-size: 1rem;
  line-height: 1.5;
  margin: 0;
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

.upload-box {
  border: 2px dashed rgba(0, 0, 0, 0.1);
  border-radius: 12px;
  padding: 2rem;
  text-align: center;
  background: #f8fafc;
  cursor: pointer;
  transition: border-color 0.3s, background-color 0.3s;
}

.upload-box:hover {
  border-color: var(--primary);
  background: rgba(0, 71, 255, 0.01);
}

.upload-icon {
  color: var(--primary);
  width: 36px;
  height: 36px;
  margin-bottom: 0.8rem;
}

.upload-placeholder {
  color: var(--gray);
  font-size: 0.95rem;
  margin: 0;
}

.upload-filename {
  color: var(--primary-dark);
  font-weight: 600;
  font-size: 1rem;
  margin: 0;
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
  background: #eee;
  color: var(--gray);
}

.btn-back:hover {
  background: #ddd;
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

.testimonials-section {
  background: linear-gradient(to bottom, white 0%, #f9fafb 100%);
  padding: 120px 0;
  border-top: 1px solid rgba(0, 0, 0, 0.02);
}

.testimonials-tag {
  color: var(--primary);
  font-weight: 800;
  letter-spacing: 0.2em;
  font-size: 0.9rem;
  text-transform: uppercase;
  display: inline-block;
  margin-bottom: 1rem;
}

.testimonials-title {
  margin-top: 0;
  margin-bottom: 5rem;
  color: var(--primary-dark);
  font-size: 2.8rem;
  font-weight: 800;
}

.testimonials-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  max-width: 1100px;
  margin: 0 auto;
}

.testimonial-card {
  background: white;
  padding: 3.5rem;
  border-radius: 30px;
}

.quote-icon {
  color: var(--primary);
  width: 40px;
  height: 40px;
  margin-bottom: 2rem;
}

.testimonial-text {
  font-size: 1.15rem;
  line-height: 1.8;
  margin-bottom: 2.5rem;
  color: var(--gray);
}

.testimonial-author strong {
  display: block;
  font-size: 1.25rem;
  color: var(--primary-dark);
  font-weight: 700;
  margin-bottom: 0.3rem;
}

.testimonial-author span {
  color: var(--primary);
  font-size: 0.95rem;
  font-weight: 600;
}

@media (max-width: 992px) {
  .info-grid {
    grid-template-columns: 1fr;
  }
  .steps-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
    max-width: 400px;
    margin: 0 auto;
  }
  .testimonials-grid {
    grid-template-columns: 1fr;
    max-width: 600px;
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

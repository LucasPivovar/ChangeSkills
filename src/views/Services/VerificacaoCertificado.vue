<script setup>
import { ref } from 'vue'

const code = ref('')
const verified = ref(false)
const showResult = ref(false)

function verifyCertificate() {
  if (code.value.trim()) {
    showResult.value = true
    verified.value = true
  }
}
</script>

<template>
  <div class="verificacao-view">
    <!-- Hero -->
    <section class="mesh-bg hero-section">
      <div class="container active hero-content">
        <span class="hero-tag">SEGURANÇA E AUTENTICIDADE</span>
        <h1 class="hero-title">Verificação de Certificados</h1>
        <p class="hero-desc">
          Valide a autenticidade dos certificados emitidos pela Change Skills Idiomas.
        </p>
      </div>
    </section>

    <!-- Verification Area -->
    <section class="container content-section">
      <div class="glass-card validator-container">
        <h2>Validação de Certificado</h2>
        <p class="validator-desc">Insira o código do seu certificado abaixo para verificar sua autenticidade.</p>
        
        <form @submit.prevent="verifyCertificate" class="validator-form">
          <input 
            v-model="code"
            type="text" 
            placeholder="CS-XXXX-XXXX" 
            required 
            class="validator-input"
          >
          <button type="submit" class="btn-verify">Verificar Certificado</button>
        </form>

        <transition name="fade">
          <div v-if="showResult" class="result-box">
            <div v-if="verified" class="result-success">
              <span class="success-icon">✅</span>
              <div class="success-text">
                <h4>Certificado Válido!</h4>
                <p>Emitido para o aluno conforme os registros oficiais.</p>
              </div>
            </div>
          </div>
        </transition>
      </div>
    </section>
  </div>
</template>

<style scoped>
.verificacao-view {
  width: 100%;
}

.hero-section {
  padding: 240px 0 100px 0;
  text-align: center;
  background: linear-gradient(135deg, #f5f7ff 0%, #eef2ff 100%);
  position: relative;
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

.hero-desc {
  font-size: 1.3rem;
  color: var(--gray);
  max-width: 700px;
  margin: 0 auto;
  font-weight: 400;
  line-height: 1.6;
}

.content-section {
  padding: 60px 0 120px 0;
}

.glass-card {
  background: white;
  border-radius: 40px;
  padding: 4rem;
  box-shadow: var(--shadow-premium);
  border: 1px solid rgba(0, 0, 0, 0.03);
  text-align: center;
}

.validator-container {
  max-width: 600px;
  margin: 0 auto;
}

.validator-container h2 {
  font-size: 2.2rem;
  color: var(--primary-dark);
  margin-bottom: 1rem;
  font-weight: 800;
}

.validator-desc {
  font-size: 1.15rem;
  color: var(--gray);
  margin-bottom: 3rem;
}

.validator-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.validator-input {
  width: 100%;
  padding: 1.2rem 1.5rem;
  border-radius: 15px;
  border: 1px solid rgba(0, 0, 0, 0.08);
  background: #f8fafc;
  font-size: 1.25rem;
  text-align: center;
  letter-spacing: 2px;
  outline: none;
  transition: all 0.3s;
  box-sizing: border-box;
}

.validator-input:focus {
  border-color: var(--primary);
  background: white;
}

.btn-verify {
  width: 100%;
  font-size: 1.1rem;
  padding: 1.2rem;
  border-radius: 9999px;
  font-weight: 700;
  border: none;
  cursor: pointer;
  transition: all 0.3s;
  background: var(--primary);
  color: white;
  box-shadow: 0 10px 25px rgba(0, 71, 255, 0.2);
}

.btn-verify:hover {
  background: var(--primary-dark);
  transform: translateY(-2px);
  box-shadow: 0 15px 30px rgba(0, 71, 255, 0.3);
}

.result-box {
  margin-top: 2.5rem;
}

.result-success {
  padding: 1.8rem;
  background: #e6f4ea;
  border-radius: 15px;
  display: flex;
  align-items: center;
  gap: 1.2rem;
  text-align: left;
  border: 1px solid rgba(30, 142, 62, 0.1);
}

.success-icon {
  font-size: 2rem;
  flex-shrink: 0;
}

.success-text h4 {
  font-size: 1.2rem;
  color: #137333;
  margin: 0 0 0.3rem 0;
  font-weight: 700;
}

.success-text p {
  font-size: 0.95rem;
  color: #137333;
  margin: 0;
  opacity: 0.9;
}

/* Transitions */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 3rem;
  }
  .hero-desc {
    font-size: 1.1rem;
  }
  .glass-card {
    padding: 2.5rem 1.5rem;
  }
}
</style>

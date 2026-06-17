<script setup>
import { onMounted } from 'vue'
import { Calendar, Award, Clock, ArrowRight } from '@lucide/vue'

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
  <div class="agendamento-view">
    <!-- Hero Section -->
    <section class="page-hero">
      <div class="container text-center reveal active hero-content">
        <span class="hero-tag">PROFICIENCY TEST</span>
        <h1 class="hero-title">Agendamento de <br><span class="gradient-text">Conversa.</span></h1>
        <p class="hero-desc">Descubra seu ponto de partida para a fluência total com nossa avaliação comunicativa.</p>
      </div>
    </section>

    <!-- Content Section -->
    <section class="container content-section">
      <div class="scheduler-card reveal">
        <div class="card-left">
          <h2>Agende sua conversa</h2>
          <p>Nossa entrevista de nivelamento é um bate-papo descontraído de 15 a 20 minutos com um de nossos professores para identificar sua fluência prática e indicar a melhor turma/modalidade para você.</p>
          
          <div class="features-list">
            <div class="feature-item">
              <Clock class="feature-icon" />
              <div>
                <h4>Rápido & Dinâmico</h4>
                <p>Apenas 15 a 20 minutos de conversa oral online.</p>
              </div>
            </div>
            <div class="feature-item">
              <Award class="feature-icon" />
              <div>
                <h4>Avaliação Precisa</h4>
                <p>Alinhado ao Quadro Europeu Comum de Referência (CEFR).</p>
              </div>
            </div>
          </div>
        </div>
        
        <div class="card-right">
          <div class="calendar-box">
            <Calendar class="calendar-icon" />
            <p>Escolha a melhor data e horário para agendar sua conversa diretamente conosco via WhatsApp.</p>
            <a href="https://wa.me/555481223965?text=Olá,%20gostaria%20de%20agendar%20uma%20conversa!" target="_blank" class="btn-schedule">
              Agendar via WhatsApp <ArrowRight class="btn-icon" />
            </a>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.agendamento-view {
  width: 100%;
}

.page-hero {
  padding: 240px 0 100px 0;
  background: linear-gradient(135deg, #f5f7ff 0%, #eef2ff 100%);
  text-align: center;
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
  max-width: 700px;
  margin: 0 auto;
  font-weight: 400;
  line-height: 1.6;
}

.content-section {
  padding: 100px 0;
}

.scheduler-card {
  max-width: 1000px;
  margin: 0 auto;
  background: white;
  border-radius: 40px;
  box-shadow: var(--shadow-premium);
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  overflow: hidden;
  border: 1px solid rgba(0, 0, 0, 0.03);
}

.card-left {
  padding: 5rem 4rem;
  text-align: left;
}

.card-left h2 {
  font-size: 2.2rem;
  color: var(--primary-dark);
  margin-bottom: 2rem;
  font-weight: 800;
}

.card-left p {
  font-size: 1.1rem;
  color: var(--gray);
  line-height: 1.7;
  margin-bottom: 3rem;
}

.features-list {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.feature-item {
  display: flex;
  gap: 1.5rem;
  align-items: flex-start;
}

.feature-icon {
  width: 28px;
  height: 28px;
  color: var(--primary);
  flex-shrink: 0;
  margin-top: 3px;
}

.feature-item h4 {
  font-size: 1.2rem;
  color: var(--primary-dark);
  margin-bottom: 0.5rem;
  font-weight: 700;
}

.feature-item p {
  font-size: 0.95rem;
  color: var(--gray);
  margin: 0;
  line-height: 1.5;
}

.card-right {
  background: linear-gradient(135deg, #001233 0%, #002255 100%);
  padding: 5rem 4rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.calendar-box {
  border: 2px dashed rgba(255, 255, 255, 0.2);
  border-radius: 30px;
  padding: 4rem 2.5rem;
  text-align: center;
  color: white;
  width: 100%;
}

.calendar-icon {
  width: 48px;
  height: 48px;
  color: var(--accent);
  margin-bottom: 2rem;
}

.calendar-box p {
  font-size: 1.05rem;
  line-height: 1.6;
  opacity: 0.85;
  margin-bottom: 2.5rem;
}

.btn-schedule {
  background: var(--primary);
  color: white;
  text-decoration: none;
  padding: 1.2rem 2rem;
  border-radius: 15px;
  font-weight: 700;
  font-size: 1.05rem;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  transition: var(--transition);
  box-shadow: 0 10px 25px rgba(0, 71, 255, 0.3);
}

.btn-schedule:hover {
  background: white;
  color: var(--primary-dark);
  transform: translateY(-3px);
  box-shadow: 0 15px 30px rgba(255, 255, 255, 0.2);
}

.btn-icon {
  width: 18px;
  height: 18px;
}

@media (max-width: 992px) {
  .scheduler-card {
    grid-template-columns: 1fr;
  }
  .card-left, .card-right {
    padding: 4rem 2.5rem;
  }
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 3rem;
  }
  .hero-desc {
    font-size: 1.1rem;
  }
}
</style>

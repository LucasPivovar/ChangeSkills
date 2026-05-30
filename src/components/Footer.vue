<script setup>
import { RouterLink } from 'vue-router'
import { t } from '@/i18n'

const currentYear = new Date().getFullYear()
</script>

<template>
  <footer class="global-footer">
    <div class="container footer-container">
      <!-- Grid layout -->
      <div class="footer-grid">
        <!-- Brand identity -->
        <div class="footer-brand">
          <img src="/assets/img/logo-change.png?v=2" alt="Logo Change Skills" class="footer-logo">
          <p class="footer-brand-text">{{ t('footerBrand') }}</p>
        </div>
        
        <!-- Institutional pathways -->
        <div>
          <h4 class="footer-heading">{{ t('footerInstitucional') }}</h4>
          <ul class="footer-links">
            <li><RouterLink to="/nossa-escola">{{ t('school') }}</RouterLink></li>
            <li><RouterLink to="/nossa-escola#professores">{{ t('footerTeachers') }}</RouterLink></li>
            <li><RouterLink to="/services/solicitacao-certificado">{{ t('footerCertificados') }}</RouterLink></li>
            <li><RouterLink to="/services/verificacao-certificado">{{ t('footerValidation') }}</RouterLink></li>
          </ul>
        </div>
        
        <!-- Courses routes -->
        <div>
          <h4 class="footer-heading">{{ t('footerCursos') }}</h4>
          <ul class="footer-links">
            <li><RouterLink to="/cursos/ingles">{{ t('ingles', 'home') }}</RouterLink></li>
            <li><RouterLink to="/cursos/espanhol">{{ t('espanhol', 'home') }}</RouterLink></li>
            <li><RouterLink to="/cursos/frances">{{ t('frances', 'home') }}</RouterLink></li>
            <li><RouterLink to="/cursos/portugues">{{ t('portugues', 'home') }}</RouterLink></li>
          </ul>
        </div>
        
        <!-- Services redirects -->
        <div>
          <h4 class="footer-heading">{{ t('footerServicos') }}</h4>
          <ul class="footer-links">
            <li><RouterLink to="/services/traducoes">{{ t('footerTraducoes') }}</RouterLink></li>
            <li><RouterLink to="/services/aulas-conversacao">{{ t('servicoCardTitle2', 'home') }}</RouterLink></li>
          </ul>
          
          <div class="footer-socials">
            <a href="https://www.instagram.com/change.skills/" target="_blank" rel="noopener" aria-label="Instagram">
              <svg class="social-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
              </svg>
            </a>
            <a href="#" aria-label="Facebook">
              <svg class="social-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>
              </svg>
            </a>
            <a href="#" aria-label="LinkedIn">
              <svg class="social-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
                <rect x="2" y="9" width="4" height="12"></rect>
                <circle cx="4" cy="4" r="2"></circle>
              </svg>
            </a>
          </div>
        </div>
      </div>
      
      <!-- Footer bottom details -->
      <div class="footer-bottom">
        <span>{{ currentYear }} © {{ t('footerRights') }}</span>
        <span>{{ t('footerDev') }} <strong>Page Facilitado</strong></span>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.global-footer {
  padding: 120px 0 60px 0;
  background: var(--primary-dark);
  color: white;
}

.footer-container {
  display: flex;
  flex-direction: column;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr 1fr;
  gap: 4rem;
  margin-bottom: 4rem;
}

.footer-brand {
  display: flex;
  flex-direction: column;
}

.footer-logo {
  height: 50px;
  filter: brightness(0) invert(1);
  margin-bottom: 2.5rem;
  align-self: flex-start;
}

.footer-brand-text {
  color: #FFFFFF;
  font-size: 1.1rem;
  line-height: 1.6;
  max-width: 300px;
  margin: 0;
}

.footer-heading {
  color: var(--accent);
  margin-bottom: 2.5rem;
  font-size: 1.2rem;
  font-weight: 700;
  margin-top: 0;
}

.footer-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  margin: 0;
  padding: 0;
}

.footer-links a {
  color: #FFFFFF;
  text-decoration: none;
  transition: color 0.3s;
  font-size: 1.05rem;
  font-weight: 500;
  display: inline-block;
}

.footer-links a:hover {
  color: var(--accent);
  opacity: 1;
}

.footer-socials {
  display: flex;
  gap: 1.5rem;
  align-items: center;
  margin-top: 2rem;
}

.footer-socials a {
  color: white;
  text-decoration: none;
  transition: all 0.3s;
  opacity: 0.8;
  display: flex;
  align-items: center;
  justify-content: center;
}

.footer-socials a:hover {
  color: var(--accent);
  opacity: 1;
  transform: translateY(-3px);
}

.social-icon {
  width: 24px;
  height: 24px;
}

.footer-bottom {
  text-align: center;
  opacity: 0.3;
  padding-top: 4rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 0.9rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}

@media (max-width: 992px) {
  .footer-grid {
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
  }
}

@media (max-width: 600px) {
  .footer-grid {
    grid-template-columns: 1fr;
    gap: 2.5rem;
  }
  
  .footer-bottom {
    flex-direction: column;
    text-align: center;
    gap: 0.5rem;
  }
}
</style>

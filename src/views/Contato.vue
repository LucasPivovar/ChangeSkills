<script setup>
import { onMounted, ref } from 'vue'
import { Send, Phone, Mail } from '@lucide/vue'
import { t } from '@/i18n'

const name = ref('')
const email = ref('')
const message = ref('')

function handleSubmit() {
  const successMsg = t('alertSuccess', 'contact').replace('{name}', name.value)
  alert(successMsg)
  name.value = ''
  email.value = ''
  message.value = ''
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
  <div class="contato-view">
    <!-- Contact Hero -->
    <section class="contact-hero">
      <div class="container hero-content">
        <span class="hero-tag">{{ t('heroTag', 'contact') }}</span>
        <h1 class="hero-title">{{ t('heroTitle', 'contact') }} <span class="highlight">{{ t('heroHighlight', 'contact') }}</span></h1>
        <p class="hero-desc">
          {{ t('heroDesc', 'contact') }}
        </p>
      </div>
    </section>

    <!-- Main Grid Section -->
    <section class="contact-main">
      <div class="container">
        <div class="contact-grid">
          <!-- Message Form Card -->
          <div class="contact-card reveal active">
            <h2 class="card-title">{{ t('cardTitle', 'contact') }}</h2>
            
            <form @submit.prevent="handleSubmit" class="message-form">
              <div class="form-group">
                <label for="name">{{ t('nameLabel', 'contact') }}</label>
                <input 
                  id="name" 
                  v-model="name"
                  type="text" 
                  class="form-control" 
                  :placeholder="t('namePlaceholder', 'contact')" 
                  required
                >
              </div>
              
              <div class="form-group">
                <label for="email">{{ t('emailLabel', 'contact') }}</label>
                <input 
                  id="email" 
                  v-model="email"
                  type="email" 
                  class="form-control" 
                  :placeholder="t('emailPlaceholder', 'contact')" 
                  required
                >
              </div>
              
              <div class="form-group">
                <label for="message">{{ t('messageLabel', 'contact') }}</label>
                <textarea 
                  id="message" 
                  v-model="message"
                  class="form-control" 
                  rows="6" 
                  :placeholder="t('messagePlaceholder', 'contact')" 
                  required
                ></textarea>
              </div>
              
              <div class="form-action">
                <button type="submit" class="btn-send">
                  {{ t('btnSend', 'contact') }} <Send class="btn-send-icon" />
                </button>
              </div>
            </form>
          </div>

          <!-- Channel Info Card -->
          <div class="info-card reveal active">
            <h3 class="info-title">{{ t('infoTitle', 'contact') }}</h3>
            
            <div class="info-item">
              <div class="info-icon"><Phone class="channel-icon" /></div>
              <div class="info-text">
                <h4>{{ t('channelPhone', 'contact') }}</h4>
                <p>+55 (54) 8122-3965</p>
              </div>
            </div>

            <div class="info-item">
              <div class="info-icon"><Mail class="channel-icon" /></div>
              <div class="info-text">
                <h4>{{ t('channelEmail', 'contact') }}</h4>
                <p>contato@changeskills.com.br</p>
              </div>
            </div>

            <div class="info-socials">
              <h4>{{ t('infoSocials', 'contact') }}</h4>
              <div class="social-badges">
                <a href="https://wa.me/555481223965" target="_blank" rel="noopener" class="badge-wa" aria-label="WhatsApp">
                  <svg viewBox="0 0 24 24" class="svg-social"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg>
                </a>
                <a href="https://www.instagram.com/change.skills/" target="_blank" rel="noopener" class="badge-insta" aria-label="Instagram">
                  <svg viewBox="0 0 24 24" class="svg-social"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm3.98-10.906a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/></svg>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.contato-view {
  width: 100%;
  background: var(--bg-light);
  min-height: 100vh;
}

.contact-hero {
  background: var(--primary-dark);
  padding: 220px 0 120px 0;
  color: white;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.contact-hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: url('/assets/img/image.png') center/cover;
  opacity: 0.15;
  z-index: 0;
}

.hero-content {
  position: relative;
  z-index: 2;
}

.hero-tag {
  color: var(--accent);
  font-weight: 800;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  display: block;
  margin-bottom: 1.5rem;
  font-size: 0.9rem;
}

.hero-title {
  font-size: 5rem;
  font-weight: 800;
  margin-bottom: 2rem;
  margin-top: 0;
}

.hero-title .highlight {
  color: var(--accent);
}

.hero-desc {
  font-size: 1.4rem;
  opacity: 0.8;
  max-width: 700px;
  margin: 0 auto;
  line-height: 1.6;
  font-weight: 300;
}

.contact-main {
  padding-bottom: 120px;
  background: var(--bg-light);
}

.contact-grid {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 4rem;
  margin-top: -80px;
  position: relative;
  z-index: 10;
}

.contact-card {
  background: white;
  padding: 4rem;
  border-radius: 40px;
  box-shadow: 0 30px 60px rgba(0, 0, 0, 0.08);
  border: 1px solid rgba(0, 0, 0, 0.03);
}

.card-title {
  font-size: 2.5rem;
  color: var(--primary-dark);
  margin-bottom: 2.5rem;
  margin-top: 0;
  font-weight: 800;
}

.message-form {
  display: flex;
  flex-direction: column;
  gap: 1.8rem;
  text-align: left;
}

.form-group label {
  display: block;
  font-weight: 600;
  color: var(--primary-dark);
  margin-bottom: 0.8rem;
  font-size: 0.95rem;
}

.form-control {
  width: 100%;
  padding: 1.2rem;
  border-radius: 15px;
  border: 1px solid #eee;
  background: #fafafa;
  font-family: inherit;
  font-size: 1rem;
  transition: var(--transition);
  box-sizing: border-box;
}

.form-control:focus {
  outline: none;
  border-color: var(--primary);
  background: white;
  box-shadow: 0 10px 20px rgba(0, 58, 112, 0.05);
}

textarea.form-control {
  resize: vertical;
}

.form-action {
  text-align: right;
}

.btn-send {
  background: var(--primary-dark);
  color: white;
  padding: 1.2rem 3rem;
  border-radius: 100px;
  border: none;
  font-weight: 700;
  font-size: 1.1rem;
  cursor: pointer;
  transition: var(--transition);
  display: inline-flex;
  align-items: center;
  gap: 1rem;
}

.btn-send:hover {
  background: var(--primary);
  transform: translateY(-3px);
  box-shadow: 0 15px 30px rgba(0, 58, 112, 0.2);
}

.btn-send-icon {
  width: 18px;
  height: 18px;
}

/* Info card channel styling */
.info-card {
  background: white;
  padding: 4rem;
  border-radius: 40px;
  box-shadow: var(--shadow-premium);
  border: 1px solid rgba(0, 0, 0, 0.03);
  height: fit-content;
  display: flex;
  flex-direction: column;
  justify-content: center;
  min-height: 100%;
  box-sizing: border-box;
  text-align: left;
}

.info-title {
  font-size: 1.8rem;
  color: var(--primary-dark);
  margin-bottom: 3rem;
  margin-top: 0;
  font-weight: 700;
}

.info-item {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 2.5rem;
  align-items: flex-start;
}

.info-icon {
  width: 50px;
  height: 50px;
  background: rgba(0, 58, 112, 0.05);
  border-radius: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--primary);
  flex-shrink: 0;
}

.channel-icon {
  width: 24px;
  height: 24px;
}

.info-text h4 {
  font-size: 1.1rem;
  color: var(--primary-dark);
  margin-bottom: 0.3rem;
  margin-top: 0;
  font-weight: 700;
}

.info-text p {
  color: var(--gray);
  line-height: 1.5;
  margin: 0;
  font-size: 1.05rem;
}

.info-socials {
  margin-top: 3.5rem;
  padding-top: 2rem;
  border-top: 1px solid #eee;
}

.info-socials h4 {
  font-size: 1rem;
  color: var(--primary-dark);
  margin-bottom: 1.5rem;
  margin-top: 0;
  font-weight: 700;
}

.social-badges {
  display: flex;
  gap: 1.2rem;
}

.social-badges a {
  width: 40px;
  height: 40px;
  color: white;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: var(--transition);
}

.badge-wa {
  background: #25D366;
}

.badge-wa:hover {
  background: #1ed760;
  transform: translateY(-3px) scale(1.05);
}

.badge-insta {
  background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
}

.badge-insta:hover {
  transform: translateY(-3px) scale(1.05);
}

.svg-social {
  width: 20px;
  height: 20px;
  fill: currentColor;
}

@media (max-width: 992px) {
  .contact-grid {
    grid-template-columns: 1fr;
    margin-top: 40px;
  }
  .contact-card {
    padding: 2.5rem;
  }
  .info-card {
    padding: 3rem 2.5rem;
  }
}
</style>

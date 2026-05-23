import re

file_path = r"c:\Users\patov\Documents\Projects\ChangeSkills\ChangeSkills\contato.html"

new_form = '''
                    <!-- Form -->
                    <div class="contact-card reveal active" style="background: white; border-radius: 40px; box-shadow: 0 30px 60px rgba(0,0,0,0.08); padding: 4rem; border: 1px solid rgba(0,0,0,0.03); position: relative;">
                        <h2 style="font-size: 2.5rem; color: var(--primary-dark); margin-bottom: 2.5rem;">Envie uma mensagem</h2>
                        
                        <!-- Progress Bar -->
                        <div style="display: flex; justify-content: space-between; position: relative; margin-bottom: 3rem;">
                            <div style="position: absolute; top: 50%; left: 0; width: 100%; height: 2px; background: #e2e8f0; z-index: 1; transform: translateY(-50%);"></div>
                            <div class="progress-line" style="position: absolute; top: 50%; left: 0; height: 2px; background: var(--primary); z-index: 2; transform: translateY(-50%); transition: width 0.4s; width: 0%;"></div>
                            
                            <div class="step-indicator" id="ind-1" style="width: 35px; height: 35px; background: var(--primary); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; z-index: 3; position: relative; transition: all 0.4s;">1</div>
                            <div class="step-indicator" id="ind-2" style="width: 35px; height: 35px; background: #e2e8f0; color: var(--gray); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; z-index: 3; position: relative; transition: all 0.4s;">2</div>
                            <div class="step-indicator" id="ind-3" style="width: 35px; height: 35px; background: #e2e8f0; color: var(--gray); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; z-index: 3; position: relative; transition: all 0.4s;">3</div>
                            <div class="step-indicator" id="ind-4" style="width: 35px; height: 35px; background: #e2e8f0; color: var(--gray); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; z-index: 3; position: relative; transition: all 0.4s;">4</div>
                        </div>

                        <form id="wizard-form" style="display: flex; flex-direction: column; gap: 1.2rem;" onsubmit="event.preventDefault(); alert('Mensagem enviada com sucesso!');">
                            
                            <!-- ETAPA 1: Pessoais -->
                            <div class="form-step" id="step-1" style="display: block;">
                                <h3 style="color: var(--primary-dark); font-size: 1.5rem; font-weight: 700; margin-bottom: 1.5rem; text-align: left;">1. Seus Dados</h3>
                                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
                                    <div class="form-group" style="margin-bottom: 0;">
                                        <label>Nome *</label>
                                        <input type="text" class="form-control" placeholder="Seu nome" required>
                                    </div>
                                    <div class="form-group" style="margin-bottom: 0;">
                                        <label>Sobrenome</label>
                                        <input type="text" class="form-control" placeholder="Sobrenome">
                                    </div>
                                </div>
                                <div style="text-align: right; margin-top: 2rem;">
                                    <button type="button" onclick="nextStep(2)" class="btn-send" style="padding: 1rem 2rem; border-radius: 99px; border: none; background: var(--primary); color: white; cursor: pointer; transition: 0.3s; font-weight: 700;">Próximo <i data-lucide="arrow-right" style="width: 18px; vertical-align: middle;"></i></button>
                                </div>
                            </div>

                            <!-- ETAPA 2: Contato -->
                            <div class="form-step" id="step-2" style="display: none;">
                                <h3 style="color: var(--primary-dark); font-size: 1.5rem; font-weight: 700; margin-bottom: 1.5rem; text-align: left;">2. Dados de Contato</h3>
                                <div class="form-group" style="margin-bottom: 1.2rem;">
                                    <label>E-mail *</label>
                                    <input type="email" class="form-control" placeholder="exemplo@email.com" required>
                                </div>
                                <div class="form-group" style="margin-bottom: 1.2rem;">
                                    <label>Telefone / WhatsApp *</label>
                                    <input type="tel" class="form-control" placeholder="(00) 00000-0000" required>
                                </div>
                                <div style="display: flex; justify-content: space-between; margin-top: 2rem;">
                                    <button type="button" onclick="nextStep(1)" style="background: transparent; color: var(--primary); border: 2px solid var(--primary); cursor: pointer; padding: 1rem 2rem; border-radius: 99px; font-weight: 700; display: inline-flex; align-items: center; gap: 8px;"><i data-lucide="arrow-left" style="width: 18px;"></i> Voltar</button>
                                    <button type="button" onclick="nextStep(3)" class="btn-send" style="padding: 1rem 2rem; border-radius: 99px; border: none; background: var(--primary); color: white; cursor: pointer; transition: 0.3s; font-weight: 700;">Próximo <i data-lucide="arrow-right" style="width: 18px; vertical-align: middle;"></i></button>
                                </div>
                            </div>

                            <!-- ETAPA 3: Preferência -->
                            <div class="form-step" id="step-3" style="display: none;">
                                <h3 style="color: var(--primary-dark); font-size: 1.5rem; font-weight: 700; margin-bottom: 1.5rem; text-align: left;">3. Preferência de Contato</h3>
                                <label style="display: block; font-weight: 600; color: var(--primary-dark); margin-bottom: 0.8rem; font-size: 0.95rem;">Como prefere que entremos em contato? *</label>
                                <div style="display: flex; flex-direction: column; gap: 1rem; margin-bottom: 1.5rem;">
                                    <label style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.08); border-radius: 12px; padding: 1rem; display: flex; align-items: center; gap: 1rem; cursor: pointer;">
                                        <input type="radio" name="pref_contato" value="whatsapp" checked style="accent-color: var(--primary); width: 18px; height: 18px;">
                                        <span style="font-weight: 600; color: var(--primary-dark);">💬 Mensagem no WhatsApp</span>
                                    </label>
                                    <label style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.08); border-radius: 12px; padding: 1rem; display: flex; align-items: center; gap: 1rem; cursor: pointer;">
                                        <input type="radio" name="pref_contato" value="email" style="accent-color: var(--primary); width: 18px; height: 18px;">
                                        <span style="font-weight: 600; color: var(--primary-dark);">📧 Enviar E-mail</span>
                                    </label>
                                    <label style="background: #f8fafc; border: 1px solid rgba(0,0,0,0.08); border-radius: 12px; padding: 1rem; display: flex; align-items: center; gap: 1rem; cursor: pointer;">
                                        <input type="radio" name="pref_contato" value="ligacao" style="accent-color: var(--primary); width: 18px; height: 18px;">
                                        <span style="font-weight: 600; color: var(--primary-dark);">📞 Receber Ligação</span>
                                    </label>
                                </div>
                                <div style="display: flex; justify-content: space-between; margin-top: 2rem;">
                                    <button type="button" onclick="nextStep(2)" style="background: transparent; color: var(--primary); border: 2px solid var(--primary); cursor: pointer; padding: 1rem 2rem; border-radius: 99px; font-weight: 700; display: inline-flex; align-items: center; gap: 8px;"><i data-lucide="arrow-left" style="width: 18px;"></i> Voltar</button>
                                    <button type="button" onclick="nextStep(4)" class="btn-send" style="padding: 1rem 2rem; border-radius: 99px; border: none; background: var(--primary); color: white; cursor: pointer; transition: 0.3s; font-weight: 700;">Próximo <i data-lucide="arrow-right" style="width: 18px; vertical-align: middle;"></i></button>
                                </div>
                            </div>

                            <!-- ETAPA 4: Assunto -->
                            <div class="form-step" id="step-4" style="display: none;">
                                <h3 style="color: var(--primary-dark); font-size: 1.5rem; font-weight: 700; margin-bottom: 1.5rem; text-align: left;">4. Assunto e Mensagem</h3>
                                <div class="form-group" style="margin-bottom: 1.2rem;">
                                    <label>Assunto</label>
                                    <select class="form-control" style="appearance: none; -webkit-appearance: none; -moz-appearance: none; background-image: url('data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2224%22 height=%2224%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22%2364748b%22 stroke-width=%222%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22><polyline points=%226 9 12 15 18 9%22></polyline></svg>'); background-repeat: no-repeat; background-position: right 1.5rem center; background-size: 1.2rem;">
                                        <option>Informações sobre Cursos</option>
                                        <option>Aulas de Conversação</option>
                                        <option>Parcerias Corporativas</option>
                                        <option>Suporte ao Aluno</option>
                                        <option>Outros</option>
                                    </select>
                                </div>
                                <div class="form-group" style="margin-bottom: 1.2rem;">
                                    <label>Mensagem</label>
                                    <textarea class="form-control" rows="5" placeholder="Como podemos ajudar?" style="resize: vertical;"></textarea>
                                </div>
                                <div style="display: flex; justify-content: space-between; margin-top: 2rem;">
                                    <button type="button" onclick="nextStep(3)" style="background: transparent; color: var(--primary); border: 2px solid var(--primary); cursor: pointer; padding: 1rem 2rem; border-radius: 99px; font-weight: 700; display: inline-flex; align-items: center; gap: 8px;"><i data-lucide="arrow-left" style="width: 18px;"></i> Voltar</button>
                                    <button type="submit" class="btn-send" style="padding: 1rem 2rem; border-radius: 99px; border: none; background: var(--primary-dark); color: white; cursor: pointer; transition: 0.3s; font-weight: 700;">Enviar Mensagem <i data-lucide="send" style="width: 18px; vertical-align: middle;"></i></button>
                                </div>
                            </div>
                        </form>
                    </div>
'''

script_block = """
    <script>
        function nextStep(step) {
            document.querySelectorAll('.form-step').forEach(el => el.style.display = 'none');
            document.getElementById('step-' + step).style.display = 'block';
            
            document.querySelectorAll('.step-indicator').forEach((el, index) => {
                if (index < step) {
                    el.style.background = 'var(--primary)';
                    el.style.color = 'white';
                } else {
                    el.style.background = '#e2e8f0';
                    el.style.color = 'var(--gray)';
                }
            });
            
            let progress = ((step - 1) / 3) * 100;
            document.querySelector('.progress-line').style.width = progress + '%';
        }
    </script>
"""

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the contact-card section
pattern = re.compile(r'<!-- Form -->\s*<div class="contact-card.*?</div>\s*<!-- Info -->', re.DOTALL)
new_content = pattern.sub(new_form + '\n                    <!-- Info -->', content)

# Inject script block if not present
if "function nextStep(step)" not in new_content:
    new_content = new_content.replace('</body>', script_block + '\n</body>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated contato.html")

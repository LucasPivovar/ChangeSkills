import re

file_path = r"c:\Users\patov\Documents\Projects\ChangeSkills\ChangeSkills\services\traducoes.html"

new_form = '''
                    <!-- Progress Bar -->
                    <div style="display: flex; justify-content: space-between; position: relative; margin-bottom: 3rem;">
                        <div style="position: absolute; top: 50%; left: 0; width: 100%; height: 2px; background: #e2e8f0; z-index: 1; transform: translateY(-50%);"></div>
                        <div class="progress-line" style="position: absolute; top: 50%; left: 0; height: 2px; background: var(--primary); z-index: 2; transform: translateY(-50%); transition: width 0.4s; width: 0%;"></div>
                        
                        <div class="step-indicator" id="ind-1" style="width: 35px; height: 35px; background: var(--primary); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; z-index: 3; position: relative; transition: all 0.4s;">1</div>
                        <div class="step-indicator" id="ind-2" style="width: 35px; height: 35px; background: #e2e8f0; color: var(--gray); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; z-index: 3; position: relative; transition: all 0.4s;">2</div>
                        <div class="step-indicator" id="ind-3" style="width: 35px; height: 35px; background: #e2e8f0; color: var(--gray); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; z-index: 3; position: relative; transition: all 0.4s;">3</div>
                        <div class="step-indicator" id="ind-4" style="width: 35px; height: 35px; background: #e2e8f0; color: var(--gray); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; z-index: 3; position: relative; transition: all 0.4s;">4</div>
                    </div>

                    <form id="wizard-form" style="display: flex; flex-direction: column; gap: 1.2rem;" onsubmit="event.preventDefault(); alert('Solicitação enviada com sucesso!');">
                        
                        <!-- ETAPA 1: Pessoais -->
                        <div class="form-step" id="step-1" style="display: block;">
                            <h3 style="color: var(--primary-dark); font-size: 1.5rem; font-weight: 700; margin-bottom: 1.5rem; text-align: left;">1. Seus Dados</h3>
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
                                <div>
                                    <label style="display: block; font-weight: 600; color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 0.95rem;">Nome *</label>
                                    <input type="text" placeholder="Nome" required style="width: 100%; padding: 1.1rem 1.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.08); background: #f8fafc; font-size: 1rem; outline: none; transition: border-color 0.3s;">
                                </div>
                                <div>
                                    <label style="display: block; font-weight: 600; color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 0.95rem;">Sobrenome</label>
                                    <input type="text" placeholder="Sobrenome" style="width: 100%; padding: 1.1rem 1.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.08); background: #f8fafc; font-size: 1rem; outline: none; transition: border-color 0.3s;">
                                </div>
                            </div>
                            <div style="text-align: right; margin-top: 2rem;">
                                <button type="button" onclick="nextStep(2)" class="btn-vip" style="border: none; cursor: pointer; padding: 1rem 2rem; border-radius: 99px; font-weight: 700; background: var(--primary); color: white; transition: 0.3s;">Próximo <i data-lucide="arrow-right" style="width: 18px; vertical-align: middle;"></i></button>
                            </div>
                        </div>

                        <!-- ETAPA 2: Contato -->
                        <div class="form-step" id="step-2" style="display: none;">
                            <h3 style="color: var(--primary-dark); font-size: 1.5rem; font-weight: 700; margin-bottom: 1.5rem; text-align: left;">2. Dados de Contato</h3>
                            <div style="margin-bottom: 1.2rem;">
                                <label style="display: block; font-weight: 600; color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 0.95rem;">E-mail *</label>
                                <input type="email" placeholder="exemplo@email.com" required style="width: 100%; padding: 1.1rem 1.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.08); background: #f8fafc; font-size: 1rem; outline: none; transition: border-color 0.3s;">
                            </div>
                            <div style="margin-bottom: 1.2rem;">
                                <label style="display: block; font-weight: 600; color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 0.95rem;">Telefone / WhatsApp *</label>
                                <input type="tel" placeholder="(00) 00000-0000" required style="width: 100%; padding: 1.1rem 1.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.08); background: #f8fafc; font-size: 1rem; outline: none; transition: border-color 0.3s;">
                            </div>
                            <div style="display: flex; justify-content: space-between; margin-top: 2rem;">
                                <button type="button" onclick="nextStep(1)" style="background: transparent; color: var(--primary); border: 2px solid var(--primary); cursor: pointer; padding: 1rem 2rem; border-radius: 99px; font-weight: 700; display: inline-flex; align-items: center; gap: 8px;"><i data-lucide="arrow-left" style="width: 18px;"></i> Voltar</button>
                                <button type="button" onclick="nextStep(3)" class="btn-vip" style="background: var(--primary); color: white; border: none; cursor: pointer; padding: 1rem 2rem; border-radius: 99px; font-weight: 700;">Próximo <i data-lucide="arrow-right" style="width: 18px; vertical-align: middle;"></i></button>
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
                                <button type="button" onclick="nextStep(4)" class="btn-vip" style="background: var(--primary); color: white; border: none; cursor: pointer; padding: 1rem 2rem; border-radius: 99px; font-weight: 700;">Próximo <i data-lucide="arrow-right" style="width: 18px; vertical-align: middle;"></i></button>
                            </div>
                        </div>

                        <!-- ETAPA 4: Documento -->
                        <div class="form-step" id="step-4" style="display: none;">
                            <h3 style="color: var(--primary-dark); font-size: 1.5rem; font-weight: 700; margin-bottom: 1.5rem; text-align: left;">4. Detalhes do Documento</h3>
                            <div style="margin-bottom: 1.2rem;">
                                <label style="display: block; font-weight: 600; color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 0.95rem;">Título ou Área do Documento</label>
                                <input type="text" placeholder="Ex: Nutrição Animal" style="width: 100%; padding: 1.1rem 1.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.08); background: #f8fafc; font-size: 1rem; outline: none; transition: border-color 0.3s;">
                            </div>
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1.2rem;">
                                <div>
                                    <label style="display: block; font-weight: 600; color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 0.95rem;">Idioma Original</label>
                                    <select style="width: 100%; padding: 1.1rem 1.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.08); background: #f8fafc; font-size: 1rem; outline: none;">
                                        <option>Português</option><option>Inglês</option><option>Espanhol</option>
                                    </select>
                                </div>
                                <div>
                                    <label style="display: block; font-weight: 600; color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 0.95rem;">Traduzir para</label>
                                    <select style="width: 100%; padding: 1.1rem 1.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.08); background: #f8fafc; font-size: 1rem; outline: none;">
                                        <option>Inglês</option><option>Português</option><option>Espanhol</option>
                                    </select>
                                </div>
                            </div>
                            <div style="margin-bottom: 1.2rem;">
                                <label style="display: block; font-weight: 600; color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 0.95rem;">Anexar Arquivo (Opcional)</label>
                                <div style="border: 2px dashed rgba(0,0,0,0.1); border-radius: 12px; padding: 2rem; text-align: center; background: #f8fafc; cursor: pointer; transition: 0.3s;" onmouseover="this.style.borderColor='var(--primary)'" onmouseout="this.style.borderColor='rgba(0,0,0,0.1)'" onclick="document.getElementById('file-upload').click()">
                                    <i data-lucide="upload-cloud" style="color: var(--primary); width: 32px; height: 32px; margin-bottom: 0.5rem;"></i>
                                    <p style="color: var(--gray); font-size: 0.95rem; margin: 0;">Clique para escolher o arquivo (.pdf, .doc, .docx)</p>
                                    <input type="file" id="file-upload" style="display: none;" accept=".pdf,.doc,.docx">
                                </div>
                            </div>
                            <div style="margin-bottom: 1.2rem;">
                                <label style="display: block; font-weight: 600; color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 0.95rem;">Observações</label>
                                <textarea rows="3" placeholder="Informações adicionais..." style="width: 100%; padding: 1.1rem 1.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.08); background: #f8fafc; font-size: 1rem; outline: none; transition: border-color 0.3s; resize: vertical;"></textarea>
                            </div>
                            <div style="display: flex; justify-content: space-between; margin-top: 2rem;">
                                <button type="button" onclick="nextStep(3)" style="background: transparent; color: var(--primary); border: 2px solid var(--primary); cursor: pointer; padding: 1rem 2rem; border-radius: 99px; font-weight: 700; display: inline-flex; align-items: center; gap: 8px;"><i data-lucide="arrow-left" style="width: 18px;"></i> Voltar</button>
                                <button type="submit" class="btn-vip" style="background: var(--primary-dark); color: white; border: none; cursor: pointer; padding: 1rem 2rem; border-radius: 99px; font-weight: 700;">Finalizar e Enviar <i data-lucide="check" style="width: 18px; vertical-align: middle;"></i></button>
                            </div>
                        </div>

                    </form>
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

# Replace the whole <form id="traducao-form" ...> ... </form> section
pattern = re.compile(r'<form id="traducao-form".*?</form>', re.DOTALL)
new_content = pattern.sub(new_form, content)

# Remove any existing nextStep, prevStep functions if present
old_script_pattern = re.compile(r'<script>\s*let currentStep.*?function.*?function.*?</script>', re.DOTALL)
new_content = old_script_pattern.sub('', new_content)

# Inject script block if not present
if "function nextStep(step)" not in new_content:
    new_content = new_content.replace('</body>', script_block + '\n</body>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated traducoes.html")

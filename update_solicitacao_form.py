import re

file_path = r"c:\Users\patov\Documents\Projects\ChangeSkills\ChangeSkills\services\solicitacao-certificado.html"

new_form = '''
                    <!-- Progress Bar -->
                    <div style="display: flex; justify-content: space-between; position: relative; margin-bottom: 3rem;">
                        <div style="position: absolute; top: 50%; left: 0; width: 100%; height: 2px; background: #e2e8f0; z-index: 1; transform: translateY(-50%);"></div>
                        <div class="progress-line" style="position: absolute; top: 50%; left: 0; height: 2px; background: var(--primary); z-index: 2; transform: translateY(-50%); transition: width 0.4s; width: 0%;"></div>
                        
                        <div class="step-indicator" id="ind-1" style="width: 35px; height: 35px; background: var(--primary); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; z-index: 3; position: relative; transition: all 0.4s;">1</div>
                        <div class="step-indicator" id="ind-2" style="width: 35px; height: 35px; background: #e2e8f0; color: var(--gray); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; z-index: 3; position: relative; transition: all 0.4s;">2</div>
                        <div class="step-indicator" id="ind-3" style="width: 35px; height: 35px; background: #e2e8f0; color: var(--gray); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; z-index: 3; position: relative; transition: all 0.4s;">3</div>
                    </div>

                    <form id="wizard-form" style="display: flex; flex-direction: column; gap: 1.2rem; text-align: left;" onsubmit="event.preventDefault(); alert('Solicitação de certificado enviada com sucesso!');">
                        
                        <!-- ETAPA 1: Pessoais -->
                        <div class="form-step" id="step-1" style="display: block;">
                            <h3 style="color: var(--primary-dark); font-size: 1.5rem; font-weight: 700; margin-bottom: 1.5rem; text-align: left;">1. Dados do Aluno</h3>
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
                                <div>
                                    <label style="display: block; font-weight: 600; color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 0.95rem;">Nome Completo *</label>
                                    <input type="text" placeholder="Como deve aparecer no certificado" required style="width: 100%; padding: 1.1rem 1.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.08); background: #f8fafc; font-size: 1rem; outline: none; transition: border-color 0.3s;">
                                </div>
                                <div>
                                    <label style="display: block; font-weight: 600; color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 0.95rem;">CPF ou RG *</label>
                                    <input type="text" placeholder="Documento de identificação" required style="width: 100%; padding: 1.1rem 1.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.08); background: #f8fafc; font-size: 1rem; outline: none; transition: border-color 0.3s;">
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
                                <label style="display: block; font-weight: 600; color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 0.95rem;">E-mail para Envio *</label>
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

                        <!-- ETAPA 3: Curso -->
                        <div class="form-step" id="step-3" style="display: none;">
                            <h3 style="color: var(--primary-dark); font-size: 1.5rem; font-weight: 700; margin-bottom: 1.5rem; text-align: left;">3. Informações do Curso</h3>
                            
                            <div style="margin-bottom: 1.2rem;">
                                <label style="display: block; font-weight: 600; color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 0.95rem;">Módulo / Curso Concluído *</label>
                                <input type="text" placeholder="Ex: Adult Fast Track - Nível B2" required style="width: 100%; padding: 1.1rem 1.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.08); background: #f8fafc; font-size: 1rem; outline: none; transition: border-color 0.3s;">
                            </div>
                            
                            <div style="margin-bottom: 1.2rem;">
                                <label style="display: block; font-weight: 600; color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 0.95rem;">Data de Conclusão *</label>
                                <input type="date" required style="width: 100%; padding: 1.1rem 1.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.08); background: #f8fafc; font-size: 1rem; outline: none; transition: border-color 0.3s;">
                            </div>
                            
                            <div style="display: flex; justify-content: space-between; margin-top: 2rem;">
                                <button type="button" onclick="nextStep(2)" style="background: transparent; color: var(--primary); border: 2px solid var(--primary); cursor: pointer; padding: 1rem 2rem; border-radius: 99px; font-weight: 700; display: inline-flex; align-items: center; gap: 8px;"><i data-lucide="arrow-left" style="width: 18px;"></i> Voltar</button>
                                <button type="submit" class="btn-vip" style="background: var(--primary-dark); color: white; border: none; cursor: pointer; padding: 1rem 2rem; border-radius: 99px; font-weight: 700;">Solicitar Certificado <i data-lucide="check" style="width: 18px; vertical-align: middle;"></i></button>
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
            
            let progress = ((step - 1) / 2) * 100;
            document.querySelector('.progress-line').style.width = progress + '%';
        }
    </script>
"""

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the whole <form> ... </form> section inside the card
pattern = re.compile(r'<form.*?style="display: flex; flex-direction: column; gap: 1\.5rem; text-align: left;".*?</form>', re.DOTALL)
new_content = pattern.sub(new_form, content)

# Inject script block if not present
if "function nextStep(step)" not in new_content:
    new_content = new_content.replace('</body>', script_block + '\n</body>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated solicitacao-certificado.html")

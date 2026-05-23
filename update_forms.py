import os
import re
import glob

base_path = r"c:\Users\patov\Documents\Projects\ChangeSkills\ChangeSkills\cursos\modalidades"
html_files = glob.glob(os.path.join(base_path, "*.html"))

new_form_section = '''
        <!-- Agendamento Form (3 Etapas) -->
        <section id="agendamento" style="background: var(--bg-light); padding: 100px 0;">
            <div class="container" style="max-width: 800px; margin: 0 auto;">
                <div class="reveal" style="text-align: center; margin-bottom: 3rem;">
                    <span style="color: var(--primary); font-weight: 800; letter-spacing: 0.2em; text-transform: uppercase;">Professional Trial</span>
                    <h2 style="font-size: 3rem; margin-top: 1rem; color: var(--primary-dark);">Agende sua aula <span style="color: var(--primary);">Grátis</span></h2>
                </div>
                
                <div class="reveal" style="background: white; padding: 3.5rem; border-radius: 40px; box-shadow: 0 30px 60px rgba(0,0,0,0.15); border: 1px solid rgba(0,0,0,0.03);">
                    
                    <!-- Indicador de Progresso -->
                    <div style="display: flex; justify-content: space-between; margin-bottom: 2rem; position: relative;">
                        <div style="position: absolute; top: 50%; left: 0; width: 100%; height: 2px; background: #e2e8f0; z-index: 1; transform: translateY(-50%);"></div>
                        <div class="progress-line" style="position: absolute; top: 50%; left: 0; width: 0%; height: 2px; background: var(--primary); z-index: 2; transform: translateY(-50%); transition: width 0.4s ease;"></div>
                        
                        <div class="step-indicator active" style="width: 35px; height: 35px; border-radius: 50%; background: var(--primary); color: white; display: flex; align-items: center; justify-content: center; font-weight: bold; z-index: 3; transition: all 0.3s; border: 4px solid white;">1</div>
                        <div class="step-indicator" style="width: 35px; height: 35px; border-radius: 50%; background: #e2e8f0; color: var(--gray); display: flex; align-items: center; justify-content: center; font-weight: bold; z-index: 3; transition: all 0.3s; border: 4px solid white;">2</div>
                        <div class="step-indicator" style="width: 35px; height: 35px; border-radius: 50%; background: #e2e8f0; color: var(--gray); display: flex; align-items: center; justify-content: center; font-weight: bold; z-index: 3; transition: all 0.3s; border: 4px solid white;">3</div>
                    </div>

                    <form id="multiStepForm" style="display: flex; flex-direction: column; gap: 1.2rem;" onsubmit="event.preventDefault(); alert('Solicitação enviada!');">
                        
                        <!-- ETAPA 1: Dados Pessoais -->
                        <div class="form-step" id="step-1">
                            <h3 style="color: var(--primary-dark); font-size: 1.5rem; font-weight: 700; margin-bottom: 1.5rem; text-align: left;">Dados Pessoais</h3>
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-bottom: 1.2rem;">
                                <div>
                                    <label style="display: block; font-weight: 600; color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 0.95rem;">Nome *</label>
                                    <input type="text" placeholder="Seu nome" required style="width: 100%; padding: 1.1rem 1.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.08); background: #f8fafc; font-size: 1rem; outline: none; transition: border-color 0.3s;">
                                </div>
                                <div>
                                    <label style="display: block; font-weight: 600; color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 0.95rem;">Sobrenome</label>
                                    <input type="text" placeholder="Sobrenome" style="width: 100%; padding: 1.1rem 1.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.08); background: #f8fafc; font-size: 1rem; outline: none; transition: border-color 0.3s;">
                                </div>
                            </div>
                            <div style="text-align: right; margin-top: 2rem;">
                                <button type="button" onclick="nextStep(2)" class="btn-vip" style="border: none; cursor: pointer; padding: 1rem 2rem; border-radius: 99px; font-weight: 700;">Próximo <i data-lucide="arrow-right" style="width: 18px;"></i></button>
                            </div>
                        </div>

                        <!-- ETAPA 2: Contato -->
                        <div class="form-step" id="step-2" style="display: none;">
                            <h3 style="color: var(--primary-dark); font-size: 1.5rem; font-weight: 700; margin-bottom: 1.5rem; text-align: left;">Como falamos com você?</h3>
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
                                <button type="button" onclick="nextStep(3)" class="btn-vip" style="border: none; cursor: pointer; padding: 1rem 2rem; border-radius: 99px; font-weight: 700;">Próximo <i data-lucide="arrow-right" style="width: 18px;"></i></button>
                            </div>
                        </div>

                        <!-- ETAPA 3: Objetivos -->
                        <div class="form-step" id="step-3" style="display: none;">
                            <h3 style="color: var(--primary-dark); font-size: 1.5rem; font-weight: 700; margin-bottom: 1.5rem; text-align: left;">Nível e Objetivo</h3>
                            <div style="margin-bottom: 1.2rem;">
                                <label style="display: block; font-weight: 600; color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 0.95rem;">Nível atual de Inglês? *</label>
                                <select required style="width: 100%; padding: 1.1rem 1.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.08); background: #f8fafc; font-size: 1rem; outline: none; transition: border-color 0.3s;">
                                    <option value="" disabled selected>Selecione seu nível</option>
                                    <option value="nunca">Nunca estudei o idioma</option>
                                    <option value="iniciante">Iniciante / Básico</option>
                                    <option value="intermediario">Intermediário</option>
                                    <option value="avancado">Avançado</option>
                                </select>
                            </div>
                            <div style="margin-bottom: 1.2rem;">
                                <label style="display: block; font-weight: 600; color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 0.95rem;">Qual seu principal objetivo? *</label>
                                <select required style="width: 100%; padding: 1.1rem 1.5rem; border-radius: 12px; border: 1px solid rgba(0,0,0,0.08); background: #f8fafc; font-size: 1rem; outline: none; transition: border-color 0.3s;">
                                    <option value="" disabled selected>Selecione seu objetivo</option>
                                    <option value="carreira">Desenvolvimento Profissional / Carreira</option>
                                    <option value="viagem">Viagens ou Intercâmbio</option>
                                    <option value="academico">Estudos / Fins Acadêmicos</option>
                                    <option value="pessoal">Crescimento Pessoal / Hobbies</option>
                                </select>
                            </div>
                            <div style="display: flex; justify-content: space-between; margin-top: 2rem;">
                                <button type="button" onclick="nextStep(2)" style="background: transparent; color: var(--primary); border: 2px solid var(--primary); cursor: pointer; padding: 1rem 2rem; border-radius: 99px; font-weight: 700; display: inline-flex; align-items: center; gap: 8px;"><i data-lucide="arrow-left" style="width: 18px;"></i> Voltar</button>
                                <button type="submit" class="btn-vip" style="border: none; cursor: pointer; padding: 1rem 2rem; border-radius: 99px; font-weight: 700;">Finalizar <i data-lucide="check" style="width: 18px;"></i></button>
                            </div>
                        </div>

                    </form>
                </div>
            </div>
        </section>
'''

# The script logic
import sys

def replace_forms():
    updated = 0
    # The pattern matches <!-- Agendamento Form --> to </section>
    pattern = re.compile(r'<!--\s*(CTA / Agendamento|Agendamento Form|Agendamento|Form Section)\s*-->[\s\S]*?</section>', re.IGNORECASE)
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if pattern.search(content):
            new_content = pattern.sub(new_form_section, content)
            
            # Need to also inject the script block just before </body>
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
            
            let progress = (step - 1) * 50;
            document.querySelector('.progress-line').style.width = progress + '%';
        }
    </script>
"""
            # Inject script before </body> if not already there
            if "function nextStep(step)" not in new_content:
                new_content = new_content.replace('</body>', script_block + '</body>')

            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated += 1
            print(f"Updated forms in {os.path.basename(file)}")
    print(f"Total files updated: {updated}")

if __name__ == "__main__":
    replace_forms()

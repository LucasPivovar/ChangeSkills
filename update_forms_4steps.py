import os
import glob
import re

base_path = r"c:\Users\patov\Documents\Projects\ChangeSkills\ChangeSkills"
modalidades_files = glob.glob(os.path.join(base_path, "cursos", "modalidades", "*.html"))

new_form_section = '''        <!-- Agendamento Form -->
        <section id="agendamento" style="padding: 120px 0; background: var(--bg-light); position: relative;">
            <div class="container" style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">
                <div class="reveal">
                    <span style="color: var(--accent); font-weight: 800; letter-spacing: 0.2em; display: block; margin-bottom: 0.5rem; text-transform: uppercase;">Agende sua aula</span>
                    <h2 style="font-size: clamp(2.5rem, 4vw, 3.5rem); margin-bottom: 1.5rem; color: var(--primary-dark);">Dê o primeiro passo rumo à fluência</h2>
                    <p style="font-size: 1.2rem; color: var(--gray); line-height: 1.6; margin-bottom: 2rem;">Preencha o formulário e nossa equipe entrará em contato para agendar uma conversa sobre seus objetivos.</p>
                </div>
                
                <div class="glass-card reveal" style="background: white; padding: 3rem; border-radius: 30px; box-shadow: 0 30px 60px rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.03); position: relative;">
                    
                    <!-- Progress Bar -->
                    <div style="display: flex; justify-content: space-between; position: relative; margin-bottom: 3rem;">
                        <div style="position: absolute; top: 50%; left: 0; width: 100%; height: 2px; background: #e2e8f0; z-index: 1; transform: translateY(-50%);"></div>
                        <div class="progress-line" style="position: absolute; top: 50%; left: 0; height: 2px; background: var(--primary); z-index: 2; transform: translateY(-50%); transition: width 0.4s; width: 0%;"></div>
                        
                        <div class="step-indicator" id="ind-1" style="width: 35px; height: 35px; background: var(--primary); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; z-index: 3; position: relative; transition: all 0.4s;">1</div>
                        <div class="step-indicator" id="ind-2" style="width: 35px; height: 35px; background: #e2e8f0; color: var(--gray); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; z-index: 3; position: relative; transition: all 0.4s;">2</div>
                        <div class="step-indicator" id="ind-3" style="width: 35px; height: 35px; background: #e2e8f0; color: var(--gray); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; z-index: 3; position: relative; transition: all 0.4s;">3</div>
                        <div class="step-indicator" id="ind-4" style="width: 35px; height: 35px; background: #e2e8f0; color: var(--gray); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; z-index: 3; position: relative; transition: all 0.4s;">4</div>
                    </div>

                    <form id="wizard-form" onsubmit="event.preventDefault(); alert('Enviado com sucesso!');">
                        
                        <!-- ETAPA 1: Pessoais -->
                        <div class="form-step" id="step-1" style="display: block;">
                            <h3 style="color: var(--primary-dark); font-size: 1.5rem; font-weight: 700; margin-bottom: 1.5rem; text-align: left;">1. Dados Pessoais</h3>
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

                        <!-- ETAPA 4: Objetivos -->
                        <div class="form-step" id="step-4" style="display: none;">
                            <h3 style="color: var(--primary-dark); font-size: 1.5rem; font-weight: 700; margin-bottom: 1.5rem; text-align: left;">4. Nível e Objetivo</h3>
                            <div style="margin-bottom: 1.2rem;">
                                <label style="display: block; font-weight: 600; color: var(--primary-dark); margin-bottom: 0.5rem; font-size: 0.95rem;">Nível atual do idioma? *</label>
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
                                <button type="button" onclick="nextStep(3)" style="background: transparent; color: var(--primary); border: 2px solid var(--primary); cursor: pointer; padding: 1rem 2rem; border-radius: 99px; font-weight: 700; display: inline-flex; align-items: center; gap: 8px;"><i data-lucide="arrow-left" style="width: 18px;"></i> Voltar</button>
                                <button type="submit" class="btn-vip" style="background: var(--primary-dark); color: white; border: none; cursor: pointer; padding: 1rem 2rem; border-radius: 99px; font-weight: 700;">Finalizar <i data-lucide="check" style="width: 18px; vertical-align: middle;"></i></button>
                            </div>
                        </div>

                    </form>
                </div>
            </div>
        </section>
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

def replace_forms():
    updated = 0
    pattern = re.compile(r'<!--\s*(Agendamento Form \(3 Etapas\)|Agendamento Form|CTA / Agendamento|Agendamento|Form Section)\s*-->[\s\S]*?</section>', re.IGNORECASE)
    
    for file in modalidades_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if pattern.search(content):
            new_content = pattern.sub(new_form_section, content)
            
            # Remove old script block if exists
            old_script_pattern = re.compile(r'<script>\s*function nextStep\(step\).*?</script>', re.DOTALL)
            new_content = old_script_pattern.sub('', new_content)
            
            new_content = new_content.replace('</body>', script_block + '</body>')

            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            updated += 1
            print(f"Updated forms in {os.path.basename(file)}")
    print(f"Total files updated: {updated}")

if __name__ == "__main__":
    replace_forms()

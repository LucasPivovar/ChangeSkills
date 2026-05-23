import os

html_path = r"c:\Users\patov\Documents\Projects\ChangeSkills\ChangeSkills\index.html"
output_path = r"c:\Users\patov\Documents\Projects\ChangeSkills\ChangeSkills\area-do-aluno.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

header = content.split('</header>')[0] + '</header>'
# update title in header
header = header.replace('<title>Change Skills Idiomas | Oficial</title>', '<title>Área do Aluno | Change Skills Idiomas</title>')

footer = '<footer' + content.split('<footer')[1]

body = """
    <div class="menu-overlay"></div>
    <main style="background: var(--primary-dark); min-height: 100vh; padding: 180px 0 120px; position: relative; overflow: hidden;">
        <!-- Background elements -->
        <div style="position: absolute; top: -10%; left: -10%; width: 600px; height: 600px; background: var(--primary); filter: blur(250px); opacity: 0.3; border-radius: 50%; z-index: 0;"></div>
        
        <div class="container reveal active" style="position: relative; z-index: 1;">
            <div style="text-align: left; margin-bottom: 4rem;">
                <span style="color: var(--accent); font-weight: 800; letter-spacing: 0.2em; display: block; margin-bottom: 0.5rem; text-transform: uppercase;">Hub Digital</span>
                <h1 style="color: white; font-size: clamp(3rem, 5vw, 4.5rem); margin-bottom: 1rem;">Área do Aluno</h1>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem;">
                
                <a href="#" class="glass-card" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; padding: 3.5rem 2rem; text-align: center; color: white; text-decoration: none; transition: all 0.3s; display: block;" onmouseover="this.style.background='rgba(255,255,255,0.08)'; this.style.transform='translateY(-5px)';" onmouseout="this.style.background='rgba(255,255,255,0.03)'; this.style.transform='translateY(0)';">
                    <i data-lucide="layout-grid" style="color: var(--accent); width: 48px; height: 48px; margin-bottom: 1.5rem;"></i>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Login Portal Pearson</h3>
                    <p style="color: rgba(255,255,255,0.6); line-height: 1.5;">Acesse materiais, exercícios e conteúdos do seu curso.</p>
                </a>
                
                <a href="#" class="glass-card" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; padding: 3.5rem 2rem; text-align: center; color: white; text-decoration: none; transition: all 0.3s; display: block;" onmouseover="this.style.background='rgba(255,255,255,0.08)'; this.style.transform='translateY(-5px)';" onmouseout="this.style.background='rgba(255,255,255,0.03)'; this.style.transform='translateY(0)';">
                    <i data-lucide="user-plus" style="color: var(--accent); width: 48px; height: 48px; margin-bottom: 1.5rem;"></i>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Cadastro de Novos Alunos</h3>
                    <p style="color: rgba(255,255,255,0.6); line-height: 1.5;">Preencha seus dados e realize sua matrícula em poucos minutos.</p>
                </a>

                <a href="services/agendamento-nivelamento.html" class="glass-card" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; padding: 3.5rem 2rem; text-align: center; color: white; text-decoration: none; transition: all 0.3s; display: block;" onmouseover="this.style.background='rgba(255,255,255,0.08)'; this.style.transform='translateY(-5px)';" onmouseout="this.style.background='rgba(255,255,255,0.03)'; this.style.transform='translateY(0)';">
                    <i data-lucide="calendar-check" style="color: var(--accent); width: 48px; height: 48px; margin-bottom: 1.5rem;"></i>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Agendamento de Nivelamento</h3>
                    <p style="color: rgba(255,255,255,0.6); line-height: 1.5;">Descubra o módulo ideal para o seu nível atual de conhecimento.</p>
                </a>

                <a href="services/solicitacao-certificado.html" class="glass-card" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; padding: 3.5rem 2rem; text-align: center; color: white; text-decoration: none; transition: all 0.3s; display: block;" onmouseover="this.style.background='rgba(255,255,255,0.08)'; this.style.transform='translateY(-5px)';" onmouseout="this.style.background='rgba(255,255,255,0.03)'; this.style.transform='translateY(0)';">
                    <i data-lucide="award" style="color: var(--accent); width: 48px; height: 48px; margin-bottom: 1.5rem;"></i>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Certificado</h3>
                    <p style="color: rgba(255,255,255,0.6); line-height: 1.5;">Solicite e emita o seu certificado de conclusão.</p>
                </a>

                <a href="services/verificacao-certificado.html" class="glass-card" style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 24px; padding: 3.5rem 2rem; text-align: center; color: white; text-decoration: none; transition: all 0.3s; display: block;" onmouseover="this.style.background='rgba(255,255,255,0.08)'; this.style.transform='translateY(-5px)';" onmouseout="this.style.background='rgba(255,255,255,0.03)'; this.style.transform='translateY(0)';">
                    <i data-lucide="shield-check" style="color: var(--accent); width: 48px; height: 48px; margin-bottom: 1.5rem;"></i>
                    <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Verificação de Certificado</h3>
                    <p style="color: rgba(255,255,255,0.6); line-height: 1.5;">Verifique a autenticidade de um certificado Change Skills.</p>
                </a>
            </div>
        </div>
    </main>
"""

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(header + body + footer)

print("Created area-do-aluno.html")

import os
import re
import glob

base_path = r"c:\Users\patov\Documents\Projects\ChangeSkills\ChangeSkills"
html_files = glob.glob(os.path.join(base_path, "**", "*.html"), recursive=True)

def get_nav_html(depth):
    prefix = "../" * depth
    
    inicio = f"{prefix}index.html"
    escola = f"{prefix}nossa-escola.html"
    cursos = f"{prefix}index.html#cursos"
    contato = f"{prefix}contato.html"
    aluno = f"#"
    
    return f'''<ul class="nav-list" style="display: flex; gap: 3rem; list-style: none; align-items: center;">
                <li style="position: relative;">
                    <a href="{inicio}" style="text-decoration: none; color: var(--primary-dark); font-weight: 600; font-size: 1.1rem; transition: color 0.3s; display: block; padding: 0.5rem 0;" 
                       onmouseover="this.style.color='var(--primary)'; this.querySelector('.nav-line').style.width='100%'" 
                       onmouseout="this.style.color='var(--primary-dark)'; this.querySelector('.nav-line').style.width='0%'">
                        Início
                        <span class="nav-line" style="position: absolute; bottom: 0; left: 0; width: 0; height: 2px; background: var(--primary); transition: width 0.3s;"></span>
                    </a>
                </li>
                <li style="position: relative;">
                    <a href="{escola}" style="text-decoration: none; color: var(--primary-dark); font-weight: 600; font-size: 1.1rem; transition: color 0.3s; display: block; padding: 0.5rem 0;" 
                       onmouseover="this.style.color='var(--primary)'; this.querySelector('.nav-line').style.width='100%'" 
                       onmouseout="this.style.color='var(--primary-dark)'; this.querySelector('.nav-line').style.width='0%'">
                        Nossa Escola
                        <span class="nav-line" style="position: absolute; bottom: 0; left: 0; width: 0; height: 2px; background: var(--primary); transition: width 0.3s;"></span>
                    </a>
                </li>
                <li style="position: relative;">
                    <a href="{cursos}" style="text-decoration: none; color: var(--primary-dark); font-weight: 600; font-size: 1.1rem; transition: color 0.3s; display: block; padding: 0.5rem 0;" 
                       onmouseover="this.style.color='var(--primary)'; this.querySelector('.nav-line').style.width='100%'" 
                       onmouseout="this.style.color='var(--primary-dark)'; this.querySelector('.nav-line').style.width='0%'">
                        Cursos
                        <span class="nav-line" style="position: absolute; bottom: 0; left: 0; width: 0; height: 2px; background: var(--primary); transition: width 0.3s;"></span>
                    </a>
                </li>
                <li style="position: relative;">
                    <a href="{contato}" style="text-decoration: none; color: var(--primary-dark); font-weight: 600; font-size: 1.1rem; transition: color 0.3s; display: block; padding: 0.5rem 0;" 
                       onmouseover="this.style.color='var(--primary)'; this.querySelector('.nav-line').style.width='100%'" 
                       onmouseout="this.style.color='var(--primary-dark)'; this.querySelector('.nav-line').style.width='0%'">
                        Contato
                        <span class="nav-line" style="position: absolute; bottom: 0; left: 0; width: 0; height: 2px; background: var(--primary); transition: width 0.3s;"></span>
                    </a>
                </li>
                <li style="position: relative;">
                    <a href="{aluno}" style="text-decoration: none; color: var(--primary-dark); font-weight: 600; font-size: 1.1rem; transition: color 0.3s; display: block; padding: 0.5rem 0;" 
                       onmouseover="this.style.color='var(--primary)'; this.querySelector('.nav-line').style.width='100%'" 
                       onmouseout="this.style.color='var(--primary-dark)'; this.querySelector('.nav-line').style.width='0%'">
                        Área do Aluno
                        <span class="nav-line" style="position: absolute; bottom: 0; left: 0; width: 0; height: 2px; background: var(--primary); transition: width 0.3s;"></span>
                    </a>
                </li>
            </ul>'''

def get_footer_html(depth):
    prefix = "../" * depth
    return f'''<footer style="padding: 120px 0 60px 0; background: var(--primary-dark); color: white;">
        <div class="container">
            <div style="display: grid; grid-template-columns: 1.5fr 1fr 1fr 1fr; gap: 4rem; margin-bottom: 4rem;">
                <div>
                    <img src="https://changeskills.com.br/wp-content/uploads/2022/11/logo-change.png"
                        style="height: 50px; filter: brightness(0) invert(1); margin-bottom: 2.5rem;">
                    <p style="opacity: 0.6; font-size: 1.1rem; line-height: 1.6; max-width: 300px;">A ponte definitiva entre você e o mundo. Educação com excelência global.</p>
                </div>
                <div>
                    <h4 style="color: var(--accent); margin-bottom: 2.5rem; font-size: 1.2rem;">Institucional</h4>
                    <ul style="list-style: none; display: flex; flex-direction: column; gap: 1.2rem; opacity: 0.7;">
                        <li><a href="{prefix}index.html#escola" style="color: white; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='white'">Nossa Escola</a></li>
                        <li><a href="{prefix}nossos-teachers.html" style="color: white; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='white'">Professores</a></li>
                        <li><a href="{prefix}services/solicitacao-certificado.html" style="color: white; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='white'">Certificados</a></li>
                        <li><a href="{prefix}services/verificacao-certificado.html" style="color: white; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='white'">Validação de Certificados</a></li>
                    </ul>
                </div>
                <div>
                    <h4 style="color: var(--accent); margin-bottom: 2.5rem; font-size: 1.2rem;">Cursos</h4>
                    <ul style="list-style: none; display: flex; flex-direction: column; gap: 1.2rem; opacity: 0.7;">
                        <li><a href="{prefix}cursos/ingles.html" style="color: white; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='white'">Inglês</a></li>
                        <li><a href="{prefix}cursos/espanhol.html" style="color: white; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='white'">Espanhol</a></li>
                        <li><a href="{prefix}cursos/frances.html" style="color: white; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='white'">Francês</a></li>
                        <li><a href="{prefix}cursos/portugues.html" style="color: white; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='white'">Português</a></li>
                    </ul>
                </div>
                <div>
                    <h4 style="color: var(--accent); margin-bottom: 2.5rem; font-size: 1.2rem;">Serviços</h4>
                    <ul style="list-style: none; display: flex; flex-direction: column; gap: 1.2rem; opacity: 0.7; margin-bottom: 2rem;">
                        <li><a href="{prefix}services/traducoes.html" style="color: white; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='white'">Traduções</a></li>
                        <li><a href="{prefix}services/aulas-conversacao.html" style="color: white; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='white'">Aulas de Conversação</a></li>
                    </ul>
                    <div style="display: flex; gap: 1.5rem; opacity: 0.8; align-items: center; margin-top: 1rem;">
                        <a href="#" style="color: white; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='white'"><i data-lucide="instagram"></i></a>
                        <a href="#" style="color: white; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='white'"><i data-lucide="facebook"></i></a>
                        <a href="#" style="color: white; transition: color 0.3s;" onmouseover="this.style.color='var(--accent)'" onmouseout="this.style.color='white'"><i data-lucide="linkedin"></i></a>
                    </div>
                </div>
            </div>
            <div style="text-align: center; opacity: 0.3; padding-top: 4rem; border-top: 1px solid rgba(255,255,255,0.1); font-size: 0.9rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                <span>2026 © Change Skills — Todos os direitos reservados.</span>
                <span>Desenvolvido por <strong>Page Facilitado</strong></span>
            </div>
        </div>
    </footer>'''

pattern_header = re.compile(r'<ul class="nav-list"[^>]*>[\s\S]*?</ul>')
pattern_footer = re.compile(r'<footer[^>]*>[\s\S]*?</footer>')

for file in html_files:
    rel_path = os.path.relpath(file, base_path)
    parts = rel_path.split(os.path.sep)
    depth = len(parts) - 1
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    if pattern_header.search(new_content):
        new_content = pattern_header.sub(get_nav_html(depth), new_content)
    
    if pattern_footer.search(new_content):
        new_content = pattern_footer.sub(get_footer_html(depth), new_content)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated: {rel_path} (depth={depth})")

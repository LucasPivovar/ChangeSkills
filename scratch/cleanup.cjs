const fs = require('fs');
const path = require('path');

const rootDir = path.join(__dirname, '..');

const filesToDelete = [
  'area-do-aluno.html',
  'area-do-aluno-utf8.html',
  'cadastro-aluno.html',
  'cadastro-aluno-utf8.html',
  'contato.html',
  'contato-utf8.html',
  'index-static.html',
  'index-utf8.html',
  'nossa-escola.html',
  'nossa-escola-utf8.html',
  'cursos-ingles-utf8.html',
  'cursos-espanhol-utf8.html',
  'cursos-frances-utf8.html'
];

filesToDelete.forEach(file => {
  const filePath = path.join(rootDir, file);
  if (fs.existsSync(filePath)) {
    fs.unlinkSync(filePath);
    console.log(`Deleted ${file}`);
  }
});

const dirsToDelete = [
  'cursos',
  'services'
];

dirsToDelete.forEach(dir => {
  const dirPath = path.join(rootDir, dir);
  if (fs.existsSync(dirPath)) {
    fs.rmSync(dirPath, { recursive: true, force: true });
    console.log(`Deleted directory ${dir}`);
  }
});

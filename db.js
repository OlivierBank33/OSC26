// ============================================================
//  OSC26 — db.js
//  FONCTIONS HELPER UNIQUEMENT — ne pas modifier pour ajouter des questions
//  Pour ajouter/modifier des questions, éditez questions.js
// ============================================================

// Helper : récupère les modules disponibles
function getModules() {
  const mods = [...new Set(DB.map(q => q.module))].sort();
  return ['TOUS', ...mods];
}

// Helper : filtre par module, exclut les questions sans bonne réponse (r === -1)
function getQuestions(module = 'TOUS') {
  return DB.filter(q => q.r !== -1 && (module === 'TOUS' || q.module === module));
}

// Helper : mélange un tableau (Fisher-Yates)
function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

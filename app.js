// ============================================================
//  OSC26 — app.js
//  Mode 1 : Entraînement (quiz depuis DB)
//  Mode 2 : Créer un QCM (builder)
// ============================================================

const $ = id => document.getElementById(id);
const letters = ['A', 'B', 'C', 'D', 'E', 'F'];

function escHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;')
    .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function showToast(msg, duration = 2500) {
  const t = $('toast');
  t.textContent = msg;
  t.classList.remove('hidden');
  clearTimeout(showToast._t);
  showToast._t = setTimeout(() => t.classList.add('hidden'), duration);
}

// ═══════════════════════════════════════════════════════════
//  Navigation onglets
// ═══════════════════════════════════════════════════════════
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
      btn.classList.add('active');
      $('tab-' + btn.dataset.tab).classList.add('active');
    });
  });

  initQuiz();
  initBuilder();
});

// ═══════════════════════════════════════════════════════════
//  MODE QUIZ
// ═══════════════════════════════════════════════════════════
let quizState = {
  questions: [],
  current: 0,
  answers: [],     // index choisi par l'utilisateur (-1 si pas répondu)
  score: 0,
  module: 'TOUS',
  qty: 30
};

function initQuiz() {
  buildModuleButtons();
  updateAvailableCount();

  // Qty
  document.querySelectorAll('.qty-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.qty-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      quizState.qty = btn.dataset.qty === 'all' ? 'all' : parseInt(btn.dataset.qty);
      updateAvailableCount();
    });
  });

  $('btn-start-quiz').addEventListener('click', startQuiz);
  $('btn-quit-quiz').addEventListener('click', () => {
    $('quiz-screen').classList.add('hidden');
    $('quiz-setup').classList.remove('hidden');
  });
  $('btn-validate').addEventListener('click', validateAnswer);
  $('btn-next').addEventListener('click', nextQuestion);
  $('btn-retry').addEventListener('click', () => {
    $('quiz-results').classList.add('hidden');
    startQuiz();
  });
  $('btn-back-setup').addEventListener('click', () => {
    $('quiz-results').classList.add('hidden');
    $('quiz-setup').classList.remove('hidden');
  });
  $('btn-review').addEventListener('click', toggleReview);
}

function buildModuleButtons() {
  const container = $('module-buttons');
  getModules().forEach(mod => {
    const btn = document.createElement('button');
    btn.className = 'mod-btn' + (mod === 'TOUS' ? ' active' : '');
    btn.textContent = mod;
    btn.addEventListener('click', () => {
      document.querySelectorAll('.mod-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      quizState.module = mod;
      updateAvailableCount();
    });
    container.appendChild(btn);
  });
}

function updateAvailableCount() {
  const pool = getQuestions(quizState.module);
  const n = quizState.qty === 'all' ? pool.length : Math.min(quizState.qty, pool.length);
  $('available-count').textContent = `${pool.length} question(s) disponible(s) — ${n} sera(ont) tirée(s) au sort.`;
}

function startQuiz() {
  const pool = getQuestions(quizState.module);
  if (pool.length === 0) { showToast('Aucune question disponible pour ce module.'); return; }

  const shuffled = shuffle(pool);
  const n = quizState.qty === 'all' ? shuffled.length : Math.min(quizState.qty, shuffled.length);
  quizState.questions = shuffled.slice(0, n);
  quizState.current  = 0;
  quizState.answers  = new Array(n).fill(-1);
  quizState.score    = 0;

  $('quiz-setup').classList.add('hidden');
  $('quiz-results').classList.add('hidden');
  $('quiz-screen').classList.remove('hidden');

  renderQuestion();
}

function renderQuestion() {
  const q   = quizState.questions[quizState.current];
  const idx = quizState.current;
  const n   = quizState.questions.length;

  $('q-current').textContent = idx + 1;
  $('q-total').textContent   = n;
  $('live-score').textContent = quizState.score;
  $('progress-bar').style.width = ((idx / n) * 100) + '%';

  $('quiz-module-tag').textContent = q.module;
  $('quiz-question-text').textContent = q.text;

  // Choices
  const choicesEl = $('quiz-choices');
  choicesEl.innerHTML = q.choices.map((c, i) => `
    <div class="choice-option" data-idx="${i}">
      <span class="choice-letter">${letters[i]}.</span>
      <span>${escHtml(c)}</span>
    </div>
  `).join('');

  choicesEl.querySelectorAll('.choice-option').forEach(opt => {
    opt.addEventListener('click', () => selectChoice(parseInt(opt.dataset.idx)));
  });

  $('quiz-feedback').className = 'quiz-feedback hidden';
  $('quiz-feedback').textContent = '';
  $('btn-validate').disabled = true;
  $('btn-validate').classList.remove('hidden');
  $('btn-next').classList.add('hidden');
}

function selectChoice(idx) {
  document.querySelectorAll('.choice-option').forEach(o => o.classList.remove('selected'));
  document.querySelectorAll('.choice-option')[idx].classList.add('selected');
  quizState.answers[quizState.current] = idx;
  $('btn-validate').disabled = false;
}

function validateAnswer() {
  const q         = quizState.questions[quizState.current];
  const chosen    = quizState.answers[quizState.current];
  const correct   = q.r;
  const isCorrect = chosen === correct;

  if (isCorrect) quizState.score++;

  // Colorize choices
  document.querySelectorAll('.choice-option').forEach((opt, i) => {
    opt.classList.add('disabled');
    if (i === correct) opt.classList.add('correct-ans');
    else if (i === chosen && !isCorrect) opt.classList.add('wrong-ans');
  });

  // Feedback
  const fb = $('quiz-feedback');
  fb.classList.remove('hidden', 'feedback-ok', 'feedback-fail');
  if (isCorrect) {
    fb.classList.add('feedback-ok');
    fb.textContent = '✅ Bonne réponse !' + (q.explication ? ' — ' + q.explication : '');
  } else {
    fb.classList.add('feedback-fail');
    fb.textContent = `❌ Mauvaise réponse. La bonne réponse était : ${letters[correct]}. ${q.explication || ''}`;
  }

  $('btn-validate').classList.add('hidden');
  $('live-score').textContent = quizState.score;

  if (quizState.current < quizState.questions.length - 1) {
    $('btn-next').classList.remove('hidden');
  } else {
    setTimeout(showResults, 900);
  }
}

function nextQuestion() {
  quizState.current++;
  $('btn-next').classList.add('hidden');
  renderQuestion();
}

function showResults() {
  $('quiz-screen').classList.add('hidden');
  $('quiz-results').classList.remove('hidden');

  const total   = quizState.questions.length;
  const correct = quizState.score;
  const wrong   = total - correct;
  const pct     = Math.round((correct / total) * 100);

  $('score-pct').textContent  = pct;
  $('stat-correct').textContent = correct;
  $('stat-wrong').textContent   = wrong;
  $('stat-total').textContent   = total;

  const circle = $('score-circle');
  circle.classList.remove('great', 'ok', 'bad');
  if (pct >= 70)      circle.classList.add('great');
  else if (pct >= 50) circle.classList.add('ok');
  else                circle.classList.add('bad');

  let title = '', sub = '';
  if (pct >= 90) { title = 'Excellent !';       sub = 'Maîtrise parfaite du cours.'; }
  else if (pct >= 70) { title = 'Bien joué !';  sub = 'Bon niveau, continuez comme ça.'; }
  else if (pct >= 50) { title = 'Passable';      sub = 'Des lacunes à combler.'; }
  else                { title = 'À retravailler'; sub = 'Reprenez le cours et réessayez.'; }

  $('results-title').textContent    = title;
  $('results-subtitle').textContent = sub;

  $('review-list').classList.add('hidden');
  $('review-list').innerHTML = '';
}

function toggleReview() {
  const list = $('review-list');
  if (!list.classList.contains('hidden')) { list.classList.add('hidden'); return; }

  list.innerHTML = quizState.questions.map((q, i) => {
    const chosen    = quizState.answers[i];
    const correct   = q.r;
    const isOk      = chosen === correct;
    const choicesHtml = q.choices.map((c, ci) => {
      let cls = '';
      if (ci === chosen && isOk)   cls = 'user-correct';
      if (ci === chosen && !isOk)  cls = 'user-wrong';
      if (ci === correct && !isOk) cls = 'show-correct';
      return cls ? `<div class="review-choice ${cls}">${letters[ci]}. ${escHtml(c)}</div>` : '';
    }).join('');
    return `
      <div class="review-item ${isOk ? 'ok' : 'fail'}">
        <div class="review-q-num">Q${i + 1} — ${q.module}</div>
        <div class="review-q-text">${escHtml(q.text)}</div>
        ${choicesHtml}
        ${q.explication ? `<div class="review-expl">💡 ${escHtml(q.explication)}</div>` : ''}
      </div>
    `;
  }).join('');

  list.classList.remove('hidden');
  $('btn-review').textContent = '📋 Masquer les corrections';
  // After toggling open, change button text for next click
  $('btn-review').onclick = () => {
    list.classList.add('hidden');
    $('btn-review').textContent = '📋 Voir les corrections';
    $('btn-review').onclick = toggleReview;
  };
}

// ═══════════════════════════════════════════════════════════
//  MODE BUILDER (localStorage)
// ═══════════════════════════════════════════════════════════
const STORAGE_KEY = 'qcm_builder_data';
let builderState = { title: '', description: '', questions: [] };

function initBuilder() {
  loadBuilderState();
  renderPreview();

  $('btn-add-choice').addEventListener('click', () => addChoiceRow());
  $('choices-container').addEventListener('click', e => {
    if (e.target.classList.contains('btn-remove-choice'))
      removeChoiceRow(e.target.closest('.choice-row'));
  });
  $('btn-add-question').addEventListener('click', addQuestion);
  $('q-text').addEventListener('keydown', e => { if (e.key === 'Enter') addQuestion(); });
  $('questions-list').addEventListener('click', e => {
    const btn = e.target.closest('button');
    if (!btn) return;
    const id = btn.dataset.id;
    if (btn.classList.contains('btn-delete-q')) deleteQuestion(id);
    if (btn.classList.contains('btn-up'))       moveQuestion(id, -1);
    if (btn.classList.contains('btn-down'))     moveQuestion(id, +1);
  });
  $('qcm-title').addEventListener('input', renderPreview);
  $('qcm-desc').addEventListener('input', renderPreview);
  $('btn-clear').addEventListener('click', clearAll);
  $('btn-export-json').addEventListener('click', exportJSON);
  $('btn-export-pdf').addEventListener('click', () => window.print());

  $('modal-cancel').addEventListener('click', () => {
    $('modal-overlay').classList.add('hidden');
    _pendingConfirm = null;
  });
  $('modal-confirm').addEventListener('click', () => {
    $('modal-overlay').classList.add('hidden');
    if (_pendingConfirm) { _pendingConfirm(); _pendingConfirm = null; }
  });
  $('modal-overlay').addEventListener('click', e => {
    if (e.target === $('modal-overlay')) {
      $('modal-overlay').classList.add('hidden');
      _pendingConfirm = null;
    }
  });
}

function saveBuilderState() { localStorage.setItem(STORAGE_KEY, JSON.stringify(builderState)); }
function loadBuilderState() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) builderState = JSON.parse(raw);
  } catch { /* ignore */ }
}

let choiceCount = 2;

function getChoiceRows() { return [...document.querySelectorAll('.choice-row')]; }

function rebuildChoiceIndexes() {
  getChoiceRows().forEach((row, i) => {
    row.dataset.index = i;
    row.querySelector('input[type="radio"]').value = i;
    row.querySelector('.choice-input').placeholder = `Choix ${letters[i] ?? i + 1}`;
  });
}

function addChoiceRow(value = '') {
  const container = $('choices-container');
  const rows = getChoiceRows();
  if (rows.length >= 6) { showToast('Maximum 6 choix.'); return; }
  const idx = rows.length;
  const div = document.createElement('div');
  div.className = 'choice-row';
  div.dataset.index = idx;
  div.innerHTML = `
    <input type="radio" name="correct" value="${idx}" title="Bonne réponse" />
    <input type="text" class="choice-input" placeholder="Choix ${letters[idx] ?? idx + 1}" value="${escHtml(value)}" />
    <button class="btn-remove-choice" title="Supprimer">✕</button>
  `;
  container.appendChild(div);
  choiceCount++;
}

function removeChoiceRow(row) {
  if (getChoiceRows().length <= 2) { showToast('Minimum 2 choix.'); return; }
  row.remove();
  rebuildChoiceIndexes();
}

function resetChoiceForm() {
  [...$('choices-container').querySelectorAll('.choice-row')].forEach(r => r.remove());
  choiceCount = 0;
  addChoiceRow();
  addChoiceRow();
}

function genId() { return Date.now().toString(36) + Math.random().toString(36).slice(2, 6); }

function renderPreview() {
  const title = $('qcm-title').value.trim();
  const desc  = $('qcm-desc').value.trim();
  const hdr   = $('preview-header');
  if (title || desc) {
    $('preview-title').textContent = title || '(Sans titre)';
    $('preview-desc').textContent  = desc;
    hdr.classList.remove('hidden');
  } else { hdr.classList.add('hidden'); }

  const list = $('questions-list');
  $('question-count').textContent = `${builderState.questions.length} question(s)`;

  if (builderState.questions.length === 0) {
    list.innerHTML = '<div class="empty-state">Aucune question pour l\'instant.<br/>Remplissez le formulaire à gauche.</div>';
    return;
  }
  list.innerHTML = builderState.questions.map((q, idx) => `
    <div class="question-card" data-id="${q.id}">
      <div class="q-header">
        <span class="q-num">${idx + 1}</span>
        <span class="q-text">${escHtml(q.text)}</span>
        <div class="q-actions">
          ${idx > 0 ? `<button class="btn-up" data-id="${q.id}" title="Monter">▲</button>` : ''}
          ${idx < builderState.questions.length - 1 ? `<button class="btn-down" data-id="${q.id}" title="Descendre">▼</button>` : ''}
          <button class="btn-delete-q" data-id="${q.id}" title="Supprimer">🗑</button>
        </div>
      </div>
      <ul class="choice-list">
        ${q.choices.map((c, ci) => `
          <li class="choice-item ${c.correct ? 'correct' : ''}">
            <span class="choice-letter">${letters[ci] ?? ci + 1}.</span>
            ${escHtml(c.text)} ${c.correct ? '✓' : ''}
          </li>`).join('')}
      </ul>
      ${q.explication ? `<div class="q-explication">💡 ${escHtml(q.explication)}</div>` : ''}
    </div>
  `).join('');
}

function addQuestion() {
  const text = $('q-text').value.trim();
  if (!text) { showToast('⚠️ Entrez l\'intitulé de la question.'); return; }
  const rows = getChoiceRows();
  const checkedRadio = document.querySelector('input[name="correct"]:checked');
  const correctIndex = checkedRadio ? parseInt(checkedRadio.value) : -1;
  const choices = rows.map((row, i) => ({
    text: row.querySelector('.choice-input').value.trim() || `Choix ${letters[i] ?? i + 1}`,
    correct: i === correctIndex
  }));
  if (!choices.some(c => c.correct)) { showToast('⚠️ Cochez la bonne réponse.'); return; }
  builderState.questions.push({ id: genId(), text, choices, explication: $('q-explication').value.trim() });
  saveBuilderState();
  renderPreview();
  showToast('✅ Question ajoutée !');
  $('q-text').value = '';
  $('q-explication').value = '';
  resetChoiceForm();
  $('q-text').focus();
}

function deleteQuestion(id) {
  builderState.questions = builderState.questions.filter(q => q.id !== id);
  saveBuilderState();
  renderPreview();
  showToast('Question supprimée.');
}

function moveQuestion(id, dir) {
  const idx = builderState.questions.findIndex(q => q.id === id);
  if (idx === -1) return;
  const t = idx + dir;
  if (t < 0 || t >= builderState.questions.length) return;
  [builderState.questions[idx], builderState.questions[t]] = [builderState.questions[t], builderState.questions[idx]];
  saveBuilderState();
  renderPreview();
}

function exportJSON() {
  const data = {
    title: $('qcm-title').value.trim() || 'QCM',
    description: $('qcm-desc').value.trim(),
    createdAt: new Date().toISOString(),
    questions: builderState.questions
  };
  const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
  const url  = URL.createObjectURL(blob);
  const a    = document.createElement('a');
  a.href = url;
  a.download = (data.title.replace(/\s+/g, '_') || 'qcm') + '.json';
  a.click();
  URL.revokeObjectURL(url);
  showToast('⬇ Export JSON téléchargé.');
}

let _pendingConfirm = null;
function openModal(msg, onConfirm) {
  $('modal-message').textContent = msg;
  $('modal-overlay').classList.remove('hidden');
  _pendingConfirm = onConfirm;
}

function clearAll() {
  openModal('Supprimer toutes les questions ?', () => {
    builderState.questions = [];
    saveBuilderState();
    renderPreview();
    showToast('QCM effacé.');
  });
}

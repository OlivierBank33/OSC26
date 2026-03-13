// ============================================================
//  QCM Builder — app.js
//  Stockage local (localStorage) — prêt pour une BDD externe
// ============================================================

const STORAGE_KEY = 'qcm_builder_data';

// ── État global ──────────────────────────────────────────────
let state = {
  title: '',
  description: '',
  questions: []   // { id, text, choices: [{text, correct}], explication }
};

// ── Utilitaires ──────────────────────────────────────────────
const $ = id => document.getElementById(id);
const letters = ['A', 'B', 'C', 'D', 'E', 'F'];

function genId() {
  return Date.now().toString(36) + Math.random().toString(36).slice(2, 6);
}

function showToast(msg, duration = 2500) {
  const toast = $('toast');
  toast.textContent = msg;
  toast.classList.remove('hidden');
  clearTimeout(showToast._timer);
  showToast._timer = setTimeout(() => toast.classList.add('hidden'), duration);
}

// ── Persistance localStorage ──────────────────────────────────
function saveState() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
}

function loadState() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) state = JSON.parse(raw);
  } catch { /* ignore */ }
}

// ── Gestion des choix (formulaire) ───────────────────────────
let choiceCount = 2;

function getChoiceRows() {
  return [...document.querySelectorAll('.choice-row')];
}

function rebuildChoiceIndexes() {
  getChoiceRows().forEach((row, i) => {
    row.dataset.index = i;
    const radio = row.querySelector('input[type="radio"]');
    radio.value = i;
    const inp = row.querySelector('.choice-input');
    inp.placeholder = `Choix ${letters[i] ?? i + 1}`;
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
  const container = $('choices-container');
  // Keep label, remove all .choice-row
  [...container.querySelectorAll('.choice-row')].forEach(r => r.remove());
  choiceCount = 0;
  addChoiceRow();
  addChoiceRow();
}

// ── Rendu de l'aperçu ────────────────────────────────────────
function escHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function renderPreview() {
  // Header
  const title = $('qcm-title').value.trim();
  const desc  = $('qcm-desc').value.trim();
  const headerDiv = $('preview-header');
  if (title || desc) {
    $('preview-title').textContent = title || '(Sans titre)';
    $('preview-desc').textContent  = desc;
    headerDiv.classList.remove('hidden');
  } else {
    headerDiv.classList.add('hidden');
  }

  // Questions
  const list = $('questions-list');
  $('question-count').textContent = `${state.questions.length} question(s)`;

  if (state.questions.length === 0) {
    list.innerHTML = '<div class="empty-state">Aucune question pour l\'instant.<br/>Remplissez le formulaire à gauche.</div>';
    return;
  }

  list.innerHTML = state.questions.map((q, idx) => `
    <div class="question-card" data-id="${q.id}">
      <div class="q-header">
        <span class="q-num">${idx + 1}</span>
        <span class="q-text">${escHtml(q.text)}</span>
        <div class="q-actions">
          ${idx > 0 ? `<button class="btn-up" data-id="${q.id}" title="Monter">▲</button>` : ''}
          ${idx < state.questions.length - 1 ? `<button class="btn-down" data-id="${q.id}" title="Descendre">▼</button>` : ''}
          <button class="btn-delete-q" data-id="${q.id}" title="Supprimer">🗑</button>
        </div>
      </div>
      <ul class="choice-list">
        ${q.choices.map((c, ci) => `
          <li class="choice-item ${c.correct ? 'correct' : ''}">
            <span class="choice-letter">${letters[ci] ?? ci + 1}.</span>
            ${escHtml(c.text)}
            ${c.correct ? '✓' : ''}
          </li>`).join('')}
      </ul>
      ${q.explication ? `<div class="q-explication">💡 ${escHtml(q.explication)}</div>` : ''}
    </div>
  `).join('');
}

// ── Ajouter une question ──────────────────────────────────────
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

  if (!choices.some(c => c.correct)) {
    showToast('⚠️ Cochez la bonne réponse (bouton radio vert).'); return;
  }

  const question = {
    id: genId(),
    text,
    choices,
    explication: $('q-explication').value.trim()
  };

  state.questions.push(question);
  saveState();
  renderPreview();
  showToast('✅ Question ajoutée !');

  // Reset form
  $('q-text').value = '';
  $('q-explication').value = '';
  resetChoiceForm();
  $('q-text').focus();
}

// ── Supprimer / déplacer questions ───────────────────────────
function deleteQuestion(id) {
  state.questions = state.questions.filter(q => q.id !== id);
  saveState();
  renderPreview();
  showToast('Question supprimée.');
}

function moveQuestion(id, direction) {
  const idx = state.questions.findIndex(q => q.id === id);
  if (idx === -1) return;
  const target = idx + direction;
  if (target < 0 || target >= state.questions.length) return;
  [state.questions[idx], state.questions[target]] = [state.questions[target], state.questions[idx]];
  saveState();
  renderPreview();
}

// ── Export JSON ───────────────────────────────────────────────
function exportJSON() {
  const data = {
    title: $('qcm-title').value.trim() || 'QCM',
    description: $('qcm-desc').value.trim(),
    createdAt: new Date().toISOString(),
    questions: state.questions
  };
  const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
  const url  = URL.createObjectURL(blob);
  const a    = document.createElement('a');
  a.href     = url;
  a.download = (data.title.replace(/\s+/g, '_') || 'qcm') + '.json';
  a.click();
  URL.revokeObjectURL(url);
  showToast('⬇ Export JSON téléchargé.');
}

// ── Export PDF (impression) ───────────────────────────────────
function exportPDF() {
  window.print();
}

// ── Modal confirmation ────────────────────────────────────────
let _pendingConfirm = null;

function openModal(message, onConfirm) {
  $('modal-message').textContent = message;
  $('modal-overlay').classList.remove('hidden');
  _pendingConfirm = onConfirm;
}

// ── Effacer tout ──────────────────────────────────────────────
function clearAll() {
  openModal('Supprimer toutes les questions ?', () => {
    state.questions = [];
    saveState();
    renderPreview();
    showToast('QCM effacé.');
  });
}

// ── Event listeners ───────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  loadState();
  renderPreview();

  // Ajouter un choix
  $('btn-add-choice').addEventListener('click', () => addChoiceRow());

  // Délégation : supprimer un choix
  $('choices-container').addEventListener('click', e => {
    if (e.target.classList.contains('btn-remove-choice')) {
      removeChoiceRow(e.target.closest('.choice-row'));
    }
  });

  // Ajouter question
  $('btn-add-question').addEventListener('click', addQuestion);

  // Entrée clavier dans le champ question
  $('q-text').addEventListener('keydown', e => {
    if (e.key === 'Enter') addQuestion();
  });

  // Délégation aperçu : supprimer / déplacer
  $('questions-list').addEventListener('click', e => {
    const btn = e.target.closest('button');
    if (!btn) return;
    const id = btn.dataset.id;
    if (btn.classList.contains('btn-delete-q')) deleteQuestion(id);
    if (btn.classList.contains('btn-up'))       moveQuestion(id, -1);
    if (btn.classList.contains('btn-down'))     moveQuestion(id, +1);
  });

  // Live update de l'aperçu header
  $('qcm-title').addEventListener('input', renderPreview);
  $('qcm-desc').addEventListener('input', renderPreview);

  // Effacer tout
  $('btn-clear').addEventListener('click', clearAll);

  // Export
  $('btn-export-json').addEventListener('click', exportJSON);
  $('btn-export-pdf').addEventListener('click', exportPDF);

  // Modal
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
});

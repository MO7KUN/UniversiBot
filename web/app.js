'use strict';
const messages = document.querySelector('#messages');
const form = document.querySelector('#chat-form');
const input = document.querySelector('#message');
const status = document.querySelector('#status');
const pagesPreview = new URLSearchParams(location.search).get('preview') === 'pages';
function sessionId() {
  return typeof crypto.randomUUID === 'function' ? crypto.randomUUID() : 'session-' + Date.now() + '-' + Math.random().toString(36).slice(2);
}
let sender = sessionId();
let pending = false;
function bubble(text, kind) {
  const element = document.createElement('div');
  element.className = 'bubble ' + kind;
  element.textContent = text; // Never interpret model output as HTML.
  messages.append(element);
  messages.scrollTop = messages.scrollHeight;
}
function welcome() { bubble('Bonjour, bienvenue ! 👋\nJe suis UniversiBot. Comment puis-je vous aider aujourd’hui ?','bot'); }
async function send(text) {
  text = text.trim();
  if (pagesPreview || !text || pending || text.length > 1000) return;
  pending = true;
  document.querySelectorAll('button').forEach(b => b.disabled = true);
  bubble(text, 'user'); input.value = ''; status.textContent = 'UniversiBot prépare sa réponse…';
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 65000);
  try {
    const response = await fetch('/api/chat', {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({sender,message:text}),signal:controller.signal});
    if (!response.ok) throw new Error('HTTP ' + response.status);
    const replies = await response.json();
    if (!Array.isArray(replies)) throw new Error('Invalid response');
    const texts = replies.filter(r => typeof r.text === 'string' && r.text.trim());
    if (!texts.length) throw new Error('Empty response');
    texts.forEach(r => bubble(r.text,'bot'));
    status.textContent = 'Réponse reçue · Vous pouvez poursuivre la discussion.';
  } catch (error) {
    bubble('Le service est indisponible pour le moment. Vérifiez que les conteneurs sont démarrés, puis réessayez.','bot error');
    status.textContent = 'Message sans réponse. Vous pouvez le renvoyer.';
    input.value = text;
  } finally {
    clearTimeout(timeout); pending = false;
    document.querySelectorAll('button').forEach(b => b.disabled = false);
    input.focus();
  }
}
form.addEventListener('submit', event => { event.preventDefault(); send(input.value); });
document.querySelectorAll('[data-message]').forEach(button => button.addEventListener('click', () => send(button.dataset.message)));
document.querySelector('#reset').addEventListener('click', () => { if (pending) return; sender = sessionId(); messages.replaceChildren(); welcome(); status.textContent = 'Nouvelle session de conversation.'; input.value = ''; input.focus(); });
welcome();


if (pagesPreview) {
  const notice = 'Aperçu de l’interface · Le serveur Rasa n’est pas hébergé sur GitHub Pages. Lancez le projet avec Docker pour discuter.';
  bubble(notice, 'bot');
  status.textContent = notice;
  input.disabled = true;
  input.placeholder = 'Conversation disponible avec le serveur Rasa';
  document.querySelectorAll('#send, [data-message], #reset').forEach(button => button.disabled = true);
}

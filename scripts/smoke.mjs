// Integration check against a running, genuinely trained Rasa service.
const base = process.env.UNIVERSIBOT_URL || 'http://localhost:8080';
const sender = 'smoke-' + crypto.randomUUID();
for (const [message, expected] of [['bonjour', /assistant/i], ['Quels sont les horaires de la bibliothèque ?', /18 h/]]) {
  const response = await fetch(base + '/api/chat', {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({sender,message}),signal:AbortSignal.timeout(65000)});
  if (!response.ok) throw new Error('HTTP ' + response.status);
  const replies = await response.json();
  if (!Array.isArray(replies) || !replies.some(r => expected.test(r.text || ''))) throw new Error('Unexpected response: ' + JSON.stringify(replies));
  console.log('PASS:', message);
}


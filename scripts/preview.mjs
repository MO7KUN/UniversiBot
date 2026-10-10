import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
const assets = new Map([
  ['/', ['index.html', 'text/html; charset=utf-8']],
  ['/app.js', ['app.js', 'text/javascript; charset=utf-8']],
  ['/style.css', ['style.css', 'text/css; charset=utf-8']],
]);
createServer(async (req, res) => {
  const item = assets.get(new URL(req.url, 'http://localhost').pathname);
  if (!item || req.method !== 'GET') { res.writeHead(404); res.end(); return; }
  try {
    const body = await readFile(new URL('../web/' + item[0], import.meta.url));
    res.writeHead(200, {'Content-Type':item[1]}); res.end(body);
  } catch { res.writeHead(500); res.end(); }
}).listen(8090, '127.0.0.1', () => console.log('UniversiBot interface preview: http://localhost:8090'));

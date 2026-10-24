/* Idioma da interface dos apps (Routine).
 *
 * O texto de origem da interface é o português. Quando o aluno escolhe o idioma que estuda,
 * este script carrega /assets/ui/<código>.js (window.ROUTINE_UI[código]) e troca os textos da
 * página — inclusive os que os apps criam depois — por correspondência exata ou por padrão:
 *   exact:    { 'Nova rodada': '새 라운드' }
 *   patterns: [['Acertos na rodada: {n}', '이번 라운드 정답: {n}']]
 * {n} casa só números; {0}, {1}… casam qualquer trecho, que também passa pelo dicionário.
 * Conteúdo de estudo (frases, opções, textos) fica marcado com data-ui-skip ou lang e não muda.
 * Explicações das questões e o guia continuam em português (apoio didático).
 */
(() => {
  'use strict';
  const target = window.ROUTINE_LANGUAGE || 'en';
  const KEY = `routine-ui-lang-${target}`;
  const NATIVE = { en: 'English', ko: '한국어', zh: '中文', es: 'Español', ja: '日本語', fr: 'Français', it: 'Italiano', de: 'Deutsch' };
  const read = () => { try { return localStorage.getItem(KEY); } catch (_) { return null; } };
  const ui = read() === target ? target : 'pt';
  const SKIP = 'script,style,textarea,[data-ui-skip],[contenteditable]';
  const ATTRS = ['placeholder', 'title', 'aria-label'];
  let dict = null;
  let compiled = [];

  const escRe = s => s.replace(/[.*+?^$()|[\]\\]/g, '\\$&');
  function compile(src) {
    const names = [];
    const body = src.split(/(\{n\}|\{\d\})/).map(part => {
      if (part === '{n}') { names.push('n'); return '(\\d+(?:[.,]\\d+)?)'; }
      if (/^\{\d\}$/.test(part)) { names.push(Number(part[1])); return '(.+?)'; }
      return escRe(part).replace(/\{/g, '\\{').replace(/\}/g, '\\}');
    }).join('');
    return { re: new RegExp(`^${body}$`, 's'), names };
  }

  function ensure() {
    if (dict || ui === 'pt' || !window.ROUTINE_UI?.[target]) return;
    dict = window.ROUTINE_UI[target];
    compiled = (dict.patterns || []).map(([src, dst]) => ({ ...compile(src), dst }));
  }

  function translate(text, depth = 0) {
    ensure();
    if (!dict) return null;
    if (Object.hasOwn(dict.exact, text)) return dict.exact[text];
    for (const { re, names, dst } of compiled) {
      const m = text.match(re);
      if (!m) continue;
      let n = 0;
      const nums = [];
      const vars = {};
      names.forEach((name, i) => { if (name === 'n') nums.push(m[i + 1]); else vars[name] = m[i + 1]; });
      return dst.replace(/\{n\}|\{(\d)\}/g, (all, i) => {
        if (all === '{n}') return nums[n++] ?? '';
        const v = vars[i] ?? '';
        return (depth < 2 && translate(v.trim(), depth + 1)) || v;
      });
    }
    // Rótulos compostos ("A1 · Negócios · The short receipt"): traduz cada parte conhecida.
    if (depth < 2 && text.includes(' · ')) {
      const parts = text.split(' · ');
      const out = parts.map(p => translate(p.trim(), depth + 1) ?? p);
      if (out.some((p, i) => p !== parts[i])) return out.join(' · ');
    }
    return null;
  }
  const t = s => (ui === 'pt' ? s : translate(String(s).trim()) ?? s);

  const done = new WeakMap();
  function textNode(node) {
    const raw = node.data;
    if (done.get(node) === raw) return;
    const trimmed = raw.trim();
    if (!trimmed || !/\p{L}/u.test(trimmed) || node.parentElement?.closest(SKIP)) return;
    const out = translate(trimmed);
    if (out != null && out !== trimmed) node.data = raw.replace(trimmed, out);
    done.set(node, node.data);
  }
  function attrs(el) {
    if (el.closest(SKIP)) return;
    for (const a of ATTRS) {
      const v = el.getAttribute(a);
      if (!v) continue;
      const out = translate(v.trim());
      if (out != null && out !== v) el.setAttribute(a, out);
    }
  }
  function walk(root) {
    if (root.nodeType === Node.TEXT_NODE) { textNode(root); return; }
    if (root.nodeType !== Node.ELEMENT_NODE && root.nodeType !== Node.DOCUMENT_NODE) return;
    if (root.nodeType === Node.ELEMENT_NODE) {
      if (root.matches(SKIP)) return;
      attrs(root);
    }
    const tw = document.createTreeWalker(root, NodeFilter.SHOW_TEXT | NodeFilter.SHOW_ELEMENT, {
      acceptNode: n => (n.nodeType === Node.ELEMENT_NODE && n.matches(SKIP) ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT),
    });
    for (let n = tw.nextNode(); n; n = tw.nextNode()) {
      if (n.nodeType === Node.TEXT_NODE) textNode(n);
      else attrs(n);
    }
  }

  function start() {
    ensure();
    if (!dict) return;
    if (dict.title && document.title) document.title = translate(document.title) ?? document.title;
    walk(document.body);
    new MutationObserver(list => {
      for (const m of list) {
        if (m.type === 'characterData') textNode(m.target);
        else if (m.type === 'attributes') attrs(m.target);
        else m.addedNodes.forEach(walk);
      }
    }).observe(document.body, { childList: true, subtree: true, characterData: true, attributes: true, attributeFilter: ATTRS });
  }

  // ------------------------------------------------------------ seletor
  function selector() {
    if (document.getElementById('uiLanguage')) return;
    const wrap = document.createElement('label');
    wrap.className = 'ui-language';
    wrap.setAttribute('data-ui-skip', '');
    wrap.innerHTML = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/></svg>'
      + `<span class="sr-only">Idioma da interface</span><select id="uiLanguage" aria-label="Idioma da interface">`
      + `<option value="pt">Português</option><option value="${target}">${NATIVE[target] || target}</option></select>`;
    const select = wrap.querySelector('select');
    select.value = ui;
    select.title = ui === 'pt' ? 'Idioma da interface' : (NATIVE[target] || target);
    select.addEventListener('change', () => {
      try { localStorage.setItem(KEY, select.value); } catch (_) { /* modo privado */ }
      location.reload();
    });
    const style = document.createElement('style');
    style.textContent = '.ui-language{display:inline-flex;align-items:center;gap:6px;padding:6px 10px;border-radius:999px;border:1px solid var(--line,#d9deea);background:var(--card,#fff);color:var(--ink,#111);font-size:13px;font-weight:600;cursor:pointer}'
      + '.ui-language svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:1.8}'
      + '.ui-language select{border:0;background:transparent;color:inherit;font:inherit;padding:0;cursor:pointer;width:auto;min-height:0;box-shadow:none}'
      + '.ui-language-float{position:fixed;right:14px;bottom:14px;z-index:50;box-shadow:0 8px 24px rgba(0,0,0,.15)}'
      + '.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}';
    document.head.append(style);
    const place = () => {
      const bar = document.querySelector('.cloud-accountbar__actions');
      if (bar) { wrap.classList.remove('ui-language-float'); bar.prepend(wrap); return true; }
      return false;
    };
    if (!place()) {
      wrap.classList.add('ui-language-float');
      document.body.append(wrap);
      const obs = new MutationObserver(() => { if (place()) obs.disconnect(); });
      obs.observe(document.body, { childList: true });
    }
  }

  // Ferramenta de manutenção: com localStorage "routine-ui-collect" = "1", guarda em
  // RoutineUI.missing os textos exibidos que ainda não têm tradução (para completar o dicionário).
  const missing = new Set();
  let collecting = false;
  try { collecting = localStorage.getItem('routine-ui-collect') === '1'; } catch (_) { /* sem storage */ }
  if (collecting) {
    const note = s => { s = s.trim(); if (s && /\p{L}/u.test(s) && translate(s) == null) missing.add(s); };
    const scan = root => {
      if (root.nodeType === Node.TEXT_NODE) { if (!root.parentElement?.closest(SKIP)) note(root.data); return; }
      if (root.nodeType !== Node.ELEMENT_NODE || root.closest(SKIP)) return;
      ATTRS.forEach(a => root.getAttribute(a) && note(root.getAttribute(a)));
      root.querySelectorAll('*').forEach(el => { if (!el.closest(SKIP)) ATTRS.forEach(a => el.getAttribute(a) && note(el.getAttribute(a))); });
      const tw = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
      for (let n = tw.nextNode(); n; n = tw.nextNode()) if (!n.parentElement?.closest(SKIP)) note(n.data);
    };
    document.addEventListener('DOMContentLoaded', () => {
      scan(document.body);
      new MutationObserver(list => list.forEach(m => (m.type === 'characterData' ? scan(m.target) : m.addedNodes.forEach(scan))))
        .observe(document.body, { childList: true, subtree: true, characterData: true });
    });
  }

  window.RoutineUI = { lang: ui, target, t, missing };
  const boot = () => {
    selector();
    if (ui === 'pt') return;
    document.documentElement.lang = target === 'zh' ? 'zh-CN' : target;
    if (window.ROUTINE_UI?.[target]) { start(); return; }
    const s = document.createElement('script');
    s.src = `/assets/ui/${target}.js?v=${window.ROUTINE_UI_VERSION || '1'}`;
    s.onload = start;
    document.head.append(s);
  };
  if (document.body) boot();
  else document.addEventListener('DOMContentLoaded', boot);
})();

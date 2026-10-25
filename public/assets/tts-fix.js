/* Áudio (voz do aparelho) confiável no celular — carregado no <head> de todos os apps.
 *
 * Os apps chamam speechSynthesis.cancel() e .speak() direto. No celular isso falha por três motivos:
 *  1. iPhone/Safari: a voz só é liberada depois de uma fala iniciada por um toque do usuário;
 *     falas automáticas (ex.: "Ouça e escolha") ficam mudas até lá → destravamos no primeiro toque.
 *  2. Chrome/Android: um speak() logo depois de cancel() costuma ser ignorado → esperamos um instante.
 *  3. Chrome/Android: a fala pode ser descartada da memória antes de tocar → guardamos referência.
 * Se a fala não começa em alguns segundos, mostramos um aviso com o que conferir no aparelho.
 */
(() => {
  'use strict';
  const synth = window.speechSynthesis;
  if (!synth || typeof SpeechSynthesisUtterance === 'undefined' || synth.__routineFixed) return;
  synth.__routineFixed = true;
  const nativeSpeak = synth.speak.bind(synth);
  const nativeCancel = synth.cancel.bind(synth);
  const keep = [];
  const dropped = new WeakSet();  // canceladas antes de tocar: não geram aviso
  let lastCancel = 0;
  let unlocked = false;

  function unlock() {
    if (unlocked) return;
    unlocked = true;
    try {
      const u = new SpeechSynthesisUtterance(' ');
      u.volume = 0;
      nativeSpeak(u);
    } catch (_) { /* sem voz: nada a destravar */ }
  }
  ['pointerdown', 'touchend', 'keydown', 'click'].forEach(type => addEventListener(type, unlock, { capture: true, passive: true }));

  synth.cancel = () => { lastCancel = Date.now(); keep.forEach(u => dropped.add(u)); nativeCancel(); };
  synth.speak = utterance => {
    keep.push(utterance);
    if (keep.length > 8) keep.shift();
    watch(utterance);
    const play = () => { if (synth.paused) synth.resume(); nativeSpeak(utterance); };
    if (Date.now() - lastCancel < 150) setTimeout(play, 150);
    else play();
  };

  // Aviso quando a voz não começa (som do aparelho, voz do idioma não instalada…).
  let toast = null;
  function notify() {
    if (toast || !document.body) return;
    toast = document.createElement('div');
    toast.setAttribute('role', 'status');
    toast.style.cssText = 'position:fixed;left:12px;right:12px;bottom:14px;z-index:9999;max-width:520px;margin:auto;padding:14px 16px;border-radius:14px;'
      + 'background:#0f1b33;color:#fff;font:14px/1.45 system-ui,sans-serif;box-shadow:0 12px 30px rgba(0,0,0,.35)';
    toast.innerHTML = '<b>O áudio não começou.</b><br>Confira se o volume de mídia está alto e se o iPhone não está no modo silencioso. '
      + 'No Android, abra Configurações › Idioma › Saída de conversão de texto em voz e baixe a voz do idioma. Depois toque em ouvir de novo.'
      + '<button type="button" style="display:block;margin-top:10px;border:0;border-radius:999px;padding:7px 14px;font:inherit;font-weight:700;cursor:pointer">Entendi</button>';
    toast.querySelector('button').onclick = () => { toast.remove(); toast = null; };
    document.body.append(toast);
  }
  function watch(utterance) {
    if (!String(utterance.text || '').trim() || utterance.volume === 0) return;
    let started = false;
    utterance.addEventListener('start', () => { started = true; });
    utterance.addEventListener('end', () => { started = true; });
    utterance.addEventListener('error', e => { if (!['canceled', 'interrupted'].includes(e.error)) setTimeout(() => { if (!started) notify(); }, 0); });
    setTimeout(() => { if (!started && !dropped.has(utterance) && !synth.speaking) notify(); }, 6000);
  }
})();

from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "english-practice.html"
TARGET = ROOT / "public" / "app.html"
html = SOURCE.read_text(encoding="utf-8")
guard = '<style>html[data-cloud-auth="pending"] body{visibility:hidden}</style><script>document.documentElement.dataset.cloudAuth="pending"</script><script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script><script src="/config.js"></script><script src="/assets/cloud-sync.js?v=20261015-3"></script>'
html = html.replace('</head>', guard + '</head>', 1)
TARGET.write_text(html, encoding="utf-8")
print(f"Gerado: {TARGET}")

#!/usr/bin/env python3
"""Arma index.html de victorgalloo.github.io (perfil profesional de Victor Gallo).

Lee los artículos de ~/victorgallo-com/articulos.json y los recursos públicos de recursos.json.
Uso: python3 gen.py && git add -A && git commit -m "..." && git push
"""
import html
import json
from pathlib import Path

AQUI = Path(__file__).parent
ARTICULOS = Path.home() / "victorgallo-com" / "articulos.json"
URL = "https://victorgalloo.github.io/"

REDES = [
    ("victorgallo.com", "https://victorgallo.com/"),
    ("LinkedIn", "https://www.linkedin.com/in/victorgalloo/"),
    ("Podcast en Spotify", "https://open.spotify.com/show/60qzhpDBnYBmHSvoOHZEcJ"),
    ("Medium", "https://medium.com/@victor_76481"),
    ("X", "https://x.com/victorgallomx"),
    ("TikTok", "https://www.tiktok.com/@victorgallooo"),
    ("Facebook", "https://www.facebook.com/VictorGallogbm"),
    ("GitHub", "https://github.com/victorgalloo"),
]
RAYOS_X = "https://victorgallo.com/rayos-x/?utm_source=github&utm_medium=perfil&utm_campaign=github_pages"

e = html.escape


def main() -> None:
    articulos = json.loads(ARTICULOS.read_text())
    recursos = json.loads((AQUI / "recursos.json").read_text()) if (AQUI / "recursos.json").exists() else []
    lis_art = "\n".join(
        f'      <li><a href="{e(a["url"])}">{e(a["titulo"])}</a><span>{e(a["descripcion"])}</span></li>'
        for a in articulos
    )
    lis_rec = "\n".join(
        f'      <li><a href="{e(r["url"])}">{e(r["titulo"])}</a><span>{e(r["descripcion"])}</span></li>'
        for r in recursos
    )
    redes = " · ".join(f'<a href="{e(u)}" rel="me noopener">{e(n)}</a>' for n, u in REDES)
    ld = {
        "@context": "https://schema.org",
        "@type": "ProfilePage",
        "url": URL,
        "inLanguage": "es-MX",
        "mainEntity": {
            "@type": "Person",
            "@id": "https://victorgallo.com/#victor",
            "name": "Victor Gallo",
            "alternateName": "Victor Jiménez Gallo",
            "jobTitle": "Account Executive",
            "worksFor": {"@type": "Organization", "@id": "https://superleads.mx/#org", "name": "SuperLeads",
                          "url": "https://superleads.mx/"},
            "url": "https://victorgallo.com/",
            "sameAs": [u for _, u in REDES[1:]] + [URL],
        },
    }
    out = f"""<!doctype html>
<html lang="es-MX">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Victor Gallo · Account Executive en SuperLeads · Admisiones con datos</title>
<meta name="description" content="Victor Gallo ayuda a colegios y universidades privadas a inscribir más alumnos, con datos. Account Executive en SuperLeads. Artículos, podcast y recursos.">
<link rel="me" href="https://victorgallo.com/">
<meta property="og:title" content="Victor Gallo · Admisiones con datos">
<meta property="og:description" content="Ayudo a colegios y universidades a inscribir más alumnos, con datos.">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="https://victorgallo.com/assets/og-victor.jpg">
<style>
:root{{--az:#05103a;--tx:#1d2433;--su:#5b6478;--ve:#0f9d58}}
*{{box-sizing:border-box}}body{{margin:0;font:17px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--tx);background:#f7f8fb}}
main{{max-width:760px;margin:0 auto;padding:48px 22px 64px}}
header{{display:flex;gap:22px;align-items:center;flex-wrap:wrap}}
header img{{width:112px;height:112px;border-radius:50%;object-fit:cover}}
h1{{margin:0;font-size:2rem;color:var(--az)}}h2{{margin:40px 0 10px;font-size:1.2rem;color:var(--az)}}
.cargo{{margin:4px 0 0;color:var(--su)}}a{{color:#1a4fd6}}
ul{{list-style:none;padding:0;margin:0}}li{{padding:10px 0;border-bottom:1px solid #e3e6ee}}
li span{{display:block;color:var(--su);font-size:.93rem}}
.cta{{display:inline-block;margin-top:14px;background:var(--ve);color:#fff;padding:11px 18px;border-radius:8px;text-decoration:none;font-weight:600}}
footer{{margin-top:44px;color:var(--su);font-size:.9rem}}
</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<main>
  <header>
    <img src="https://victorgallo.com/assets/victor-gallo.webp" alt="Victor Gallo" width="112" height="112">
    <div>
      <h1>Victor Gallo</h1>
      <p class="cargo">Account Executive en <a href="https://superleads.mx/">SuperLeads</a> · Ayudo a colegios y universidades a inscribir más alumnos, con datos.</p>
    </div>
  </header>

  <h2>Qué hago</h2>
  <p>Hablo todos los días con dueños y directores de colegios y universidades privadas de México sobre su proceso de admisiones: cuántas familias piden informes, cuántas visitan y cuántas se inscriben. Leo esos números como un financiero, porque de ahí vengo: seis años de venta consultiva en banca y mercados de capital (BanBajío, Globant, GBM) antes de llegar a SuperLeads. Certificación AMIB Figura III, Contaduría y Finanzas en la EBC y CS50 de Harvard.</p>
  <p>Lo que aprendo en esas llamadas lo escribo en el Blog SuperLeads y lo cuento en el podcast <em>Admisiones con datos</em>.</p>
  <a class="cta" href="{e(RAYOS_X)}">Agenda tu Rayos X de Inscripciones conmigo</a>

  <h2>Artículos</h2>
  <ul>
{lis_art}
  </ul>
  <p><a href="https://victorgallo.com/articulos/">Todos mis artículos en victorgallo.com</a></p>

  <h2>Podcast</h2>
  <p><a href="https://open.spotify.com/show/60qzhpDBnYBmHSvoOHZEcJ">Victor Gallo · Admisiones con datos</a> (Spotify): cada artículo, narrado en episodios cortos para directores de admisiones.</p>
{"" if not recursos else f'''
  <h2>Recursos públicos</h2>
  <ul>
{lis_rec}
  </ul>
'''}
  <h2>Dónde encontrarme</h2>
  <p>{redes}</p>

  <footer>Página principal: <a href="https://victorgallo.com/">victorgallo.com</a>. Esta es mi página de perfil en GitHub Pages.</footer>
</main>
</body>
</html>
"""
    (AQUI / "index.html").write_text(out)
    print("index.html", len(out), "bytes;", len(articulos), "artículos;", len(recursos), "recursos")


if __name__ == "__main__":
    main()

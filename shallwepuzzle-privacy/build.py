"""Build all nineteen static privacy pages from the shared policy source."""
from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / 'policy.json').read_text())
assert isinstance(data['contact'], str) and '@' in data['contact']
assert data['package'] == 'kr.shall.we.puzzle'
languages = data['languages']
assert len(languages) == 19
labels = {
    'ko': '언어', 'en': 'Language', 'ja': '言語', 'de': 'Sprache',
    'fr': 'Langue', 'es': 'Idioma', 'pt-BR': 'Idioma',
    'zh-Hant': '語言', 'zh-Hans': '语言', 'id': 'Bahasa',
    'th': 'ภาษา', 'vi': 'Ngôn ngữ', 'ms': 'Bahasa', 'fil': 'Wika',
    'my': 'ဘာသာစကား', 'km': 'ភាសា', 'lo': 'ພາສາ', 'tet': 'Lian',
    'ta': 'மொழி',
}

def shape(value):
    if isinstance(value, dict):
        return {key: shape(item) for key, item in value.items()}
    if isinstance(value, list):
        return [shape(item) for item in value]
    return type(value).__name__

def paragraphs(items):
    return ''.join(f'<p>{escape(text)}</p>' for text in items)

def page_path(language):
    return '' if language == 'ko' else language + '/'

for item in languages:
    language = item['code']
    content = data[language]
    assert shape(content) == shape(data['en']), language
    assert [s['id'] for s in content['sections']] == [s['id'] for s in data['en']['sections']]
    prefix = './' if language == 'ko' else '../'
    home = prefix
    alternates = ''.join(
        f'<link rel="alternate" hreflang="{entry["code"]}" href="{prefix}{page_path(entry["code"])}">'
        for entry in languages)
    switcher = ''.join(
        f'<a href="{prefix}{page_path(entry["code"])}" lang="{entry["code"]}" hreflang="{entry["code"]}"'
        + (' aria-current="page"' if entry['code'] == language else '')
        + f'>{escape(entry["name"])}</a>'
        for entry in languages)
    rendered = []
    for section in content['sections']:
        body = paragraphs(section.get('paragraphs', []))
        if section.get('rows'):
            body += '<div class="table-wrap"><table><thead><tr>'
            body += ''.join(f'<th scope="col">{escape(t)}</th>' for t in section['headers'])
            body += '</tr></thead><tbody>'
            for row in section['rows']:
                assert len(row) == len(section['headers']), (language, section['id'])
                body += '<tr>'
                for i, text in enumerate(row):
                    tag = 'th' if i == 0 else 'td'
                    scope = ' scope="row"' if i == 0 else ''
                    label = escape(section['headers'][i], quote=True)
                    body += f'<{tag}{scope} data-label="{label}">{escape(text)}</{tag}>'
                body += '</tr>'
            body += '</tbody></table></div>'
        body += paragraphs(section.get('after', []))
        if section.get('contact'):
            body += f'<p><a href="mailto:{escape(data["contact"])}">{escape(data["contact"])}</a></p>'
        if section.get('sources'):
            body += '<ul>' + ''.join(
                f'<li><a href="{escape(source["url"])}" rel="noreferrer">{escape(source[language])}</a></li>'
                for source in data['sources']) + '</ul>'
        rendered.append(f'<section id="{section["id"]}"><h2>{escape(section["title"])}</h2>{body}</section>')
    toc = ''.join(f'<li><a href="#{s["id"]}">{escape(s["title"])}</a></li>' for s in content['sections'])
    html = f'''<!doctype html>
<html lang="{language}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'self'; script-src 'self'; base-uri 'none'; form-action 'none'">
<meta name="description" content="{escape(data['app'] + ' — ' + content['title'])}">
<title>{escape(data['app'])} | {escape(content['title'])}</title>
<script src="{prefix}app-view.js?v=1"></script>
<link rel="stylesheet" href="{prefix}privacy.css?v=1">
{alternates}
<link rel="alternate" hreflang="x-default" href="{prefix}en/">
</head>
<body>
<a class="skip" href="#policy">{escape(content['skip'])}</a>
<header><a class="brand" href="{home}">ShallWePuzzle</a><nav aria-label="{labels[language]}">{switcher}</nav></header>
<main id="policy">
<h1>{escape(content['title'])}</h1>
<p class="muted">{escape(content['dateLabel'])}: <time datetime="{data['effective']}">{data['effective']}</time></p>
<p>{escape(content['intro'])}</p>
<aside class="summary">{escape(content['summary'])}</aside>
<p>{escape(content['contactLabel'])}: <a href="mailto:{escape(data['contact'])}">{escape(data['contact'])}</a></p>
<nav class="contents" aria-label="{escape(content['contents'])}"><h2>{escape(content['contents'])}</h2><ul>{toc}</ul></nav>
{''.join(rendered)}
</main>
<footer>ShallWePuzzle · kr.shall.we.puzzle · <a href="mailto:{escape(data['contact'])}">{escape(data['contact'])}</a></footer>
</body></html>
'''
    target = ROOT / page_path(language) / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html)
    print(target.relative_to(ROOT))

(ROOT / '.nojekyll').touch()

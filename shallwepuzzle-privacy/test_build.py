"""Focused checks for the multilingual public policy and its generated links."""
from html.parser import HTMLParser
import json
from pathlib import Path
import unittest
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tags = []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

class PolicyPages(unittest.TestCase):
    def test_all_languages_have_full_policy_and_resolvable_links(self):
        data = json.loads((ROOT / 'policy.json').read_text())
        codes = {item['code'] for item in data['languages']}
        self.assertEqual(codes, {
            'ko', 'en', 'ja', 'de', 'fr', 'es', 'pt-BR', 'zh-Hant', 'zh-Hans',
            'id', 'th', 'vi', 'ms', 'fil', 'my', 'km', 'lo', 'tet', 'ta',
        })
        for code in codes:
            with self.subTest(language=code):
                path = ROOT / ('' if code == 'ko' else code) / 'index.html'
                html = path.read_text()
                page = Page(html)
                self.assertIn(('html', {'lang': code}), page.tags)
                sections = {attrs['id'] for tag, attrs in page.tags if tag == 'section'}
                self.assertEqual(sections, {section['id'] for section in data['en']['sections']})
                self.assertEqual(len(sections), 12)
                current = [a for tag,a in page.tags if tag == 'a' and a.get('aria-current') == 'page']
                self.assertEqual(len(current), 1)
                self.assertEqual(current[0]['lang'], code)
                self.assertEqual({a['hreflang'] for t,a in page.tags if t == 'a' and 'hreflang' in a}, codes)
                self.assertIn('app-view.js?v=1', html)
                self.assertNotIn('<iframe', html)
                for tag, attrs in page.tags:
                    link = attrs.get('href', '')
                    parsed = urlsplit(link)
                    if parsed.scheme or parsed.netloc or not link:
                        continue
                    target = (path.parent / parsed.path).resolve() if parsed.path else path
                    if target.is_dir():
                        target /= 'index.html'
                    self.assertTrue(target.is_file(), (code, link))
                    if parsed.fragment:
                        targets = Page(target.read_text()).tags
                        self.assertIn(parsed.fragment, {a.get('id') for _,a in targets})
                for source in data['sources']:
                    self.assertIn(source[code], html)
                    self.assertIn(source['url'], html)
                self.assertIn(data['contact'], html)

if __name__ == '__main__':
    unittest.main()

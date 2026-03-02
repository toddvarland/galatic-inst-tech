from html.parser import HTMLParser
from pathlib import Path


class _Parser(HTMLParser):
    pass


def test_index_html_exists_and_parses():
    html = Path("index.html").read_text(encoding="utf-8")
    _Parser().feed(html)


def test_logo_links_to_homepage_file():
    html = Path("index.html").read_text(encoding="utf-8")
    assert 'href="index.html" class="logo"' in html


def test_no_home_page_nav_label():
    html = Path("index.html").read_text(encoding="utf-8")
    assert ">Home Page<" not in html


def test_required_nav_links_present():
    html = Path("index.html").read_text(encoding="utf-8")
    for sec in ["#about", "#core", "#academics", "#community", "#news"]:
        assert f'href="{sec}"' in html

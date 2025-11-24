import unittest
from crawl import (normalize_url, get_h1_from_html,
                   get_first_paragraph_from_html, get_urls_from_html)


class TestCrawl(unittest.TestCase):
    def test_https(self):
        input_url = "https://blog.boot.dev/path"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    def test_https_trailing_slash(self):
        input_url = "https://blog.boot.dev/path/"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    def test_http(self):
        input_url = "http://blog.boot.dev/path"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    def test_http_trailing_slash(self):
        input_url = "http://blog.boot.dev/path/"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            normalize_url("")

    def test_invalid_url(self):
        with self.assertRaises(ValueError):
            normalize_url("not_a_valid_url")

    def test_get_h1_from_html_basic(self):
        input_body = '<html><body><h1>Test Title</h1></body></html>'
        actual = get_h1_from_html(input_body)
        expected = "Test Title"
        self.assertEqual(actual, expected)

    def test_get_h1_from_html_no_h1(self):
        input_body = '<html><body><p>Test paragraph</p></body></html>'
        actual = get_h1_from_html(input_body)
        expected = ""
        self.assertEqual(actual, expected)

    def test_get_h1_from_html_multiple_h1(self):
        input_body = '''
        <html>
            <body>
                <h1>First Title</h1>
                <h1>Second Title</h1>
            </body>
        </html>
        '''
        actual = get_h1_from_html(input_body)
        expected = "First Title"
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_main_priority(self):
        input_body = '''<html><body>
            <p>Outside paragraph.</p>
            <main>
                <p>Main paragraph.</p>
            </main>
        </body></html>'''
        actual = get_first_paragraph_from_html(input_body)
        expected = "Main paragraph."
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_first_if_no_main(self):
        input_body = '''<html><body>
            <p>First paragraph.</p>
            <p>Second paragraph.</p>
        </body></html>'''
        actual = get_first_paragraph_from_html(input_body)
        expected = "First paragraph."
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_no_p_tag(self):
        input_body = '<html><body><h1>Test Title</h1></body></html>'
        actual = get_first_paragraph_from_html(input_body)
        expected = ""
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_absolute(self):
        input_url = "https://blog.boot.dev"
        input_body = '''
        <html><body>
            <a href="https://blog.boot.dev"><span>Boot.dev</span></a>
        </body></html>
        '''
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://blog.boot.dev"]
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_relative(self):
        input_url = "https://blog.boot.dev"
        input_body = '''
        <html><body>
            <a href="lessons"><span>Boot.dev</span></a>
        </body></html>
        '''
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://blog.boot.dev/lessons"]
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_many_urls(self):
        input_url = "https://blog.boot.dev"
        input_body = '''
        <html><body>
            <a href="https://blog.boot.dev"><span>Boot.dev</span></a>
            <a href="https://blog.boot.dev/absolute"><span>Boot.dev</span></a>
            <a href="relative"><span>Boot.dev</span></a>
        </body></html>
        '''
        actual = get_urls_from_html(input_body, input_url)
        expected = [
            "https://blog.boot.dev",
            "https://blog.boot.dev/absolute",
            "https://blog.boot.dev/relative",
        ]
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_unnormalized(self):
        input_url = "https://blog.boot.dev"
        input_body = '''
        <html><body>
            <a href="https://blog.boot.dev/"><span>Boot.dev</span></a>
        </body></html>
        '''
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://blog.boot.dev/"]
        self.assertEqual(actual, expected)

    def test_get_urls_from_html_no_href(self):
        input_url = "https://blog.boot.dev"
        input_body = '''
        <html><body>
            <a><span>Boot.dev</span></a>
        </body></html>
        '''
        actual = get_urls_from_html(input_body, input_url)
        # with self.assertRaises(Exception):
        #     normalize_url("")
        expected = []
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

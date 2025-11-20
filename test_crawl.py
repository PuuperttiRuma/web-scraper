import unittest
from crawl import normalize_url


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



if __name__ == "__main__":
    unittest.main()
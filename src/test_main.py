import unittest

from main import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_valid_h1(self):
        markdown = "# Hello World"
        self.assertEqual(extract_title(markdown), "Hello World")
    
    def test_no_h1(self):
        markdown = "## Subheader\nSome content"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertTrue("No h1 header found" in str(context.exception))
    
    def test_h1_with_spaces(self):
        markdown = "#    Hello World   "
        self.assertEqual(extract_title(markdown), "Hello World")

if __name__ == '__main__':
    unittest.main()
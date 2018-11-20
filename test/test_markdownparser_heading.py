import unittest
from markdownparser import MarkdownParser

class TestMarkdownParserHeading(unittest.TestCase):

    def setUp(self):
        self.parser = MarkdownParser(use_file=False)

    def test_single_heading_returns_h1(self):
        parse_string = '''
# hello
'''
        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<h1>hello</h1>')

    def test_double_heading_returns_h2(self):
        parse_string = '''
## hello
'''
        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<h2>hello</h2>')
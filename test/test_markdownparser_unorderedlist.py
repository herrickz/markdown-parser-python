import unittest
from markdownparser import MarkdownParser

class TestMarkdownParserUnorderedList(unittest.TestCase):

    def setUp(self):
        self.parser = MarkdownParser(use_file=False)

    def test_unorderedlist_with_two_bullet_points(self):
        parse_string = '''
- first
- second
'''
        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<ul><li>first</li><li>second</li></ul>')
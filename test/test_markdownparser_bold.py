import unittest
from markdownparser import MarkdownParser

class TestMarkdownParserBold(unittest.TestCase):

    def setUp(self):
        self.parser = MarkdownParser(use_file=False)

    def test_bold_strips_star_characters(self):
        parse_string = '**Bold**'

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<strong>Bold</strong>')

    def test_bold_strips_multiple_star_characters(self):
        parse_string = '****Bold****'

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<strong>Bold</strong>')

    
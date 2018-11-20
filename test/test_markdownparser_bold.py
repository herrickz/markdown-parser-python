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

    def test_single_strikethrough_within_bold(self):
        parse_string = '****Bold text with ~~strikethrough~~****'

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<strong>Bold text with <del>strikethrough</del></strong>')

    def test_multiple_strikethrough_within_bold(self):
        parse_string = '****Bold text with ~~multiple~~ ~~strikethroughs~~****'

        markdown_list = self.parser.parse(parse_string)
        
        self.assertEqual(markdown_list[0].to_html(), '<strong>Bold text with <del>multiple</del> <del>strikethroughs</del></strong>')

    def test_italic_single_within_bold_at_end(self):
        parse_string = '****Bold text with *Italic*****'

        markdown_list = self.parser.parse(parse_string)
        
        self.assertEqual(markdown_list[0].to_html(), '<strong>Bold text with <em>Italic</em></strong>')

    def test_italic_multiple_within_bold_at_begin_and_end(self):
        parse_string = '*****Italic* Bold text with *Italic*****'

        markdown_list = self.parser.parse(parse_string)
        
        self.assertEqual(markdown_list[0].to_html(), '<strong><em>Italic</em> Bold text with <em>Italic</em></strong>')
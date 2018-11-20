import unittest
from markdownparser import MarkdownParser

class TestMarkdownParserItalic(unittest.TestCase):

    def setUp(self):
        self.parser = MarkdownParser(use_file=False)

    def test_italic_strips_star_characters(self):
        parse_string = '*Italic*'

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<em>Italic</em>')

    def test_italic_with_single_bold_text_inside_reduces(self):
        parse_string = '*Italic with **Bold** text*'

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<em>Italic with <strong>Bold</strong> text</em>')

    def test_italic_with_multiple_bold_text_inside_reduces(self):
        parse_string = '*Italic with **Bold** and another **Bold** text*'

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<em>Italic with <strong>Bold</strong> and another <strong>Bold</strong> text</em>')

    def test_italic_with_bold_at_start_and_end(self):
        parse_string = '***Bold** inside of italic and at **End***'

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<em><strong>Bold</strong> inside of italic and at <strong>End</strong></em>')
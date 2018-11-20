import unittest
from markdownparser import MarkdownParser

class TestMarkdownParserStrikethrough(unittest.TestCase):

    def setUp(self):
        self.parser = MarkdownParser(use_file=False)

    def test_italic_inside_strikethrough(self):
        parse_string = '~~*strikethrough and italics*~~'

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<del><em>strikethrough and italics</em></del>')

    def test_mixed_bold_italic_inside_strikethrough(self):
        parse_string = '~~***bold and italics***~~'

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<del><em><strong>bold and italics</strong></em></del>')

    def test_strikethrough_multiple_tildas_returns_strikethrough_text(self):
        parse_string = '~~~~multiple strikes~~~~'

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<del>multiple strikes</del>')

    def test_strikethrough_multiple_tildas_and_tilda_in_middle(self):
        parse_string = '~~~~strike ~ through~~~~'

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<del>strike ~ through</del>')

    def test_strikethrough_with_single_bold_inside_reduces_to_strike_and_bold(self):
        parse_string = '~~**strike and bold**~~'

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<del><strong>strike and bold</strong></del>')

    def test_strikethrough_with_multiple_bold_inside_reduces_to_strike_and_bold(self):
        parse_string = '~~**strike** and **bold**~~'

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<del><strong>strike</strong> and <strong>bold</strong></del>')

    def test_strikethrough_with_multiple_italic_reduces_strike_and_italic(self):
        parse_string = '~~*strike* and *italic*~~'

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<del><em>strike</em> and <em>italic</em></del>')

    def test_strikethrough_with_multiple_bold_and_italic_inside_reduces_bold_and_italic(self):
        parse_string = '~~*strike* and *italic* and **bold** and **another bold**~~'

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<del><em>strike</em> and <em>italic</em> and <strong>bold</strong> and <strong>another bold</strong></del>')

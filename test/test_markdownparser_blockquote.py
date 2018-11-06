
import unittest
from markdownparser import MarkdownParser

class TestMarkdownParserBlockQuote(unittest.TestCase):

    def setUp(self):
        self.parser = MarkdownParser(use_file=False)

    def test_blockquote_does_not_capture_greater_than_with_non_whitespace_before(self):
        
        parse_string = '''
textbefore> greater than sign
> capture me
> second line to capture'''

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), 'textbefore> greater than sign')
        self.assertEqual(markdown_list[1].to_html(), '<blockquote>capture me second line to capture </blockquote>')
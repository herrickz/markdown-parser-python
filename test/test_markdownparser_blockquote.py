
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

    def test_blockquote_captures_lines_with_no_greater_than_sign_preceded_by_line_with_greater_than_sign(self):
        parse_string = '''
> first 
    one level
        block
            quote with spaces
        '''

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<blockquote>first one level block quote with spaces </blockquote>')

    def test_blockquote_captures_lines_with_no_spaces_or_greater_than_preceded_by_line_with_greater_than(self):
        parse_string = '''
>blockquote
with
no spaces at beginning
    of
    some lines
    '''
        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<blockquote>blockquote with no spaces at beginning of some lines </blockquote>')

    def test_blockquote_captures_lines_with_three_spaces_at_beginning(self):
        parse_string = '''
   > three spaces
   > starting from here
   and also not beginning with greater than sign
        '''

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<blockquote>three spaces starting from here and also not beginning with greater than sign </blockquote>')

    def test_blockquote_single_and_two_level(self):
        parse_string = '''
>two level blockquote
>>very very basic
        '''

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<blockquote>two level blockquote <blockquote>very very basic </blockquote></blockquote>')

    def test_blockquote_splits_blockquotes_separated_by_line_with_no_bracket_single_and_double_mixed(self):
        parse_string = '''
> first level
>> second
>> no greater than on
next line
>> this should be a new block quote
>> with this in it
and also this
        '''

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<blockquote>first level <blockquote>second no greater than on next line </blockquote><blockquote> this should be a new block quote with this in it and also this </blockquote></blockquote>')

    def test_blockquote_does_not_split_blockquotes_on_one_level_blockquote_between_double_blockquotes(self):
        parse_string = '''
> 1
>> 2
>> 3
> 4
>> 5
>> 6
7
        '''

        markdown_list = self.parser.parse(parse_string)

        self.assertEqual(markdown_list[0].to_html(), '<blockquote>1 <blockquote>2 3 4 5 6 7 </blockquote></blockquote>')

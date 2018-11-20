import unittest
from markdownparser import MarkdownParser

class TestMarkdownParserOrderedList(unittest.TestCase):

    def setUp(self):
        self.parser = MarkdownParser(use_file=False)

    def test_orderedlist_with_two_bullet_points(self):
        parse_string = '''
1. first
2. second
'''

        markdown_list = self.parser.parse(parse_string)

        expected_html = '<ul><li>1. first</li><li>2. second</li></ul>'

        self.assertEqual(markdown_list[0].to_html(), expected_html)

    def test_orderedlist_should_remove_trailing_whitespace(self):
        parse_string = '''
1. spaces here     
2. spaces also here     
'''

        markdown_list = self.parser.parse(parse_string)

        expected_html = '<ul><li>1. spaces here</li><li>2. spaces also here</li></ul>'

        self.assertEqual(markdown_list[0].to_html(), expected_html)

    # TODO: Failing test
#     def test_orderedlist_with_bullet_point_and_sub_bullet_point(self):
#         parse_string = '''
# 1. first bullet point
#     1. sub bullet point
# '''

#         markdown_list = self.parser.parse(parse_string)

#         expected_html = '<ul><li>1. first bullet point</li><ul><li>1. sub bullet point</li></ul></ul>'

#         self.assertEqual(markdown_list[0].to_html(), expected_html)

    # TODO: Failing test
#     def test_orderedlist_first_bullet_point_indented_by_six_spaces(self):
#         parse_string = '''
#       1. first
# '''

#         markdown_list = self.parser.parse(parse_string)

#         expected_html = '<ul><ul><li>1. first</li></ul></ul>'

#         self.assertEqual(markdown_list[0].to_html(), expected_html)

    
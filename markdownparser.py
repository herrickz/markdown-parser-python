from tokens import *

import ply.lex as lex

lex.lex(debug=False)

from grammar import *

import ply.yacc as yacc
yacc.yacc()

class MarkdownParser:
    
    def __init__(self, use_file=True):
        self.use_file = use_file
        markdown_list.clear()

    def parse(self, parse_string=''):

        string_to_parse = ''

        if self.use_file:
            with open('markdown.md', 'r') as markdown_file:
                string_to_parse = markdown_file.read()
        else:
            string_to_parse = parse_string
        
        yacc.parse(string_to_parse.strip())

        return markdown_list
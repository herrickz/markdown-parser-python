from models.heading import Heading
from models.codeblock import CodeBlock
from models.blockquote import BlockQuote
from models.inlinetext import InlineText
from models.orderedlist import OrderedList
from models.unorderedlist import UnorderedList
from inlinetextreducer import InlineTextReducer

markdown_list = []
code_block_id_iter = 0

inline_text_reducer = InlineTextReducer()

def p_statements_multiple(p):
    'statements : statements statement'

def p_statements_single(p):
    'statements : statement'

def p_statement_heading1(p):
    'statement : HEADING1'
    markdown_list.append(Heading(value=p[1], heading_size=1))

def p_statement_heading2(p):
    'statement : HEADING2'
    markdown_list.append(Heading(value=p[1], heading_size=2))

def p_statement_code_block(p):
    'statement : CODEBLOCK'
    global code_block_id_iter
    markdown_list.append(CodeBlock(value=p[1], code_block_id=code_block_id_iter))

    code_block_id_iter += 1

def p_statement_ordered_list(p):
    'statement : ORDERED_LIST'
    markdown_list.append(OrderedList(value=p[1]))

def p_statement_unordered_list(p):
    'statement : UNORDERED_LIST'
    markdown_list.append(UnorderedList(value=p[1]))

def p_statement_newline(p):
    'statement : NEWLINE'

def p_statement_block_quote(p):
    'statement : BLOCKQUOTE'
    markdown_list.append(BlockQuote(value=p[1]))

def p_statement_inline_text(p):
    'statement : inline_text_meta'
    markdown_list.append(InlineText(value=p[1]))

def p_inline_text_meta_many(p):
    'inline_text_meta : inline_text_meta inline_text'
    p[0] = p[1] + p[2]

def p_inline_text_meta_single(p):
    'inline_text_meta : inline_text'
    p[0] = p[1]

def p_inline_text_strike_through(p):
    'inline_text : STRIKE_THROUGH'

    strike_through_inner_text = p[1].replace('~~', '')

    reduced_text = inline_text_reducer.inline_text_reduce_strike(strike_through_inner_text)

    p[0] = f'<del>{reduced_text}</del>'

def p_inline_text_italic(p):
    'inline_text : ITALIC'

    italic_inner_text = p[1][1:-1]

    reduced_text = inline_text_reducer.inline_text_reduce_italic(italic_inner_text)

    p[0] = f'<em>{reduced_text}</em>'

def p_inline_text_italic_bold_inside(p):
    'inline_text : ITALIC_BOLD_INSIDE'

    italic_inner_text = p[1][1:-1]

    reduced_text = inline_text_reducer.inline_text_reduce_italic(italic_inner_text)

    p[0] = f'<em>{reduced_text}</em>'

def p_inline_text_bold(p):
    'inline_text : BOLD'

    stripped_bold_text = p[1].replace('**', '')

    reduced_inner_text = inline_text_reducer.inline_text_reduce_bold(stripped_bold_text)

    p[0] = f'<strong>{reduced_inner_text}</strong>'

def p_inline_text_long_text(p):
    'inline_text : long_text'
    p[0] = p[1]

def p_long_text_many(p):
    'long_text : TEXT long_text'
    p[0] = p[1] + p[2]

def p_long_text_single(p):
    'long_text : TEXT'
    p[0] = p[1]

def p_error(p):
    print(f'Syntax error at: {p.value}')
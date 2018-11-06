
tokens = (
    'HEADING1', 'HEADING2',
    'CODEBLOCK',
    'BLOCKQUOTE',
    'STRIKE_THROUGH',
    'ITALIC', 'ITALIC_BOLD_INSIDE',
    'BOLD',
    'NEWLINE',
    'TEXT',
    'ORDERED_LIST',
    'UNORDERED_LIST',
    'TABLE'
)

def t_HEADING2(t):
    r'[ ]*\#\#.*'
    t.value = t.value.replace('##', '', 1)
    t.value = t.value.strip()

    return t

def t_HEADING1(t):
    r'[ ]*\#.*'
    t.value = t.value.replace('#', '', 1)
    t.value = t.value.strip()

    return t

def t_CODEBLOCK(t):
    r'```[^```]*```'
    
    return t

def t_BLOCKQUOTE(t):
    r'(?<![^\s])\s{0,3}((>.+?)\n)([^\n](.?)\n?)+'

    return t

def t_ORDERED_LIST(t):
    r'[1-9]\..+\n?'

    return t

def t_UNORDERED_LIST(t):
    r'(-\s.+\n?)+'

    return t

def t_STRIKE_THROUGH(t):
    r'(~~){1,}[^\s~].*?[^\s~](~~){1,}'

    return t

def t_ITALIC(t):
    r'\*[^\s\*].*?[^\s\*]\*(?!\*)'

    return t

def t_ITALIC_BOLD_INSIDE(t):
    r'((\*)(((\*\*){1,}.+?(\*\*){1,})|[^\s\*]).*?(((\*\*){1,}.+?(\*\*){1})|[^\s\*])\*)'

    return t

def t_BOLD(t):
    r'(\*\*){1,}(\*.*?\*|[^\s]).*?(\*.*?\*|[^\s])(\*\*){1,}'

    return t

def t_NEWLINE(t):
    r'(\r\n|\r|\n)'
    
    return t

def t_TEXT(t):
    r'.+?'
    
    return t

def t_error(t):
    print(f'Illegal character: {t.value}')
    t.lexer.skip(1)
    
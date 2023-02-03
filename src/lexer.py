import re
import MToken

def lexer(source_code):
    keywords = ["if", "else", "for", "while"]
    token_specification = [
        ("NUMBER",  r'\d+(\.\d*)?'),   # Integer or decimal number
        ("ASSIGN", r'='),           # Assignment operator
        ("END",    r';'),            # Statement separator
        ("ID",     r'[A-Za-z]+'),     # Identifiers
        ("OP",     r'[+\-*]'),       # Arithmetic operators
        ("SKIP",   r'[ \t\n]'),         # Skip over spaces and tabs
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    get_token = re.compile(tok_regex).match
    line_num = 1
    line_start = 0
    for mo in iter(get_token, None):
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value in keywords:
            kind = value
        elif kind == 'SKIP':
            line_start = mo.end()
            continue
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
        yield MToken(kind, value, line_num, mo.start()-line_start)

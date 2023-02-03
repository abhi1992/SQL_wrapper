import ply.yacc as yacc

import MToken

def p_statement_assign(p):
    'statement : ID "=" expression'
    p[0] = ('assign', p[1], p[3])

def p_statement_expr(p):
    'statement : expression'
    p[0] = ('expr', p[1])

def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression'''
    p[0] = (p[2], p[1], p[3])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number', p[1])

def p_expression_id(p):
    'expression : ID'
    p[0] = ('id', p[1])

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

while True:
    try:
        s = input('Input CMD > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)

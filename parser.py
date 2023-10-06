# parser.py
import ply.yacc as yacc
from lexer import tokens


# Definir las reglas del analisis sintactico 

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_mult(p):
    'term : term MULT factor'
    p[0] = p[1] * p[3]
#
def p_term_div(p):
    'term : term DIAG factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : PAR_LEFT expression PAR_RIGHT'
    p[0] = p[2]

def p_comparison_expression(p):
    '''
    comparison_expression : expression LESS_THAN expression
                         | expression GREATER_THAN expression
    '''
    if p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]





# Crea el analizador sintáctico
parser = yacc.yacc()

# Define una función para analizar una expresión
def parse_expression(expression):
    return parser.parse(expression)

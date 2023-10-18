# parser.py
import ply.yacc as yacc
from tokens import tokens


# Definir las reglas del analisis sintactico 
def p_program_declaration(p):
    'program_declaration : PROGRAM ID SEMICOLON'
    # Realiza acciones semánticas para manejar la declaración del programa
    # p[0] podría contener información sobre el programa

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
                         | expression LESS_EQUAL expression
                         | expression GREATER_EQUAL expression
                         | expression DOUBLE_EQUAL expression
                         | expression NOT_EQUAL expression
    '''
    if p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]

def p_function_call(p):
    'function_call : ID t_PAR_LEFT argument_list t_PAR_RIGHT'
    # Realiza acciones semánticas para manejar llamadas a funciones con argumentos variables
    # p[0] podría contener el resultado de la función llamada

def p_argument_list(p):
    'argument_list : argument_list t_COMMA expression'
    # Realiza acciones semánticas para manejar una lista de argumentos separados por comas
    # p[0] podría contener información sobre la lista de argumentos

def p_argument_list_single(p):
    'argument_list : expression'
    # Realiza acciones semánticas para manejar un solo argumento
    # p[0] podría contener información sobre el argumento

def p_function_call_with_array(p):
    'function_call : ID t_PAR_LEFT array_argument t_PAR_RIGHT'
    # Realiza acciones semánticas para manejar llamadas a funciones con argumentos de arreglo
    # p[0] podría contener el resultado de la función llamada

def p_array_argument(p):
    'array_argument : t_BRACKET_LEFT expression t_BRACKET_RIGHT'
    # Realiza acciones semánticas para manejar un argumento de arreglo
    # p[0] podría contener información sobre el argumento de arreglo
#Se define los tipos de funciones que puede utilizar
def p_type(p): 
    '''
    type : INT
         | FLOAT
         | VOID 
    
    '''
#par ala declaracion de arreglos
def p_array_declaration(p):
    '''
    array_declaration : ID '[' NUMBER ']'
    '''
def p_vars_section(p):
    'vars_section : VARS var_declaration_list'
    # Realiza acciones semánticas para manejar la sección de declaraciones globales
    # p[0] podría contener información sobre las declaraciones globales

def p_var_declaration_list(p):
    'var_declaration_list : var_declaration_list var_declaration'
    # Realiza acciones semánticas para manejar una lista de declaraciones globales
    # p[0] podría contener información sobre la lista de declaraciones

def p_var_declaration_list_single(p):
    'var_declaration_list : var_declaration'
    # Realiza acciones semánticas para manejar una sola declaración global
    # p[0] podría contener información sobre la declaración global

def p_var_declaration(p):
    'var_declaration : type ID SEMICOLON'
    # Realiza acciones semánticas para manejar una declaración global
    # p[0] podría contener información sobre la declaración global

def p_if_statement(p):
    '''
    if_statement : IF condition_statement block
    '''
    # Realiza acciones semánticas para manejar la estructura "if"
    # p[0] podría contener información sobre la estructura

def p_else_statement(p):
    '''
    else_statement : ELSE block
    '''
    # Realiza acciones semánticas para manejar la estructura "else"
    # p[0] podría contener información sobre la estructura

def p_write_statement(p):
    '''
    write_statement : WRITE LPAREN argument_list RPAREN SEMICOLON
    '''
    # Realiza acciones semánticas para manejar la estructura "write"
    # p[0] podría contener información sobre la estructura

# Crea el analizador sintáctico
parser = yacc.yacc()

# Define una función para analizar una expresión
def parse_expression(expression):
    return parser.parse(expression)

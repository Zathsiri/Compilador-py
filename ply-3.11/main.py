import ply.lex as lex
import ply.yacc as yacc



#Palabras reservadas

reserved ={
    'function'  :   'FUNCTION',
    'vars'      :   'VARS',
    'program'   :   'PROGRAM',
    'main'      :   'MAIN',
    'void'      :   'VOID',
    'int'       :   'INT',
    'float'     :   'FLOAT',
    'char'      :   'CHAR',
    'if'        :   'IF',
    'else'      :   'ELSE',
    'return'    :   'RETURN',
    'end'       :   'END',
    'read'      :   'READ',
    'write'     :   'WRITE',
    'for'       :   'FOR',
    'while'     :   'WHILE',
    

}

tokens = [
    'ID',  #ID
    'CTEI',#CONSTANTE ENTERA
    'CTEF', #CONSTANTE FLOTANTE
    'CTEC', #CONSTANTE CHAR
    'CTESTRING',#COSNTANTE STRING
    'EQUALS', #=
    'COMPARE',#==
    'PLUS', #+
    'MINUS',#-
    'MUL',#*
    'DIV',#/
    'LT', #LESS THAN <
    'GT', #GREATER THAN >
    'LTE', #LESS THAN OR EQUAL <=
    'GTE', #GRETER THAN OR EQUAL >=
    'AND', #&&
    'OR', #||
    'LPAREN', #(
    'RPAREN', #)
    'COMMA', #,
    'SEMICOLON', 
    'NE', #NOT EQUAL
    'LBRACKET', #[
    'RBRACKET', #]
    'LCURLY', #{
    'RCURLY',#}
    'TRANSPUESTA', 
    'INVERSA',
    'DETERMINANTE', 
    'COMILLA' # ''
] + list(reserved.values())

t_SEMICOLON = r'\;'
t_COMMA = r'\,'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_EQUALS = r'\='
t_COMPARE = r'\=='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMILLA = r'\"'
t_MUL = r'\*'
t_DIV = r'\/'
t_GT = r'\>'
t_LT = r'\<'
t_GTE = r'\>='
t_LTE = r'\<='
t_NE = r'\!=' 
t_AND = r'\&&'
t_OR = r'\|'
t_TRANSPUESTA = r'\¡'
t_DETERMINANTE = r'\$'
t_INVERSA = r'\?'
t_ignore = ' \t\n'

#Identificador de ID's
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    #if t.value in reserved:
    #t.type = reserved[t.value]
    t.type = reserved.get(t.value, 'ID')
    return t

#identificador de INT
def t_CTEI(t):
    #r'\d+'
    r'0|[-+]?[1-9][0-9]*'
    t.value = int(t.value)
    return t

#Identificador de FLOAT
def t_CTEF(t):
    #r'\d+\.\d+'
    r'[-+]?\d*\.\d+'
    t.value = float(t.value)
    return t

#Identificador de STRING
def t_CTESTRING(t):
    r'\'[\w\d\s\,. ]*\'|\"[\w\d\s\,. ]*\"'
    return t

#en el caso de encontrar un error que se despliegue donde 
def t_error(t):
    t.lexer.skip(1)
    lexer = lex.lex()

import ply.lex as lex
import ply.yacc as yacc
from tablaVariables import tabVar, tabFunc
from cuboSem import Cubo
from stack import Stack
from memory import Memo

#Palabras reservadas

reserved ={
    'function'  :   'FUNCTION',
    'var'      :   'VAR',
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
    'for'       :   'FOR', #lo mas probable es que no lo saque
    'while'     :   'WHILE',
    'to'        :   'TO'
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
    'AND', #&
    'OR', #|
    'LPAREN', #(
    'RPAREN', #)
    'COMMA', #,
    'SEMICOLON', 
    'NE', #!=
    'LBRACKET', #[
    'RBRACKET', #]
    'LCURLY', #{
    'RCURLY',#}
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
t_AND = r'\&'
t_OR = r'\|'
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

tablaFunc= tabFunc()   
actualFunType = ''
fid = ''
varId = ''
paramId = '' 

# aqui pondre todas las pilas para cuadruplos para eso cree la clase de Stack



def p_programa(p):
        '''
        programa : PROGRAM ID SEMICOLON addP programa1 
        '''
        global programId
        programId = p[2]
        p[0] = 'PROGRAMA COMPILADO'

def p_addP(p):
    'addP :'
    global actualFunType, fid
    actualFunType = 'programa'
    fid = 'programa'
    global tablaFunc
    tablaFunc.addFunction(actualFunType, fid, 0, [], [], 0)

def p_programa1(p):
    '''
	programa1 : vars quadMain modules main_end programa2
	programa1 : vars quadMain modules
	          | programa2
	'''

def p_programa2(p):
    '''
	programa2 :  main 
	'''   

def p_main(p):
    '''
	main : MAIN save_function LPAREN param2 RPAREN LCURLY vars statement RCURLY END
	'''
    global actualFunType
    actualFunType = p[1]
    global fid
    fid = p[1]
    global tablaFunc
    tablaFunc.addFunction(actualFunType, fid, 0, [], [], 0)



#las 3 tipos de variables aceptadas 
def p_tipo(p):
    '''
    tipo : INT guardaTipoVar
         | FLOAT guardaTipoVar
         | CHAR guardaTipoVar 
    '''
#aqui se guarda el tipo de variable 
def p_guardaTipoVar(p): 
    'guardaTipoVar : '
    global actual_varTipo
    actual_varTipo = p[-1]
         
def p_vars(p):
    '''
    vars : var 
         | empty
    '''     

def p_var(p):
    '''
    var : VAR var2 
    '''        
def p_var1(p):
    '''
        var1 : ID
            | ID COMMA var1 addV
            | ID arr 
            | ID arr COMMA var1 addV 
            | empty 
    '''
    global varId
    varId = p[1]

def p_addV(p):
    'addV :'
    global tablaFunc
    global varId
    global actual_varTipo
    if not varId ==None:

            if tablaFunc.searchTabFunc(fid):
                tablaFunc.addVar(fid, actual_varTipo, varId)
            else:
             SystemExit()
#aqui esta la recursividad para tener diferntes tipos de variables
def p_var2(p):
    '''
        var2 : var2 tip var1 SEMICOLON addV
            | empty

    '''

def p_modules(p):
    '''
    modules : function modules
            | empty
    
    ''' 

def p_save_function(p):
    'save_function : '
    global actualFunType
    global fid
    global tablaFunc

    if p[-1] == 'main':
        actualFunType = 'main'
        fid = p[-1]
        tablaFunc.addFunction(actualFunType, fid, 0, [],[], 0)
    else:
        actualFunType = p[-2]
        fid =p[-1]
        tablaFunc.addFunction(actualFunType, fid, 0, [],[], 0)

def p_function(p):
    '''
    fun : FUNCTION VOID fun1
             | FUNCTION INT fun2
             | FUNCTION FLOAT fun2
    '''
def p_fun1(p):
    '''
    fun1 : ID save_function LPAREN param2 RPAREN SEMICOLON LCURLY vars fun_goto  statement RCURLY end_func 
    '''
def p_fun2(p):
    '''
    fun2 : ID save_function LPAREN param2 RPAREN SEMICOLON LCURLY vars fun_goto  statement RETURN operadorReturn exp quad_return SEMICOLON RCURLY end_func 
    '''


parser = yacc.yacc()

if __name__ =='__main__':
    fileName = 'test1.txt'
    info= fileName.read()
    fileName.close()
    lexer.input(info)
    while True:
        tk = lexer.token()
        if not tk:
            break
    else:
        print("syntax error")
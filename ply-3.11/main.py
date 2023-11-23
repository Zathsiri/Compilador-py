import ply.lex as lex
import ply.yacc as yacc
from disponible import dispo
from tablaVariables import tabVar, tabFunc
from cuboSem import Cubo
from maquinaVirtual import *
from stack import Stack
from memory import Memo
import sys 
import json
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
    'for'       :   'FOR', 
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
    t.type = reserved.get(t.value, 'ID')
    return t

#identificador de INT
def t_CTEI(t):
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

# las pilas para los cuadruplos
stackN= Stack()
stackT= Stack()
operadores = Stack()
cuadrulpos = []
arreglos = []
functions = []
pendientes = 0
end_proc = []
salto_end_proc = 0


countParams=0

#Instanciare objetos para las clases que se utilizan 
cubo = Cubo()
saltos = Stack()
salto_fun = Stack()




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

def p_quadMain(p):
    'quadMain : '
    global saltos, cuadrulpos
    cuad =('GOTOMAIN', 'main', -1, None)
    cuadrulpos.append(cuad)
    saltos.push(len(cuadrulpos)-1)

def p_main_end(p):
    'main_end : '
    end = saltos.pop()
   # llenar_quad(end, -1) 


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
        var2 : var2 tipo var1 SEMICOLON addV
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

def p_fun_goto(p):
    'fun_goto : '
    global functions
    nombre = p[-8]
    salto = (nombre, len(cuadrulpos))
    functions.append(salto)

def p_end_func(p):
    'end_func : '
    global cuadrulpos, tablaFunc

    cuad = ('ENDFUNC',None, None, -1)
    cuadrulpos.append(cuad)
    end_proc.append(len(cuadrulpos)-1)
    tablaFunc.reset_temp_add()

def p_operadorReturn(p):
    'operadorReturn : '
    global operadores
    operadores.push('return')

def p_quad_Return(p):
    'quad_return : '
    global cuadrulpos, stackN, stackT, operadores, actualFunType
    if operadores.size() > 0:
        if operadores.top() == 'return':
            operadores2 = operadores.pop()
            result = stackN.pop()

            cuad = (operadores2, -1, -1, result)
            cuadrulpos.append(cuad)

        else:
            print('Type missmatch')
            
def p_statement(p):
    '''
    statement : statement1 statement
              | empty
    '''

def p_statement1(p):
    '''
    statement : asignacion SEMICOLON
              | llamada SEMICOLON
              | lectura SEMICOLON
              | escritura SEMICOLON
              | if
              | while
    '''

def p_asignacion(p):
    '''
    asignacion : ID saveId2 EQUALS addOperadorName exp genera_quad_asignacion
               | ID saveId2 arr EQUALS addOperadorName exp genera_quad_asignacion
    
    '''

def p_asignacion(p):
     '''
    asignacion : ID saveId2 EQUALS addOperadorName exp genera_quad_asignacion
               | ID saveId2 arr EQUALS addOperadorName exp genera_quad_asignacion
               | ID saveId2 mat EQUALS addOperadorName exp genera_quad_asignacion
    ''' 

def p_genera_quad_asignacion(p):
    'genera_quad_asignacion : '
    global stackT, stackN, operadores, cuadrulpos

    if operadores.size() >0 :
        op = tabFunc.get_op_mem(operadores.top())
        operadores2 = operadores.pop()
        op_d = stackN.pop()
        op_dt = stackT.pop()
        op_i = stackN.pop()
        op_it = stackT.pop()
        res = cubo.getType(op_it, op_dt, operadores2)
        
        if res != 'ERROR':
            cuad = (op_it, op_dt, operadores2)
            cuadrulpos.append(cuad)
        else:
            print('no hay nada :c')
            sys.exit()

def p_addOperadorName(p):
    'addOperadorName : '
    global operadores
    aux = p[-1]
    operadores.push(aux)

def p_param1(p):
    '''
    param1 : ID addParam
           | ID COMMA param1 addParam
           | ID arr
           | ID COMMA param1
           | empty
    '''
    global primerP
    primerP = p[1]

def p_addParam(p):
    'addParam : '
    global tablaFunc, paramId, primerP, actual_varTipo
    paramId = p[-1]
    print("en params entra", paramId)
    print("leyendo->", primerP)
    if not paramId == None and paramId is not None:
        if tablaFunc.searchTabFunc(fid):
            tablaFunc.addParametros_tabFunc(fid, actual_varTipo, primerP)
            tablaFunc.addVar(fid, actual_varTipo, primerP)
            tablaFunc.addParametros_tabFunc(fid, actual_varTipo, paramId)
            tablaFunc.addVar(fid, actual_varTipo, paramId)
            print(paramId, "esta en -> ", fid)
            print(primerP, "el id del parametro esta en ->", fid)
        else:
            SystemExit()

def p_param2(p):
    '''
    param2 : param2 tipo param1
           | empty
    '''

def p_llamada(p):
    '''
    llamada : ID era_call LPAREN aux_exp quad_param RPAREN  gosub_quad llena_endproc
    '''

def p_aux_exp(p):
    '''
    aux_exp : exp
            | exp COMMA aux_exp
            | empty
    '''

def p_quad_param(p):
    '''quad_param : '''
    global cuadrulpos, countParams, nameV, llamadaID, pendientes
    llamadaID = p[.4]
    print("llamadaID->" , llamadaID)
    totalParams = tablaFunc.getNumeroParametros(llamadaID)

    if not stackN.is_empty():
        val = stackN.pop()
        print("Valor del parametro->", val)
        if not countParams == totalParams:
            print("Parametro actualizados ->", totalParams)
            cuad = ('PARAM', val, None, pendientes)
            cuadrulpos.append(cuad)
            stackN.pop()
            countParams +=1
        else:
            print("parametros excedidos")
        
def p_llenar_endproc(p):
    'llena_endproc : '
    global end_proc, salto_end_proc
    end = end_proc().pop
    tempo = list(cuadrulpos[end])
    cuadrulpos[end] = tuple(tempo)

def p_era_call(p):
    'era_call : '
    global cuadrulpos, countParams, nameV
    nameV = p[-1]
    countParams = 0
    cuad = ('ERA', None, None, nameV)
    cuadrulpos.append(cuad)
    saltos.push(len(cuadrulpos)-1)

def p_gosub_quad(p):
    'gosub_quad : '
    global cuadrulpos, functions, salto_end_proc
    gosub_call = p[-6]

    for i in functions:
        if i[0] == gosub_call:
            end = i[1]
    cuad = ('GOSUB', gosub_call, None, end)
    cuadrulpos.append(cuad)
    salto_end_proc = len(cuadrulpos)

# se para detectar y dar las instrucciones de if
def p_if(p):
    '''
    if : IF LPAREN exp RPAREN if_quad LCURLY statement RCURLY else end_if   
    '''
#para las intrucciones del else
def p_else(p):
    '''
    else : ELSE else_quad LCURLY statement RCURLY
         | empty
    '''

def p_for_op(p):
    'for_op : '
    global operadores, cuadrulpos, saltos

    op = tablaFunc.get_op_mem('for')
    operadores.push(op)
    saltos.push(len(cuadrulpos))

def p_for_quad(p):
    'for_quad : '
    global stackN, stackT, cuadrulpos, saltos
    resT = stackT.pop()

    if resT == 'bool':
        valor = stackN.pop()
        cuad =('GOTOV', valor, None, -1)
        cuadrulpos.append(cuad)
        saltos.push(len(cuadrulpos)-1)
    else:
        print('Error en el cuadruplo')
        sys.exit()

def p_for(p):
    '''
    for : FOR for_op LPAREN for1 RPAREN for_quad LCURLY statement RCURLY for_end
    '''
 
def p_for1(p):
    '''
    for1 :   
    '''


#aqui es donde se marca el fin del loop
def p_loop_end(p):
    'loop_end : '
    global stackN, stackT, cuadrulpos, saltos
    end = saltos.pop()
    retro = saltos.pop()
    cuad = ('GOTO', None, None, retro)
    cuadrulpos.append(cuad)
   #llenar_quad(end, retro) 

def p_while_quad(p):
    'while_quad : '
    global stackN, stackT, cuadrulpos, saltos
    tipoRes = stackT.pop()

    if tipoRes == 'bool':
        valor = stackN.pop()
        cuad = ('GOTOF', valor, None, -1)
        print('cuadruplo: ', str(cuad))
        cuadrulpos.append(cuad)
        saltos.push(len(cuadrulpos)-1)

    else:
        print('eroro dentro del cuadruplo del while')
        sys,exit()

def p_while_op(p):
    'while_op :'    
    global operadores, cuadrulpos, saltos
    op = tablaFunc.get_op_mem('while')
    operadores.push(op)
    saltos.push(len(cuadrulpos))

def p_while(p):
    '''
    while : WHILE while_op LPAREN exp RPAREN while_quad LCURLY statement
    '''

def p_escritura(p):
    '''
    escritura : WRITE LPAREN operadorWrite escritura1 operadorWriteQuad RPAREM
    '''
def p_escritura1(p):
    '''
    escritura1 : escritura2 COMMA escritura 2
               | escritura2
    '''
def p_escritura2(p):
    '''
    escritura2 : COMILLA CTESTRING COMILLA
               | CTEI saveCTE operatorWriteQuad
               | CTEF saveCTE operatorWriteQuad
               | exp
    '''
def p_lectura(p):
    '''
    lectura : READ operatorRead LPAREN exp operatorReadQuad RPAREN
    '''


def p_exp(p):
    '''
    exp : nexp
        | nexp OR addOperadorName
    '''

def genera_cuadruplo():
    global operadores, stackN, stackT, cuadrulpos

    if operadores.size() > 0:
        op=tablaFunc.get_op_mem(operadores.top())
        operando2 = operadores.pop()
        op_d= stackN.pop()
        op_dt= stackT.pop()
        op_i= stackN.pop()
        op_it= stackT.pop()

        resT = cubo.getType(op_it, op_dt, operando2)
        if resT !='ERORR':
            res = dispo.next()

        tablaFunc.addTempMem(resT, res, fid)
        varT = tablaFunc.getTemp_mem(res)

        cuad = (op, op_i, op_d, varT)
        cuadrulpos.append(cuad)

        stackN.push(varT)
        stackT.push(resT)

        
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
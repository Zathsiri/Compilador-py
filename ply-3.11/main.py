
import ply.lex as lex
import ply.yacc as yacc
from ply import yacc
from disponible import dispo
from tablaVariables import tabVar, tabFunc
from cuboSem import Cubo
from maquinaVirtual import *
from stack import Stack
from memory import Memo
import sys 
import os

#Palabras reservadas

reserved = {
    'function'  :   'FUNCTION',
    'var'       :   'VAR',
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
    'from'      :   'FROM',
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
    'COMILLA' # ""
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
#t_ignore_COMMENT = r'%%.*'

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

#para poder comentar en el codigo 
#def t_COMMENT(t):
#   r'%%.*'
#  pass

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
primerP = None


countParams=0

#Instanciare objetos para las clases que se utilizan 
cubo = Cubo()
saltos = Stack()
salto_fun = Stack()
dispo_instance = dispo()




def p_programa(p):
    '''
    programa : PROGRAM ID SEMICOLON addP programa1 
    '''
    global programId
    programId = p[2]
    p[0] = 'PROGRAMA COMPILADO'

def p_addP(p):
    'addP : '
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
	main : MAIN save_fun LPAREN param2 RPAREN LCURLY vars statement RCURLY END
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
    llenar_quad(end, -1) 


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
                tablaFunc.addVari(fid, actual_varTipo, varId)
            else:
             SystemExit()

#aqui esta la recursividad para tener diferntes tipos de variables
def p_var2(p):
    '''
        var2 : var2 tipo var1 SEMICOLON addV
            | empty

    '''

def p_arr(p):
    '''
    arr : LBRACKET CTEI RBRACKET
        | LBRACKET exp RBRACKET 
    '''

def p_modules(p):
    '''
    modules : fun modules
            | empty
    
    ''' 

def p_save_fun(p):
    'save_fun : '
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

def p_fun(p):
    '''
    fun : FUNCTION VOID fun1
        | FUNCTION INT fun2
        | FUNCTION CHAR fun2
        | FUNCTION FLOAT fun2
    '''

def p_fun1(p):
    '''
    fun1 :  ID save_fun LPAREN param2 RPAREN SEMICOLON LCURLY vars fun_goto  statement RCURLY end_func
    '''

def p_fun2(p):
    '''
    fun2 : ID save_fun LPAREN param2 RPAREN SEMICOLON LCURLY vars fun_goto  statement RETURN operadorReturn exp quad_return SEMICOLON RCURLY end_func 
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
            res = stackN.pop()

            cuad = (operadores2, -1, -1, res)
            cuadrulpos.append(cuad)

        else:
            print('Type missmatch')
            sys.exit()
            
def p_statement(p):
    '''
    statement : statement1 statement
              | empty
    '''

def p_statement1(p):
    '''
    statement1 : asignacion SEMICOLON
                | llamada SEMICOLON
                | lectura SEMICOLON
                | escritura SEMICOLON
                | for
                | if
                | while
    '''

def p_asignacion(p):
     '''
    asignacion : ID saveId2 EQUALS addOperadorName exp genera_quad_asignacion
               | ID saveId2 arr EQUALS addOperadorName exp genera_quad_asignacion
    ''' 

def p_genera_quad_asignacion(p):
    'genera_quad_asignacion : '
    global stackT, stackN, operadores, cuadrulpos

    if operadores.size() >0 :
        op = tablaFunc.get_op_mem(operadores.top())
        operadores2 = operadores.pop()
        op_d = stackN.pop()
        op_dt = stackT.pop()
        op_i = stackN.pop()
        op_it = stackT.pop()
        res = cubo.getType(op_it, op_dt, operadores2)
        
        if res != 'ERROR':
            cuad = (op, op_d , None, op_i)
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
            tablaFunc.addVari(fid, actual_varTipo, primerP)
            tablaFunc.addParametros_tabFunc(fid, actual_varTipo, paramId)
            tablaFunc.addVari(fid, actual_varTipo, paramId)
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
    llamadaID = p[-4]
    print("llamadaID->" , llamadaID)
    totalParams = tablaFunc.getNumeroParametros(llamadaID)

    if not stackN.is_empty():
        val = stackN.pop()
        print("Valor del parametro->", val)
        if not countParams == totalParams:
            print("Parametro actualizados ->", countParams)
            cuad = ('PARAM', val, None, pendientes)
            operadores.push('PARAM')
            print('PARAM->,', nameV, str(cuad))
            cuadrulpos.append(cuad)
            stackN.pop()
            countParams +=1
        else:
            print("parametros excedidos")
        
def p_llenar_endproc(p):
    'llena_endproc : '
    global end_proc, salto_end_proc
    end = end_proc.pop()
    tempo = list(cuadrulpos[end])
    tempo[3] = salto_end_proc
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
    cuad = ('GOSUB', gosub_call, None, end) #type: ignore
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
    resT = stackN.pop()

    if resT == 'bool':
        val = stackN.pop()
        cuad = ('GOTOV', val, None, -1)
        cuadrulpos.append(cuad)
        saltos.push(len(cuadrulpos)-1)
    else:
        print("error en el cuadruplo del for")
        sys.exit()

def p_for(p):
    '''
    for : FOR for_op LPAREN for1 RPAREN for_quad LCURLY statement RCURLY for_end
    '''
 
def p_for1(p):
    '''
    for1 : FROM asignacion TO exp
    '''
#aqui es donde se marca el fin del loop
def p_loop_end(p):
    'loop_end : '
    global stackN, stackT, cuadrulpos, saltos
    end = saltos.pop()
    retro = saltos.pop()
    cuad = ('GOTO', None, None, retro)
    cuadrulpos.append(cuad)
    llenar_quad(end, retro) 

def p_for_end(p):
    'for_end : '
    global stackN, stackT, cuadrulpos, saltos
    end = saltos.pop()
    retro = saltos.pop()
    retro = int(retro) + 1
    cuad = ('GOTO', None, None, retro)
    cuadrulpos.append(cuad)
    llenar_quad(end, retro)


def p_while_quad(p):
    'while_quad : '
    global stackN, stackT, cuadrulpos, saltos
    resT = stackT.pop()

    if resT == 'bool':
        val = stackN.pop()
        cuad = ('GOTOF', val, None, -1)
        print('cuad:', str(cuad))
        cuadrulpos.append(cuad)
        saltos.push(len(cuadrulpos)-1)
    else:
        print('Error en el cuadruplo del while')
        sys.exit()


def p_while_op(p):
    'while_op :'    
    global operadores, cuadrulpos, saltos
    op = tablaFunc.get_op_mem('while')
    operadores.push(op)
    saltos.push(len(cuadrulpos))

def p_while(p):
    '''
    while : WHILE while_op LPAREN exp RPAREN while_quad LCURLY statement loop_end
    '''

def p_escritura(p):
    '''
    escritura : WRITE LPAREN operadorWrite escritura1 operadorWriteQuad RPAREN
    '''
def p_escritura1(p):
    '''
    escritura1 : escritura2 COMMA escritura2
               | escritura2
    '''
def p_escritura2(p):
    '''
    escritura2 : COMILLA CTESTRING COMILLA
               | CTEI saveCTE operadorWriteQuad
               | CTEF saveCTE operadorWriteQuad
               | exp
    '''
def p_lectura(p):
    '''
    lectura : READ operatorRead LPAREN exp operatorReadQuad RPAREN
    '''


def p_exp(p):
    '''
    exp : nexp
        | nexp OR addOperadorName nexp genera_quad_or
    '''

def genera_cuadruplo():
    global operadores, stackN, stackT, cuadrulpos
    if operadores.size() > 0:
        op = tablaFunc.get_op_mem(operadores.top())
        op2 = operadores.pop()
        op_d = stackN.pop()
        op_dt = stackT.pop()
        op_i = stackN.pop()
        op_it = stackT.pop()

        resT = cubo.getType(op_it, op_dt,op2)
        if resT != 'ERROR':
            res = dispo_instance.next()

            tablaFunc.addTempMem(resT, res, fid)
            vartempo = tablaFunc.getTemp_mem(res)
            cuad =(op, op_i, op_d, vartempo)
            cuadrulpos.append(cuad)
            stackN.push(vartempo)
            stackT.push(resT)
        else:
            print('no se pudo generar :c')
    else:
        print('pila de operadores vacia')
    
def p_genera_quad_or(p):
    'genera_quad_or : '
    global operadores
    if operadores.size()> 0:
        if operadores.top()== '|':
            genera_cuadruplo()

def p_genera_quad_and(p):
    'genera_quad_and :'
    if operadores.size()> 0:
        if operadores.top() == '&':
            genera_cuadruplo()

def p_compare_quad(p):
    'compare_quad : '
    global operadores
    if operadores.size() > 0:
        if operadores.top() == '<' or operadores.top() == '>' or operadores.top() == '<=' or operadores.top() == '>=' or operadores.top() == '==' or operadores.top() == '!=':
            genera_cuadruplo()

def p_if_quad(p):
    'if_quad : '
    global stackN, stackT, cuadrulpos, saltos
    resT = stackT.pop()
    
    if resT=='bool':
        valor = stackN.pop()
        cuad=('GOTOF', valor, None, -1)
        cuadrulpos.append(cuad)
        saltos.push(len(cuadrulpos)-1)

    else:
        print('Error en el cruadruplo de IF')
        sys.exit()

def p_end_if(p):
    'end_if : '
    global saltos
    end = saltos.pop()
    llenar_quad(end, -1)


def p_else_quad(p):
    'else_quad : '
    global cuadrulpos, saltos
    cuad = ('GOTO', None, None, -1)
    cuadrulpos.append(cuad)
    elsAux = saltos.pop()
    saltos.push(len(cuadrulpos)-1)
    llenar_quad(elsAux, -1)

def llenar_quad(end, cont):
    global cuadrulpos
    temp = list(cuadrulpos[end])
    temp[3] = len(cuadrulpos)
    cuadrulpos[end] = tuple(temp)

def p_nexp(p):
    '''
    nexp : compexp
         | compexp AND addOperadorName compexp genera_quad_and    
    '''

def p_compexp(p):
    '''
    compexp : sumexp
            | compexp1 sumexp
    ''' 

def p_compexp1(p):
    '''
    compexp1 : sumexp GT addOperadorName sumexp compare_quad
             | sumexp LT addOperadorName sumexp compare_quad
             | sumexp GTE addOperadorName sumexp compare_quad
             | sumexp LTE addOperadorName sumexp compare_quad
             | sumexp NE addOperadorName sumexp compare_quad
             | sumexp COMPARE addOperadorName sumexp compare_quad
    ''' 


def p_sumexp(p):
    '''
    sumexp : mulexp 
           | mulexp PLUS addOperadorName mulexp genera_sum_quad
           | mulexp MINUS addOperadorName mulexp genera_sum_quad
    '''    

def p_genera_sum_quad(p):
    'genera_sum_quad : '
    global operadores
    if operadores.size() > 0:
        if operadores.top()== '+' or operadores.top() == '-':
            genera_cuadruplo()

def p_genera_quad_mul(p):
    'genera_mul_quad : '
    global operadores
    if operadores.size() > 0:
        if operadores.top() == '*' or operadores.top() == '/':
            genera_cuadruplo()

def p_operadorWrite(p):
    'operadorWrite : '
    global operadores
    operadores.push('write')

def p_operadorWriteQuad(p):
    'operadorWriteQuad : '
    global operadores
    if operadores.size() > 0:
        if operadores.top()== 'write':
            op =tablaFunc.get_op_mem('write')
            operadorAux = operadores.pop()
            valor = stackN.pop()
            cuad = (op, None, None, valor)
            cuadrulpos.append(cuad)

def p_operatorRead(p):
    'operatorRead : '
    global operadores
    operadores.push('read')


def p_operatorReadQuad(p):
    'operatorReadQuad : '
    global operadores
    if operadores.size() > 0:
        if operadores.top() == 'read':
            op = tablaFunc.get_op_mem('read')
            op_aux = operadores.pop()
            valor = stackN.pop()
            stackT.pop()
            cuad = (op, None, None, valor)
            cuadrulpos.append(cuad)

def p_mulexp(p):
    '''
    mulexp : pexp 
           | pexp MUL addOperadorName pexp genera_mul_quad
           | pexp DIV addOperadorName pexp genera_mul_quad
    '''


def p_pexp(p):
    '''
    pexp : var1 saveId 
         | CTEI saveCTE
         | CTEF saveCTE
         | CTEC saveCTE
         | CTESTRING saveCTE  
         | llamada
         | LPAREN exp RPAREN
    '''


def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def p_saveId(p):
    '''saveId :'''
    global varId, tablaFunc, fid, stackN, stackT, pendientes
    if not varId == None:
        if tablaFunc.searchVarTabFunc(fid, varId):
            tipos = tablaFunc.getVarTipo(varId, fid)
            
            tablaFunc.addVarMem(tipos, varId, fid)
            varMemo = tablaFunc.getVarMem(varId)
            print("variable-> ", varId, varMemo)

            if paramId == varId:
                print("same")
                pendientes = varMemo

            if tipos:
                stackT.push(tipos)
                stackN.push(varMemo)
                print("direccion -> ", varId, "->", varMemo)

            else:
                SystemExit()

def p_saveId2(p):
    '''saveId2 : '''
    global varId, tablaFunc, fid, stackN, stackT
    varId = p[-1]

    if tablaFunc.searchVarTabFunc(fid, varId):
        tipo =tablaFunc.getVarTipo(varId,fid)
        memov = tablaFunc.getVarMem(varId)

        stackT.push(tipo)
        stackN.push(memov)
    else:
        SystemExit()

def p_saveCTE(p):
    '''saveCTE : '''
    global cte, t, cteA, arreglos
    cte = p[-1]
    t = type(cte)

    tablaFunc.add_cte_mem(cte)

    cte_address = tablaFunc.get_cte_mem(cte)
    cteA = (cte, cte_address)

    if not cteA in arreglos:
        arreglos.append(cteA)
    else:
        "Esta constante ya existe "

    if(t == int):
        stackT.push('int')
        stackN.push(cte_address)

    elif(t == float):
        stackT.push('float')
        stackN.push(cte_address)

    else:
        stackT.push('char')
        stackN.push(cte_address)



def p_error(p):
    if p is not None:
        print(f"syntax error en el input {p.value!r}, línea {p.lineno}, posición {find_column(p)}")
    else:
        print("final inesperado en el input")
#aqui te medio ayuda con la sintaxis de las pruebas te intenta la ubicacion del error 

def find_column(p):
    last_cr = lexer.lexdata.rfind('\n', 0, p.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (p.lexpos - last_cr) + 1
    return column     

        
parser = yacc.yacc()

if __name__ =='__main__':
    try:
        # Get the current working directory
        print("Current Working Directory:", os.getcwd())
    
        archivo = 'ply-3.11/prueba1.txt'
        print(archivo)
        # Check if the file exists
        if os.path.exists(archivo):
            arc = open(archivo, 'r')
            info = arc.read()
            arc.close()

            lexer.input(info)
            while True:
                tok = lexer.token()
                if not tok:
                    break

            if parser.parse(info, tracking=True) == 'Compilacion completa':
                print("Sintaxis correcta")

                f = open('cuadruplos.txt', 'w')
                for i in cuadrulpos:
                    f.write(str(i) + '\n')
                f.close()

                c = open("const.txt", 'w')
                for i in arreglos:
                    c.write(str(i) + '\n')
                c.close()

                # Ponemos a funcionar la maquina virtual
                mv = MaVi()
                mv.rebuildCte()
                q = mv.clear_quad()
                mv.reading(q)
        else:
            print(f"Error: File '{archivo}' not found.")

    except EOFError:
        print("EOFError")
else:
    print("Syntax error")
# Definición de tokens
tokens = (
    'NEWLINE',
    'SEMICOLON',
    'PAR_LEFT',
    'PAR_RIGHT',
    'BRACKET_LEFT',
    'BRACKET_RIGHT',
    'PERIOD',
    'COLON',
    'PLUS',
    'MINUS',
    'MULT',
    'DIAG',
    'PERC',
    'LESS_THAN',
    'GREATER_THAN',
    'AND',
    'OR',
    'EQUAL',
    'DOUBLE_EQUAL',
    'NOT_EQUAL',
    'LESS_EQUAL',
    'GREATER_EQUAL',
    'ID',
    'DIGIT_INTEGER',
    'DIGIT_DECIMAL',
    'INT',
    'FLOAT',
    'VOID',
    'CHAR',
    'PROGRAM',
    'VARS',
    'LEFT_BRACE',
    'RIGHT_BRACE',
    'IF',
    'ELSE',
    'WRITE'


)

# Definición de reglas para tokens
t_NEWLINE = r'\\n'
t_SEMICOLON = r';'
t_PAR_LEFT = r'\('
t_PAR_RIGHT = r'\)'
t_PERIOD = r'\.'
t_COLON = r':'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIAG = r'/'
t_PERC = r'%'
t_COMMA = r','
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_AND = r'&'
t_OR = r'\|'
t_EQUAL = r'='
t_NOT_EQUAL = r'!='
t_LESS_EQUAL = r'<='
t_GREATER_EQUAL = r'>='
t_DOUBLE_EQUAL = r'=='
t_BRACKET_LEFT = r'\['  # Corchete izquierdo
t_RBRACKET_RIGHT = r'\]'  # Corchete derecho
t_ID = r'[a-zA-Z][a-zA-Z0-9]*'
t_DIGIT_INTEGER = r'[0-9]+'
t_DIGIT_DECIMAL = r'[0-9]+\.[0-9]+'
t_LEFT_BRACE = r'\{'
t_RIGHT_BRACE = r'\}'

# Tokens para tipos de datos
t_INT = r'int'
t_FLOAT = r'float'
t_VOID = r'void'
t_CHAR = r'char'
#Token para la funcion 
t_FUNCTION = r'function'
#token del programa 
t_PROGRAM = r'program'
#token de la declariacion de las variables
t_VARS = r'vars'
# Expresiones regulares para los tokens
t_IF = r'if'
t_ELSE = r'else'
#Token del write 
t_WRITE = r'write'

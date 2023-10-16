# Definición de tokens
tokens = (
    'NEWLINE',
    'SEMICOLON',
    'PAR_LEFT',
    'PAR_RIGHT',
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
    'NOT_EQUAL',
    'LESS_EQUAL',
    'GREATER_EQUAL',
    'ID',
    'DIGIT_INTEGER',
    'DIGIT_DECIMAL',
    'INT',
    'FLOAT',
    'VOID'
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
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_AND = r'&'
t_OR = r'\|'
t_EQUAL = r'='
t_NOT_EQUAL = r'!='
t_LESS_EQUAL = r'<='
t_GREATER_EQUAL = r'>='
t_ID = r'[a-zA-Z][a-zA-Z0-9]*'
t_DIGIT_INTEGER = r'[0-9]+'
t_DIGIT_DECIMAL = r'[0-9]+\.[0-9]+'

# Tokens para tipos de datos
t_INT = r'int'
t_FLOAT = r'float'
t_VOID = r'void'
#Token para la funcion 
t_FUNCTION = r'function'
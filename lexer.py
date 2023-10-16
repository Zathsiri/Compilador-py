#Author: Gilberto Berttolini Alvarado

import ply.lex as lex
from tokens import tokens


#Definicion de reglas para algunos tokens especificos
#para el ID
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    return t

#Para el numero entero
def t_INTERGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#para numeros con decimales
def t_DIGIT_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

#Ignorar espacios en blanco y saltos de linea
t_ignore = ' \t\n'

#Funcion para manejar los errores lexicos
def t_error(t):
    print("Error lexico: Caracter no valid '%s'" % t.valeu[0])
    t.lexer.skip(1)

# Regla para caracteres no válidos
def t_error(t):
    print("Error léxico: Carácter no válido '%s'" % t.value[0])
    t.lexer.skip(1)  # Omitir el carácter no válido

# Regla para comentarios con "%%"
def t_COMMENT(t):
    r'%%.*'
    pass  # Los comentarios se omiten y no se devuelven como tokens

# Regla para manejar el final del archivo (EOF)
def t_eof(t):
    # Realizar alguna acción si es necesario al llegar al final del archivo
    return None

# Creación del analizador léxico
lexer = lex.lex()

#prueba de analizador lexico
if __name__ == "__main__":
    lexer = lex.lex()
    while True:
        data = input("Ingrese una expresión: ")
        lexer.input(data)
        for token in lexer:
            print(token)

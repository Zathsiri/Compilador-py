class Memo:
    def __init__(self):
    #aqui se pondran los diccionarios para las varibles 
        self.globales   = {}
        self.constantes = {}
        self.locales    = {}
        self.temporales = {}
        self.operadores = {
                '+' : 1,
                '-' : 2,
                '*' : 3,
                '/' : 4,
                '<' : 5,
                '>' : 6,
                '<=' : 7,
                '>=' : 8,
                '==' : 9,
                '!=' : 10,
                '&&' : 11,
                '||' : 12,
                '=' : 13,
                'for' : 14, # no estoy esperando sacar el codigo del for pero por si acaso lo pondre
                'while' : 15, 
                'read' : 16,
                'print' : 17,
                'GOTO' : 18,
                'GOTOF' : 19,
                'GOTOV' : 20,
                'ERA' : 21,
                'GOSUB' : 22,
                'return': 23,
                'ENDPROC' : 24,
                'VER': 25,
                'END': 26, 
        }

#GLOBALES 
        self.gint = 1000  # Rango permitido: 1000 a 2999
        self.gfloat = 3000  # Rango permitido: 3000 a 4999
        self.gchar = 5000  # Rango permitido: 5000 a 6999
        self.gbool = 7000  # Rango permitido: 7000 a 8999
#TEMPORALES


#LOCALES


#CONSTANTES
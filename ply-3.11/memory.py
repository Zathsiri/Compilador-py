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

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
                '&' : 11,
                '|' : 12,
                '=' : 13,
                'for' : 14, # no estoy esperando sacar el codigo del for pero por si acaso lo pondre
                'while' : 15, 
                'read' : 16,
                'write' : 17,
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
        self.tint = 11000  # Rango permitido: 11000 a 12999
        self.tfloat = 13000  # Rango permitido: 13000 a 14999
        self.tchar = 15000  # Rango permitido: 15000 a 16999
        self.tcool = 17000  # Rango permitido: 17000 a 18999

#LOCALES
        self.lint = 23000  # Rango permitido: 23000 a 25999
        self.lfloat = 26000  # Rango permitido: 26000 a 28999
        self.lchar = 29000  # Rango permitido: 29000 a 30999
        self.lbool = 31000  # Rango permitido: 31000 a 32999

#CONSTANTES
        self.ctei = 45000  # Rango permitido: 45000 a 45999
        self.ctef = 46000  # Rango permitido: 46000 a 46999
        self.ctec = 47000  # Rango permitido: 47000 a 47999
        self.cteString = 48000  # Rango permitido: 48000 a 48999

# Funciones para la ejecucion 
def value_to_memory(self, address, value):
        if address >= 1000 and address < 9000: 
            if address < 3000:
                self.globales[address] = value
           
            elif address < 5000:
                self.globales[address] = value
            
            elif address < 7000:
                self.globales[address] = value
            
            else: 
                self.globales[address] = value
        
        
        elif address >= 23000 and address <= 31000:
            if address < 26000 and address >= 23000:
                self.locales[address] = value
           
            elif address < 29000 and address >=26000:
                self.locales[address] = value
            
            elif address < 31000 and address >= 29000:
                self.locales[address] = value
            
            elif address < 33000 and address >= 31000:
                self.locales[address] = value
           
            else:
                print("index out of range")
            
        elif address >= 45000 and address <49000:
            if address < 46000:
                self.constants[address] = value
            elif address <47000:
                self.constants[address] = value
            elif address <48000:
                self.constants[address] = value  
            elif address <49000:
                self.constants[address] = value    
            else:
                print("index out of range")  
        else:
            if address < 19000 and address >= 11000: 
                if address < 13000 and address >= 11000:
                    self.temporal[address] = value
                
                elif address < 15000 and address >= 13000:
                    self.temporal[address] = value
                
                
                elif address < 17000 and address >= 15000:
                    self.temporal[address] = value
               
                
                elif address < 19000 and address >= 17000:
                    self.temporal[address] = value
                
                else:
                    print("Out of range")  


def value_from_memory(self, address):
        if address < 9000:
            if address < 3000 and address >= 1000:
                 return self.globales[address]
           
            elif address < 5000 and address >= 3000:
                return self.globales[address]
    
            elif address < 7000 and address >= 5000:               
                return self.globales[address]
            
            elif address < 9000 and address >= 7000:     
                return self.globales[address]
            else:
                print ("index ouf range") 

                
        elif address >= 23000 and address < 33000:
            
            if address < 26000 and address >= 23000:               
                if address in self.locales:
                    return self.locales[address]
        
            elif address < 29000 and address >= 26000: 
                return self.locales[address]

            elif address < 31000 and address >= 29000:
                return self.locales[address]

            elif address < 33000 and address >= 31000:
                return self.locales[address]
            
            else:
                print("index out of range")
                
        elif address < 49000 and address >=45000:
            if address <46000:
                return self.constants[address]
           
            elif address <47000:
                return self.constants[address]
           
            elif address <48000:
                return self.constants[address]
            
            elif address < 49000:
                return self.constants[address]
            
            else:
                print("index out of range")
        
        else:   
            if address < 13000:
                    return self.temporal[address]
            
            elif address < 15000:
                    return self.temporal[address]
            
            elif address < 17000:
                    return self.temporal[address]
            
            elif address < 19000:
                    return self.temporal[address]
            else:
                print("index ouf of range")

#Funciones de asegnacion de memoria 
def set_var_direction(self, tipo, id, funId):
        #VARIABLES GLOBALES
        if funId == 'programa':
            if tipo == 'int':
                if self.gint <3000:
                    address = self.gi
                    self.gint += 1
                else:
                    print("index out of range")
                    
            elif tipo == 'float':
                if self.gfloat < 5000:
                    address = self.gfloat
                    self.gfloat += 1

                else:
                    print("index out of range")

            elif tipo == 'char':
                if self.gchar < 7000:
                    address = self.gchar
                    self.gchar += 1
                else:
                    print("index out of range")

            else:
                if self.gbool < 9000:
                    address = self.gbool
                    self.gbool += 1
         
        
        else:
            if tipo == 'int':

                if self.lint <26000:
                    address = self.lint
                    self.lint += 1
                else:
                    print("index out of range")

            elif tipo == 'float':
                if self.lfloat < 29000:
                    address = self.lfloat
                    self.lfloat += 1

                else:
                    print("index out of range")
                    
            elif tipo == 'char':
                if self.lchar < 31000:
                    address = self.lchar
                    self.lchar += 1
                    
                else:
                    print("index out of range")

            else:
                if self.lbool < 33000:
                    address = self.lbool
                    self.lbool += 1

        return address

#Manejo de constantes

def set_cte(self, val):
        if isinstance(val, int):
            if(self.ctei < 46000):
                address = self.ctei
                self.ctei += 1

        
        elif isinstance(val, float):
            if self.ctef < 47000:
                address = self.ctef
                self.ctef += 1

        elif isinstance(val, str):
            if len(val)<2:
                if self.ctec < 48000:
                    address = self.cteString
                    self.ctec += 1
                    
            else:
                if self.cteString < 49000:
                    address = self.cteString
                    self.cteString += 1
                    
        return address 
    
def set_var_address(self, tipo, vid, funId):
        if self.get_var_address(vid) == -1:    
            ad = self.set_var_direction(tipo, vid, funId)
            self.locales[vid] = {
                'address': ad
            }

def get_var_address(self, temp):
        if temp in self.locales.keys():
            return self.locales[temp]['address']
        else:
            return -1
        
def set_temp_address(self, tipo, vid, funId):
        if self.get_temp_address(vid) == -1:           
            ad = self.set_temp_direction(tipo, vid, funId)
            self.temporal[vid] = {
                'address': ad
            }

def get_temp_address(self, temp):
        if temp in self.temporal.keys():
            return self.temporal[temp]['address']
        else:
            return -1
    


def set_cte_address(self, val):
        if self.get_cte_address(val) == -1:
            ad = self.set_cte(val)
            self.constants[val] = {
            'address': ad
            }
        
        
def get_cte_address (self, val):
        if val in self.constants.keys():
            return self.constants[val]["address"]       
        else:
            return -1
    
def get_operator_address(self, op):
        if op in self.operators.keys():
            return self.operators[op]
        
#Reseteo las direcciones de los temporales 
        self.liint = 23000
        self.lfloat = 26000
        self.lchar = 29000
        self.lbool = 31000
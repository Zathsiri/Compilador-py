class Memo:
    def __init__(self):
    #aqui se pondran los diccionarios para las varibles 
        self.globales   = {}
        self.constantes = {}
        self.locales    = {}
        self.temporales = {}
        self.operadores ={
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
                'for' : 14,
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
        self.tbool = 17000  # Rango permitido: 17000 a 18999

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
                self.constantes[address] = value
            elif address <47000:
                self.constantes[address] = value
            elif address <48000:
                self.constantes[address] = value  
            elif address <49000:
                self.constantes[address] = value    
            else:
                print("index out of range")  
        else:
            if address < 19000 and address >= 11000: 
                if address < 13000 and address >= 11000:
                    self.temporales[address] = value
                        
                elif address < 15000 and address >= 13000:
                    self.temporales[address] = value
                        
                        
                elif address < 17000 and address >= 15000:
                    self.temporales[address] = value
                    
                        
                elif address < 19000 and address >= 17000:
                    self.temporales[address] = value
                        
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
                return self.constantes[address]
                
            elif address <47000:
                return self.constantes[address]
                
            elif address <48000:
                return self.constantes[address]
                    
            elif address < 49000:
                return self.constantes[address]
                    
            else:
                print("index out of range")
                
        else:   
            if address < 13000:
                    return self.temporales[address]
                    
            elif address < 15000:
                    return self.temporales[address]
                    
            elif address < 17000:
                    return self.temporales[address]
                    
            elif address < 19000:
                    return self.temporales[address]
            else:
                print("index ouf of range")

        #Funciones de asegnacion de memoria 
    def set_var_direction(self, tipo, id, funId, size):
        #VARIABLES GLOBALES
        #print ("variable a guardar", tipo, id, funId, size)
        if funId == 'programa':
            print("estoy guardando global ")
            if tipo == 'int':
                if self.gint <3000:
                    address = self.gint
                    self.gint += size
                    print("rango" , address , self.gint )
                else:
                    print("index out of range")
                            
            elif tipo == 'float':
                if self.gfloat < 5000:
                    address = self.gfloat
                    self.gfloat += size
    
                else:
                    print("index out of range")

            elif tipo == 'char':
                if self.gchar < 7000:
                    address = self.gchar
                    self.gchar += size
                else:
                    print("index out of range")

            else:
                if self.gbool < 9000:
                    address = self.gbool
                    self.gbool += size
                
                #variables locales
        else:
            if tipo == 'int':

                if self.lint <26000:
                    address = self.lint
                    self.lint += size
                else:
                    print("index out of range")

            elif tipo == 'float':
                if self.lfloat < 29000:
                    address = self.lfloat
                    self.lfloat += size

                else:
                    print("index out of range")
                            
            elif tipo == 'char':
                if self.lchar < 31000:
                    address = self.lchar
                    self.lchar += size
                            
                else:
                    print("index out of range")

            else:
                if self.lbool < 33000:
                    address = self.lbool
                    self.lbool += size
        print("id2", id, "address", address)
        return address
                        
    def set_temp_direction(self, tipo, id, funId):
        if tipo == 'int':
            if self.tint <13000:
                address = self.tint
                self.tint += 1

            else:
                    print("index out of range")

        elif tipo == 'float':
            if self.tfloat < 15000:                
                address = self.tfloat
                self.tfloat += 1
            else:
                    print("index out of range")
                            
        elif tipo == 'char':
            if self.tchar < 17000:
                address = self.tchar                 
                self.tchar += 1            
            else:
                print("index out of range")
                    
        else:
            if self.tbool < 20000:                   
                address = self.tbool
                self.tbool += 1
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
            
    def set_var_address(self, tipo, vid, funId, size):
        if self.get_var_address(vid) == -1:    
            ad = self.set_var_direction(tipo, vid, funId, size)
            print("estoy guardando", vid)
            self.locales[vid] = {
            'address': ad
            }

    def get_var_address(self, temp):
        if temp in self.locales.keys():
            print("esta en locales", temp)
            for key, value in self.locales.items():
                print (key, value)
            return self.locales[temp]['address']
        else:
            return -1

    def get_var_global(self,temp):

        if temp in self.globales.keys():
            return self.globales[temp]['address']
        else: 
            return -1
                
    def set_temp_address(self, tipo, vid, funId):
        if self.get_temp_address(vid) == -1:           
            ad = self.set_temp_direction(tipo, vid, funId)
            self.temporales[vid] = {
            'address': ad
            }

    def get_temp_address(self, temp):
        if temp in self.temporales.keys():
            return self.temporales[temp]['address']
        else:
            return -1
            

    def set_cte_address(self, val):
        if self.get_cte_address(val) == -1:
            ad = self.set_cte(val)
            self.constantes[val] = {
            'address': ad
            }
                
                
    def get_cte_address (self, val):
        if val in self.constantes.keys():
            return self.constantes[val]["address"]       
        else:
            return -1
            
    def get_operator_address(self, op):
        if op in self.operadores.keys():
            return self.operadores[op]
                
    def p_reset_temp_vals(self):
        self.lint = 23000
        self.lfloat = 26000
        self.lchar = 29000
        self.lbool = 31000
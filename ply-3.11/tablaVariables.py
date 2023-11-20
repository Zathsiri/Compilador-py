from memory import Memo

class tabVar:
    def __init__(self):
        self.var_list ={}
             
    def add(self, tipo, id, address):
        self.var_list[id] ={
            'tipo': tipo,
            'address': address
        }
        
    def searchVars(self, id):
        return id in self.var_list.keys()
    
    def printVars(self):
        print(self.var_list.items())

    def getTipo(self, id):
        return self.var_list[id]['tipo']

#tabla de funciones 

class tabFunc():
    
    #constructor de la clase con un diccionario para las funciones y su objeto de memoria
    def __init__(self):
        self.funciones= {}
        self.mem = Memo()
    
    #crea la funcion y la agrega
    def addFunction(self,tipo, id, nParams, tParams, idParams, nVars):
        if self.funciones.get(id) == None:
            self.funciones[id]= {
                'tipo' : tipo,  #el tipo de nuestra funcion 
                'nParams' : nParams, #numer de parametrps de la funcion
                'tParams' : tParams, #el tipó de parametro 
                'idParams' : idParams, #El nombre del parametro
                'vars' :    tabVar(),
                'nVars' : nVars #numero de vairables 
            }
    
    #busca el nombre de una funcion en especifico
    def search_tabFunc(self, id):
        return id in self.funciones
    
    #busca el nombre de una variable
    def searchVarTabFunc(self, fid, id):
        if self.funciones[fid]['vars'].searchVars(id) or self.funciones['programa'][vars].searchVars(id):
            return True
        else:
            print('variable', id, ' inexistente')

    #busca el tipo de una variable  y verifica donde debe de ir 
    def getVarTipo(self, id, fid):
        if self.funciones[fid]['vars'].searchVars(id):
            return self.funciones[fid][vars].getTipo(id)
        else:
            print('variable', id, ' inexistente')
    
    #esta funcion agrega una varible
    def addVar(self, fid, tipo, id):
        if self.funciones[fid]['vars'].searchVars(id):
            print('La variable', id, ' ya existe en el scope', fid)
    
     # si no existe en el local aun lo agrego
        elif not self.funciones[fid]['vars'].searchVars(id):
            ad = self.m.set_var_direction(tipo, id, fid)
            self.funciones[fid]['vars'].add(tipo, id, ad)
            self.funciones[fid]['nVars'] = self.funciones[fid]['nVars'] + 1
    
    # si existe como global no lo agrego y aviso que ya estaba
        elif self.funciones['programa']['vars'].searchVars(id):
            print('La variable', id, ' ya existe en el programa como global')
        
    # si no existe como global lo agrego como global
        elif self.funciones['programa']['vars'].searchVars(id):
            ad = self.m.set_var_direction('programa', id, fid)
            self.funciones['programa']['vars'].add(tipo, id, ad)
            self.funciones['programa']['nVars'] = self.funciones[fid]['nVars'] + 1

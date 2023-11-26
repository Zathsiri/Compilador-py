from memory import Memo

class tabVar:
   
    def __init__(self):
        self.var_list ={}
             
    def addVar(self, tipo, id, address):
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
    def searchTabFunc(self, id):
        return id in self.funciones
    
    #busca el nombre de una variable
    def searchVarTabFunc(self, fid, id):
        if self.funciones[fid]['vars'].searchVars(id) or self.funciones['programa']['vars'].searchVars(id):
           return True
        else:
            print('variable ->', id, 'no esta presente') 
   
    #busca el tipo de una variable  y verifica donde debe de ir 
    def getVarTipo(self, id, fid):
        if self.funciones[fid]['vars'].searchVars(id) or self.funciones['programa']['vars'].searchVars(id):
            return self.funciones[fid]['vars'].getTipo(id)
        else:
            print('variable->', id, 'no esta presente')


    #esta funcion agrega una varible
    def addVari(self, fid, tipo, id):
        if self.funciones[fid]['vars'].searchVars(id):
            print('variable->', id, ' ya se encuentra en el scope')
        #si todavia no esta en la memoria local la agrego a esta 
        elif not self.funciones[fid]['vars'].searchVars(id):
           addV = self.mem.set_var_address(tipo, id, fid)
           self.funciones[fid]['vars'].addVar(tipo, id, addV)
           self.funciones[fid]['nvars'] = self.funciones[fid]['nvars'] + 1

        #si existe como una global, no la agrego
        elif self.funciones['programa']['vars'].searchVars(id):
            print('variable->', id, 'ya se encuentra como un programa global')

        #si todavia esta no esta, ahora si la agrego
        elif self.funciones['programa']['vars'].searchVars(id):
            addV = self.mem.set_var_direction('programa', id, fid)
            self.funciones['programa']['vars'].addVar(tipo, id, addV)
            self.funciones['programa']['nvars'] = self.funciones[fid]['nvars'] + 1


     #se agrega la variable a la direccion de memoria 
    def addVarMem(self, tipo, vid, funId):
        self.mem.set_var_address(tipo, vid, funId)    
        
    #se obtiene la direccion de memoria de la variable
    def getVarMem(self, var):
        return self.mem.get_var_address(var)

    #se obitiene el numero de parametros 
    def getNumeroParametros(self, fid):
        return self.funciones[fid]['nParams']

    def addParametros_tabFunc(self, fid, NVar, TVar):
        self.funciones[fid]['nParams'] =self.funciones[fid]['nParams']+ 1
        self.funciones[fid]['idParams'].append(NVar)
        self.funciones[fid]['tParams'].append(TVar)


    #se agregan los temporales a la tabla de memoria 
    def addTempMem(self, tipo, vid, funId):
        self.mem.set_temp_address(tipo, vid, funId)    
        
    #se obtiene la direccion del temporal de memoria 
    def getTemp_mem(self, temp):
        return self.mem.get_temp_address(temp)
        
    #se agrega  y obtienen constantes
    def add_cte_mem(self, val):
        self.mem.set_cte_address(val)
        

    def get_cte_mem(self, val):
        return self.mem.get_cte_address(val) 
    

    def get_op_mem(self, op):
        return self.mem.get_operator_address(op)

    #resetep de los temporales      
    def reset_temp_add(self):
        self.mem.p_reset_temp_vals()

    # Print de una variable      
    def print_fun_vars(self, fid):
        if fid in self.funciones:
            self.funciones[fid]['vars'].printVars()

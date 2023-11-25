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
        if fid in self.funciones:
            print(f"Función {fid} encontrada")
            if 'vars' in self.funciones[fid]:
                print(f"Variable 'vars' encontrada en la función {fid}")
                if tabVar.searchVars(self.funciones[fid]['vars'], id):
                    print(f"Variable {id} encontrada en la función {fid}")
                    return True
                else:
                    print(f'Error: variable {id} no encontrada en la función {fid}')
                    return False
            else:
                print(f'Error: No hay variable "vars" en la función {fid}')
                return False
        else:
            print(f'Error: función {fid} inexistente')
            return False

    def print_vars(self):
        print(self.funciones.items())
   
    #busca el tipo de una variable  y verifica donde debe de ir 
    def getVarTipo(self, id, fid):
        if fid in self.funciones:
            print(f"Función {fid} encontrada")
            if 'vars' in self.funciones[fid]:
                print(f"Variable 'vars' encontrada en la función {fid}")
                if tabVar.searchVars(self.funciones[fid]['vars'], id):
                    print(f"Variable {id} encontrada en la función {fid}")
                    return tabVar.getTipo(self.funciones[fid]['vars'], id)
                else:
                    print(f'Error: variable {id} no encontrada en la función {fid}')
                    return None  # o maneja el error según tu lógica
            else:
                print(f'Error: No hay variable "vars" en la función {fid}')
                return None  # o maneja el error según tu lógica
        else:
            print(f'Error: función {fid} inexistente')
            return None  # o maneja el error según tu lógica
    
    #esta funcion agrega una varible
    def addVari(self, fid, tipo, id):
        vars_func = self.funciones[fid]['vars']
        vars_programa = self.funciones['programa']['vars']

        if tabVar.searchVars(vars_func, id):
            print(f'La variable {id} ya existe en el scope {fid}')
        elif not tabVar.searchVars(vars_func, id):
            ad = self.mem.set_var_direction(tipo, id, fid)
            tabVar.addVar(vars_func, tipo, id, ad)
            self.funciones[fid]['nVars'] += 1
        elif tabVar.searchVars(vars_programa, id):
            print(f'La variable {id} ya existe en el programa como global')
        elif not tabVar.searchVars(vars_programa, id):
            ad = self.mem.set_var_direction(tipo, id, 'programa')
            tabVar.addVar(vars_programa, tipo, id, ad)
            self.funciones['programa']['nVars'] += 1
     
     
     #se agrega la variable a la direccion de memoria 
    def addVarMem(self, tipo, vid, funId):
        self.mem.set_var_address(tipo, vid, funId)    
        
    #se obtiene la direccion de memoria de la variable
    def getVarMem(self, var):
        return self.mem.get_var_address(var)

    #se obitiene el numero de parametros 
    def getNumeroParametros(self, fid):
        return self.funciones[fid]['nParams']

    #se agregan lso paramaertos  a la tabla de funciones 
    def addParametros_tabFunc(self, fid, nameVar, varTipo):
        self.funciones[fid]['nParams'] = self.funciones[fid]['nParams'] + 1
        self.funciones[fid]['idParams'].append(nameVar)
        self.funciones[fid]['tParams'].append(varTipo)
    
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
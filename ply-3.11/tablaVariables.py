class tabVar:
    def __init__(self):
        self.var_list ={}
             
    def add(self, tipo, id, address):
        self.var_list[id] ={
            'tipo': tipo,
            'address': address
        }
        
    def search_vars(self, id):
        return id in self.var_list.keys()
    
    def print_vars(self):
        print(self.var_list.items())

    def get_Tipo(self, id):
        return self.var_list[id]['tipo']

#crear aqui la tabla de Funciones y agregar ? 
import memory
import sys


class MaVi():
    def __init__(self):
        self.cuads = []
        self.iterators = []
        self.pending = []
        self.pendingDirection = []
        self.memo = memory.Memo()
        self.start_time = 0
        self.instructionPointer = 0
        self.activation_record = []

    def rebuildCte(self):
        with open('const.txt', 'r') as cteList:
            lines = []
            for line in cteList:
                lines.append(eval(line))
            
            for line in lines:
                self.memo.value_to_memory(line[1], line[0])

    def clear_quad(self):
        with open('cuadruplos.txt', 'r') as cuadList:
            cuads = []
            for line in cuadList:
                cuads.append(eval(line))
            return cuads
    
    def reading (self, cuads):  
        while self.instructionPointer != len(cuads):
            if cuads[self.instructionPointer][0] == self.memo.get_operator_address('+'):
                self.plus(cuads[self.instructionPointer])
                self.instructionPointer += 1
                
            elif cuads[self.instructionPointer][0] == self.memo.get_operator_address('-'):
                self.minus(cuads[self.instructionPointer])
                self.instructionPointer += 1
                
            elif cuads[self.instructionPointer][0] == self.memo.get_operator_address('*'):
                self.multi(cuads[self.instructionPointer])
                self.instructionPointer += 1
                
            elif cuads[self.instructionPointer][0] == self.memo.get_operator_address('/'):
                self.division(cuads[self.instructionPointer])
                self.instructionPointer += 1
            
            elif cuads[self.instructionPointer][0] == self.memo.get_operator_address('<'):
                self.LT(cuads[self.instructionPointer])
                self.instructionPointer += 1
                    
            elif cuads[self.instructionPointer][0] == self.memo.get_operator_address('>'):
                self.GT(cuads[self.instructionPointer])   
                self.instructionPointer +=1
                
            elif cuads[self.instructionPointer][0] == self.memo.get_operator_address('<='):
                self.LTE(cuads[self.instructionPointer])
                self.instructionPointer += 1
                
            elif cuads[self.instructionPointer][0] == self.memo.get_operator_address('>='):
                self.GTE(cuads[self.instructionPointer])
                self.instructionPointer += 1
                
            elif cuads[self.instructionPointer][0] == self.memo.get_operator_address('=='):
                self.compare(cuads[self.instructionPointer])
                self.instructionPointer += 1   
                
            elif cuads[self.instructionPointer][0] == self.memo.get_operator_address('!='):
                self.NE(cuads[self.instructionPointer])
                self.instructionPointer += 1
                
            elif cuads[self.instructionPointer][0] == self.memo.get_operator_address('&'):
                self.andcomp(cuads[self.instructionPointer])
                self.instructionPointer += 1

            elif cuads[self.instructionPointer][0] == self.memo.get_operator_address('|'):
                self.orcomp(cuads[self.instructionPointer])
                self.instructionPointer += 1
        
            elif cuads[self.instructionPointer][0] == self.memo.get_operator_address('='):
                self.asignacion(cuads[self.instructionPointer])
                self.instructionPointer += 1
                
            elif cuads[self.instructionPointer][0] == self.memo.get_operator_address('read'):
                self.inputOP(cuads[self.instructionPointer]) 
                self.instructionPointer += 1

            elif cuads[self.instructionPointer][0] == self.memo.get_operator_address('print'):
                self.writing(cuads[self.instructionPointer]) 
                self.instructionPointer += 1
                
            elif cuads[self.instructionPointer][0] == 'GOTO':
                self.goto(cuads[self.instructionPointer])
                            
            elif cuads[self.instructionPointer][0] == 'GOTOF':
                self.gotof(cuads[self.instructionPointer])
                
            elif cuads[self.instructionPointer][0] == 'GOTOV':
                self.gotov(cuads[self.instructionPointer])
                
            elif cuads[self.instructionPointer][0] == 'GOSUB':
                self.goto(cuads[self.instructionPointer])
                
            elif cuads[self.instructionPointer][0] == 'ERA':
                self.era(cuads[self.instructionPointer])
                
            elif cuads[self.instructionPointer][0] == 'ENDFUNC':
                self.goto(cuads[self.instructionPointer])
            
            elif cuads[self.instructionPointer][0] == 'GOTOMAIN':
                self.gotomain(cuads[self.instructionPointer])
              
            elif cuads[self.instructionPointer][0] == 'PARAM':
                print('ENTRO A PARAM en VM', cuads[2])
                self.param(cuads[self.instructionPointer])
            else: 
                sys.exit()
    
        
#operadores logicos 

    def GT(self, cuads):
        # Obtener valores de memoria para los operandos
        operand1 = self.memo.value_from_memory(cuads[1])
        operand2 = self.memo.value_from_memory(cuads[2])

        # Comparación y asignación del resultado
        if operand1 is not None and operand2 is not None:
            if operand1 > operand2:
                self.memo.value_to_memory(cuads[3], True)
            else:
                self.memo.value_to_memory(cuads[3], False)
        else:
            print("Error: Al menos uno de los operandos es None.")
            # Otra lógica de manejo de error si es necesario
    def LT(self, cuads):
        operand1 = self.memo.value_from_memory(cuads[1])
        operand2 = self.memo.value_from_memory(cuads[2])

        # Comparación y asignación del resultado
        if operand1 is not None and operand2 is not None:
            if operand1 < operand2:
                self.memo.value_to_memory(cuads[3], True)
            else:
                self.memo.value_to_memory(cuads[3], False)
        else:
            print("Error: Al menos uno de los operandos es None.")
    
    def GTE(self, cuads):
        operand1 = self.memo.value_from_memory(cuads[1])
        operand2 = self.memo.value_from_memory(cuads[2])

        # Comparación y asignación del resultado
        if operand1 is not None and operand2 is not None:
            if operand1 >= operand2:
                self.memo.value_to_memory(cuads[3], True)
            else:
                self.memo.value_to_memory(cuads[3], False)
        else:
            print("Error: Al menos uno de los operandos es None.")


    def LTE(self, cuads):
        operand1 = self.memo.value_from_memory(cuads[1])
        operand2 = self.memo.value_from_memory(cuads[2])

        # Comparación y asignación del resultado
        if operand1 is not None and operand2 is not None:
            if operand1 <= operand2:
                self.memo.value_to_memory(cuads[3], True)
            else:
                self.memo.value_to_memory(cuads[3], False)
        else:
            print("Error: Al menos uno de los operandos es None.")
    
    def NE(self, cuads):
        if self.memo.value_from_memory(cuads[1]) != self.memo.value_from_memory(cuads[2]):
           self.memo.value_to_memory(cuads[3], True)
        else:
           self.memo.value_to_memory(cuads[3], False)
    
    def compare(self, cuads):
        if self.memo.value_from_memory(cuads[1]) == self.memo.value_from_memory(cuads[2]):
           self.memo.value_to_memory(cuads[3], True)
        else:
           self.memo.value_to_memory(cuads[3], False)
    #&
    def andcomp(self, cuads):
        if self.memo.value_from_memory(cuads[1]) and self.memo.value_from_memory(cuads[2]):
           self.memo.value_to_memory(cuads[3], True)
        else:
           self.memo.value_to_memory(cuads[3], False)
    #|
    def orcomp(self, cuads):
        if self.memo.value_from_memory(cuads[1]) or self.memo.value_from_memory(cuads[2]):
           self.memo.value_to_memory(cuads[3], True)
        else:
           self.memo.value_to_memory(cuads[3], False)
 
  # write
    def writing(self, cuads):
        if isinstance(cuads[1], str):
            print(cuads[1])
        else:
            print(self.memo.value_from_memory(cuads[3]))

# input
    def inputOP(self, cuads):
        inputMV = input()
        if inputMV.isdigit():
            self.memo.value_to_memory(cuads[3], int(inputMV))
        
        elif inputMV.replace('.','',1).isdigit():
            self.memo

        else:
            self.memo.value_to_memory(cuads[3], inputMV)


#operadores artimetico

    def multi(self, cuads):
        operand1 = self.memo.value_from_memory(cuads[1])
        operand2 = self.memo.value_from_memory(cuads[2])

        if operand1 is not None and operand2 is not None:
            result = operand1 * operand2
            self.memo.value_to_memory(cuads[3], result)
        else:
            print("Error: Al menos uno de los operandos es None.")

    def division(self, cuads):
        operand1 = self.memo.value_from_memory(cuads[1])
        operand2 = self.memo.value_from_memory(cuads[2])

        if operand1 is not None and operand2 is not None:
            result = operand1 / operand2
            self.memo.value_to_memory(cuads[3], result)
        else:
            print("Error: Al menos uno de los operandos es None.")

    def plus(self, cuads):
        operand1 = self.memo.value_from_memory(cuads[1])
        operand2 = self.memo.value_from_memory(cuads[2])

        if operand1 is not None and operand2 is not None:
            result = operand1 + operand2
            self.memo.value_to_memory(cuads[3], result)
        else:
            print("Error: Al menos uno de los operandos es None.")
    
    def minus(self, cuads):
        operand1 = self.memo.value_from_memory(cuads[1])
        operand2 = self.memo.value_from_memory(cuads[2])

        if operand1 is not None and operand2 is not None:
            result = operand1 - operand2
            self.memo.value_to_memory(cuads[3], result)
        else:
            print("Error: Al menos uno de los operandos es None.")
    
    def asignacion(self, cuads):
        self.memo.value_to_memory(cuads[3], self.memo.value_from_memory(cuads[3]))

#saltos

    def gotof(self, cuads):
        if not self.memo.value_from_memory(cuads[1]):
            self.instructionPointer = int(cuads[3])
        else:
            self.instructionPointer +=1
    
    def goto(self, cuads):
        self.instructionPointer = int(cuads[3])
    
    def gotov(self, cuads):
        if not self.memo.value_from_memory(cuads[1]):
            self.instructionPointer = int(cuads[3])
        else:
            self.instructionPointer +=1
    
    def gotomain(self, cuads):
        self.instructionPointer = int(cuads[3])
    
    def returnV(self, cuads):
        self.memo.value_to_memory(cuads[3], self.memo.value_from_memory(cuads[1]))
        self.instructionPointer +=1

    def era(self, cuads):
        self.instructionPointer +=1
    
    def param(self, cuads):
        if cuads[2] == None:
            self.memo.value_to_memory(cuads[3], self.memo.value_from_memory(cuads[1]))
            self.instructionPointer +=1
    
    

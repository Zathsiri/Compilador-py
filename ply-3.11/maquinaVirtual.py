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
        with open('constantantes.txt', 'r') as cteList:
            lines = []
            for line in cteList:
                lines.append(eval(line))
            
            for line in lines:
                self.memo.value_to_memory(line[1], line[0])


#operadores artimetico

    def multi(self, cuad):
        tempo = self.memo.value_from_memory(cuad[1]) * self.memo.value_from_memory(cuad[2])
        self.memo.value_to_memory(cuad[3], tempo)

    def division(self, cuad):
        tempo = self.memo.value_from_memory(cuad[1]) / self.memo.value_from_memory(cuad[2])
        self.memo.value_to_memory(cuad[3], tempo)

    def plus(self, cuad):
        tempo = self.memo.value_from_memory(cuad[1]) + self.memo.value_from_memory(cuad[2])
        self.memo.value_to_memory(cuad[3], tempo)
    
    def minus(self, cuad):
        tempo = self.memo.value_from_memory(cuad[1]) - self.memo.value_from_memory(cuad[2])
        self.memo.value_to_memory(cuad[3], tempo)
    
    def asignacion(self, cuad):
        self.memo.value_to_memory(cuad[3], self.memo.value_from_memory(cuad[3]))

#saltos

    def gotof(self, cuad):
        if not self.memo.value_from_memory(cuad[1]):
            self.instructionPointer = int(cuad[3])
        else:
            self.instructionPointer +=1
    
    def goto(self, cuad):
        self.instructionPointer = int(cuad[3])
    
    def gotov(self, cuad):
        if not self.memo.value_from_memory(cuad[1]):
            self.instructionPointer = int(cuad[3])
        else:
            self.instructionPointer +=1
    
    def gotomain(self, cuad):
        self.instructionPointer = int(cuad[3])
    
    def returnV(self, cuad):
        self.memo.value_to_memory(cuad[3], self.memo.value_from_memory(cuad[1]))
        self.instructionPointer +=1

    def era(self, cuad):
        self.instructionPointer +=1
    
    def param(self, cuad):
        if cuad[2] == None:
            self.memo.value_to_memory(cuad[3], self.memo.value_from_memory(cuad[1]))
            self.instructionPointer +=1

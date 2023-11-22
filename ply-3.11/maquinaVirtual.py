import memory

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

    

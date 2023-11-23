class dispo(object):
    def __init__(self):
        self.dispo = 0
        self.tmem = 'T'

    def next(self):
        self.dispo += 1
        return self.tmem + str(self.dispo)
        
    def clear(self):
        self.dispo = 0
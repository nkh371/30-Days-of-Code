class Student(Person):
    def __init__(self,first,last,id1,scores):
        Person.__init__(self,first,last,id1)
        self.ar = scores
        
    def calculate(self):
        size = len(self.ar)
        c = 0
        for i in self.ar:
            c += i
        c = c / size
        if  c >= 90:
            return 'O'
        elif c >= 80:
            return 'E'
        elif c >= 70:
            return 'A'
        elif c >= 55:
            return 'P'
        elif c >= 40:
            return 'D'
        else:
            return 'T'

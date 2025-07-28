class Wizard():
    def __init__ (self, name):
        if not name:
            raise ValueError
        self.name = name

#put Wizard in the parameter means let Student inherence the Wizard
class Student(Wizard):
    def __init__ (self,name,house):
        if not name:
            raise ValueError
        self.name = name
        self.house = house

class Professor(Wizard):
    def __init__ (self,name,subject):
        if not name:
            raise ValueError
        self.name = name
        self.subject = subject

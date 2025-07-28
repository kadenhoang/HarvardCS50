class Wizard():
    def __init__ (self, name):
        if not name:
            raise ValueError
        self.name = name

#put Wizard in the parameter means let Student inherence the Wizard
class Student(Wizard):
    def __init__ (self,name,house):
        super().__init__(name)
        self.house = house

# super() let me access the initialized value "name" in the mother class "Wizard"
class Professor(Wizard):
    def __init__ (self,name,subject):
        super().__init__(name)
        self.subject = subject


def main():
    student = Student()

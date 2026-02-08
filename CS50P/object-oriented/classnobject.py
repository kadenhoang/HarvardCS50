class Student:
    #a function in a class is called Method

    
    def __init__(self,name,house): #constructor to initialize variables of the object
        #self = this in Java, refer to the object\must declare as the first attribute in every function
        #declare attributes within this function
        self._name = name # "_" = protected\ "__" = private (use withtin the method and dont touch it)
        self._house = house

    def __str__(self):
        return (f"{self._name} from {self._house}")

    @property #function getter / use to get a encapsulated variable
    def house(self):
        return self._house

    @property #function getter / use to get a encapsulated variable
    def name(self):
        return self._name

    @house.setter #function setter/ update or change a encapsualted variable
    def house(self,house):
        if not house in ["Gryffindor","Ravenclaw","Slytherin","Hufflepuff"]:
            raise ValueError("Invalid House")
        self._house = house 

    @name.setter #function setter/ update or change a encapsualted variable
    def name(self , name):
        if not name:
            raise ValueError("Invalid Name")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    #create an object from class Student
    #student = Student(name, house)

    #or just return the object of Student class
    return Student(name,house)

def main():
    student = get_student()
    #people can still override 'house' in main so use getter, setter to protect it
    # "." is use to access varialbe stored in a object
    student.house = "Nha Que"
    #student now is a object, to call an object manually: use student.variable
    #or use __str__
    print(student)

if __name__ == "__main__":
    main()

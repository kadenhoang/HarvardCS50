class Student:
    #a function in a class is called Method

    #initialize a function and variables for the class
    def __init__(self,name,house):
    #make a third variable "self" to store name,house
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        self.house = house

    #self is refer to the object being created and has the varialbes

    def __str__(self):
        return (f"{self.name} from {self.house}")

    #function and variable must have different name
    @property #function getter
    def house(self):
        return self._house

    @house.setter #function setter
    def house(self,house):
        if not house in ["Gryffindor","Ravenclaw","Slytherin","Hufflepuff"]:
            raise ValueError("Invalid House")
        self._house = house

def main():
    student = get_student()
    #people can still override house in main so use getter, setter to protect it
    student.house = "Nha Que"
    #student now is a object, to call an object manually: use student.variable
    #or use __str__
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    #create an object from class Student
    return Student(name,house)


if __name__ == "__main__":
    main()

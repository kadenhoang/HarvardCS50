class Student:
    #a function in a class is called Method

    #initialize a function and variables for the class
    #after this function, other function in class will be able to use the variables assigned in it
    def __init__(self,name,house):
    #make a third variable "self" to store name,house
        self._name = name
        self._house = house

    #self is refer to the object being created and store the varialbes
    def __str__(self):
        return (f"{self.name} from {self.house}")

    #function and variable must have different name
    @property #function getter / make the function as property
    def house(self):
        return self._house

    @property #to use the function without ()
    #make the data read-only and cannot be changed in the main function
    def name(self):
        return self._name

    @house.setter #function setter/ set how the attribute(variable belong to the class) can be change under our rule
    def house(self,house):
        if not house in ["Gryffindor","Ravenclaw","Slytherin","Hufflepuff"]:
            raise ValueError("Invalid House")
        self._house = house #the "_" means private use withtin the method and dont touch it

    @name.setter
    def name(self , name):
        if not name:
            raise ValueError("Invalid Name")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    #create an object from class Student
    #student = Student(name, house)
    #or just return Student class and assigned it in the main
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

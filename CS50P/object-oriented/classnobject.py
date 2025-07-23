class Student:
    #initialize a function for the class
    def __init__(self,name,house):
    #make a third variable "self" to store name,house
        self.name = name
        self.house = house

def main():
    student = get_student()
    #student now is a object, to call an object: use student.variable
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    #create an object from class Student
    student = Student(name,house)
    return student

if __name__ == "__main__":
    main()

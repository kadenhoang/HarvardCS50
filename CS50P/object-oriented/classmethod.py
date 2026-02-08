class Student:

    def __init__(self,name,house): #constructor (self. = this. Java, must be explicitly declared)
        self.__name = name # '_' = protected | '__' = private (can still be access using mangled name: _className_var)
        self.__house = house

    def __str__(self):
        return f"{self.__name} is in {self.__house}"

    @classmethod #use to call the  method wt creating an object
    def get(cls):
        # 'cls' reference to the class,
        # input now can be used within the class
        name = input("Name:")
        house = input("House:")
        return cls(name,house)

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()

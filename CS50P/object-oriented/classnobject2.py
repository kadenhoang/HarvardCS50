class Student:
    def __init__(self,name,house):
        self.name = name
        self.house = house

    def __str__(self):
        print(f"{self.name} is in {self.house}")

    @classmethod #use the method wt creating an object
    def get(cls):
        # 'cls' refer to the class,
        # input now can be used within the class
        name = input("Name:")
        house = input("House:")
        return cls(name,house)

def main():
    student = Student()
    print(student)

def __main__ == __






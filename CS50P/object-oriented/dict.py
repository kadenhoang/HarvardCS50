def main ():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

#dict is mutatble so I can change the variable if needed
def get_student():
    student = {}
    student['name'] = input("Name:")
    student['house'] = input("House:")

    # or

    # name = input('Name:')
    # house = input('House:')
    # return {'name': name, 'house' : house}
    return student

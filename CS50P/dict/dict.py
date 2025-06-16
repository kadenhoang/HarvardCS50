def main():
    # there are many way to create a dictionary
    # 1. using curly braces
    student = {"name": "Vu"}
    # 2. using the dict() constructor
    student["school"] = "UW-Stout"
    # 3. using the update() method
    student.update({"age": "31", "nationality": "Vietnamese"})
    print(report(student))

def report(student):
    return f"""
name: {student["name"]}
school: {student.get("school", "Unknown")}
age: {student["age"]}
nationality: {student.get("nationality", "Unknown")}
"""

main()

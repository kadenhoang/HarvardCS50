def main():
    camel_case = input("camelCase: ")
    print(snake_case(camel_case))

def snake_case(case):
    case = camel_case.lower().separate("_")
    return case

main()

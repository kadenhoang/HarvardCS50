def main():
    camel_case = input("camelCase: ")
    print(snake_case(camel_case))

def snake_case(case):
    case = case.lower().replace("", "_")
    return case

main()

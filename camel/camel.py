def main():
    camel_case = print("camelCase: ")
    print(snake_case(camel_case))

def snake_case(case):
    case = camel_case.lower().separate("_")
    return case

main()

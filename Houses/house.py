name = input("Enter name: ").title().strip()

match name:
    case "Harry" | "Ron":
        print("Gryffindor")
    case "Malfroy":
        print("Syltherin")
    case _:
        print("Who tf r u takin abt?" )

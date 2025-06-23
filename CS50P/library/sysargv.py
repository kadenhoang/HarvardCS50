from sys import argv

if len(argv) < 2:
    print("Too few argurment")


elif len(argv) > 2:
    print("Too many argurment")


else:
    print("hello,", argv[1])


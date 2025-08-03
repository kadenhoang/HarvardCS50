def main():
    speak = convert(input("Say something: "))
    print(speak)

def convert(speak):
    speak = speak.replace(":)","🙂").replace(":(","🙁")
    return speak

main()


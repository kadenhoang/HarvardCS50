def main():
    string = input("Enter a string: ")
    print(shorten(string))

def shorten(word):
    vowels = "ueoaiUEOAI"
    for char in word:
        if char in vowels:
            word = word.replace(char,"")

    return word


if __name__ == "__main__":
    main()

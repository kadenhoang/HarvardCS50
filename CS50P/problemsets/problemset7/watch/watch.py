import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    #search for the link in the HTML
    match = re.search(r"https://www\.youtube\.com/embed/([a-zA-Z0-9_-]+)", s)
    #if the input does not have this type of link
    if not match:
        return None

    return f"https://youtu.be/{match.group(1)}"




if __name__ == "__main__":
    main()

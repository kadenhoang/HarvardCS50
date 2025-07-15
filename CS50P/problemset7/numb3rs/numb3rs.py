import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # match the IP Address format with user input
    match = re.match(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if not match:
        return False

    #check for each group for range
    for group in match.groups():
        if not 0 <= int(group) <= 255:
            return False

    return True

if __name__ == "__main__":
    main()

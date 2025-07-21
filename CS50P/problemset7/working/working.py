import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    #search for h,m,p to match and set it ino groups
    match = re.search(r"^(\d{1,2})(\:\d{2})?\s(AM|PM) to (\d{1,2})(\:\d{2})?\s(AM|PM)$", s)
    if not match:
        raise ValueError("Invalid format")

    h1, m1, p1, h2, m2, p2 = match.groups()

    h1 = int(h1)
    m1 = int(m1) if m1 else 0
    h2 = int(h2)
    m2 = int(m2) if m2 else 0

    #condition the period
    if p1 == "AM":
            h1 = 0 if h1 == 12  else h1
    else:
            h1 = 12 if h1 == 12 else h1 + 12

    if p2 == "AM":
            h2 = 0 if h2 == 12 else h2
    else:
            h2 = 12 if h2 == 12 else h2 + 12

    return(f"{h1:02}:{m1:02} to {h2:02}:{m2:02}")


if __name__ == "__main__":
    main()

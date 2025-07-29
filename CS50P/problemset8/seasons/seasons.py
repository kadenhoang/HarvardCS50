from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    birthdate = input("Birth date:")
    year, month, day = check_birthday(birthdate)
    try:
        date_of_birth = date(int(year),int(month),int(day))
    except:
        sys.exit("Invalid date")

    date_of_today = date.today()
    diff = date_of_today - date_of_birth
    total_minutes = diff.days * 24 * 60
    word_minutes = p.number_to_words(total_minutes, andword="")
    print(word_minutes.capitalize() + "minutes")


def check_birthday(birthdate):
        if re.match(r"^\d{4}-\d{2}-\d{2}$", birthdate):
            year, month, day = birthdate.split("-")
            return year, month, day
        else:
             sys.exit()



if __name__ == "__main__":
    main()

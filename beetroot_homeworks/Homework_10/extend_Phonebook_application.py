import json
import os

PHONE_BOOK_PATH = "phone_book.json"
PERSON_DETAILS = ("first name", "second name", "city", "state")


def initialize():
    if not os.path.exists(PHONE_BOOK_PATH):
        with open(PHONE_BOOK_PATH, "w") as file:
            json.dump({}, file)


def read():
    with open(PHONE_BOOK_PATH, "r") as file:
        book = json.load(file)

    return book


def write(number, details):
    book = read()
    book[number] = details
    with open(PHONE_BOOK_PATH, "w") as file:
        json.dump(book, file)


def add_or_update():
    number = input("Please enter a number: ")
    details = {}
    for item in PERSON_DETAILS:
        details[item] = input(f"Please enter {item}: ")

    write(number, details)


def find_by_number(number):
    book = read()
    print(book.get(number, "Not_Found"))


def find_by_city_or_state(location):
    book = read()
    for number, person_details in book.items():
        if person_details["city"] == location or person_details["state"] == location:
            print(number, person_details)


def find_by_name(name):
    book = read()
    for number, person_details in book.items():
        if (
            person_details["first name"] == name 
            or person_details["second name"] == name
        ):
            print(number, person_details)



def delete(number):
    book = read()
    del book[number]
    with open(PHONE_BOOK_PATH, "w") as file:
        book = json.dump(book, file)
    
    # return book


if __name__ == "__main__":
    initialize()
    add_or_update()
    print(read())
    
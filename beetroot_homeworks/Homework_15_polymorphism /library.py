class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        print(self.name, self.year, self.author)

    def __repr__(self):
        print(self.name, self.year, self.author)


class Author:
    def __init__(self, name, country, birthday, books=[]):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books

    def __str__(self):
        return self.name + self.country + self.birthday


class Library:
    books = []

    def new_book(self, name: str, year: int, author: Author):
        b = Book(name, year, author)
        self.books.append(
            [b.name, b.year, b.author.name, b.author.country, b.author.birthday]
        )
        return b

    def group_by_author(self, author: Author):
        aut = []
        for name in self.books:
            if name[2] == author.name:
                aut.append([name[0], name[1], name[2], name[3], name[4]])
        return aut

    def group_by_year(self, year: int):
        list_group_year = []
        for value in self.books:
            if year == value[1]:
                list_group_year.append(
                    [value[0], value[1], value[2], value[3], value[4]]
                )
        return list_group_year

    def __str__(self):
        return str(self.books)

    def __repr__(self):
        print(self.books)


author_1 = Author("John", "UA", "01.01.1991")
l = Library()

l.new_book("book1", 2021, author_1)


author_2 = Author("Bill", "KZ", "02.02.1992")
l.new_book("book2", 2020, author_2)

author_3 = Author("Bob", "LA", "03.02.1993")
l.new_book("book3", 2021, author_3)
author_4 = Author("Kenny", "USA", "04.02.1994")
l.new_book("book4", 2022, author_4)

print(l)

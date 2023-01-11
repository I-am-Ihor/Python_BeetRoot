class Animal:
    def talk(self):
        raise TypeError("Please write def in child class")


class Dog(Animal):
    def talk(self):
        print("woof woof")


class Cat(Animal):
    def talk(self):
        print("meow")


cat = Cat()
dog = Dog()


def voice():
    a = input("How voice do you want to hear? Cat or Dog? ")
    if a.title() == "Cat":
        return cat.talk()
    if a.title() == "Dog":
        return dog.talk()


voice()

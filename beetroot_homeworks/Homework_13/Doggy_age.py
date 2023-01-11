class Dog:
    age_factor = 7

    def __init__(self, age_dog) -> None:
        self.age_dog = age_dog

    def human_age(self):

        return self.age_dog * self.age_factor


dog = Dog(10)
print(dog.human_age())

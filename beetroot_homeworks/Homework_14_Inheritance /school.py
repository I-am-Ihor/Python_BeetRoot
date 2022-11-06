class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname

    def __repr__(self) -> str:
        return self.name + " " + self.surname


class Teachers(Person):
    def __init__(self, name, surname, salary) -> None:
        super().__init__(name, surname)
        self.salary = salary

    def __repr__(self) -> str:
        return super().__repr__() + " " + str(self.salary)


class Students(Person):
    def __init__(self, name, surname, stipend, cource) -> None:
        super().__init__(name, surname)
        self.stipend = stipend
        self.cource = cource

    def __repr__(self) -> str:
        return super().__repr__() + " " + str(self.stipend) + " " + str(self.cource)
    
student = Person('Ihor', 'Taran')
print(student)
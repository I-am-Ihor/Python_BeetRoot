class Product:
    def __init__(self, _type: str, name: str, price: int, visible=True) -> None:
        self.type = _type
        self.name = name
        self.price = price
        self.visible = visible


class ProductStore(Product):
    def __init__(self, _type: str, name: str, price=0, amount=50, income=0) -> None:
        super().__init__(_type, name, price)
        self.amount = amount
        self.income = income

    def add(self, amount):

        self.price += self.price / 100 * amount
        return self.price

    def set_discount(self, percent, identifier_type: str):
        if percent <= 100 and identifier_type == self.type:
            self.price -= self.price / 100 * percent
            return self.price
        else:
            return "percent > 100 or not type"

    def sell_product(self, value):

        if value <= self.amount:
            self.amount -= value

            if self.amount <= 0:
                self.visible = False

            return self.amount
        else:

            return "Нет такого кол-ва!"

    def get_income(self, value):
        self.income = value * self.price
        return self.income

    def get_all_products(self):
        if self.visible == True:
            return [self.name, self.type, self.price, self.amount]
        else:
            return "Недоступен"

    def get_product_info(self, name):
        if name == self.name:
            return (self.name, self.amount)

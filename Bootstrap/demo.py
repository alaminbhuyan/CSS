
class Mobile:
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price

    def display(self):
        print(f"Name: {self.name}, Model: {self.model}, price: {self.price}")




obj = Mobile("Sumsung", "M10", 10500)

obj.display()
class Coffee:
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size

    def __str__(self):
        return f"{self.size} {self.name} - ${self.price:.2f}"

    def get_details(self):
        return {
            "name": self.name,
            "price": self.price,
            "size": self.size
        }

def create_coffee(name, price, size):
    return Coffee(name, price, size)

def list_coffees(coffee_list):
    return [str(coffee) for coffee in coffee_list]
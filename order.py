class Order:
    def __init__(self, customer, coffee, price):
        from customer import Customer
        from coffee import Coffee
        if not isinstance(customer, Customer):
            raise ValueError("Customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be a Coffee instance")
        if not isinstance(price, float):
            raise ValueError("Price must be a float")
        if not 1.0 <= price <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        self._customer = customer
        self._coffee = coffee
        self._price = price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    def __str__(self):
        return f"{self._customer} ordered {self._coffee} for ${self._price:.2f}"
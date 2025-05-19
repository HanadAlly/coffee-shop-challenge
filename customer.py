class Customer:
    def __init__(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
            self._orders = []
        else:
            raise ValueError("Customer name must be a string between 1 and 15 characters.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name
        else:
            raise ValueError("Customer name must be a string between 1 and 15 characters.")

    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.orders().append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.orders():
            return None
        customer_spending = {}
        for order in coffee.orders():
            customer = order.customer
            customer_spending[customer] = customer_spending.get(customer, 0) + order.price
        return max(customer_spending, key=customer_spending.get, default=None)

    def __str__(self):
        return self._name
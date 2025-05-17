class Order:
    def __init__(self, order_id, customer, coffee, quantity):
        self.order_id = order_id
        self.customer = customer
        self.coffee = coffee
        self.quantity = quantity

    def get_order_details(self):
        return {
            "order_id": self.order_id,
            "customer": self.customer,
            "coffee": self.coffee,
            "quantity": self.quantity
        }

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def __str__(self):
        return f"Order {self.order_id}: {self.quantity} x {self.coffee} for {self.customer}"
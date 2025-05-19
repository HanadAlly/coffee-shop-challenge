import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")

    def test_initializer_valid(self):
        self.assertEqual(self.customer.name, "Alice")

    def test_initializer_invalid_name(self):
        with self.assertRaises(ValueError):
            Customer("") 
        with self.assertRaises(ValueError):
            Customer("A" * 16)  
        with self.assertRaises(ValueError):
            Customer(123)  

    def test_name_setter_valid(self):
        self.customer.name = "Bob"
        self.assertEqual(self.customer.name, "Bob")

    def test_name_setter_invalid(self):
        with self.assertRaises(ValueError):
            self.customer.name = ""  
        with self.assertRaises(ValueError):
            self.customer.name = "A" * 16  

    def test_orders(self):
        order = self.customer.create_order(self.coffee, 4.5)
        self.assertEqual(self.customer.orders(), [order])

    def test_coffees(self):
        self.customer.create_order(self.coffee, 4.5)
        self.assertEqual(self.customer.coffees(), [self.coffee])

    def test_create_order(self):
        order = self.customer.create_order(self.coffee, 4.5)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 4.5)

    def test_most_aficionado(self):
        customer2 = Customer("Bob")
        self.customer.create_order(self.coffee, 4.5)
        customer2.create_order(self.coffee, 3.0)
        self.assertEqual(Customer.most_aficionado(self.coffee), self.customer)

if __name__ == '__main__':
    unittest.main()
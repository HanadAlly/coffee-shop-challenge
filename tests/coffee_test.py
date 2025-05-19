import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        self.coffee = Coffee("Espresso")
        self.customer = Customer("Alice")

    def test_coffee_creation(self):
        self.assertEqual(self.coffee.name, "Espresso")

    def test_coffee_name_invalid(self):
        with self.assertRaises(ValueError):
            Coffee("Ab")  
        with self.assertRaises(ValueError):
            Coffee(123)  

    def test_coffee_name_immutable(self):
        with self.assertRaises(AttributeError):
            self.coffee.name = "Latte"

    def test_orders(self):
        order = self.customer.create_order(self.coffee, 4.5)
        self.assertEqual(self.coffee.orders(), [order])

    def test_customers(self):
        self.customer.create_order(self.coffee, 4.5)
        self.assertEqual(self.coffee.customers(), [self.customer])

    def test_num_orders(self):
        self.customer.create_order(self.coffee, 4.5)
        self.assertEqual(self.coffee.num_orders(), 1)
        self.assertEqual(Coffee("Mocha").num_orders(), 0)

    def test_average_price(self):
        self.customer.create_order(self.coffee, 4.5)
        self.assertEqual(self.coffee.average_price(), 4.5)
        self.assertEqual(Coffee("Mocha").average_price(), 0)

if __name__ == '__main__':
    unittest.main()
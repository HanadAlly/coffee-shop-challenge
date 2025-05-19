import unittest
from coffee import Coffee

class TestCoffee(unittest.TestCase):

    def setUp(self):
        self.coffee = Coffee("Espresso", 2.5)

    def test_coffee_creation(self):
        self.assertEqual(self.coffee.name, "Espresso")
        self.assertEqual(self.coffee.price, 2.5)

    def test_coffee_price_update(self):
        self.coffee.price = 3.0
        self.assertEqual(self.coffee.price, 3.0)

    def test_coffee_name_update(self):
        self.coffee.name = "Latte"
        self.assertEqual(self.coffee.name, "Latte")

if __name__ == '__main__':
    unittest.main()
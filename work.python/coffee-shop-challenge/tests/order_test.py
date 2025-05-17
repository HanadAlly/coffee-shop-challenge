import unittest
from order import Order  # Assuming Order class is defined in order.py

class TestOrder(unittest.TestCase):

    def setUp(self):
        self.order = Order(customer_id=1, coffee_id=2, quantity=3)

    def test_order_creation(self):
        self.assertEqual(self.order.customer_id, 1)
        self.assertEqual(self.order.coffee_id, 2)
        self.assertEqual(self.order.quantity, 3)

    def test_order_quantity(self):
        self.order.quantity = 5
        self.assertEqual(self.order.quantity, 5)

    def test_order_total_price(self):
        self.order.quantity = 3
        self.order.price_per_unit = 2.5  # Assuming price_per_unit is an attribute
        self.assertEqual(self.order.total_price(), 7.5)  # Assuming total_price is a method

if __name__ == '__main__':
    unittest.main()
import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer(name="John Doe", email="john@example.com")

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.email, "john@example.com")

    def test_customer_update(self):
        self.customer.name = "Jane Doe"
        self.assertEqual(self.customer.name, "Jane Doe")

    def test_customer_email_validation(self):
        with self.assertRaises(ValueError):
            self.customer.email = "invalid-email"

if __name__ == '__main__':
    unittest.main()
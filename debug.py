from customer import Customer
from coffee import Coffee
from order import Order

alice = Customer("Alice")
bob = Customer("Bob")

latte = Coffee("Latte")
mocha = Coffee("Mocha")

alice.create_order(latte, 4.5)
alice.create_order(mocha, 5.0)

bob.create_order(latte, 3.0)

print(latte.num_orders())  
print(latte.average_price())  
print(bob.orders())  
print(alice.coffees())  

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
print(f"Number of Latte orders: {latte.num_orders()}")  
print(f"Average Latte price: ${latte.average_price():.2f}")  
print(f"Bob's orders:")
for order in bob.orders():
    print(f"  {order}")  
print(f"Alice's coffees: {', '.join(str(coffee) for coffee in alice.coffees())}")  
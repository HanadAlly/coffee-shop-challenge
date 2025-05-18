from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Alice")
c2 = Customer("Bob")

latte = Coffee("Latte")
mocha = Coffee("Mocha")

c1.create_order(latte, 4.5)
c1.create_order(mocha, 5.0)
c2.create_order(latte, 3.0)

print(latte.num_orders())         # 2
print(latte.average_price())      # 3.75
print(c1.coffees())               # [latte, mocha]

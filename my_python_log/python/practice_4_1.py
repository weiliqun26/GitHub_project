pizzas = ["margherita", "pepperoni", "hawaiian", "bbq chicken"]
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I really love pizza!")
animals = ["dog", "cat", "rabbit"]
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("Any of these animals would make a great pet!")

friends_pizzas = pizzas[:]
print(friends_pizzas)
friends_pizzas.append("veggie")
print(f"my favorite pizzas are:{pizzas[:]}")
print(f"my frients's favorite pizzas are:{friends_pizzas[:]}")

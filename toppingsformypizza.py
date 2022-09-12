stand_top_price = 0.95
special_top_price = 1.35
pizza_base_price = 14.95

standard_tops = ['cheese', 'pepperoni', 'mushrooms', 'onion', 'spaghetti']

ordering = True

prompt = "enter a topping, or 'checkout' to check out: "

current_pizza = []
while ordering:
    topping = input(prompt)
    if topping.lower() == 'checkout':
        ordering = False
    else:
        current_pizza.append(topping.lower())

print("\n\nYou ordered a pizza with the following toppings: ")
for topping in current_pizza:
    print(f"\t-{topping}")
    if topping in standard_tops:
        pizza_base_price += stand_top_price
    else:
        pizza_base_price += special_top_price

print(f"\nYour pizza will cost you {pizza_base_price:.2f}")

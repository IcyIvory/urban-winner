# list in dictionary
pizza = {
    'crust': 'stuffed',
    'stand_toppings': ['cheese', 'pepperoni', 'bacon'],
    'base_sauce': 'alfredo',
    'opp_toppings': ['salami', 'gouda', 'portabello mushrooms']
}
if pizza['base_sauce'] != 'tomato':
    print(f"You ordered a {pizza['crust']}-crust pizza with a base of {pizza['base_sauce']} sauce.")
else:
    print(f"You ordered a {pizza['crust']}-crust pizza.")

print("It has the following toppings:")
toppings = []
for topping in pizza['stand_toppings']:
    toppings.append(topping)
for topping in pizza['opp_toppings']:
    toppings.append(topping)
for topping in toppings:
    print(f"\t-{topping.title()}")
menu = {
    "Cappuccino": 159,
    "Hot Café Latte": 169,
    "Café Americano": 159,
    "Café Mocha": 189,
    "Filter Coffee": 159,
    "Vanilla Cappuccino": 169,
    "Espresso Shot": 149,
    "King Cappuccino": 189,
    "King Latte": 199,
    "Hot Ethiopian Latte": 259,
    "Honey Cinnamon Coffee": 159,
    "Flat White Coffee": 169,
    "Turmeric Ginger Cappuccino": 169}

print("Welcome to our cafe! Here is our menu:")
for item, price in menu.items():
    print(f"{item}: ₹{price}")
    
order_total = 0

order = input("Please enter the name of the coffee you would like to order:")
if order in menu:
        order_total += menu[order]
        print(f"Added {order} to your order. Current total: ₹{order_total}")
else:
        print("Sorry, that item is not on the menu.")

more = input("Would you like to order anything else?: (yes/no)")
while more.lower() == "yes":
        another_order = input("Please enter the name of the coffee you would like to order: ")
        if another_order in menu:
            order_total += menu[another_order]
            print(f"Added {another_order} to your order. Current total: ₹{order_total}")
        else:
            print("Sorry that item is not in the menu.")

        more = input("Would you like to order anything else?: (yes/no)")
        
        if more.lower() != "yes":
            break

print(f"Your final order total is ₹{order_total}. Thank you for your order!")

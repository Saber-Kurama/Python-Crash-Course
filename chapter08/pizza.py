def mark_pizza(size, *toppings):
    """制作披萨"""
    print(f"Making a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"{topping}")
class Pizza:

    def __init__(self, size, crust):
        # establish the properties of each pizza
        # wish a default value
        self.size = size
        self.crust = crust
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)
    
    def print_order(self):
        if len(self.toppings) == 0:
            self.toppings = "nothing on it"
        elif len(self.toppings) == 1:
            self.toppings = f"just {self.toppings[0]}"
        elif len(self.toppings) == 2:
            self.toppings = f"{self.toppings[0]} and {self.toppings[1]}"
        elif len(self.toppings) > 2:
            self.toppings = f"{', '.join(self.toppings[:-1])}, and {self.toppings[-1]}"
        print(f"I would like a {self.size}, {self.crust} pizza with {self.toppings}.")



veggie = Pizza("16-inch", "thin crust")
# veggie.size = "16-inch"
# veggie.crust = "thin crust"
veggie.add_topping("olives")
veggie.add_topping("tomatoes")
veggie.add_topping("spinach")
veggie.add_topping("onion")
veggie.add_topping("mushrooms")
veggie.print_order()

print()

hawaiian_bbq = Pizza("12-inch", "original crust")
# hawaiian_bbq.size = "12-inch"
# hawaiian_bbq.crust = "original crust"
hawaiian_bbq.add_topping("chicken")
hawaiian_bbq.add_topping("bacon")
hawaiian_bbq.add_topping("onion")
hawaiian_bbq.add_topping("pineapple")
hawaiian_bbq.add_topping("bbq sauce")
hawaiian_bbq.print_order()

print()

cheese = Pizza("8-inch", "deep dish")
# cheese.size = "8-inch"
# cheese.crust = "deep dish"
cheese.add_topping("cheese")
cheese.print_order()

print()

bread = Pizza("8-inch", "deep dish")
# bread.size = "8-inch"
# bread.crust = "deep dish"
bread.print_order()

print()

pepperoni = Pizza("16-inch", "original crust")
pepperoni.add_topping("pepperoni")
pepperoni.add_topping("extra cheese")
pepperoni.print_order()

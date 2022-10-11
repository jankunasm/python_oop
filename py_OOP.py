# item1 = "Snapple"
# item1_price = 2
# item1_quantity = 200
# item1_price_total = item1_price * item1_quantity

# print(type(item1))
# print(type(item1_price))
# print(type(item1_quantity))
# print(type(item1_price_total))

class Item:
    pay_rate = 0.8 # The pay rate after 20 percent discount
    
    def __init__(self, name: str, price: float, quantity: float):
        # Run validations to the recieved arguments
        assert price >= 0, f"Price {price} cannot be under 0!"
        assert quantity >= 0, f"Quantity {quantity} cannot be under 0!"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * Item.pay_rate

item1 = Item("Snapple", 2, 200)

item2 = Item("Vitamin_water", 1.99, 250)

item3 = Item("Coke", 1.50, 430)

item4 = Item("Mountain_dew", 1.50, 220)

item5 = Item("Arizona_tea", 2, 345)

# item1.apply_discount()
# item2.apply_discount()

# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

# print(Item.__dict__)

# print(Item.pay_rate)

# print(item1.name)
# print(item2.name)
# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
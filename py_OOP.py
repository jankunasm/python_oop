import csv
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
    
    all = []
    
    def __init__(self, name: str, price: float, quantity: float):
        # Run validations to the recieved arguments
        assert price >= 0, f"Price {price} cannot be under 0!"
        assert quantity >= 0, f"Quantity {quantity} cannot be under 0!"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * Item.pay_rate
        
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = float(item.get('quantity')),
            )
    @staticmethod    
    def is_integer(num):
        # We will count out the floats that are point zero for i.e. 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
            
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


class Phone(Item):
    
    def __init__(self, name: str, price: float, quantity: float, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )
        assert broken_phones >= 0, f"Broken Phones {broken_phones} cannot be under 0!"
        
        self.broken_phones = broken_phones

phone1 = Phone("iphone10", 500, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("iphone11", 700, 5, 1)

print(Item.all)
print(Phone.all)


item1 = Item("Snapple", 2, 200)

item2 = Item("Vitamin_water", 1.99, 250)

item3 = Item("Coke", 1.50, 430)

item4 = Item("Mountain_dew", 1.50, 220)

item5 = Item("Arizona_tea", 2, 345)

# Using a for loop to print all names of every object added to list
for instance in Item.all:
    print(instance.name)
    
Item.instantiate_from_csv()
print(Item.all)

print(Item.is_integer(7))

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
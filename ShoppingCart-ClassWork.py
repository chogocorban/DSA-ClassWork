class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_items(self, item_name: str, qty: int, unit_price:float):
        #Do the explanation here....
        self.items.append((item_name, qty, unit_price))

    def remove_item(self,item_name: str):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_total(self) -> float:
        total = 0.0

        for name, qty, price in self.items:
            total += qty * price

        return total

    def summary(self):
        print("Cart Contents")
        for name, qty, price in self.items:
            print(f"{name}: {qty} @ Ksh {price:.3f} each")
        print(f"Total: Ksh {self.calculate_total():.2f}\n")

def checkout(cart: ShoppingCart):
    cart.summary()
    print(f"Final amount: Ksh {cart.calculate_total():.2f}\n")

    #Usage
if __name__ == "__main__":

    cart: ShoppingCart = ShoppingCart()
    cart.add_items("Kiwi",50, 79.2)
    cart.add_items("Papaya",30, 40.3)
    cart.add_items("Guava",10, 20.1)
    cart.add_items("Mango",50, 7.6)

    print(">>> Regular Cart <<<")

    checkout(cart)


#     def add_item(self, age, count):
#         self.age = age
#         self.count = count
#         bool1 = True
#         print(f"{age}, {count}, {bool1}")
#
# obj1: ShoppingCart = ShoppingCart()
# obj2: ShoppingCart = ShoppingCart()
#
# obj2.bool1 = False
#
# obj1.add_item(20,1)
# obj2.add_item(30,2)
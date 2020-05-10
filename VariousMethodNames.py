class Product:
    __total = 0  # class DATA MEMBERs

    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price

    def find(self):
        self.sub = self.qty * self.price
        Product.__total += self.sub

    @staticmethod
    def show2():
        pass

    @classmethod
    def show1(cls):
        print("Total = ", cls.__total)


ob1 = Product("a", 1, 1)
print(ob1.find) # bound method with address (self) as default argument
print(ob1.show1) # class method with class name as default argument
print(ob1.show2) # static method with no default argument
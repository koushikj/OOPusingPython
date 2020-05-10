
class Product:
    __total = 0   # static data member OR class DATA MEMBERs

    def __init__(self,name,qty,price):
        self.name = name
        self.qty = qty
        self.price = price

    def findsub(self):
        self.subtotal = self.qty * self.price
        Product.__total = Product.__total + self.subtotal

    def show(self):
        print(self.name, self.qty, self.price, self.subtotal, Product.__total)

    def getTotal(self):
        return Product.__total

    @staticmethod
    def getTotalStatic():
        print("Total from static method is:",Product.__total)

    @classmethod
    def getTotalClass(cls):
        print("Total from Class method is:",cls.__total)

p1 = Product("a",2,10)
p2 = Product("b",1,20)
p3 = Product("a",3,30)
p4 = Product("b",4,40)
p1.findsub()
p2.findsub()
p3.findsub()
p4.findsub()
p1.show()
p2.show()
p3.show()
p4.show()

print("Total from main method is:",p1.getTotal())
Product.getTotalStatic()
p1.getTotalStatic() # not suggested

# call class method using objects instead of class name
Product.getTotalClass() ## not suggested
p1.getTotalClass()  ## suggested


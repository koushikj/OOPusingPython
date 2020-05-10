class Express1:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute(self):
        self.result = self.a **2 + self.b ** 2

    def show(self):
        print("Express a = %s  b = %s :: a^2 + b^2 =%s" % (self.a, self.b,self.result))


class Express2(Express1):  # syntax to inherit a CLASS/s

    def __init__(self, a, b, c):
        super().__init__(a, b)      #constructor cascading
        self.c = c

    def compute2(self):
        self.compute()
        self.result2 = self.result / self.c**2


    def display(self):
        print("Express2 c = %s :: Final (a^2 + b^2)/c^2 = %s " % (self.c, self.result2))


express2 = Express2(4,4,2)
print(vars(express2))
print(dir(express2))

print("----")
express2.compute2()
express2.show()
express2.display()



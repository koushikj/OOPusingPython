class Alpha:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print("ALPHA a = %s  b = %s " % (self.a, self.b))


class Beta(Alpha):  # syntax to inherit a CLASS/s

    def __init__(self, a, b, c, d):
        super().__init__(a, b)      #constructor cascading
        self.c = c
        self.d = d

    def display(self):
        print("BEta c = %s  d = %s " % (self.c, self.d))


beta = Beta(1,2,3,4)
beta.display()
beta.show() # alpha's method calling with beta instance
print(vars(beta))
print(dir(beta))

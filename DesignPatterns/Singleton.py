class Sample:
    __flag = False

    def __new__(cls, *args, **kwargs):
        if not Sample.__flag:
            Sample.__flag = super(Sample,cls).__new__(cls)
            print("Object got created")
        return Sample.__flag

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def show(self):
        print("a = %s , b= %s" %(self.a, self.b))


ob1 = Sample(10,20)
print("OB1 =", id(ob1))
ob1.show()

ob2 = Sample(20,30)     #uses the same instance instead of creating new instance.
print("OB2 =", id(ob2))

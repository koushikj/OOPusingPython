from SumOfSquares import Express

e1 = Express.Express()
print(e1)
print(type(e1))
print(vars(e1))
print(e1.ans)       # objects in python are dictionary
print(Express.Express.__mro__)  # method resolution order - polymorphism - shows the base class

e1.set(2,4)
print(e1.__dict__)

e1.find()
e1.show()

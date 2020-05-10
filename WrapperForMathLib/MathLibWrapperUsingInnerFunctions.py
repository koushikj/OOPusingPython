#from WrapperForMathLib import MathLib


def Outer(fnptr):
    def inner(*args, **kwargs):
        print("hi")
        res = fnptr(*args, **kwargs)
        print("bye")
        return res
    return inner()


print(MathLib.add(1, 2))  # using actual mathlib add function
MathLib.add(2, 3)

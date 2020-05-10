from WrapperForMathLib import MathLib


def wrapper(fnptr, *args, **kwargs):
    print("customized wrpapper for ", fnptr.__name__)
    result = fnptr(*args, **kwargs)
    print(result)


print(MathLib.add(1, 2))  # using actual mathlib add function
wrapper(MathLib.add, 1, 2)  # using wrapper customized mathlib add function

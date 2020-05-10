# Functions are Objects in python

def Outer(message):
    a = 10
    b = 80

    def inner():
        c = 30
        ans = a + b + c
        print("------ Answer is =", ans)
        print("inner locals::", locals())

    print("outer locals::", locals())
    return inner


fnptr1 = Outer("hai bye")  # fnptr1 holds the address of inner function, to invoke call fnptr1()
fnptr2 = Outer("hai bye")  # creates new instance for Outer function
print(fnptr1.__name__)
print(fnptr1.__doc__)
print(fnptr1.__defaults__)
print(fnptr1.__code__)  # though the instance are different, the code (output) is same here for fnptr1 and fnptr2
print(fnptr2.__code__)  # though the instance are different, the code (output) is same here for fnptr1 and fnptr2
fnptr1()  # calling inner function, by this time outer function is died, but still it contains value of Outer. This
# is called closure. Closure will hold the dependant
# values from Outer function

print("Main locals::", locals())

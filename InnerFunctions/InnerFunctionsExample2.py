
#Functions are Objects in python

def Outer(message):
    a = 10
    b = 80
    def inner():
        c=30
        ans = a +b + c
        print("------ Answer is =",ans)
        print("inner locals::", locals())
    print("outer locals::", locals())
    return inner


fnptr1 = Outer("hai bye")
fnptr2 = Outer("hai bye")   # creates new instance for Outer function
print(fnptr1)
print(fnptr2)
print("Main locals::", locals())

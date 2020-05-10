def Outer(message):
    a = 10
    b = 80
    def inner():
        c=30
        ans = a +b + c
        print("Answer is =",ans)
        print("inner locals::", locals())
    inner()
    print("Outer locals::", locals())


Outer("hai bye")
print("Main locals::", locals())

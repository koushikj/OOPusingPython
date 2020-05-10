from StudentsResults.Stundent import Student

st1 = Student("ravi", 8, [80, 70, 60, 90, 50])
st1.findtotal()
st1.findAverage()
st1.show()

st4 = Student("ravi", 8, [80, 70, 60, 90, 50])
st4.findtotal()
st4.findAverage()
st4.show()


st2 = Student("hari", 8, [70, 55, 90, 50, 75])
st2.findtotal()
st2.findAverage()
st2.show()

res = st1.compareAverage(st2)

st3 = Student() # default constructor
st3.findtotal()
st3.findAverage()
st3.show()


# operator overloading
print(st1 == st4) # this will call __eq__(self, other)
print("BEST is ",res)

print(st1)
print(st4)
print(st2)

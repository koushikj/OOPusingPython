from Employee import Employee

e1 = Employee(1001,"arun",15000)
e2 = Employee(1002,"ravi",25000)
e3 = Employee(1004,"john",26000)
e4 = Employee(1003,"hari",27000)
e5 = Employee(1003,"kj",30000)

# preffered
e1.getEmpCount() # class method
Employee.getAvgSalary() # static method

# not prefered
Employee.getEmpCount()  #class method
e1.getAvgSalary() # static method

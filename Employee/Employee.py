class Employee:
    __total = 0
    __sal = 0

    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal =sal
        Employee.__total += 1
        Employee.__sal += sal

    @classmethod
    def getEmpCount(cls):
        print("total emp",cls.__total)

    @staticmethod
    def getAvgSalary():
        print("Average salary :",Employee.__sal/Employee.__total)

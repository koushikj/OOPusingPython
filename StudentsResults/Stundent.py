class Student:
    def __init__(self,name=None,standard=0,marks=[0]):  # to handle both default constructor (without any parameter) and parametrized constructor
        self.name = name
        self.standard = standard
        self.marks = marks

    def findtotal(self):
        self.total = sum(self.marks)

    def show(self):
        print(self.total)
        print(self.average)

    def findAverage(self):
        self.average = (self.total/len(self.marks))

    def compareAverage(self, student2):
        print(self.average)
        print(student2.average)
        if self.average > student2.average:
            return self.name
        else:
            return student2.name

    # operator overloading. this gets called for ==
    def __eq__(self, other):
        print(self.name)
        print(other.average)
        if self.average == other.average and self.name == other.name and self.standard == other.standard:
            return True
        else:
            return False

    # operator overloading. this gets called when object is printed (similar to override the .toString in java)
    def __str__(self):
        return "Student( %s, %s, %s)" %(self.name,self.standard,self.marks)



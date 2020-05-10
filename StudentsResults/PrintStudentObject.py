class Student :
    def __init__(self,name=None,standard=0,marks=[0]):
        self.name=name
        self.standard =standard
        self.marks=marks

    def __getitem__(self, item):
        if item == 0:
            return self.name
        elif item ==1:
            return self.standard
        elif item ==2:
            return self.marks
        else:
            raise "IndexError"


ob1 = Student("ajith",5,[10,20,30])

print(ob1[0])  # ajith
print(ob1[1])  # 5
print(ob1[2])  # [10,20,30]
#print(ob1[3])  # IndexError -- this will throw error

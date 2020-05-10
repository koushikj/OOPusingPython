class Student:
    def __init__(self, name=None, std=0, marks=[0]):
        self.name = name
        self.std = std
        self.marks = marks

    def __getitem__(self, index):
        if index in self.__dict__:
            return self.__dict__[index]
        else:
            raise KeyError


ob1 = Student("ajith", 5, [10, 20, 30])

print(ob1["name"])  # ajith
print(ob1["std"])  # 5
print(ob1["marks"])  # [10,20,30]
#print(ob1["avg"])  # [10,20,30]  -- this will throw error


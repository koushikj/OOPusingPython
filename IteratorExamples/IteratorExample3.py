class Emp:

    def __init__(self, name, dept, loc, sal):
        self.name = name
        self.dept = dept
        self.loc = loc
        self.sal = sal
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count == 1:
            return self.name
        elif self.count == 2:
            return self.dept
        elif self.count == 3:
            return self.loc
        elif self.count == 4:
            return self.sal
        else:
            self.count = 0
            raise StopIteration


eob = Emp("Harish", "finan", "blr", 45000)

print("using for loop.. ")
for elem in eob:
    print(elem)

print("")
print("using next...")
it = iter(eob)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#print(next(it)) # will throw StopIteration exception


# ex2:-
# =====
class Emp:

    def __init__(self, name, dept, loc, sal):
        self.name = name
        self.dept = dept
        self.loc = loc
        self.sal = sal

    def __iter__(self):
        return iter(self.__dict__.values())


eob = Emp("Harish", "finan", "blr", 45000)

for elem in eob:
    print(elem)

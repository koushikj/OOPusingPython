class Express:
    def __init__(self):     #CONSTRUCTOR
        self.a = 0
        self.b = 0
        self.ans = 0

    def show(self):
        print(self.a,self.b,self.ans)

    def find(self):
        self.ans = self.a**2 + self.b**2

    def set(self,p,q):
        self.a = p
        self.b = q

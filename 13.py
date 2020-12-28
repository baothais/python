# Ham constructor(khoi tao) trong python
class Addition:
    first = 0
    second = 0
    answer = 0

    def __init__(self, f, s):
        self.first = f
        self.second = s
    
    def calculater(self):
        self.answer = self.first + self.second

    def display(self):
        return "first: %d; second: %d; answer: %d" %(self.first, self.second, self.answer)

def main1():
    f = int(input("Enter first: "))
    s = int(input("Enter second: "))

    a = Addition(f, s)
    a.calculater()
    print(a.display())

if __name__=="__main__":
    main1()
    
# Ham destructor(ham huy)

"""syntax:       
def __del__(self):
    #body of destructor"""

class Employee:
    def __init__(self):
        print("Empoyee created")

    def __del__(self):
        print("Destructor called, Employ deleted")

obj = Employee()
del obj


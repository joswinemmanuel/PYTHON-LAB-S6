class Arithmetic:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show_details(self):
        print(f"X : {self.x} \t Y: {self.y}")
    
    def add(self):
        return f"{self.x} + {self.y} = {self.x + self.y}"

    def sub(self):
        return f"{self.x} - {self.y} = {self.x - self.y}"
    
    def mul(self):
        return f"{self.x} * {self.y} = {self.x * self.y}"
    
    def div(self):
        return f"{self.x} / {self.y} = {self.x / self.y}"
    
    def mod(self):
        return f"{self.x} % {self.y} = {self.x % self.y}"
    

a1 = Arithmetic(10, 20)
a1.show_details()
print(a1.add())
print(a1.sub())
print(a1.mul())
print(a1.div())
print(a1.mod())

'''
X : 10   Y: 20
10 + 20 = 30
10 - 20 = -10
10 * 20 = 200
10 / 20 = 0.5
10 % 20 = 10
'''

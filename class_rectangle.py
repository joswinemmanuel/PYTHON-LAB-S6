class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    
    def area(self):
        return self.length * self.breadth
    
r1 = Rectangle(5, 4)
print("Perimeter of rectangle is : ", r1.perimeter())
print("Area of rectangle is : ", r1.area())

'''
Perimeter of rectangle is :  18
Area of rectangle is :  20
'''

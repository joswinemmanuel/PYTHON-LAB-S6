class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def display_details(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Salary : {self.salary}")
        
p1 = Person("Joswin", 24, 1000000000)
p1.display_details()

'''
Name : Joswin
Age : 24
Salary : 1000000000
'''

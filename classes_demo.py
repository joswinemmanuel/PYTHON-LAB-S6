class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show_name(self):
        print("Animal name is : ", self.name)
        
    def show_details(self):
        print(f"{self.name} is {self.age} year old")

dog = Animal("Rex", 5)
cat = Animal("Ruby", 8)
mouse = Animal("Jerry", 2)

dog.show_name()
dog.show_details()
cat.show_name()
cat.show_details()
mouse.show_name()
mouse.show_details()

'''
Animal name is :  Rex
Rex is 5 year old
Animal name is :  Ruby
Ruby is 8 year old
Animal name is :  Jerry
Jerry is 2 year old
'''

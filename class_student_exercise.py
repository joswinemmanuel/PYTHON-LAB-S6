class Student:
    def readData(self):
        self.roll_number = int(input("Enter student roll number : "))
        self.name = input("Enter student name : ")
        self.mark = [0] * 3
        for i in range(0, 3):
            self.mark[i] = int(input(f"Enter mark of subject {i+1} : "))
    
    def computeTotal(self):
        total = 0
        for i in self.mark:
            total += i
        return total
    
    def print_details(self):
        print(f"Roll number : {self.roll_number}")
        print(f"Name : {self.name}")
        print("Marks :", *self.mark)
        print(f"Total : {self.computeTotal()}")
        
s1 = Student()
s1.readData()
s1.print_details()

'''
Enter student roll number : 41
Enter student name : Joswin
Enter mark of subject 1 : 100
Enter mark of subject 2 : 100
Enter mark of subject 3 : 100
Roll number : 41
Name : Joswin
Marks : 100 100 100
Total : 300
'''

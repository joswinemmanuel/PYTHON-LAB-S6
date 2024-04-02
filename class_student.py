class Student(object):
    def __init__(self, name, sub_number):
        self.name = name
        self.sub_number = sub_number
        self.score = []
        for count in range(sub_number):
            self.score.append(0)
    
    def add_score(self):
        for i in range(self.sub_number):
            self.score[i] = int(input(f"Enter score of subject {i+1} : "))
            

S1 = Student("Joswin", 5)

print("Before adding score")
print(f"{S1.name} scored {S1.score}", end="\n\n")

S1.add_score()

print("\nAfter adding score")
print(f"{S1.name} scored {S1.score}", end="\n")

'''
Before adding score
Joswin scored [0, 0, 0, 0, 0]

Enter score of subject 1 : 50 
Enter score of subject 2 : 50
Enter score of subject 3 : 50
Enter score of subject 4 : 50
Enter score of subject 5 : 50

After adding score
Joswin scored [50, 50, 50, 50, 50]
'''

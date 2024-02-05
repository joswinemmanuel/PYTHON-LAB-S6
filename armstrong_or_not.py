n = input("Enter the number to check : ")
length = len(n)
sum = 0

for i in n:
    sum += int(i)**length

if sum == int(n):
    print(f'{n} is an armstrong number')
else:
    print(f'{n} is not an armstrong number')

'''
D:\joswin_python>python3 armstrong_or_not.py
Enter the number to check : 153 
153 is an armstrong number

D:\joswin_python>python3 armstrong_or_not.py
Enter the number to check : 123
123 is not an armstrong number

D:\joswin_python>python3 armstrong_or_not.py
Enter the number to check : 1634
1634 is an armstrong number
'''
n = int(input("Enter number of elements : "))
l=[]
for i in range(n):
    l.append(int(input(f"Enter the element {i+1} : ")))
    
l.sort()

if n % 2 != 0:
    print(f"The median is : {l[n//2]}")
else:
    print(f"The median is : {(l[n//2 - 1] + l[n//2]) / 2}")

'''
Enter number of elements : 5
Enter the element 1 : 1 
Enter the element 2 : 5
Enter the element 3 : 4
Enter the element 4 : 2
Enter the element 5 : 3
The median element is : 3
'''

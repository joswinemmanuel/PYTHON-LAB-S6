n = int(input("Enter the number of elements : "))
l = [int(input(f"Enter the element {i+1} : ")) for i in range(n)]

print(f"Before sorting : {l}")

for i in range(n):
    for j in range(n-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
            
print(f"After sorting : {l}")

'''
Enter the number of elements : 5
Enter the element 1 : 10
Enter the element 2 : 2
Enter the element 3 : 4
Enter the element 4 : 6
Enter the element 5 : 2
Before sorting : [10, 2, 4, 6, 2]
After sorting : [2, 2, 4, 6, 10]
'''

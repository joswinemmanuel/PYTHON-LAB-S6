n = int(input("Enter the number of rows : "))
m = int(input("Enter the number of columns : "))

M1, M2, M3 = [], [], []

print("Enter elements of Matrix 1")
for i in range(n):
    M1.append([])
    for j in range(m):
        M1[i].append(int(input(f"Enter element M1[{i}][{j}] : ")))

print("Enter elements of Matrix 2")
for i in range(n):
    M2.append([])
    for j in range(m):
        M2[i].append(int(input(f"Enter element M1[{i}][{j}] : ")))
        
print(f"MATRIX 1 IS : {M1}")
print(f"MATRIX 2 IS : {M2}")

for i in range(n):
    M3.append([])
    for j in range(m):
        M3[i].append(M1[i][j] + M2[i][j])
print(f"Their sum is : {M3}")

'''
Enter the number of rows : 2
Enter the number of columns : 3
Enter elements of Matrix 1
Enter element M1[0][0] : 1
Enter element M1[0][1] : 2
Enter element M1[0][2] : 3
Enter element M1[1][0] : 4
Enter element M1[1][1] : 5
Enter element M1[1][2] : 6
Enter elements of Matrix 2
Enter element M1[0][0] : 1
Enter element M1[0][1] : 2
Enter element M1[0][2] : 3
Enter element M1[1][0] : 1
Enter element M1[1][1] : 2
Enter element M1[1][2] : 3
MATRIX 1 IS : [[1, 2, 3], [4, 5, 6]]
MATRIX 2 IS : [[1, 2, 3], [1, 2, 3]]
Their sum is : [[2, 4, 6], [5, 7, 9]]
'''

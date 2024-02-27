n = int(input("Enter the number of rows : "))
m = int(input("Enter the number of columns : "))

M, T = [], []

print("Enter elements of Matrix")
for i in range(n):
    M.append([])
    for j in range(m):
        M[i].append(int(input(f"Enter element M[{i}][{j}] : ")))

for i in range(m):
    T.append([])
    for j in range(n):
        T[i].append(M[j][i])
    

print(f"Matrix is : {M}")
print(f"Transpose is : {T}")

'''
Enter the number of rows : 2
Enter the number of columns : 3
Enter elements of Matrix
Enter element M[0][0] : 1
Enter element M[0][1] : 2
Enter element M[0][2] : 3
Enter element M[1][0] : 4
Enter element M[1][1] : 5
Enter element M[1][2] : 6
Matrix is : [[1, 2, 3], [4, 5, 6]]
Transpose is : [[1, 4], [2, 5], [3, 6]]
'''

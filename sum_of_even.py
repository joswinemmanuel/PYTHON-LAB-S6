n = int(input("Enter the length : "))
even_sum = 0
for i in range(n):
    a = int(input("Enter number : "))
    if a%2 == 0:
        even_sum += a
print("The sum of even number is : ", even_sum)
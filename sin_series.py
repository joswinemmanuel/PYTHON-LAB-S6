import math
 
def sin(x, n):
    sine = 0
    for i in range(n):
        sign = (-1)**i
        y = x * (math.pi/180)
        sine += ((y**(2*i+1)) / math.factorial(2*i+1)) * sign 
    return sine
 
x = int(input("Enter value of x : "))
n = int(input("Enter value of n : "))
 
print(sin(x, n))

'''
Enter value of x : 45
Enter value of n : 5
0.7071067829368671
'''

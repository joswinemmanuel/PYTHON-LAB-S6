import math

def cos(x, n):
    cosine = 0
    for i in range(n):
        sign = (-1)**i
        y = x * (math.pi/180)
        cosine += sign * ((y**(2*i)) / math.factorial(2*i))
    return cosine

x = int(input("Enter value of x : "))
n = int(input("Enter value of n : "))

print(cos(x, n))

'''
Enter value of x : 30
Enter value of n : 5
0.8660254042103523
'''

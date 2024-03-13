def pow(a, b):
    power_val = 1
    for i in range(b):
        power_val *= a
    return power_val 

a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
print(f"{a} ** {b} = {pow(a, b)}")

'''
Enter value of a : 5
Enter value of b : 3
5 ** 3 = 125
'''

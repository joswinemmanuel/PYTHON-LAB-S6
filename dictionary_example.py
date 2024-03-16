d = {}
n = int(input("Enter number of values : "))

for i in range(1, n+1):
    key = int(input(f"Key {i} : "))
    val = input(f"Value {i} : ")
    d[key] = val

print(f"\nThe dictinoary is : {d}")


'''
Enter number of values : 3
Key 1 : 1
Value 1 : One
Key 2 : 2
Value 2 : Two
Key 3 : 3
Value 3 : Three

The dictinoary is : {1: 'One', 2: 'Two', 3: 'Three'}
'''

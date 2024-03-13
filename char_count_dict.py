s = input("Enter the string : ")
d = {}

for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

print(d)

'''
Enter the string : banana
{'b': 1, 'a': 3, 'n': 2}
'''

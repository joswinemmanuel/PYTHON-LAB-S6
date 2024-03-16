d = {4:'four', 1:'one', 3:'three', 2:'two'}
new_d = {}

for i in sorted(d):
    new_d[i] = d[i]

print(new_d)

'''
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
'''

bday = {}

n = int(input("Enter number of person : "))

for i in range(1, n+1):
    name = input(f"Enter name of person {i} : ")
    day = input(f"Enter birthday of person {i} : ")
    bday[name] = day

n = input("\nEnter the person name to find bday of : ")
if n in bday:
    print(f"Birthday : {bday[n]}")
else:
    print("Person not in dictionary")

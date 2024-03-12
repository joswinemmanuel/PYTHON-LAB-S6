def odd_even(n):
    if n%2 == 0:
        print("Even")
    else:
        print("Odd")

def positive_negative(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

def all_factors(n):
    for i in range(1, n+1):
        if n%i == 0:
            print(i)

while True:
    print('''\n1) Odd or Even
2) Positive or Negative
3) All Factors
4) Exit''')
    
    op = int(input("Enter your option : "))
    if op not in [1, 2, 3]:
        print("Exiting")
        break

    n = int(input("Enter the number : "))

    if op == 1:
        odd_even(n)
    elif op == 2:
        positive_negative(n)
    elif op == 3:
        all_factors(n)

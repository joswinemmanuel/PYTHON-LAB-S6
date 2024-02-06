
a = "This is a string"
print(a)

x = input("Enter a string : ")
print("Length of string : ", len(x))

print("String slicing")
print(f"First two characters : {x[:2]}")
print(f"Last two characters : {x[len(x)-2:]}")
print(f"Every other characters : {x[::2]}")
print(f"Reverse of the string : {x[::-1]}")

print(f"Type of x is : {type(x)}")

'''
This is a string
Enter a string : Joswin
Length of string :  6
String slicing
First two characters : Jo
Last two characters : in
Every other characters : Jsi
Reverse of the string : niwsoJ
Type of x is : <class 'str'>
'''
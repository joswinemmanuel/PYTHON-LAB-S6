x = int(input("Enter the X coordinate of the point : "))
y = int(input("Enter the Y coordinate of the point : "))

if x>0 and y>0:
    print(f"({x}, {y}) in the First Quadrant")
elif x<0 and y>0:
    print(f"({x}, {y}) in the Second Quadrant")
elif x<0 and y<0:
    print(f"({x}, {y}) in the Third Quadrant")
elif x>0 and y<0:
    print(f"({x}, {y}) in the Fourth Quadrant")
elif x==0:
    print(f"({x}, {y}) on the X axis")
elif y==0:
    print(f"({x}, {y}) on the Y axis")
else:
    print(f"({x}, {y}) the origin")
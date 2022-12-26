# Get three number ...

x = float(input("Enter x ->"))
y = float(input("Enter y ->"))
z = float(input("Enter z ->"))

largest = x

if y > x:
    if y >= z:
        largest = y
    else:
        largest = z
elif z > x:
    largest = z


print(largest)


# you can use max() function to get largest of user numbers

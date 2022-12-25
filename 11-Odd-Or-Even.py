# in this few line of code we want to check if a number is odd or even and show result

number = int(input())
result = None

if number % 2 == 0:
    result = "Even"
else:
    result = "Odd"

print(result)

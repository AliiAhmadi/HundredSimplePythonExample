
number = float(input("Enter your number ->"))
message = None
if number > 0:
    message = "Positive"
elif number < 0:
    message = "negative"
else:
    message = "Zero"

print(message)

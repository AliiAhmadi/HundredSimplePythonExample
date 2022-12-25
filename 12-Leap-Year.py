
year = int(input())

isLeap = False

if year % 100 == 0:
    if year % 400 == 0:
        isLeap = True
elif year % 4 == 0:
    isLeap = True

print("Leap" if isLeap else "Not leap")

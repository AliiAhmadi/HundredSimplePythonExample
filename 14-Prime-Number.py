
number = int(input())

isPrime = True

for i in range(2, number):
    if number % i == 0:
        isPrime = False
        break

print("Is Prime" if isPrime else "Is not Prime")

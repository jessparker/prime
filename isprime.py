import math
x = int(input("Enter a number: "))
i = 2
sqrt_x = math.sqrt(x)
isPrime = True

print("_________")

while i < sqrt_x:
    if x % i == 0:
        print(i, "is a factor of", x, "(", i, "x", int(x / i), "=", int(i * (x / i)), ")")
        isPrime = False
    i += 1

if isPrime:
    print(x, "is a prime number.")
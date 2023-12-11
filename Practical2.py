n = int(input("Enter n = "))

# 1. Check if 'n' is prime
if n == 2:
    print("'n' is prime.")
elif n % 2 == 0:
    print("'n' is not prime")
else:
    divisor = 3
    isPrime = True
    while divisor <= n / 2:
        if n % divisor == 0:
            isPrime = False
            break
        divisor += 2
    if isPrime:
        print("'n' is prime.")
    else:
        print("'n' is not prime.")

# 2. Generate all prime numbers till 'n'
print("Prime numbers till 'n'")
if n >= 2:
    print(2)
number = 3
while number <= n:
    if number % 2 == 0:
        number += 1
        continue
    else:
        divisor = 3
        isPrime = True
        while divisor <= number / 2:
            if number % divisor == 0:
                isPrime = False
                break
            divisor += 2
        if isPrime:
            print(number)
    number += 1

# 3. Generate first 'n' prime numbers
print("First 'n' prime numbers")
print(2)
number = 2
count = 1
while count < n:
    number += 1
    if number % 2 == 0:
        continue
    else:
        divisor = 3
        isPrime = True
        while divisor <= number / 2:
            if number % divisor == 0:
                isPrime = False
                break
            divisor += 2
        if isPrime:
            print(number)
            count += 1

# 4. Calculate sum of first 'n' natural numbers
print("Sum of first 'n' natural numbers")
number = 1
sum = 0
for i in range(n):
    sum += number
    number += 1
print(sum)

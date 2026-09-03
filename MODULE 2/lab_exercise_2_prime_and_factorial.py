# Lab Exercise 2: Prime Number and Factorial Programs

# Prime Number
print("===== PRIME NUMBER CHECK =====")
number = int(input("Enter a positive integer: "))

if number < 2:
    print(f"{number} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

# Factorial
print("\n===== FACTORIAL =====")
number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"Factorial of {number} = {factorial}")

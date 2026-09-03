# Lab Exercise 3: Fibonacci Series Using Recursion


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print("===== FIBONACCI SERIES USING RECURSION =====")
terms = int(input("Enter the number of terms: "))

if terms <= 0:
    print("Please enter a positive number of terms.")
else:
    print("Fibonacci series:")
    for i in range(terms):
        print(fibonacci(i), end=" ")
    print()

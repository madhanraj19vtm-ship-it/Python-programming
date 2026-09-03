# Lab Exercise 2: Variables, Operators, and Input/Output

name = input("Enter your name: ")
age = int(input("Enter your age: "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n--- Output ---")
print("Name:", name)
print("Age:", age)
print("Age next year:", age + 1)

print("\n--- Arithmetic Operators ---")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
    print("Floor Division:", num1 // num2)
    print("Modulus:", num1 % num2)
else:
    print("Division, floor division, and modulus are not possible with zero.")

print("Power:", num1 ** num2)

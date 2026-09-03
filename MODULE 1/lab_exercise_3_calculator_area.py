# Lab Exercise 3: Simple Calculator and Area Calculations

print("--- Simple Calculator ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operator.")

print("\n--- Area Calculator ---")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = input("Choose a shape (1/2/3): ")

if choice == "1":
    radius = float(input("Enter radius: "))
    area = 3.14159 * radius * radius
    print("Area of circle:", area)
elif choice == "2":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    print("Area of rectangle:", area)
elif choice == "3":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Area of triangle:", area)
else:
    print("Invalid choice.")

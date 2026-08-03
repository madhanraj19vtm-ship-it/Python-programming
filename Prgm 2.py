# Accept two numbers from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Perform operations
add = a + b
sub = a - b
mul = a * b
div = a / b
floor_div = a // b
mod = a % b
exp = a ** b

# Display results
print("\n----- Results -----")
print(f"Addition       : {add}")
print(f"Subtraction    : {sub}")
print(f"Multiplication : {mul}")
print(f"Division       : {div}")
print(f"Floor Division : {floor_div}")
print(f"Modulus        : {mod}")
print(f"Exponentiation : {exp}")

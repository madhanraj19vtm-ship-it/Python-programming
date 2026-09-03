# Mini Project: Unit Converter
# Converts common units of length, weight, and temperature.

print("===== UNIT CONVERTER =====")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Kilograms to Pounds")
print("4. Pounds to Kilograms")
print("5. Celsius to Fahrenheit")
print("6. Fahrenheit to Celsius")

choice = input("Enter your choice (1-6): ")
value = float(input("Enter the value to convert: "))

if choice == "1":
    result = value * 0.621371
    print(f"{value} km = {result:.2f} miles")
elif choice == "2":
    result = value * 1.60934
    print(f"{value} miles = {result:.2f} km")
elif choice == "3":
    result = value * 2.20462
    print(f"{value} kg = {result:.2f} pounds")
elif choice == "4":
    result = value * 0.453592
    print(f"{value} pounds = {result:.2f} kg")
elif choice == "5":
    result = (value * 9 / 5) + 32
    print(f"{value}°C = {result:.2f}°F")
elif choice == "6":
    result = (value - 32) * 5 / 9
    print(f"{value}°F = {result:.2f}°C")
else:
    print("Invalid choice. Please select a number from 1 to 6.")

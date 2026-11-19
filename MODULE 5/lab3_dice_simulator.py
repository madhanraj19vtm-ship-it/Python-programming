# MODULE 5 - LAB 3: Dice Simulator using random Module

import random

def roll_dice(number_of_dice):
    results = []
    for _ in range(number_of_dice):
        results.append(random.randint(1, 6))
    return results


def main():
    print("===== DICE SIMULATOR =====")

    while True:
        try:
            number = int(input("How many dice do you want to roll? "))
            if number <= 0:
                print("Please enter a number greater than zero.")
                continue
            break
        except ValueError:
            print("Please enter a valid whole number.")

    results = roll_dice(number)

    print("\nDice Results:")
    for index, value in enumerate(results, start=1):
        print(f"Dice {index}: {value}")

    print("Total:", sum(results))

    if number == 1:
        print("Highest value:", max(results))
    else:
        print("Highest value:", max(results))
        print("Lowest value:", min(results))


if __name__ == "__main__":
    main()

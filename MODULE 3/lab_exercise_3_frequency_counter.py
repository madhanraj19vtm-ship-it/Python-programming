# Lab Exercise 3: Frequency Counter using Dictionaries

text = input("Enter a word or sentence: ").lower()

frequency = {}

for character in text:
    if character.isalnum():
        frequency[character] = frequency.get(character, 0) + 1

print("\n===== FREQUENCY COUNT =====")
for item, count in sorted(frequency.items()):
    print(f"{item}: {count}")

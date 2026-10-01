# Lab Exercise 2: Student Grading System

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

name = input("Enter student name: ").strip()
number_of_subjects = int(input("Enter number of subjects: "))

marks = []

for i in range(1, number_of_subjects + 1):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

total = sum(marks)
average = total / number_of_subjects
grade = calculate_grade(average)

print("\n===== STUDENT RESULT =====")
print("Student Name:", name)
print("Marks:", marks)
print("Total Marks:", total)
print(f"Average: {average:.2f}")
print("Grade:", grade)

if grade == "F":
    print("Result: FAIL")
else:
    print("Result: PASS")

# Mini Project: Student Grading Automation
# Calculates total, average, grade, and pass/fail status for a student.

print("===== STUDENT GRADING AUTOMATION =====")

name = input("Enter student name: ")

subjects = ["Python", "Mathematics", "English", "Computer Science", "Data Structures"]
marks = []

for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

total = sum(marks)
average = total / len(marks)

if any(mark < 40 for mark in marks):
    grade = "F"
    status = "Fail"
elif average >= 90:
    grade = "A+"
    status = "Pass"
elif average >= 80:
    grade = "A"
    status = "Pass"
elif average >= 70:
    grade = "B"
    status = "Pass"
elif average >= 60:
    grade = "C"
    status = "Pass"
elif average >= 50:
    grade = "D"
    status = "Pass"
else:
    grade = "F"
    status = "Fail"

print("\n===== STUDENT RESULT =====")
print("Student Name:", name)

for subject, mark in zip(subjects, marks):
    print(f"{subject}: {mark:.1f}")

print("Total Marks:", total)
print(f"Average: {average:.2f}")
print("Grade:", grade)
print("Status:", status)

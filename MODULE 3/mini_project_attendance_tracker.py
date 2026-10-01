# Mini Project: Attendance Tracker

students = {}

def add_student():
    roll_no = input("Enter roll number: ").strip()
    name = input("Enter student name: ").strip()

    if roll_no in students:
        print("Student already exists.")
        return

    students[roll_no] = {
        "name": name,
        "present": 0,
        "total": 0
    }
    print("Student added successfully.")

def mark_attendance():
    if not students:
        print("No students available.")
        return

    print("\nEnter P for Present and A for Absent.")
    for roll_no, student in students.items():
        status = input(f"{roll_no} - {student['name']}: ").strip().upper()

        if status not in ("P", "A"):
            print("Invalid status. Marked as Absent.")
            status = "A"

        student["total"] += 1

        if status == "P":
            student["present"] += 1

    print("Attendance marked successfully.")

def view_report():
    if not students:
        print("No students available.")
        return

    print("\n===== ATTENDANCE REPORT =====")
    for roll_no, student in students.items():
        total = student["total"]
        present = student["present"]
        percentage = (present / total * 100) if total > 0 else 0

        print(
            f"{roll_no} - {student['name']} | "
            f"Present: {present}/{total} | "
            f"Attendance: {percentage:.2f}%"
        )

while True:
    print("\n===== ATTENDANCE TRACKER =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance Report")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        mark_attendance()
    elif choice == "3":
        view_report()
    elif choice == "4":
        print("Exiting Attendance Tracker.")
        break
    else:
        print("Invalid choice. Please try again.")

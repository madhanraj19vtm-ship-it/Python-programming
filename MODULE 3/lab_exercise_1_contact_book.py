# Lab Exercise 1: Contact Book using Lists and Dictionaries

contacts = []

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n===== CONTACT BOOK =====")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")

def search_contact():
    name = input("Enter name to search: ").strip().lower()

    found = False
    for contact in contacts:
        if contact["name"].lower() == name:
            print("\nContact found:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True

    if not found:
        print("Contact not found.")

while True:
    print("\n===== CONTACT BOOK MENU =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice. Please try again.")

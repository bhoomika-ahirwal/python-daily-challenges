contacts = {}


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    contacts[name] = phone

    print("Contact saved.")


def view_contacts():

    if not contacts:
        print("No contacts found.")
        return

    print("\n--- Contacts ---")

    for name, phone in contacts.items():
        print(f"{name}: {phone}")


def search_contact():
    name = input("Enter name to search: ")

    phone = contacts.get(name)

    if phone:
        print(f"{name}: {phone}")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")


while True:

    print("\n--- Contact Manager ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        break

    else:
        print("Invalid choice.")
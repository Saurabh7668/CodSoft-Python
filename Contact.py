contacts = []

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    contact = {
        'Name': name,
        'Phone Number': phone,
        'Email': email,
        'Address': address
    }
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['Name']}, Phone: {contact['Phone Number']}, Email: {contact['Email']}, Address: {contact['Address']}")

def search_contact():
    search_term = input("Enter the name or phone number to search: ")
    found_contacts = []
    for contact in contacts:
        if search_term in contact['Name'] or search_term in contact['Phone Number'] or search_term in contact['Email'] or search_term in contact['Address']:
            found_contacts.append(contact)
    if not found_contacts:
        print("No matching contacts found.")
    else:
        print("Matching Contacts:")
        for index, contact in enumerate(found_contacts, start=1):
            print(f"{index}. Name: {contact['Name']}, Phone: {contact['Phone Number']}, Email: {contact['Email']}, Address: {contact['Address']}")

def update_contact():
    view_contacts()
    try:
        index = int(input("Enter the index of the contact to update: ")) - 1
        if 0 <= index < len(contacts):
             updated_contact = contacts[index]
             updated_contact['Name'] = input("Enter updated name: ")
             updated_contact['Phone Number'] = input("Enter updated phone number: ")
             updated_contact['Email'] = input("Enter updated email: ")
             updated_contact['Address'] = input("Enter updated address: ")
             print("Contact updated successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def delete_contact():
    view_contacts()
    try:
        index = int(input("Enter the index of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            del contacts[index]
            print("Contact deleted successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

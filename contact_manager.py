class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)
        print(f"Added contact: {contact}")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contacts:")
            for contact in self.contacts:
                print(contact)

    def search_contacts(self, name):
        found_contacts = [contact for contact in self.contacts if name.lower() in contact.name.lower()]
        if found_contacts:
            print("Found contacts:")
            for contact in found_contacts:
                print(contact)
        else:
            print("No contacts found.")


def main():
    manager = ContactManager()
    
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            manager.add_contact(name, phone)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            manager.search_contacts(name)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
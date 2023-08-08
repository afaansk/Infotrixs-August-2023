#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ContactManagementSystem:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email):
        if name not in self.contacts:
            self.contacts[name] = {'phone_number': phone_number, 'email': email}
            print(f"Contact '{name}' added successfully!")
        else:
            print(f"Contact '{name}' already exists.")

    def search_contact(self, name):
        if name in self.contacts:
            contact_details = self.contacts[name]
            print(f"Contact Details for '{name}':")
            print(f"Phone Number: {contact_details['phone_number']}")
            print(f"Email: {contact_details['email']}")
        else:
            print(f"Contact '{name}' not found.")

    def update_contact(self, name, phone_number=None, email=None):
        if name in self.contacts:
            contact_details = self.contacts[name]
            if phone_number:
                contact_details['phone_number'] = phone_number
            if email:
                contact_details['email'] = email
            print(f"Contact '{name}' updated successfully!")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found.")


def main():
    contact_system = ContactManagementSystem()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_system.add_contact(name, phone_number, email)
        elif choice == '2':
            name = input("Enter contact name to search: ")
            contact_system.search_contact(name)
        elif choice == '3':
            name = input("Enter contact name to update: ")
            phone_number = input("Enter new phone number (press Enter to skip): ")
            email = input("Enter new email (press Enter to skip): ")
            contact_system.update_contact(name, phone_number, email)
        elif choice == '4':
            name = input("Enter contact name to delete: ")
            contact_system.delete_contact(name)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()


# In[ ]:





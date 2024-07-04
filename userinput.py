# create a complete user interface to ask user input amongst the following:
# 1. add a new contact (name, phone number, email)
# 2. search for a contact
# 3. update a contact

import os

# Directory to store contact files
CONTACT_DIR = "contacts"

def add_contact():
    """Adds a new contact to the contact book."""
    print("Add a New Contact")
    name = input("Enter the contact name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address (optional): ")

    # Create the contact file
    contact_file = os.path.join(CONTACT_DIR, f"{name}.txt")
    with open(contact_file, "w") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Phone: {phone}\n")
        if email:
            f.write(f"Email: {email}\n")

    print("Contact added successfully!")

def search_contact():
    """Searches for a contact in the contact book."""
    print("Search for a Contact")
    name = input("Enter the contact name: ")

    contact_file = os.path.join(CONTACT_DIR, f"{name}.txt")
    if os.path.exists(contact_file):
        with open(contact_file, "r") as f:
            print(f.read())
    else:
        print("Contact not found.")

def update_contact():
    """Updates an existing contact in the contact book."""
    print("Update a Contact")
    name = input("Enter the contact name: ")

    contact_file = os.path.join(CONTACT_DIR, f"{name}.txt")
    if os.path.exists(contact_file):
        with open(contact_file, "r") as f:
            contact_info = f.readlines()

        new_phone = input(f"Enter the new phone number (current: {contact_info[1].split(': ')[1].strip()}): ")
        new_email = input(f"Enter the new email address (current: {contact_info[2].split(': ')[1].strip() if len(contact_info) > 2 else 'None'}): ")

        with open(contact_file, "w") as f:
            f.write(contact_info[0])
            f.write(f"Phone: {new_phone}\n")
            if new_email:
                f.write(f"Email: {new_email}\n")

        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def main():
    """Main function to handle user input and options."""
    os.makedirs(CONTACT_DIR, exist_ok=True)

    while True:
        print("\nContact Book Menu:")
        print("1. Add a New Contact")
        print("2. Search for a Contact")
        print("3. Update a Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            print("Exiting the Contact Book...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

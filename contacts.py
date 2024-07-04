import sqlite3

# Database file
DB_FILE = "contacts.db"

def create_database():
    """Create the contacts database if it doesn't exist."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    phone TEXT,
                    email TEXT
                )""")
    conn.commit()
    conn.close()

def create_contact():
    """Adds a new contact to the contact book."""
    print("Add a New Contact")
    name = input("Enter the contact name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()

    print("Contact added successfully!")

def read_contact():
    """Searches for a contact in the contact book."""
    print("Search for a Contact")
    name = input("Enter the contact name: ")

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM contacts WHERE name = ?", (name,))
    contact = c.fetchone()
    conn.close()

    if contact:
        print(f"ID: {contact[0]}")
        print(f"Name: {contact[1]}")
        print(f"Phone: {contact[2]}")
        print(f"Email: {contact[3]}")
    else:
        print("Contact not found.")

def update_contact():
    """Updates an existing contact in the contact book."""
    print("Update a Contact")
    contact_id = int(input("Enter the contact ID: "))

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
    contact = c.fetchone()

    if contact:
        
        new_name = input(f"Enter the new name (current: {contact[1]}): ")
        new_phone = input(f"Enter the new phone number (current: {contact[2]}): ")
        new_email = input(f"Enter the new email address (current: {contact[3]}): ")
        if not new_name:
            new_name = contact[1]
        if not new_phone:
            new_phone = contact[2]
        if not new_email:
            new_email = contact[3]
        
        c.execute("""UPDATE contacts
                     SET name = ?, phone = ?, email = ?
                     WHERE id = ?""", (new_name, new_phone, new_email, contact_id))
        conn.commit()
        conn.close()

        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    """Deletes an existing contact from the contact book."""
    print("Delete a Contact")
    contact_id = int(input("Enter the contact ID: "))

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
    contact = c.fetchone()

    if contact:
        c.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        conn.commit()
        conn.close()
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    """Main function to handle user input and options."""
    create_database()

    while True:
        print("\nContact Book Menu:")
        print("1. Create a New Contact")
        print("2. Read a Contact")
        print("3. Update a Contact")
        print("4. Delete a Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            create_contact()
        elif choice == "2":
            read_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting the Contact Book...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

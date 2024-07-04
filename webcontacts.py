from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

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

@app.route("/")
def index():
    """Displays the main page with the contact book menu."""
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create_contact():
    """Adds a new contact to the contact book."""
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]

        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    return render_template("create.html")

@app.route("/read", methods=["GET", "POST"])
def read_contact():
    """Searches for a contact in the contact book."""
    if request.method == "POST":
        name = request.form["name"]

        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("SELECT * FROM contacts WHERE name = ?", (name,))
        contact = c.fetchone()
        conn.close()

        if contact:
            return render_template("read.html", contact=contact)
        else:
            return "Contact not found."

    return render_template("read.html")

@app.route("/update/<int:contact_id>", methods=["GET", "POST"])
def update_contact(contact_id):
    """Updates an existing contact in the contact book."""
    if request.method == "POST":
        new_name = request.form["name"]
        new_phone = request.form["phone"]
        new_email = request.form["email"]

        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
    contact = c.fetchone()
    conn.close()

    if contact:
        return render_template("update.html", contact=contact)
    else:
        return "Contact not found."

@app.route("/delete/<int:contact_id>", methods=["GET", "POST"])
def delete_contact(contact_id):
    """Deletes an existing contact from the contact book."""
    if request.method == "POST":
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        conn.commit()
        conn.close()

        return redirect(url_for("index"))

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
    contact = c.fetchone()
    conn.close()

    if contact:
        return render_template("delete.html", contact=contact)
    else:
        return "Contact not found."

if __name__ == "__main__":
    create_database()
    app.run(debug=True)

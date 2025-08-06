import sqlite3

def init_db():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_contact(name, email=None):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

def get_all_contacts():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM contacts")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_contact(contact_id):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    conn.close()
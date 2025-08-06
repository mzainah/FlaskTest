# app.py
import os
from flask import Flask, render_template, request, redirect, url_for
from database import get_all_contacts, add_contact, delete_contact

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form.get("email", "").strip() or None  # Use None if empty
        add_contact(name, email)
        return redirect(url_for("home"))  # Prevent re-submission on refresh

    contacts = get_all_contacts()  # Load from database
    return render_template("index.html", contacts=contacts)

@app.route("/delete/<int:contact_id>")
def delete(contact_id):
    delete_contact(contact_id)
    return redirect(url_for("home"))

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
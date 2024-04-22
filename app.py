from flask import Flask, redirect, render_template, request
from model import Contact

Contact.load_db()

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/contacts")

@app.route("/contacts") 
def contacts():
    q = request.args.get("q")
    if q == "":
        contacts = Contact.get_all()
    else:
        contacts = Contact.search(q)
    return render_template("index.html", contacts=contacts)

@app.route("/contacts/new")
def contacts_new_get():
    return render_template("new.html")

from flask import Flask, redirect, render_template, request
from model import Contact

Contact.load_db()

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/contacts")

@app.route("/contacts", methods=["GET"])
def contacts_get():
    q = request.args.get("q")
    if q == "":
        contacts = Contact.get_all()
    else:
        contacts = Contact.search(q)
    return render_template("index.html", contacts=contacts)

@app.route("/contacts", methods=["POST"])
def contacts_post():
    pass

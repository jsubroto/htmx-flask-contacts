from flask import Flask, redirect, render_template
from model import Contact

Contact.load_db()

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/contacts")

@app.route("/contacts")
def contacts():
    return render_template("index.html", contacts=Contact.get_all())

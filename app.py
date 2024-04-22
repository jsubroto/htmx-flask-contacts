from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/contacts")

@app.route("/contacts")
def contacts():
    return render_template("index.html")

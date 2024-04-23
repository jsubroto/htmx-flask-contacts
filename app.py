from flask import Flask, redirect, render_template, request, flash
from model import Contact

Contact.load_db()

app = Flask(__name__)
app.secret_key = b"`7C3}4C'ze!i"


@app.route("/")
def index():
    return redirect("/contacts")


@app.route("/contacts")
def contacts():
    q = request.args.get("q")
    if q is None:
        contacts = Contact.get_all()
    else:
        contacts = Contact.search(q)
    return render_template("index.html", contacts=contacts)


@app.route("/contacts/new", methods=["GET"])
def contacts_new_get():
    return render_template("new.html", contact=Contact())


@app.route("/contacts/new", methods=["POST"])
def contacts_new_post():
    c = Contact(None, request.form["firstName"], request.form["lastName"], request.form["email"], request.form["phone"])
    if c.save():
        return redirect("/contacts")
    else:
        return render_template("new.html", contact=c)


@app.route("/contacts/<int:contact_id>")
def contacts_view(contact_id):
    return render_template("view.html", contact=Contact.get_by_id(contact_id))


@app.route("/contacts/<int:contact_id>/edit", methods=["GET"])
def contacts_edit_get(contact_id):
    return render_template("edit.html", contact=Contact.get_by_id(contact_id))


@app.route("/contacts/<int:contact_id>/edit", methods=["POST"])
def contacts_edit_post(contact_id):
    c = Contact.get_by_id(contact_id)
    c.update(request.form["firstName"], request.form["lastName"], request.form["email"], request.form["phone"])
    if c.save():
        flash("Updated Contact")
        return redirect(f"/contacts/{c.id}")
    else:
        return render_template("edit.html", contact=c)


@app.route("/contacts/<int:contact_id>/delete", methods=["POST"])
def contacts_delete(contact_id):
    Contact.delete_by_id(contact_id)
    flash("Deleted Contact")
    return redirect("/contacts")

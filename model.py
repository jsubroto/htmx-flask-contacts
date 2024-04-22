import json


class Contact:

    db = {}

    def __init__(self, id=None, first_name=None, last_name=None, email=None, phone=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    @classmethod
    def load_db(cls):
        with open("dummy_contacts.json", 'r') as users_file:
            contacts = json.load(users_file)
            for c in contacts:
                cls.db[c["id"]] = Contact(c["id"], c["firstName"], c["lastName"], c["email"], c["phone"])

    @classmethod
    def get_all(cls):
        return list(cls.db.values())

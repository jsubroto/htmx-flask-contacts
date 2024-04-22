import json


class Contact:

    db = {}

    def __init__(self, id=None, first_name=None, last_name=None, email=None, phone=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def save(self):
        max_id = max(contact.id for contact in Contact.db.values())
        self.id = max_id + 1
        Contact.db[self.id] = self
        Contact.save_db()

    @classmethod
    def load_db(cls):
        with open("dummy_contacts.json", 'r') as contacts_file:
            contacts = json.load(contacts_file)
            for c in contacts:
                cls.db[c["id"]] = Contact(c["id"], c["firstName"], c["lastName"], c["email"], c["phone"])

    @classmethod
    def get_all(cls):
        return list(cls.db.values())

    @classmethod
    def search(cls, search_text):
        def is_match(full_text, search_text=search_text):
            return full_text is not None and search_text.lower() in full_text.lower()

        results = []
        for c in cls.db.values():
            if is_match(c.first_name) or is_match(c.last_name) or is_match(c.email) or is_match(c.phone):
                results.append(c)
        return results

    @classmethod
    def save_db(cls):
        with open("dummy_contacts.json", 'w') as write_file:
            json.dump([{
                "id": c.id,
                "firstName": c.first_name,
                "lastName": c.last_name,
                "email": c.email,
                "phone": c.phone
            } for c in cls.db.values()], write_file, indent=2)

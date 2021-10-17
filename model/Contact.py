import json

class Contact:
    def __init__(self, name, surname, phone, address):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.address = address

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
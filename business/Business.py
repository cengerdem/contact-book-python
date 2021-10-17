from data_access.DataAccess import ContactDataAccess

class ContactBusiness:
    def __init__(self):
        pass

    contact_data_accessor = ContactDataAccess()
    contact_list = {}

    def print_contact(self, contact):
        print("************\r\n")
        print("Record Number: ", contact["id"])
        print("Name: ", contact["name"] + " " + contact["surname"])
        print("Phone: ", contact["phone"])
        print("Address: ", contact["address"])
        print("\r\n************")

    def list_contacts(self):
        return self.contact_data_accessor.get_all()
    
    def add_contact(self, contact):
        return self.contact_data_accessor.add(contact)
        
    def delete_contact(self, id):
        return self.contact_data_accessor.delete(int(id))

        
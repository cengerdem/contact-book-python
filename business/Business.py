from data_access.DataAccess import ContactDataAccess

class ContactBusiness:
    def __init__(self):
        pass

    contact_data_accessor = ContactDataAccess()

    #Prints the given contact's properties
    def print_contact(self, contact):
        print("************\r\n")
        print("Record Number: ", contact["id"])
        print("Name: ", contact["name"] + " " + contact["surname"])
        print("Phone: ", contact["phone"])
        print("Address: ", contact["address"])
        print("\r\n************")

    #returns all contacts from db
    def list_contacts(self):
        return self.contact_data_accessor.get_all()
    
    #inserts a contact to db
    def add_contact(self, contact):
        return self.contact_data_accessor.add(contact)
        
    #deletes the contact that given id from db
    def delete_contact(self, id):
        return self.contact_data_accessor.delete(int(id))

        
import os
from datetime import datetime
from data_access.DataAccess import ContactDataAccess

class BaseBusiness():
    def __init__(self):
        pass
    
    def log_info(self, guid, operation):
        current_dir = os.path.dirname(__file__) 
        rel_path = "../info.log"
        info_log_file_path = os.path.join(current_dir, rel_path)

        f = open(info_log_file_path, "a")
        template = " Operation: {0} \n Session {1}. \n Operation Date: {2!r} \r\n\r\n"
        message = template.format(operation, guid, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        f.write(message)
        f.close()

class ContactBusiness(BaseBusiness):
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

        
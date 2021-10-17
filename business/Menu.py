import time
import sys
from model.Contact import Contact

class Menu:
    def __init__(self):
        pass

    def input_name(self):
        name = input("Name: ")
        if(name.strip() == ""):
                print("Name Is A Required Field")
                is_exit = input("Enter 0 to exit...(Enter anything except 0 to try again)")
                if is_exit == "0":
                    return None
                return  self.input_name()
        
        return name

    def input_phone(self, contact_list):
        phone = input("Phone: ")

        if(phone.strip() == ""):
                print("Phone Is A Required Field")
                is_exit = input("Enter 0 to exit...(Enter anything except 0 to try again)")
                if is_exit == "0":
                    return None
                return  self.input_phone(contact_list)
        
        for contact in contact_list:
            if contact["phone"] == phone :
                print("This phone already recorded for", contact["name"], contact["surname"])
                is_exit = input("Enter 0 to exit...(Enter anything except 0 to try again)")
                if is_exit == "0":
                    return None
                return  self.input_phone(contact_list)
        
        
        return phone


    def show_contact_menu(self, contact, contact_list, contact_business):
        contact_business.print_contact(contact)

        print("\r\n\t1- Delete Contact")
        print("\t0- Return to Contact Book")

        selection = input("\r\n\tSelect an operation: ")

        if selection == "1":
            confirm = input("Record will be delete. Do you confirm? (Y/N) ")
            
            if confirm.upper() == "Y":
                result = contact_business.delete_contact(contact["id"])
                if result == True:
                    self.show_main_menu(contact_business)
                else:
                    print("\r\nOperation failed.")
                    time.sleep(1)
                    self.show_contact_menu(contact, contact_list, contact_business)
          
            elif confirm.upper() == "N":
                print("\r\nOperation canceled...")
                time.sleep(1)
                self.show_contact_menu(contact, contact_list, contact_business)
            else:
                print("\r\nIncorrect Input")
                time.sleep(1)
                self.show_contact_menu(contact, contact_list, contact_business)

        else:
            print("\r\nIncorrect Selection")
            time.sleep(1)
            self.show_contact_menu(contact, contact_list, contact_business)

    def search_contact_by_record_number(self, contact_list, contact_business):
        contact_id = input("Enter the record number: ")
        selected_contact = None
        for contact in contact_list:
            if contact["id"] == int(contact_id):
                selected_contact = contact

        if selected_contact != None:
            self.show_contact_menu(selected_contact, contact_list, contact_business)
        else:
            print("No records found with the record number ", contact_id)
            time.sleep(1)
            self.show_main_menu(contact_business)

    def show_main_menu(self, contact_business):
        print("\r\nWelcome to Contact Book")
        print("\r\nAll of the contacts listed below: \r\n\r\n")
        
        contact_list = contact_business.list_contacts()
    
        for contact in contact_list:
            contact_business.print_contact(contact)

        time.sleep(1)
        print("\r\n\t1- Search By Record Number")
        print("\t2- Search By Name")
        print("\t3- Add New")
        print("\t0- Exit")

        selection = input("\r\n\tSelect an operation: ")

        if(selection == "1"):
            self.search_contact_by_record_number(contact_list, contact_business)

        elif(selection == "2"):
            contact_search_name = input("Enter the name: ").strip()
         
            selected_contacts = list()
            for contact in contact_list:
                contact_combined_name = contact["name"] + " " + contact["surname"]
                if contact_combined_name.find(contact_search_name) != -1 or contact["name"].find(contact_search_name.strip()) != -1 or  contact["surname"].find(contact_search_name.strip()) != -1:
                    selected_contacts.append(contact)
                    print(selected_contacts)
                

            if selected_contacts != [] and len(selected_contacts) == 1:
                self.show_contact_menu(selected_contacts[0], contact_list, contact_business)
            
            elif selected_contacts != [] and len(selected_contacts) > 1 :
                print("\r\nThere is multiple records found with this name", contact_search_name)
                time.sleep(1)
                for contact in selected_contacts:
                    contact_business.print_contact(contact)

                print("\r\nPlease search with record number")
                time.sleep(1)
                self.search_contact_by_record_number(contact_list, contact_business)

            else:
                print("No records found with the name ", contact_search_name)
                time.sleep(1)
                self.show_main_menu(contact_business)
        
        elif(selection == "3"):
            print("\r\nAdd a new contact")
            new_contact = Contact("","","","")
            new_contact.name = self.input_name()
            new_contact.surname = input("Surname: ")
            new_contact.phone = self.input_phone(contact_list)
            new_contact.address = input("Address: ")

            contact_business.add_contact(new_contact)

            self.show_main_menu(contact_business)

        elif(selection == "0"):
            print("Contact Book will close...")
            sys.exit()
        else:
            print("\r\nIncorrect Selection")
            time.sleep(1)
            self.show_main_menu(contact_business)
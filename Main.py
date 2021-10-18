import sys
from business.Business import ContactBusiness
from business.Menu import Menu

class Main:
    try:
        contact_business = ContactBusiness()
        menu = Menu()
        menu.show_main_menu(contact_business)
    except Exception as Argument:
        f = open("error.log", "a")
        f.write(str(Argument))
        f.close()
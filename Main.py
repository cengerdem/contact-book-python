from business.Business import ContactBusiness
from business.Menu import Menu

class Main:
    contact_business = ContactBusiness()
    menu = Menu()
    menu.show_main_menu(contact_business)
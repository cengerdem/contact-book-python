import uuid
import time
from datetime import datetime
from business.Menu import Menu

class Main:
    def main(self):
        try:
            # creating an uuid(guid) for each session
            guid = uuid.uuid4()
            menu = Menu()
            menu.show_main_menu(guid)
        except Exception as ex:
            print("An error occured. You can check this error in error.log. Returning to main menu...")
            time.sleep(2)

            # opens error.log file (creates if it is not exist)
            f = open("error.log", "a")
            # error log template
            template = "An exception of type {0} occurred in session {1}. Arguments:\n{2!r} \n Exception Date: {3!r} \r\n\r\n"
            message = template.format(type(ex).__name__, guid, ex.args, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            f.write(message)
            f.close()
            
            self.main()
    
if __name__ == "__main__":
    Main().main()
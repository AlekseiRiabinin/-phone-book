from view import Console
from model import Database

def start():
    c = Console()
    db = Database()

    user_choice = 0
    while user_choice != 8:
        user_choice = c.main_menu()

        if user_choice == 1:
            phone_book = db.get_phone_book()
            c.show_contacts(phone_book)             
            
        elif user_choice == 2:
            db.open_phone_book()
            c.load_success()

        elif user_choice == 3:
            db.save_phone_book()
            c.save_success()          

        elif user_choice == 4:
            new = list(c.new_contact())
            db.update_phone_book(new)

        elif user_choice == 5:
            c.show_contacts(phone_book) 
            name = c.id_contact() 
            new = list(c.new_contact())
            db.update_contact(name, new)

        elif user_choice == 6:
            name = c.id_contact()
            db.remove_contact(name)
          
        elif user_choice == 7:
            search = c.find_contact()
            result = db.search_contact(search)
            c.show_contacts(result)
            
        else: break



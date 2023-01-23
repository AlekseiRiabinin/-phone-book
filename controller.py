import view
import model

def start():
    user_choice = 0
    
    while user_choice != 8:
        user_choice = view.main_menu()

        if user_choice == 1:
            phone_book = model.get_phone_book()
            view.show_contacts(phone_book)             
            
        elif user_choice == 2:
            model.open_phone_book()
            view.load_success()

        elif user_choice == 3:
            model.save_phone_book()
            view.save_success()          

        elif user_choice == 4:
            new = list(view.new_contact())
            model.update_phone_book(new)

        elif user_choice == 5:
            print ('choice 5')    

        elif user_choice == 6:
            print ('choice 6')

        elif user_choice == 7:
            search = view.find_contact()
            result = model.search_contact(search)
            view.show_contacts(result)
            
        else: break



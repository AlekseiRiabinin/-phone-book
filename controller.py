import view

def start():
    user_choice = 0
    
    while user_choice != 8:
        user_choice = view.main_menu()

        if user_choice == 1:
            phone_book = model.get_phone_book()
            view.show_contacts(phone_book)             
            
        elif user_choice == 2:
            print ('choice 2')

        elif user_choice == 3:
            print ('choice 3')            

        elif user_choice == 4:
            print ('choice 4')

        elif user_choice == 5:
            print ('choice 5')    

        elif user_choice == 6:
            print ('choice 6')

        elif user_choice == 7:
            print ('choice 7')
            
        else: break



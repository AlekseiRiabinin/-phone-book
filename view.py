class Console:  
    def __init__(self):
        self.commands = [
            'Get all contacts',
            'Open file',
            'Save file',
            'Add contact',
            'Update contact',
            'Delete contact',
            'Find contact',
            'Exit'
        ]

    def main_menu(self):      
        print('\nPhone book menu') 
        print('-----------------') 
        for i in range(len(self.commands)):
            print(f'{i+1}. {self.commands[i]}')

        user_input = int(input('\nEnter your choice: '))
        return user_input    

    def show_contacts(self, phone_book: list):
        if len(phone_book) > 0:
            for item in phone_book:
                print(f'{item[0]} {item[1]} ({item[2]})')
        else:
            print('Phone book is empty or unloaded')  

    def load_success(self):
        print('Phonebook is loaded successfully')

    def save_success(self):
        print('Phonebook is saved successfully')

    def new_contact(self):
        name = input('\nEnter name and surname: ')
        phone = input('Enter phone number: ')
        comment = input('Enter comment: ')
        return name, phone, comment

    def find_contact(self):
        search = input('\nEnter contact details: ')
        return search       

    def id_contact(self):
        name = input('\nEnter name of contact: ')
        return name      
def main_menu():
    commands = [
        'Get all contacts',
        'Open file',
        'Save file',
        'Add contact',
        'Update contact',
        'Delete contact',
        'Find contact',
        'Exit'
    ]

    print('\nPhone book menu') 
    print('-----------------') 
    for i in range(len(commands)):
        print(f'{i+1}. {commands[i]}')

    user_input = int(input('\nEnter your choice: '))
    return user_input    

def show_contacts(phone_book: list):
    if len(phone_book) > 0:
        for item in phone_book:
            print(f'{item[0]} {item[1]} ({item[2]})')
    else:
        print('Phone book is empty or unloaded')  

def load_success():
    print('Phonebook is loaded successfully')

def save_success():
    print('Phonebook is saved successfully')

def new_contact():
    name = input('\nEnter name and surname: ')
    phone = input('Enter phone number: ')
    comment = input('Enter comment: ')
    return name, phone, comment

def find_contact():
    search = input('\nEnter contact details: ')
    return search       

def id_contact():
    name = input('\nEnter name of contact: ')
    return name      
def main_menu():
    commands = [
        'Get all contacts',
        'Save file',
        'Add contact',
        'Update contact',
        'Delete contact',
        'Find contact',
        'Exit'
    ]

    for i in range(len(commands)):
        print(f'\t{i+1}. {commands[i]}')

    user_input = int(input('\nEnter your choice: '))
    return user_input    

def show_contacts(phone_book: list):
    if len(phone_book) > 0:
        for item in phone_book:
            print(*item)
    else:
        print('Phone book is empty')           
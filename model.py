class Database:
    def __init__(self):
        self.phone_book = []
        self.path = '-phone-book/phone_book.txt'

    def get_phone_book(self):
        return self.phone_book

    def update_phone_book(self, contact: list):
        self.phone_book.append(contact)   

    def open_phone_book(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
            for line in data:
                self.phone_book.append(line.strip().split(';'))

    def save_phone_book(self):
        data = []

        for line in self.phone_book:
            data.append(';'.join(line))

        with open(self.path, 'w', encoding='UTF-8') as file:
            data = file.write('\n'.join(data))       

    def search_contact(self, search: str):
        search_results = []
        
        for line in self.phone_book:
            for field in line:
                if str(search) in field:
                    search_results.append(line)
                    break
        
        return search_results

    def remove_contact(self, name: str):
        data = []

        for line in self.phone_book:
            if name not in line[0]:
                data.append(line)
        
        self.phone_book = data          

    def update_contact(self, name: str, contact: list):
        data = []

        for line in self.phone_book:
            if name not in line[0]:
                data.append(line)    
        
        self.phone_book = data   
        self.phone_book.append(contact)        


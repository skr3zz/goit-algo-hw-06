from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
     def __init__(self, value):
        if not value:
            raise ValueError("Name can't be empty")
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError('Value error')


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        self.phones = [p for p in self.phones if str(p) != phone_number]

    
    def add_contact(args, contacts):
        name, phone = args
        contacts[name] = phone
        return 'Contact added.'
    
    def change_contact(args, contacts):
        if len(args) != 2:
            return "Invalid command format. Use 'change [name] [new_phone]'"
        name, phone = args
        if name not in contacts:
            return "Contact not found."
        contacts[name] = phone
        return "Contact updated successfully"
    
    def show_contact(args, contacts):
        if len(args) != 1:
            return "Invalid command format. Use 'show [name]'"
        name = args[0]
        if name not in contacts:
            return "Contact not found."
        return contacts[name]
    
    

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
    #
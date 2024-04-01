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
        self.phones = [p for p in self.phones if p.value != phone_number]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return "Phone number edited successfully"
        return "Phone number not found"

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def add_contact(self, name, phone):
        if name in self.data:
            self.data[name].add_phone(phone)
        else:
            record = Record(name)
            record.add_phone(phone)
            self.add_record(record)

    def change_contact(self, name, new_phone):
        if name in self.data:
            self.data[name].remove_phone(new_phone)
            self.data[name].add_phone(new_phone)
            return "Contact updated successfully"
        else:
            return "Contact not found."

    def show_contact(self, name):
        if name in self.data:
            return str(self.data[name])
        else:
            return "Contact not found."
from factories import FieldFactory, FieldType


class Record:
    def __init__(self, name):
        self.name = FieldFactory.create_field(FieldType.NAME, name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday):
        if self.birthday:
            raise ValueError("Birthday already exists")
        self.birthday = FieldFactory.create_field(FieldType.BIRTHDAY, birthday)

    def change_birthday(self, new_birthday):
        if not self.birthday:
            raise ValueError("No birthday exists to change")
        self.birthday = FieldFactory.create_field(FieldType.BIRTHDAY, new_birthday)

    def show_birthday(self):
        return self.birthday.value if self.birthday else None
    
    def add_phone(self, phone):

        phone = FieldFactory.create_field(FieldType.PHONE, phone)
        self.phones.append(phone)

    def find_phone(self, phone_number):
        return next(
            (phone for phone in self.phones if phone.value == phone_number), None
        )

    def edit_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        if phone:
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
        else:
            raise ValueError("Phone number not found")

    def remove_phone(self, phone_number):
        phone = self.find_phone(phone_number)
        if phone:
            self.phones.remove(phone)
        else:
            raise ValueError("Phone number not found")

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones}, birthday: {self.birthday.value if self.birthday else None}"

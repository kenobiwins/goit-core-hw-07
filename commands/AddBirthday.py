from .Command import Command


class AddBirthdayCommand(Command):

    def __init__(self, address_book, name, birthday=None):
        self.address_book = address_book
        self.name = name
        self.birthday = birthday

    def execute(self):
        record = self.address_book.find(self.name)
        record.add_birthday(self.birthday)


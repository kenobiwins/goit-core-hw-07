from .Command import Command


class FindRecordCommand(Command):
    def __init__(self, address_book, name):
        self.address_book = address_book
        self.name = name

    def execute(self):
        return self.address_book.find(self.name)

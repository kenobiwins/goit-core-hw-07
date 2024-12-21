from .Command import Command


class DeleteRecordCommand(Command):
    def __init__(self, address_book, name):
        self.address_book = address_book
        self.name = name

    def execute(self):
        self.address_book.delete(self.name)

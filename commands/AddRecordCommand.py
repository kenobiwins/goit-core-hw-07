from .Command import Command


class AddRecordCommand(Command):
    def __init__(self, address_book, record):
        self.address_book = address_book
        self.record = record

    def execute(self):
        self.address_book.add_record(self.record)

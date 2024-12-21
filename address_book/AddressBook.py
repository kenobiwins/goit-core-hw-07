from collections import UserDict

from memento import Memento


class AddressBook(UserDict):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(AddressBook, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __str__(self):
        return (
            "\n".join(str(record) for record in self.data.values())
            if self.data
            else "The address book is empty."
        )

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Contact not found")

    def save(self):
        return Memento(self.data)

    def restore(self, memento):
        self.data = memento.get_state()

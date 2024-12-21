from address_book import AddressBook
from commands import AddRecordCommand, DeleteRecordCommand, FindRecordCommand
from models import Record


def main():
    address_book = AddressBook()
    print(address_book)
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    add_command = AddRecordCommand(address_book, john_record)
    add_command.execute()

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")

    add_command = AddRecordCommand(address_book, jane_record)
    add_command.execute()

    print("\nCurrent Address Book:")
    print(address_book)

    find_command = FindRecordCommand(address_book, "John")
    found_record = find_command.execute()

    if found_record:
        print("\nFound Record:")
        print(found_record)

        print("\nEditing a phone number...")
        found_record.edit_phone("1234567890", "1112223333")
        print(found_record)

    delete_command = DeleteRecordCommand(address_book, "Jane")
    delete_command.execute()

    print("\nAddress Book after deletion:")
    print(address_book)

    print("\nSaving Address Book state...")
    saved_state = address_book.save()

    delete_command = DeleteRecordCommand(address_book, "John")
    delete_command.execute()

    print("\nAddress Book after deleting John:")
    print(address_book)

    print("\nRestoring Address Book state...")
    address_book.restore(saved_state)

    print("\nRestored Address Book:")
    print(address_book)


if __name__ == "__main__":
    main()

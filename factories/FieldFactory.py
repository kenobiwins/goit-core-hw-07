from models import Name, Phone

from .FieldType import FieldType


class FieldFactory:
    @staticmethod
    def create_field(field_type, value):
        match field_type:
            case FieldType.NAME:
                return Name(value)
            case FieldType.PHONE:
                return Phone(value)
            case _:
                raise ValueError("Invalid field type")

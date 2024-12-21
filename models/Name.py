from models.Field import Field
from validation.NameValidation import NameValidation


class Name(Field):
    def __init__(self, value):
        super().__init__(value, NameValidation())
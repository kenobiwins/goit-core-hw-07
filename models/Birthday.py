from models.Field import Field
from validation.BirthdayValidation import BirthdayValidation


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value, BirthdayValidation())
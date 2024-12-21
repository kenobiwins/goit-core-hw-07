from models.Field import Field
from validation.PhoneValidation import PhoneValidation


class Phone(Field):
    def __init__(self, value):
        super().__init__(value, PhoneValidation())

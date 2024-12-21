from validation.ValidationStrategy import ValidationStrategy


class Field:
    def __init__(self, value, validator: ValidationStrategy):
        self.value = validator.validate(value)

    def __str__(self):
        return str(self.value)

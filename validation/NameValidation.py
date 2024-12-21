from .ValidationStrategy import ValidationStrategy


class NameValidation(ValidationStrategy):
    def validate(self, value):
        if not value.strip():
            raise ValueError("Name couldn't be empty")
        return value.strip()

import re
from datetime import datetime

from utils import BirthdayHelper

from .ValidationStrategy import ValidationStrategy


class BirthdayValidation(ValidationStrategy):
    def validate(self, value: str) -> str:
        regex = r"^[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}$"
        if not value.strip():
            raise ValueError("Birthday couldn't be empty")

        if not re.match(regex, value):
            raise ValueError("Invalid birthday format")

        try:
            parsed_date = datetime.strptime(value, BirthdayHelper.DATE_FORMAT)

            return value if parsed_date.strftime(BirthdayHelper.DATE_FORMAT) == value else False

        except ValueError:
            return False

from datetime import timedelta, datetime, date


class BirthdayHelper:
    DATE_FORMAT = "%d.%m.%Y"

    @staticmethod
    def string_to_date(date_string, format=DATE_FORMAT):
        return datetime.strptime(date_string, format).date()

    @staticmethod
    def date_to_string(date, format=DATE_FORMAT):
        return date.strftime(format)

    def prepare_user_list(self, user_data):
        prepared_list = []

        for user in user_data:

            user_birthday = user.get("birthday", None)
            if not user_birthday:
                continue
            prepared_list.append(
                {
                    "name": user.get("name"),
                    "birthday": self.string_to_date(user_birthday),
                }
            )
        return prepared_list

    @staticmethod
    def find_next_weekday(start_date, weekday):
        days_ahead = weekday - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + timedelta(days=days_ahead)

    def adjust_for_weekend(self, birthday):
        if birthday.weekday() >= 5:
            return self.find_next_weekday(birthday, 0)
        return birthday

    def get_upcoming_birthdays(self, users, days=7):
        upcoming_birthdays = []
        today = date.today()

        prepared_users = self.prepare_user_list(users)

        for user in prepared_users:
            birthday = user.get("birthday")
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year=today.year + 1)

            if 0 <= (birthday_this_year - today).days <= days:
                adjusted_birthday = self.adjust_for_weekend(birthday_this_year)
                upcoming_birthdays.append(
                    {
                        "name": user.get("name"),
                        "congratulation_date": self.date_to_string(adjusted_birthday),
                    }
                )

        return upcoming_birthdays

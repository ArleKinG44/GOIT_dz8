from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):

    today = date.today()
    next_week = today + timedelta(days=7)

    birthdays_per_week = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': []
    }

    if len(users) == 0:
        return {}

    else:
        for user in users:
            birthday_this_year = date(today.year, user['birthday'].month, user['birthday'].day)
            birthday_next_year = date(today.year + 1, user['birthday'].month, user['birthday'].day)

            if birthday_this_year >= today and birthday_this_year <= next_week:
                next_birthday = birthday_this_year
            elif birthday_next_year >= today and birthday_next_year <= next_week:
                next_birthday = birthday_next_year
            else:
                continue

            day_of_week = next_birthday.strftime('%A')

            if day_of_week == 'Saturday' or day_of_week == 'Sunday':
                day_of_week = 'Monday'

            birthdays_per_week[day_of_week].append(user['name'])

        return birthdays_per_week


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

from datetime import date
from collections import defaultdict


def get_birthdays_per_week(users):

    today = date.today()
    weekday = today.weekday()
    birthdays = defaultdict(list)
    for user in users:
        delta = (user['birthday'].replace(year=today.year) - today).days
        if delta < 0:
            delta += 365
        if delta < 7:
            birthday_weekday = (weekday + delta) % 7
            day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                   'Friday', 'Monday', 'Monday'][birthday_weekday]
            birthdays[day].append(user['name'])

    return birthdays


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": date(1976, 1, 1)},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

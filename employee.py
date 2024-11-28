from datetime import datetime

class Employee:
    def __init__(self, full_name, birth_date, gender):
        self.full_name = full_name
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
        self.gender = gender

    @staticmethod
    def calculate_age(birth_date):
        today = datetime.today().date()
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age

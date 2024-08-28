

class Date():
    def __init__(self, day=0, month=0, year=0) -> None:
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_string):
        day, month, year = map(int, date_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    def __repr__(self) -> str:
        return f'{self.day} {self.month} {self.year}'


date2 = Date.from_string('12-34-1007')
print(date2)


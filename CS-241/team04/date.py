import calendar

class Date:
    def __init__(self):
        self.day = 1
        self.month = 1
        self.year = 2000

    def prompt(self):
        valid_month = False
        valid_year = False
        self.day = int(input('Day: '))
        while not valid_month:
            self.month = int(input('Month: '))
            if self.month in range(1,13):
                valid_month = True
        while not valid_year:
            self.year  = int(input('Year: '))
            if self.year >= 2000:
                valid_year = True

    def display(self):
        print(f'{self.month:02d}/{self.day:02d}/{self.year}')
        long_month = calendar.month_name[self.month]
        print(f'{long_month} {self.day}, {self.year}')
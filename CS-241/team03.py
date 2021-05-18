class Rational:
    def __init__(self):
        self.numerator = 0
        self.denominator = 1
        self.second_numerator = 0
        self.second_denominator = 1

    def display(self):
        self.whole_number = 0
        if self.numerator >= self.denominator:
            self.whole_number = self.numerator // self.denominator
            new_numerator = self.numerator - (self.whole_number * self.denominator)
            if new_numerator != 0:
                self.numerator = new_numerator
                print(f'{self.whole_number} {self.numerator}/{self.denominator}')
            else:
                print(f'{self.whole_number}')
        else:
            print(f"{self.numerator}/{self.denominator}")

    def prompt(self):
        self.numerator = int(input("Enter the numerator: "))
        self.denominator = int(input("Enter the denominator: "))
        self.second_numerator = int(input("Enter a second numerator: "))
        self.second_denominator = int(input("Enter a second denominator: "))

    def reduce(self):
        factor = self.numerator + 1
        numerator_modulo = 1
        denominator_modulo = 1
        while not (numerator_modulo == 0 and denominator_modulo == 0):
            if factor == 1:
                break
            factor -= 1
            numerator_modulo = self.numerator % factor
            denominator_modulo = self.denominator % factor
        self.numerator = self.numerator / factor
        self.denominator = self.denominator / factor
        
        if self.whole_number > 0:
            return f'{self.whole_number} {round(self.numerator)}/{round(self.denominator)}'
        else:
            return f'{round(self.numerator)}/{round(self.denominator)}'

    def multiply_by(self):
        self.numerator = self.numerator * self.second_numerator
        self.denominator = self.denominator * self.second_denominator
        
    def display_decimal(self):
        return self.whole_number + (self.numerator/self.denominator)


def main():
    fraction = Rational()

    fraction.display()

    fraction.prompt()

    fraction.multiply_by()

    fraction.display()

    print(fraction.reduce())

    print(fraction.display_decimal())

if __name__ == "__main__":
    main()
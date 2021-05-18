class complexNumber:

    def __init__(self):
        self.real_number_1 = 0
        self.imaginary_number_1 = 0
        self.real_number_2 = 0
        self.imaginary_number_2 = 0

    def prompt(self):
        self.real_number_1 = int(input('\nPlease enter the real part: '))
        self.imaginary_number_1 = int(input('Please enter the imaginary part: '))
        self.real_number_2 = int(input('\nPlease enter the real part: '))
        self.imaginary_number_2 = int(input('Please enter the imaginary part: '))


    def display(self):
        print('The values are:')
        print(f'{self.real_number_1} + {self.imaginary_number_1}i')
        print(f'{self.real_number_2} + {self.imaginary_number_2}i')

def main():
    compNumb = complexNumber()
    compNumb.display()
    compNumb.prompt()
    print()
    compNumb.display()

if __name__ == '__main__':
    main()
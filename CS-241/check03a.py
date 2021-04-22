class Student:
    '''Class to create a new student'''

    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.id_number = 0
    
    def prompts(self):
        self.first_name = input('Please enter your first name: ')
        self.last_name = input('Please enter your last name: ')
        self.id_number = input('Please enter your id number: ')

    def output(self):
        print(f'{self.id_number} - {self.first_name} {self.last_name}')

def main():
    student = Student()
    student.prompts()

    print('\nYour information:')
    student.output()


if __name__ == '__main__':
    main()
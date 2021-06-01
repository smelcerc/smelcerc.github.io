from collections import deque

class Student:

    def __init__(self):
        self.name = ''
        self.course = ''

    def prompt(self):
        self.name = input('Enter name: ')
        self.course = input('Enter course: ')
        return [self.name, self.course]

    def display(self):
        pass

class HelpSystem:

    def __init__(self):
        self.waiting_list = deque('')

    def is_student_waiting(self):
        if len(list(self.waiting_list)) > 0:
            return True
        else:
            return False

    def add_to_waiting_list(self, student):
        self.waiting_list.append(student)

    def help_next_student(self):
        if self.is_student_waiting():
            student = self.waiting_list.popleft()
            print(f'Now helping {student[0]} with {student[1]}')
        else:
            print('No one to help')

def main():

    quit_program = False

    help_sys = HelpSystem()

    while not quit_program:
        student = Student()
        
        print('Options:')
        print('1. Add a new student')
        print('2. Help next student')
        print('3. Quit')
        selection = int(input('Enter selection: '))

        if selection == 1:
            help_sys.add_to_waiting_list(student.prompt())
        
        elif selection == 2:
            help_sys.help_next_student()

        elif selection == 3:
            quit_program = True
        else:
            pass

if __name__ == '__main__':
    main()
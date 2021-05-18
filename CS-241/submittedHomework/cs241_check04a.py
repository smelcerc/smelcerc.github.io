'''
File: check04a.py
Author: Christopher Smelcer
W04 Prepare: Checkpoint A
'''

class Person:

    def __init__(self):
        self.name = 'anonymous'
        self.birth_year = 'unknown'

    def prompt(self):
        self.name = input('Name: ')
        self.birth_year = input('Year: ')

    def display(self):
        return f'{self.name} (b. {self.birth_year})'

class Book:

    def __init__(self):
        self.title = 'untitled'
        self.author = Person()
        self.publisher = 'unpublished'

    def prompt(self):
        print()
        print('Please enter the following:')
        self.author.prompt()
        self.title = input('Title: ')
        self.publisher = input('Publisher: ')
        print()

    def display(self):
        return f'{self.title}\nPublisher:\n{self.publisher}\nAuthor:\n{self.author.display()}'

def main():
    book = Book()
    
    print(book.display())

    book.prompt()

    print(book.display())

if __name__ == '__main__':
    main()
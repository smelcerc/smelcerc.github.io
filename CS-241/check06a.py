'''
File: check06a.py
Author: Christopher Smelcer
'''

class Book:
    def __init__(self):
        self.title = ''
        self.author = ''
        self.publication_year = 0

    def prompt_book_info(self):
        self.title = input('Title: ')
        self.author = input('Author: ')
        self.publication_year = int(input('Publication Year: '))

    def display_book_info(self):
        print(f'\n{self.title} ({self.publication_year}) by {self.author}')

class TextBook(Book):
    def __init__(self):
        super().__init__()
        self.subject = ''
    
    def prompt_book_info(self):
        return super().prompt_book_info()
    
    def prompt_subject(self):
        self.subject = input('Subject: ')
    
    def display_book_info(self):
        return super().display_book_info()
    
    def display_subject(self):
        print(f'Subject: {self.subject}')

class PictureBook(Book):
    def __init__(self):
        super().__init__()
        self.illustrator = ''

    def prompt_book_info(self):
        return super().prompt_book_info()
    
    def prompt_illustrator(self):
        self.illustrator = input('Illustrator: ')
    
    def display_book_info(self):
        return super().display_book_info()

    def display_illustrator(self):
        print(f'Illustrated by {self.illustrator}')

def main():
    book = Book()
    book.prompt_book_info()
    book.display_book_info()
    
    print()

    text_book = TextBook()
    text_book.prompt_book_info()
    text_book.prompt_subject()
    text_book.display_book_info()
    text_book.display_subject()

    print()

    picture_book = PictureBook()
    picture_book.prompt_book_info()
    picture_book.prompt_illustrator()
    picture_book.display_book_info()
    picture_book.display_illustrator()


if __name__ == '__main__':
    main()
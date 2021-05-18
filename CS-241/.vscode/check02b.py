def main():

    file_location = input('Enter file: ')

    line_count = 0
    word_count = 0

    with open(file_location, 'r') as data_file:
        content = data_file.read()

        row_split = content.split('\n')
        for i in row_split:
            line_count += 1

        word_split = content.split(' ')
        for i in word_split:
            word_count += 1

    print(f'The file contains {line_count} lines and {word_count + line_count - 1} words.')

if __name__ == '__main__':
    main()
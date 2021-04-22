def main():

    file_location = input('Enter file: ')

    line_count = 0
    word_count = 0

    data_file = open(file_location, 'rt')
    for line in data_file:
        if line != '\n':
            words = line.split(' ')
            word_count += len(words)
            line_count += 1

    print(f'The file contains {line_count} lines and {word_count} words.')

if __name__ == '__main__':
    main()

# /Users/smelcerc/Desktop/TEST_With_Will/test_test5.txt
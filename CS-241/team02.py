def prompt_filename():
    file_name = input('What is your file? ')
    return file_name

def parse_file(file_name):
    count = 0
    with open(file_name, 'r') as text_file:
        for line in text_file:
            words = line.split()
            for word in words:
                if word == 'pride' or word == 'Pride':
                    count += 1
    return count

def main():
    file_name = prompt_filename()
    pride_count = parse_file(file_name)

    print(pride_count)

if __name__ == '__main__':
    main()

# /Users/smelcerc/Desktop/test.txt
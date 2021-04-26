def prompt_filename():
    file_name = input('What is your file? ')
    return file_name

def prompt_search_term():
    search_term = input('What word/term would you like to count? ')
    return search_term.lower()

def parse_file(file_name, search_term):
    count = 0
    with open(file_name, 'r') as text_file:
        for line in text_file:
            words = line.split()
            for word in words:
                word_exist = word.lower().find(search_term)
                if word_exist != -1:
                    count += 1
    return count

def main():
    file_name = prompt_filename()
    search_term = prompt_search_term()
    word_count = parse_file(file_name, search_term)

    print(word_count)

if __name__ == '__main__':
    main()

# /Users/smelcerc/Desktop/test.txt
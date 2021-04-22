def main():
    
    number_list = []

    def prompt_number():
        positive = False
        while positive == False:
            number = int(input('Enter a positive number: '))
            if number < 0:
                print('Invalid entry. The number must be positive.')
            else:
                print()
                positive = True
        return number

    def compute_sum():
        total = 0
        for number in number_list:
            total += number
        return total

    for x in range(3):
        number_list.append(prompt_number())

    sum = compute_sum()

    print(f'The sum is: {sum}')

if __name__ == '__main__':
    main()
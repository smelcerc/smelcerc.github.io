percentage = int(input('What was your grade percentage? '))

if (len(str(percentage)) > 1) and (percentage >= 60):
    second_digit = int(str(percentage)[1])
    if second_digit >= 7 and percentage < 90:
        symbol = '+'
    elif second_digit < 3:
        symbol = '-'
    else:
        symbol = ''

if percentage >= 90:
    print('A' + symbol)
elif percentage >= 80:
    print('B' + symbol)
elif percentage >= 70:
    print('C' + symbol)
elif percentage >= 60:
    print('D' + symbol)
elif percentage < 60:
    print('F')

if percentage >= 70:
    print('Congrats you passed the class')
else:
    print('Better luck next time')
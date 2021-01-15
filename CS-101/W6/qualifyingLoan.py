print('Answer the following questions on a scale of 1 to 10:\n')

loan_size = int(input('How large is the loan? '))
credit_history = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
down_payment = int(input('How large is your down payment? '))

offer_loan = False

if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        offer_loan = True
    elif (credit_history >= 7 or income >= 7) and down_payment >=5:
        offer_loan = True
    else:
        offer_loan = False

elif loan_size < 5:
    if credit_history < 4:
        offer_loan = False
    elif income >= 7 or down_payment >= 7:
        offer_loan = True
    elif income >= 4 and down_payment >= 4:
        offer_loan = True
    else:
        offer_loan = False

else:
    offer_loan = False

if offer_loan == True:
    print('Congrats you can get a loan')
else: 
    print('Sorry but we cant offer you a loan')
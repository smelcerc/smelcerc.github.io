rider_age = int(input('What is the age of the first rider? '))
rider_height = int(input('What is the height of the first rider? '))
rider_gold_passport = input('Does the first rider have a golden passport (yes/no)? ')
second_rider = input('Is there a second rider (yes/no)? ')

second_rider_height = 0
second_rider_age = 0
second_rider_gold_passport = 'no'

if second_rider.lower() == 'yes':
    second_rider_age = int(input('What is the age of the second rider? '))
    second_rider_height = int(input('What is the height of the second rider? ')) 
    second_rider_gold_passport = input('Does the second rider have a golden passport (yes/no)? ')

can_ride = False

if rider_gold_passport.lower() == 'yes' and rider_age <= 17 and rider_age >= 12:
    rider_age = 18

if second_rider_gold_passport.lower() == 'yes' and second_rider_age <= 17 and second_rider_age >= 12:
    second_rider_age = 18

if rider_height < 36 or second_rider_height < 36:
    can_ride = False

if second_rider.lower() == 'no' and rider_age >= 18 and rider_height >= 62:
    can_ride = True

if second_rider.lower() == 'yes':
    if (rider_age >= 18 or second_rider_age >= 18) and (rider_height >= 36 and second_rider_age >= 36):
        can_ride = True

    elif (rider_age >= 12 and second_rider_age >= 12) and (rider_height >= 52 and second_rider_height >= 52):
        can_ride = True

    elif (rider_age >= 16 and second_rider_age >= 14) or (rider_age >= 14 and second_rider_age >= 16):
        can_ride = True

    else:
        can_ride = False

if can_ride == True:
    print('Welcome to the ride. Please be safe and have fun!')
else:
    print('Sorry, you may not ride.')
import random
while True:
    countinue_option = input('Do You Want To Countinue rolling Dice? (y/n)')
    die = random.randint(1, 6)
    print(die)
    if countinue_option == 'n':
        break
    

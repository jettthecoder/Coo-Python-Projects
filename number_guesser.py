import random
num = random.randint(1, 100)
while True:
    user = int(input('Enter A Number: '))
    if user == num:
        print('Woohoo You Won!')
        play_again = input('Would you like to play again? (yes/no)' )
        if play_again.lower() == 'no':
            break
    elif user < num:
        print('It\'s Higher!')
    elif user > num:
        print('It\'s Lower!')
        
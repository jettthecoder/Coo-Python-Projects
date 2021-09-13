import random
while True:
    print('Welcome To Rock Paper Scissors')
    user_choice = input('Rock, Paper or Scissors ')
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
   
    if user_choice.lower() == computer_choice:
         print(f'The computer picked {computer_choice} You picked {user_choice}')
         print('It\'s a Tie')
    elif user_choice.lower() == 'rock' and computer_choice == 'scissors':
         print(f'The computer picked {computer_choice} You picked {user_choice}')
         print('You Win!!')
    elif user_choice.lower() == 'paper' and computer_choice == 'rock':
         print(f'The computer picked {computer_choice} You picked {user_choice}')
         print('You Win!!')
    elif user_choice.lower() == 'scissors' and computer_choice == 'paper':
         print(f'The computer picked {computer_choice} You picked {user_choice}')
         print('You Win!!')
    elif user_choice.lower() == 'scissors' and computer_choice == 'rock':
         print(f'The computer picked {computer_choice} You picked {user_choice}')
         print('You Lost :(')
    elif user_choice.lower() == 'rock' and computer_choice == 'paper':
         print(f'The computer picked {computer_choice} You picked {user_choice}')
         print('You Lost :(')
    elif user_choice.lower() == 'rock' and computer_choice == 'paper':
        print(f'The computer picked {computer_choice} You picked {user_choice}')
        print('You Lost :(')
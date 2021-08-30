from math import degrees
import random

no_of_rounds = 5

def result(user_choice, comp_choice):
    if user_choice == comp_choice:
        return 'draw'
    else:
        if user_choice == 1 and comp_choice == 2:return 'comp'
        elif user_choice == 1 and comp_choice == 3: return 'user'
        elif user_choice == 2 and comp_choice == 1: return 'user'
        elif user_choice == 2 and comp_choice == 3: return 'comp'
        elif user_choice == 3 and comp_choice == 1: return 'comp'
        elif user_choice == 3 and comp_choice == 2: return 'user'
    
def options(choice):
    stone = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

    paper = '''
    _______
---'   ____)_______
          _________)
          __________)
         __________)
---._____________)
'''

    scissors = '''
    _______
---'   ____)_______
          _________)
       _____________)
      (____)
---.__(___)
'''

    options = {1:stone, 2:paper, 3:scissors}
    o = {1:'Stone', 2:'Paper', 3:'Scissors'}
    return o[choice],options[choice]

def computer_choice():
    return random.randrange(1,3)

n = 1
flag = 'y'

while True:

    if flag.lower() != 'y':
        print('Thanks for playing, have a good day')
        exit()
    u,c = 0,0
    while n < no_of_rounds:
        try:
            print("Round Number :", n)
            choice = int(input('''
Please enter you choice:
1. Press 1 for "Stone"
2. Press 2 for "Paper"
3. Press 3 for "Scissors"
'''))
            n += 1
        except ValueError as e:
            print('Please enter a correct value')
        descr, user_choice = options(choice)
        comp_option = computer_choice()
        descr1, comp_choice = options(comp_option)

        print('Your Choice:', descr)
        print(user_choice)
        print('Computer\'s Choice:', descr1)
        print(comp_choice)

        res = result(choice, comp_option)
        if res == 'user':
            print('Congo, You won the round.')
            u += 1
        elif res == 'comp':
            print('Computer won this round.')
            c += 1
        elif res == 'draw':
            print('This round is draw')
            n -= 1

        print(f'Scores: User at {u} wins and computer at {c} wins.')

    if u < c: print('Computer is the winner.')
    elif u > c: print('User is the winner.')
    elif u == c: print('This game led to draw.')
    flag = input('Enter "y" to play again.')

        


import random

n = random.randint(0,100)
flag = 'y'

while True:
    if flag.lower()=='y':
        print('\nThis is a game to guess the random number selected by the program between 1 and 100.\n\nEach time you guess a number program will provide a hint if you number is greater or smaller than the hidden number \ntill you loose or guess the correct number.\n\nGood Luck!!!\n\n')
        dif = input('Please select the difficulty level: \n\n1. Press "E" for Easy(You will get 14 chances to guess). \n2. Press "M" for Medium(You will get 10 chances to guess).\n3. Press "H" for easy(You will get 6 chances to guess).\n')
        if dif.lower() == 'e':cha = 14
        elif dif.lower() == 'm': cha = 10
        elif dif.lower() == 'h': cha = 6
        else:
            print('You entered an invalid value, please try reselecting.')
            continue
        win_flag = 'N'
        for i in range(cha):
            if i == cha-1:print('This is you last chance')
            else:print(f'You have {cha-i} chances left.')
            no_cha = i
            num=int(input('Guess a number: '))
            if num==n:
                print('Congrats, you guessed the correct number.\n\n')
                win_flag = 'Y'
                print('Press "Y" to play again')
                break
            elif num>n:
                print('Your number is greater than the hidden number. Try guessing a smaller number')
            elif num<n:
                print('Your number is smaller than the hidden number. Try guessing a bigger number')
        if win_flag == 'N':print(f'No chances left. Game over \nThe hidden number was {n}.\nPress "Y" to play again')
        flag = input()
    else: break
        

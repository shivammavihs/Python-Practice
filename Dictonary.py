flag = 'y'
while True:
    if flag == 'Y' or flag == 'y':
        print(f'Do you want to add or search a word oin dictonary. \nPress "a" to add or press "s" to search: ')
        inc = input()
        word = input('Enter your word: ')
        foundflag='n'
        if inc.upper() == 'S':
            dict = open('Dictonary.txt','r')
            for line in dict:
                wd,meaning=line.split(':')
                meaning=meaning.split(';')
                if word.lower()==wd:
                    foundflag='y'
                    if len(meaning)==1:print(f'Word: {word}\nMeaning: {meaning[0]}\b')
                    else:
                        i=1
                        print(f'Word: {word}')
                        for mean in meaning:
                            print(f'Meaning {i}: {mean}')
                            i+=1
            if foundflag=='n':print('Word Not found')
            dict.close()
        elif inc.upper() == 'A':
            dict = open('Dictonary.txt','r')
            meaning = input('Enter or paste the meaning: ')
            foundflag = 'n'
            for line in dict:
                wd=line.split(':')
                if word.lower()==wd[0]:
                    foundflag = 'y'
                    print(f'The word already exists in the dictonary. Do you want to add or update the meaning.\n1. Press "A" to add another meaning.\n2. Press "U" to update the meaning')
                    choice = input()
                    if choice.lower() == 'a':
                        dict1 = open('Dictonary.txt','r')
                        lines = dict1.readlines()
                        file = open('Dictonary.txt','w')
                        for ln in lines:
                            if ln.strip("\n") != line.strip("\n"):
                                file.write(ln)
                        file.close()
                        dict2 = open('Dictonary.txt','a')
                        dict2.write(f'{line};{meaning}')
                        print('Your meaning is added to the word inside the dictonary.')
                        dict2.close()
                        dict1.close()
                    elif choice.lower()== 'u':
                        dict1 = open('Dictonary.txt','r')
                        lines = dict1.readlines()
                        file = open('Dictonary.txt','w')
                        for ln in lines:
                            if ln.strip("\n") != line.strip("\n"):
                                file.write(ln)
                        file.close()
                        dict2 = open('Dictonary.txt','a')
                        dict2.write(f'{word.lower()}:{meaning.lower()}')
                        print('Your word updated inside the dictonary.')
                        dict2.close()
                        dict1.close()
            if foundflag == 'n':
                dict = open('Dictonary.txt','a')
                dict.write(f'\n{word.lower()}:{meaning.lower()}')
                dict.close()
                print('Your word inserted into the dictonary.')
                break
            dict.close()        

        flag = input("Press 'y' to search again: ")
    else:break
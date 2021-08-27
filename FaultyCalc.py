a = int(input('Enter first number: '))
o = input('Enter the operator: ')
if o not in ['+','-','*','x','X','/']:
    print('This Operation in not  supported or please enter a valid operator.')
    exit()
b = int(input('Enter second number: '))

if a==45 and o.lower() in ['*','x'] and b==3:
    print(555)
elif a==56 and o.lower() == '+' and b==9:
    print(77)
elif a==56 and o.lower() == '/' and b==6:
    print(4)
else:
    if o == '+':print(a+b)
    elif o == '-':print(a-b)
    elif o.lower() in['*','x']:print(a*b)
    elif o == '/':print(a/b)


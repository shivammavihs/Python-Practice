n = int(input('Enter the number of row to be printed: '))
bol = int(input('Enter "1" for True and "0" for False: '))

if bol == 1:
    start, end, step = 0,n,1
elif bol == 0:
    start, end, step = n,0,-1
else:print('invalid selection')


for i in range(start, end, step):
    j=0
    while j<=i if bol == 1 else j<i:
        print('* ',end='')
        j+=1
    print()

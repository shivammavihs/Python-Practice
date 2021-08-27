from datetime import datetime


def file_name(client, log_type):
    if client==1:
        filename = 'Harry'
    elif client==2:
        filename = 'Rohan'
    elif client==3:
        filename = 'Hammad'
    
    if log_type == 1:
        filename=filename+'_Exercise'
    elif log_type == 2:
        filename=filename+'_Food'
    return filename

def log_stats(filename, data):
    file = open(filename,'a')
    file.write('\n'+date_time()+'   '+data.lower())
    print('Data logged successfully into '+filename)
    file.close()

def read_data(filename,n):
    file = open(filename,'r')
    lines = file.readlines()
    last_lines = lines[-n:]
    if len(lines) == 0:
        print('No data found.')
    else:
        print('Below are the requested logs: ')
        for line in last_lines:
            print(line.strip('\n'))

def date_time():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")
    
choice = int(input('1. Press 1 to log a data\n2. Press 2 to view a data\n'))

client = int(input('Please enter the clietn name.\n1. Press 1 for Harry.\n2. Press 2 for Rohan.\n3. Press 3 for hammad.\n'))
log_type = int(input('Please enter the attribute you want to log.\n1. Press 1 for exercise.\n2. Press 2 from food.\n'))

if choice == 1:
    data = input('Enter the data2 to be logged: ')
    log_stats(file_name(client,log_type), data)
elif choice == 2:
    n = int(input('Enter the latest number of records required: '))
    read_data(file_name(client,log_type), n)

import csv

def takename_passwd():
    with open('npassformysql.csv','w',newline='') as file:
        wr = csv.writer(file)
        name = input('Enter the user name of your mysql server: ')
        passwd = input('Enter the password of your mysql server: ')
        head = ['Name', 'Password']
        data = []
        data.append(name)
        data.append(passwd)
        wr.writerow(head)
        wr.writerow(data)


# takename_passwd()

with open('npassformysql.csv','r') as file:
    rd = csv.reader(file)
    data = [x for x in rd]
    name = data[1][0]
    passwd = data[1][1]

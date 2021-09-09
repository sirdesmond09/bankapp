import ast
import random

customers = open('customers.txt', 'a')
staff_file = open('staff.txt', 'a')


def new_staff(fullname, email , username, password):
    new_staff = {}
    new_staff['Fullname'] = fullname
    new_staff['Email']    = email
    new_staff['username'] = username
    new_staff['password'] = password

    return new_staff

def create_account(name, email , acc_type, amount):
    new_account = {}
    new_account['Account name']    = name
    new_account['Account email']   = email
    new_account['Account type']    = acc_type
    new_account['Opening Balance'] = f'#{amount}'
    new_account['account_number']  = random.randint(1000000000, 9999999999)

    return new_account

# new_staff = new_staff('Nnebue Desmond', 'email@email.comn', 'hey', '23345')
# staff_file.write(f'{new_staff}\n')
# staff_file.close()

print('welcome')
choice = input('Please press 1 to login or 2 to close the app:\n>')

if choice == '1':
    username = input('Username: ').lower()
    password = input('Password: ').lower()
    with open('staff.txt') as file_object: 
        lines = file_object.readlines() 
    data = []
    for line in lines:
        dictionary = ast.literal_eval(line.strip('\n'))
        data.append(dictionary)

    for d in data:
        if d['username'] == username and d['password'] == password:
            print(f'Welcome {username.capitalize()}.\n\n')
            while True:
                choice = input('Please press 1 to create a new account or 2 to check account details and 3 to logout\n>_ ')
                if choice == '1':
                    name = input('Enter account name \n>_ ')
                    email = input('Enter account email \n>_ ')
                    acc_type = input('Enter account type. Savings or Current \n>_ ')
                    amount = input('Enter opening balance \n>_ ')

                    account = create_account(name, email , acc_type, amount)

                    customers.write(f'{new_staff}\n')
                    customers.close()
                    
                    print(f"The account number for {name} is {account['account_number']}")
                    print(f"Please save account number!")
                    
                elif choice == '2':
                    account_number = int(input('Please enter account number\n>_ '))
                    with open('customers.txt') as file_object: 
                        lines = file_object.readlines() 
                    
                    data = []
                    
                    for line in lines:
                        dictionary = ast.literal_eval(line.strip('\n'))
                        data.append(dictionary)

                    for d in data:
                        if d['account_number'] == account_number:
                            print(f"Account name is {d['Account name']}")
                            print(f"Account email is {d['Account email']}")                            
                            print(f"Account number is {d['account_number']}")
                            print(f"Account type is {d['Account type']}")
                            print(f"Current balance is {d['Opening Balance']}")
                        else:
                            print('Account Does not exist!')

                            
                elif choice == '3':
                    break

elif choice == '2':
    print('We hope to see you next time :)')
    exit()




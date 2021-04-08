from datetime import datetime
import random

registerBonus = 5000 # Just to perform withdrawal and deposit
time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

database = {}

def init():
    print("Welcome to Kolo Bank")
    haveAccount = int(input("Do you have an Account with us? Select 1 (yes) OR 2 (No) \n"))
    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print("You have selected Invalid option\n")
        init()

def login():
    print("**Login Your Account**")
    userAccountNumber = int(input("Enter Your Account Number\n"))
    password = input("Enter Your Password\n")
    for accountNumber, userDetails in database.items():
        if(accountNumber == userAccountNumber):
            if(userDetails[3] == password):
                bankOperation(userDetails)

    print("Invalid Account Number or Password, Try Again\n")

    login()

def register():
    print("**Register with Us** \n")
    first_name = input("Enter your first name..\n")
    last_name = input("Enter your last name..\n")
    email = input("Enter your email address..\n")
    password = input("Create password..\n")
    accountNumber = generatedAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]
    print("Your Account Has Been Created")
    print(f"Your Account Number is {accountNumber} keep it safe")
    print(f"You have received a registration bonus of {registerBonus}.\n")

    login()

def bankOperation(user):
    print(f"Welcome {user[0]}, {user[1]}")
    print(f"Your login time is {time}")
    optionSelected = int(input("What do you want to do? (1) Deposit (2) Withdrawal (3) Complaint (4) Logout (5) Exit\n"))
    if(optionSelected == 1):
        deposit()
    elif(optionSelected == 2):
        withdrawal()
    elif(optionSelected == 3):
        complaint()
    elif(optionSelected == 4):
        logout()
    elif(optionSelected == 5):
        exit()
    else:
        print("Invilid option selected, please try again")
        bankOperation(user)
        
def deposit():
    deposit = int(input("How much would you like to deposit?\n"))
    currentBalance = deposit + registerBonus
    print(f"You successfully deposit {deposit}")
    print(f"Your current balance is {currentBalance}, Thank you for banking with us.\n")
    
    otherOption = int(input("Select (1) To Perform Another Option (2) To logout\n"))
    if(otherOption == 1):
        anotherPerformance()
    elif(otherOption == 2):
        print("You have succefully Logout\n")
        logout()

def withdrawal():
    withdrawal = int(input("How much would you like to withdraw?\n"))
    if(withdrawal <= registerBonus):
        currentBalance = registerBonus - withdrawal
        print("Take your cash")
        print(f"Your current balance is {currentBalance}, Thank you for banking with us.\n")
    else:
        print("Your balance is not sufficient")
        
    otherOption = int(input("Select (1) To Perform Another Option (2) To logout\n"))
    if(otherOption == 1):
        anotherPerformance()
    elif(otherOption == 2):
        print("You have succefully Logout\n")
        logout()
        
def complaint():
    input("What issue will you like to report?\n")
    print("Thank you for contacting us\n")
    
    otherOption = int(input("Select (1) To Perform Another Option (2) To logout\n"))
    if(otherOption == 1):
        anotherPerformance()
    elif(otherOption == 2):
        print("You have succefully Logout\n")
        logout()
    else:
        print("Invalid selection, select the correct option")
        complaint()
        
def anotherPerformance():
    optionSelected = int(input("What do you want to do? (1) Deposit (2) Withdrawal (3) Complaint (4) Logout (5) Exit\n"))
    if(optionSelected == 1):
        deposit()
    elif(optionSelected == 2):
        withdrawal()
    elif(optionSelected == 3):
        complaint()
    elif(optionSelected == 4):
        logout()
    elif(optionSelected == 5):
        exit()
    else:
        print("Invilid option selected, please try again")
        
        
def generatedAccountNumber():
    return random.randrange(1111111111,9999999999)

def logout():
    login()

init()

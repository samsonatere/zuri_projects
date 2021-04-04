from datetime import datetime

validName = ["atere", "samson", "dayo"]
validPassword = ["atere123", "samson123", "dayo123"]
balance = [10000, 7000, 5000]
time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

name = input("What is your account name? \n")
if(name in validName):
    password = input("Enter your password: \n")
    userid = validName.index(name)
    if(password == validPassword[userid]):
        print(f"Welcome {name}")
        print(f"Your login time is {time}")
        print("These are the avaliable options:")
        print("1. Withdrawal")
        print("2. Deposit")
        print("3. Complaint")
        optionSelected = int(input("Please select your option:\n"))

        balanceId = validName.index(name)

        if(optionSelected == 1):
            withdrawal = int(input("How much would you like to withdraw?\n"))
            if(withdrawal <= balance[balanceId]):
                currentBalance = balance[balanceId] - withdrawal
                print("Take your cash")
                print(f"Your current balance is {currentBalance}")
            else:
                print("Your balance is not sufficient")
        elif(optionSelected == 2):
            deposit = int(input("How much would you like to deposit?\n"))
            currentBalance = deposit + balance[balanceId]
            print(f"You successfully deposit {deposit}")
            print(f"Your current balance is {currentBalance}")
        elif(optionSelected == 3):
            input("What issue will you like to report?\n")
            print("Thank you for contacting us")
        else:
            print("Invilid option selected, please try again")

    else:
        print("Password not correct, please try again")

else:
    print("Your account not found, enter a valid name")

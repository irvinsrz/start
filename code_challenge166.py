balance = 0


def create_account(name, initial_deposit = 0):
    account_name = name
    global balance 
    balance = initial_deposit
    print(f"ACCOUNT CREATED for \n{account_name} with initial deposit of {balance} pesos")
    

def check_balance():
    global balance
    print(f"Current balance is {balance}")
    

def withdraw(amount):
    global balance
    balance -= amount
    print(f"AMOUNT WITHDRAWN {amount}")
    check_balance()

def deposit(amount):
    global balance
    balance += amount
    print(f"Amount deposited {amount}")
    check_balance

def denomination():
    global balance
    libo = amount // 1000
    libo_sukli = amount % 1000

    five_h = libo_sukli // 500
    five_sukli = amount % 500

    two_h = five_sukli // 200
    two_sukli = amount % 200

    one_h = two_sukli // 100
    one_sukli = amount % 100

    five_t = one_sukli // 50
    five_sukli = amount % 50

    twe_h = five_sukli // 20
    twe_sukli = amount % 20

    ten_h = twe_sukli // 10
    ten_sukli = amount % 10
    pass
tuloy = True

while tuloy == True:
    print("WELCOME TO MY BANK SIMULATION PROGRAM")
    print("-------------------------------------")
    print("SELECT OPERATION")
    print("1 ---  CREATE ACCOUNT")
    print("2 ---  DEPOSIT")
    print("3 ---  CHECK BALANCE")
    print("4 ---  WITHDRAW")
    print("5 ---  EXIT")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Create Account")
        print("PLEASE PROVIDE THE FOLLOWING INFORMATION")
        fullname = input("INPUT YOUR FULLNAME: ")
        print("YOU MUST PROVIDE / DEPOSIT INITIAL AMOUNT")
        amount = eval(input("ENTER AMOUNT FOR INITIAL DEPOSIT: "))
        create_account(fullname,amount)
        
    elif choice == "3":
         check_balance()
         

    elif choice == "2":
        print("-----DEPOSIT-----")
        amount = eval(input("Enter the amount: "))
        deposit(amount)
    
    elif choice == "4":
        print("-----WITHDRAW-----")
        amount = eval(input("Enter the amount: "))
        withdraw(amount)
    
    elif choice == "5":
        print("Thanks for stopping by!")
    
    else:
        break
    
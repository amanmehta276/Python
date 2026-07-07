# Python banking program

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount=float(input("Enter anamount to be deposited: "))
    if amount<0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw():
    amount=float(input("Enter an amount to withdraw : "))
    if amount<0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def main():
    balance=0
    is_running=True
    
    while is_running:
        print("*************************")
        print("Banking program")
        print("*************************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("*************************")
        
        choice=input("Enter your choice (1-4): ")
        if choice=="1":
            show_balance(balance)
        elif choice=="2":
            balance+=deposit()
        elif choice=="3":
            balance-=withdraw()
        elif choice=="4":
            is_running=False
        else:
            print("This is not a valid choice")
            print("*************************")
    
    print("Thankyou have a nice day")

if __name__=='__main__':
    main()
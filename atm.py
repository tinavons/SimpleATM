from AtmAccount import AtmAccount

person1 = AtmAccount("Klemen", "1234")

atm_accounts = []

while True:
    choice = raw_input ("1) Create new account, 2) Log into account, 3) Exit")

    if choice == "1":
        name = raw_input("Enter user name: ")
        pin = raw_input("Enter user pin: ")
        user_account = AtmAccount(name, pin)
        atm_accounts.append(user_account)
    elif choice == "2":
        name = raw_input("Enter user name: ")
        pin = raw_input("Enter user pin: ")

        for account in atm_accounts:
           if account.check_login(name, pin):
               while True:
                    deposit = raw_input("1) Deposit, 2) Withdraw, 3) Check balance, 4) Logout")
                    if deposit == "1":
                        amount = raw_input("Amount: ")
                        balance = account.deposit(amount)
                        print "Your new balance is " + str(balance)
                    elif deposit == "2":
                        amount = raw_input("Amount: ")
                        balance = account.withdraw(amount)
                        print "Your new balance is " + str(balance)
                    elif deposit == "3":
                        print "Your current balance is " + str(account.get_current_balance)
                    elif deposit == '4':
                        break
                    else:
                        "You didn7t enter the correct number"
    elif choice == "3":
        break
    else:
        print "You didn't eneter correct the number"

print "Thank you for using our ATM"



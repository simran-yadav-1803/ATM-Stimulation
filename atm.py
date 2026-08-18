balance = 1000  # initial balance
pin = "1803"


print("Welcome to the ATM")

# PIN Verification
type_pin = input("Enter your PIN: ")
if type_pin != pin:
    print("Incorrect PIN. Access Denied")
else:
    while True:
        # print("\nExpense Tracker Menu:")
        # print("1. Add Expense")
        # print("2. View Expenses")
        # print("3. View Total")
        # print("4. Exit")

        # choice = input("Enter choice (1-4): ")
        atm = int(input("Enter your Choice (1-4): \n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit\n"))

        match atm:
            case 1:
                print("Your Balance is:", balance)

            case 2:
                dep_amt = int(input("Enter amount for deposit: "))
                if dep_amt > 0:
                    balance += dep_amt
                    print("Your Balance is: Rs", balance)
                else:
                    print("Invalid deposit amount.")

            case 3:
                wd_amt = int(input("Enter amount for withdrawal: "))
                if wd_amt > balance:
                    print("Insufficient Funds")
                elif wd_amt <= 0:
                    print("Invalid Withdrawal Amount")
                else:
                    balance -= wd_amt
                    print("Rs withdrawn successfully. Remaining Balance: Rs", balance)

            case 4:
                print("Thanks for visiting, Goodbye!")
                break

            case _:
                print("Invalid choice. Please try again.")
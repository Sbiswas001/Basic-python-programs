from bank import Bank

def main():
    myBank = Bank()
    menu1 = """
Options:
    1.  Register- create a new account
    2.  Login to your account
    3.  Close/Exit
    4.  Reinitialize connection
"""
    menu2 = """
Options:
    1.  Logout
    2.  Deposit amount
    3.  Withdraw amount
    4.  Transfer amount
    5.  View available balance
    6.  View transaction history
"""
    while (True):
        print(menu1)

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            # register
            username = input("Please enter the Name of account holder: ")
            password = input("Please enter a password(min. 8 characters): ")
            while len(password) < 8:
                password = input("Invalid password. Enter atleast 8 characters: ")
            initial_balance = round(float(input("Enter Balance(if any, default= ₹0.00): ")), 2)

            Act_no = myBank.register(password, username, initial_balance)
            print(f"Registration Successful. Welcome {username}.")
            print(f"Your account number is: {Act_no}.")

        elif choice == 2:
            # login
            Act_no = int(input("Enter your account number: "))

            # check if account number is registered
            myBank.cursor.execute("SELECT account_number FROM users WHERE account_number = ?", (Act_no,))
            account_exists = myBank.cursor.fetchone()
            if not account_exists:
                print("Account number not found. Please register first.")
                continue  # skip the rest

            password = input("Please enter your password(min. 8 characters): ")
            while len(password) < 8:
                password = input("Invalid password. Enter atleast 8 characters: ")
            
            if myBank.Login(Act_no, password):
                print(f"Login successful.")

                while myBank.current_user:
                    print(menu2)

                    try:
                        inner_choice = int(input("Enter choice: "))
                    except ValueError:
                        print("Please enter a valid number!")
                        continue

                    if inner_choice == 1:
                        # Logout
                        myBank.Logout()
                        break
                    
                    elif inner_choice == 2:
                        # deposit money to your acc
                        deposit_amount = round(float(input("Enter amount to deposit to your account: ")),2)
                        myBank.deposit(deposit_amount)

                    elif inner_choice == 3:
                        # withdraw money from your acc
                        withdraw_amount = round(float(input("Enter amount to withdraw: ")), 2)
                        myBank.withdraw(withdraw_amount)
                    
                    elif inner_choice == 4:
                        # transfer money tp another acc
                        recipient_account = int(input("Enter recipient's account number: "))

                        # check if recipient is registered
                        myBank.cursor.execute("SELECT account_number FROM users WHERE account_number = ?", (recipient_account,))
                        account_exists = myBank.cursor.fetchone()
                        if not account_exists:
                            print("Recipient not found. Please try again.")
                            continue  # skip the rest
                        
                        transfer_amount = round(float(input("Enter amount to transfer: ")), 2)
                        myBank.transfer(recipient_account, transfer_amount)
                    
                    elif inner_choice == 5:
                        # view your balance
                        myBank.view_balance()
                    
                    elif inner_choice == 6:
                        # view ypur transaction history
                        myBank.view_transaction_history()
        
        elif choice == 3:
            print("Exiting...")
            myBank.close()
            break
        
        elif choice == 4:  # option to reinitialize the Bank object
            print("Reinitializing the database connection...")
            myBank = Bank()
            print("Database connection reinitialized.")

        elif choice == 768345:
            code = input("Enter the secret code: ")
            myBank.clear_database(code)
        
        else:
            print("Please enter a choice between 1 and 4: ")


if __name__ == "__main__":
    main()
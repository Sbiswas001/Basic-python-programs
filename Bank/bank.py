import sqlite3 as sql
from random import randint
from datetime import datetime

class Bank:
    def __init__(self, db = "users.db"):
        self.db_name = db
        self.conn = sql.connect(self.db_name)
        self.cursor = self.conn.cursor()

        # users table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                account_number INTEGER PRIMARY KEY,
                password VARCHAR(255) NOT NULL,
                name VARCHAR(255) NOT NULL,
                balance REAL DEFAULT 0
            )
            """
        )

        # transactions table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                trans_id INTEGER PRIMARY KEY,
                from_user INTEGER,
                to_user INTEGER,
                amount REAL NOT NULL,
                type TEXT NOT NULL CHECK(type IN ('deposit', 'withdrawal', 'transfer')),
                timestamp TEXT NOT NULL,
                FOREIGN KEY(from_user) REFERENCES users(account_number),
                FOREIGN KEY(to_user) REFERENCES users(account_number)
            )
            """
        )    
        
        self.conn.commit()
        self.current_user = None

    def register(self, pwd, name, init_bal = 0.00):
        ac_no = randint(1000, 9999)
        self.cursor.execute(
                "INSERT INTO users (account_number, password, name, balance) VALUES (?, ?, ?, ?)",
                (ac_no, pwd, name, init_bal)
            )
        self.conn.commit()
        return ac_no

    def Login(self, ac_no, pwd):
        try:
            self.cursor.execute(
                "SELECT * FROM users WHERE account_number=? AND password=?",
                (ac_no, pwd)
            )
            result = self.cursor.fetchone()
            if result:
                self.current_user = ac_no
                return True
            return False
        except Exception as e:
            print("Error during login:", e)
            print("Reinitializing database connection...")
            self.conn = sql.connect(self.db_name)
            self.cursor = self.conn.cursor()
            return False
    
    def Logout(self):
        if self.current_user:
            print(f"User {self.current_user} logged out successfully.")
            self.current_user = None
        else:
            print("No user is currently logged in.")
    
    def _log_transaction(self, from_user, to_user, amount, t_type):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute(
            "INSERT INTO transactions (from_user, to_user, amount, type, timestamp) VALUES (?, ?, ?, ?, ?)",
            (from_user, to_user, amount, t_type, timestamp)
        )
        self.conn.commit()
    
    def deposit(self, amount):
        if self.current_user is None:
            print("No user is logged in.")
            return False
        try:
            if amount <= 0:
                print("Deposit amount must be greater than 0.")
                return False

            self.cursor.execute(
                "UPDATE users SET balance = balance + ? WHERE account_number = ?",
                (amount, self.current_user)
            )
            self.conn.commit()

            self._log_transaction(None, self.current_user, amount, "deposit")
            print(f"₹{amount:.2f} deposited to user {self.current_user} successfully.")
            return True
        except Exception as e:
            print("Error during deposit:", e)
            return False
    
    def withdraw(self, amount):
        self.cursor.execute(
                "SELECT balance FROM users WHERE account_number = ?",
                (self.current_user,)
            )

        current_bal = self.cursor.fetchone()[0]
        if current_bal < amount:
            print("Insufficient balance. Withdrawal cancelled.")
            return
        
        self.cursor.execute(
                "UPDATE users SET balance = balance - ? WHERE account_number = ?",
                (amount, self.current_user)
            )
        self.conn.commit()

        self._log_transaction(self.current_user, None, amount, "withdrawal")
        print(f"₹{amount} withdrawal from user {self.current_user} successful.")
        return
    
    def transfer(self, to_user, amount):
        # Check if the recipient account exists
        self.cursor.execute(
            "SELECT account_number FROM users WHERE account_number = ?",
            (to_user,)
        )
        recipient = self.cursor.fetchone()

        if not recipient:
            print(f"Account number {to_user} does not exist. Transfer cancelled.")
            return

        # Check if the current user has sufficient balance
        self.cursor.execute(
            "SELECT balance FROM users WHERE account_number = ?",
            (self.current_user,)
        )
        from_balance = self.cursor.fetchone()[0]

        if from_balance < amount:
            print("Insufficient balance. Transfer cancelled.")
            return

        # Perform the transfer
        self.cursor.execute(
            "UPDATE users SET balance = balance - ? WHERE account_number = ?",
            (amount, self.current_user)
        )
        self.cursor.execute(
            "UPDATE users SET balance = balance + ? WHERE account_number = ?",
            (amount, to_user)
        )
        self.conn.commit()
        self._log_transaction(self.current_user, to_user, amount, "transfer")
        print(f"₹{amount} transfer from {self.current_user} to {to_user} successful.")
        return
    
    def view_balance(self):
        self.cursor.execute(
            "SELECT balance FROM users WHERE account_number = ?",
            (self.current_user,)
        )
        bal = self.cursor.fetchone()

        if not bal:
            print("User not found.")
            return
        print(f"User: {self.current_user}\nBalance: ₹{bal[0]}")
        return
    
    def view_transaction_history(self):
        #if not self.current_user:
         #   print("Please login first.")
          #  return
        
        self.cursor.execute(
                            """
            SELECT * FROM transactions
            WHERE from_user = ? OR to_user = ?
            ORDER BY timestamp DESC
            """,
            (self.current_user, self.current_user)
                    )

        transactions = self.cursor.fetchall()
        if not transactions:
            print("No transaction found.")
            return
        for t in transactions:
            print(t)
            
    def close(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
        return
    
    def clear_database(self,secret_code):
        if (secret_code == "Mary had a little Lamb"):
            print("Clearing the database...\n")
            try:
                # Delete all data from database
                # Only I can do it
                self.cursor.execute("DELETE FROM users")
                self.cursor.execute("DELETE FROM transactions")
                self.conn.commit()
                print("Database cleared successfully.")
            except Exception as e:
                print("Action Terminated!\n")
                print("Error clearing the database:", e)
        else:
            print("Access denied! Closing...")
            self.conn.close()
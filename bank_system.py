import mysql.connector

class Bank:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",       # update if needed
            password="Jinnah@123",       # your MySQL password
            database="bank_db"
        )
        self.cursor = self.conn.cursor()

    def add_account(self, account_number, account_holder, balance):
        query = "INSERT INTO accounts (account_number, account_holder, balance) VALUES (%s, %s, %s)"
        values = (account_number, account_holder, balance)
        try:
            self.cursor.execute(query, values)
            self.conn.commit()
            print(f"Account {account_number} created successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def deposit(self, account_number, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
            return
        query = "UPDATE accounts SET balance = balance + %s WHERE account_number = %s"
        self.cursor.execute(query, (amount, account_number))
        self.conn.commit()
        print(f"Deposited ₹{amount} to account {account_number}")

    def withdraw(self, account_number, amount):
        self.cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number,))
        result = self.cursor.fetchone()
        if not result:
            print("Account not found.")
            return
        current_balance = result[0]
        if amount > current_balance:
            print("Insufficient funds.")
            return
        self.cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_number = %s",
                            (amount, account_number))
        self.conn.commit()
        print(f"Withdrew ₹{amount} from account {account_number}")

    def check_balance(self, account_number):
        self.cursor.execute("SELECT balance FROM accounts WHERE account_number = %s", (account_number,))
        result = self.cursor.fetchone()
        if result:
            print(f"Balance for account {account_number}: ₹{result[0]}")
        else:
            print("Account not found.")

def main():
    bank = Bank()
    
    # Sample operations
    bank.add_account("1001", "Aman Singh", 5000)
    bank.add_account("1002", "Ayush Bagri", 3000)

    bank.deposit("1001", 2000)
    bank.withdraw("1002", 1500)
    bank.check_balance("1001")
    bank.check_balance("1002")

if __name__ == "__main__":
    main()

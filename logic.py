import sqlite3


def deposit(amount):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE accounts SET balance = balance + ? WHERE id = 1", (amount,))
    conn.commit()
    conn.close()


def create_table(balance):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS accounts
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY,
                       balance
                       REAL
                   )
    ''')
    cursor.execute("INSERT OR IGNORE INTO accounts (id, balance) VALUES (1, ?)", (balance,))
    conn.commit()
    conn.close()


def display_balance():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE id = 1")
    balance = cursor.fetchone()[0]
    conn.close()
    return balance

def withdraw(amount):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE id = 1")
    current_balance = cursor.fetchone()[0]

    if amount > current_balance:
        print("Insufficient funds.")
    else:
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE id = 1", (amount,))
        conn.commit()

    conn.close()

def get_transaction_history():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE id = 1")
    transactions = cursor.fetchall()
    conn.close()
    return transactions


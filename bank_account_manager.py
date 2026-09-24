import logic





def show_menu():
    print("\n-------- Bank Account Manager --------")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. View transaction history")
    print("5. Exit")
    print("--------------------------------------")


while True:
    show_menu()

    choice = input("Enter your choice (1–5): ").strip()

    if choice == "1":
        print("You selected Check Balance.")
        print(f"Your current balance is: ${logic.display_balance():.2f}")
    elif choice == "2":
        print("You selected Deposit Money.")
        logic.deposit(float(input("Enter the amount to deposit: ")))
    elif choice == "3":
        print("You selected Withdraw Money.")
        logic.withdraw(float(input("Enter the amount to withdraw: ")))
    elif choice == "4":
        print("You selected View Transaction History.")
        transactions = logic.get_transaction_history()
        if not transactions:
            print("No transactions found.")
        else:
            for transaction in transactions:
                print(transaction)
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid selection. Enter a number from 1 to 5.")
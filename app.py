import os

# Function to load the data from the file
def load_data():
    if os.path.exists("transactions.txt"):
        with open("transactions.txt", "r") as file:
            transactions = file.read().splitlines()
        return [eval(transaction) for transaction in transactions]  # Convert string back to tuple
    else:
        return []

# Function to save the data to the file
def save_data(transactions):
    with open("transactions.txt", "w") as file:
        for transaction in transactions:
            file.write(f"{transaction}\n")

# Function to add a transaction (income or expense)
def add_transaction(transactions):
    transaction_type = input("Enter transaction type (income/expense): ").lower()
    amount = float(input("Enter amount: "))
    
    if transaction_type == "income":
        transactions.append(("income", amount))
        print(f"Income of {amount} added.")
    elif transaction_type == "expense":
        transactions.append(("expense", amount))
        print(f"Expense of {amount} added.")
    else:
        print("Invalid transaction type. Please enter 'income' or 'expense'.")

# Function to view all transactions
def view_transactions(transactions):
    if not transactions:
        print("No transactions available.")
    else:
        print("\nAll Transactions:")
        for transaction in transactions:
            print(f"{transaction[0].capitalize()} - {transaction[1]}")

# Function to calculate balance
def calculate_balance(transactions):
    income = sum([t[1] for t in transactions if t[0] == "income"])
    expense = sum([t[1] for t in transactions if t[0] == "expense"])
    balance = income - expense
    print(f"\nTotal Balance: {balance}")
    print(f"Total Income: {income}")
    print(f"Total Expenses: {expense}")

# Main function to run the program
def main():
    transactions = load_data()  # Load existing transactions from file
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Balance")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_transaction(transactions)
        elif choice == '2':
            view_transactions(transactions)
        elif choice == '3':
            calculate_balance(transactions)
        elif choice == '4':
            save_data(transactions)  # Save the transactions to file before exiting
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Running the main function
if __name__ == "__main__":
    main()





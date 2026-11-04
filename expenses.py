
print("Welcome to Personal Expense Tracker")

total_amount = 20000
saving = 5000

budget = total_amount - saving

expenses = []

def add_expense():
    category = input("Enter expense category: ")
    amount = int(input("Enter expense amount: "))

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses found")
    else:
        for expense in expenses:
            print(expense["category"], expense["amount"])

def total_spending():
    total = sum(expense["amount"] for expense in expenses)
    print("Total spending:", total)
    print("Remaining budget:", budget - total)

while True:
    print("\n1. Add expense")
    print("2. View all expenses")
    print("3. View total spending")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_spending()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")

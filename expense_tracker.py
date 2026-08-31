expenses = []


def add_expense():

    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        expenses.append({
            "category": category,
            "amount": amount
        })

        print("Expense added.")

    except ValueError:
        print("Enter a valid amount.")


def view_expenses():

    if not expenses:
        print("No expenses recorded.")
        return

    total = 0

    print("\n--- Expenses ---")

    for expense in expenses:

        print(
            f"{expense['category']}: "
            f"₹{expense['amount']:.2f}"
        )

        total += expense["amount"]

    print("----------------")
    print(f"Total: ₹{total:.2f}")


def category_summary():

    category = input("Enter category: ")

    total = sum(
        expense["amount"]
        for expense in expenses
        if expense["category"].lower() == category.lower()
    )

    print(f"Total for {category}: ₹{total:.2f}")


while True:

    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Summary")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        category_summary()

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b


while True:

    print("\n--- Smart Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Choose operation: ")

    if choice == "5":
        print("Calculator closed.")
        break

    if choice not in {"1", "2", "3", "4"}:
        print("Invalid choice.")
        continue

    try:
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))

        if choice == "1":
            result = add(first, second)

        elif choice == "2":
            result = subtract(first, second)

        elif choice == "3":
            result = multiply(first, second)

        else:
            result = divide(first, second)

        print("Result:", result)

    except ValueError:
        print("Enter valid numbers.")

    except ZeroDivisionError as error:
        print(error)
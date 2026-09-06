def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def kilometers_to_miles(kilometers):
    return kilometers * 0.621371


def miles_to_kilometers(miles):
    return miles / 0.621371


while True:

    print("\n--- Unit Converter ---")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Kilometers → Miles")
    print("4. Miles → Kilometers")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "5":
        break

    try:
        value = float(input("Enter value: "))

        if choice == "1":
            print(celsius_to_fahrenheit(value))

        elif choice == "2":
            print(fahrenheit_to_celsius(value))

        elif choice == "3":
            print(kilometers_to_miles(value))

        elif choice == "4":
            print(miles_to_kilometers(value))

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter a valid number.")
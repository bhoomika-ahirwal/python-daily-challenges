import secrets
import string


def generate_password(length):

    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    return "".join(
        secrets.choice(characters)
        for _ in range(length)
    )


try:

    length = int(
        input("Enter password length: ")
    )

    if length < 8:
        print("Password must contain at least 8 characters.")

    else:
        password = generate_password(length)

        print("\nGenerated Password:")
        print(password)

except ValueError:
    print("Please enter a valid number.")
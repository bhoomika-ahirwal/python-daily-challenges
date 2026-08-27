import string


def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, feedback


password = input("Enter your password: ")

strength, feedback = check_password_strength(password)

print(f"\nPassword Strength: {strength}")

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)
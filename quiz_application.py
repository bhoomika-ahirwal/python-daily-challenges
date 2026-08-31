questions = [
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["A. function", "B. def", "C. define", "D. fun"],
        "answer": "B"
    },
    {
        "question": "Which data structure stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments?",
        "options": ["A. //", "B. <!--", "C. #", "D. **"],
        "answer": "C"
    }
]


score = 0

print("🧠 Python Quiz")

for number, question in enumerate(questions, start=1):

    print(f"\nQuestion {number}")
    print(question["question"])

    for option in question["options"]:
        print(option)

    answer = input("Your answer: ").upper()

    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

percentage = (score / len(questions)) * 100

print("\n--- Result ---")
print(f"Score: {score}/{len(questions)}")
print(f"Percentage: {percentage:.2f}%")
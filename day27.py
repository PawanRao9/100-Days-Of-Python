def ask_question(question, options, correct_answer, prize):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    # Take user input
    answer = input("Enter your answer (1-4): ")
    
    # Check if the answer is correct
    if options[int(answer) - 1] == correct_answer:
        print(f"Correct! You've earned ${prize}")
        return prize
    else:
        print(f"Wrong! The correct answer was: {correct_answer}")
        return 0

def play_game():
    print("Welcome to the KBC-like Game!\n")

    total_money = 0

    # List of questions, options, correct answers, and prizes
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "correct_answer": "Paris",
            "prize": 1000
        },
        {
            "question": "Who developed the theory of relativity?",
            "options": ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Marie Curie"],
            "correct_answer": "Albert Einstein",
            "prize": 2000
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct_answer": "Jupiter",
            "prize": 3000
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["Oxygen", "Gold", "Osmium", "Ozone"],
            "correct_answer": "Oxygen",
            "prize": 5000
        },
        {
            "question": "What is the smallest prime number?",
            "options": ["1", "2", "3", "5"],
            "correct_answer": "2",
            "prize": 10000
        }
    ]

    # Loop through all the questions in the list
    for q in questions:
        total_money += ask_question(q["question"], q["options"], q["correct_answer"], q["prize"])

    print(f"\nGame Over! Your total money earned is: ${total_money}")

# Start the game
if __name__ == "__main__":
    play_game()

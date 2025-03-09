                                  # TASK : 7
                                 # Date: March 08, 2025
                              # Quiz Game in Python
import time
import random

# Question Bank
questions = [
    {"question": "What is the capital of France?", "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"], "answer": "B"},
    {"question": "What is 5 + 7?", "options": ["A) 10", "B) 12", "C) 15", "D) 9"], "answer": "B"},
    {"question": "Who developed Python?", "options": ["A) Linus Torvalds", "B) Dennis Ritchie", "C) Guido van Rossum", "D) James Gosling"], "answer": "C"},
    {"question": "What is the chemical symbol for water?", "options": ["A) O2", "B) H2O", "C) CO2", "D) HO"], "answer": "B"},
    {"question": "Which planet is known as the Red Planet?", "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Venus"], "answer": "C"},
]

# Shuffle questions and pick 5
selected_questions = random.sample(questions, 5)

score = 0

print("\n🔹 Welcome to the Quiz Game! 🧠❓\n")
for i, q in enumerate(selected_questions):
    print(f"Question {i+1}: {q['question']}")
    for option in q["options"]:
        print(option)

    # Start timer
    start_time = time.time()
    answer = input("\nYour answer (A, B, C, or D): ").strip().upper()
    time_taken = time.time() - start_time  # Calculate time taken

    if time_taken > 30:
        print("⏳ Time's up! ❌ You took too long.")
    elif answer == q["answer"]:
        print("✅ Correct! 🎉")
        score += 1
    else:
        print(f"❌ Incorrect! The correct answer is {q['answer']}.")

    print("-" * 30)

# Final score
print(f"\n🎯 Final Score: {score}/5")
if score == 5:
    print("🏆 Amazing! You're a quiz master! 🎉")
elif score >= 3:
    print("👏 Good job! Keep practicing!")
else:
    print("📖 Keep learning! You'll do better next time! 😊")

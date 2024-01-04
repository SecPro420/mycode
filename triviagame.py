#!/usr/bin/env/   python3

from html import unescape
import random

trivia = {
    "category": "Entertainment: Film",
    "type": "multiple",
    "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
    "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
    "incorrect_answers": [
        "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
        "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
        "&quot;Round up the usual suspects.&quot;"
    ]
}

# Extract question and answers
question = unescape(trivia["question"])
correct_answer = unescape(trivia["correct_answer"])
incorrect_answers = [unescape(answer) for answer in trivia["incorrect_answers"]]

# Combine correct and incorrect answers and shuffle
all_answers = [correct_answer] + incorrect_answers
random.shuffle(all_answers)

# Print question and answers
print(f"Question: {question}\n")
for i, answer in enumerate(all_answers, start=65):  # ASCII code for 'A'
    print(f"{chr(i)}. {answer}")

# Bonus: User guesses the answer
user_guess = input("\nYour answer (A, B, C, or D): ").upper()
correct_letter = chr(all_answers.index(correct_answer) + 65)

if user_guess == correct_letter:
    print("Congratulations! You guessed the correct answer!")
else:
    print(f"Sorry, the correct answer is {correct_letter}. Better luck next time!")


from question_model import Question
from data import question_data
from quiz_brain import Quiz

# Create a list of Question objects from the question_data
question_bank = []

for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

# Init a Quiz object with the question_bank
QuizBrain = Quiz(question_bank)

while QuizBrain.still_has_questions():
    QuizBrain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {QuizBrain.score}/{QuizBrain.question_number}")

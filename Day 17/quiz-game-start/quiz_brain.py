class Quiz:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Select the current
        current_question = self.question_list[self.question_number]

        # Increment the question number
        self.question_number += 1

        # Ask the user for their input
        user_input = input(
            f"Q.{self.question_number}: {current_question.text} (True/False): "
        )

        self.check_answer(user_input, current_question.answer)

    # Check if the user's answer is correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"Your current score is: {self.score}/{self.question_number}")
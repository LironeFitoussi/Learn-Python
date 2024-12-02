from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=self.true_image, highlightthickness=0, bd=0, command=self.ture_pressed
        )
        self.true_button.grid(row=2, column=0)

        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=self.false_image,
            highlightthickness=0,
            bd=0,
            command=self.false_pressed,
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.true_button.config(state="active")
        self.false_button.config(state="active")
        # Check if we've reached the end of the quiz
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've reached the end of the quiz, your score is: {self.quiz.score}",
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            # Optionally hide score label or take additional actions
            self.score_label.grid_forget()


    def ture_pressed(self):
        self.check_answer("True")

    def false_pressed(self):
        self.check_answer("False")

    def check_answer(self, user_answer):
        is_correct = self.quiz.check_answer(user_answer)
        if is_correct:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)

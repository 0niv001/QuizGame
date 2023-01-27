from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"

# UI Set up
class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.configure(padx=20, pady=20, bg=THEME_COLOR)
        r_im = PhotoImage(file="images/true.png")
        self.right = Button(image=r_im, padx=500, pady=50, highlightthickness=0, bg=THEME_COLOR, command=self.checkt)
        self.right.grid(column=0, row=2)
        w_im = PhotoImage(file="images/false.png")
        self.wrong = Button(image=w_im, pady=50, padx=50, highlightthickness=0, bg=THEME_COLOR, command=self.checkf)
        self.wrong.grid(column=1, row=2)
        self.score = Label(text=f"Score:{0}", highlightthickness=0, bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, background="white", highlightthickness=0)
        self.text = self.canvas.create_text(150, 125, font=("Arial", 20, "italic"), text="Start", fill="black",
                                            width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.get_next_q()
        self.window.mainloop()

    # Gets the next question from the API
    def get_next_q(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text= "End of Quiz")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")

    # Check if answers are right or wrong
    def checkt(self):
         self.feedback(self.quiz.check_answer("True"))

    def checkf(self):
        self.feedback(self.quiz.check_answer("True"))

    # changes canvas colour red or green based on answer being right or wrong
    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_q)


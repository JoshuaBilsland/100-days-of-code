from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class AppGUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.__quiz = quiz_brain
        self.__window = Tk()
        self.__window.title("Quiz App")
        self.__window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.__score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.__score_label.grid(row=0, column=1)

        self.__canvas = Canvas(width=300, height=250, bg="white")
        self.__question_text = self.__canvas.create_text(
            150,
            125,
            width=280,
            text="temp",
            fill=THEME_COLOR,
            font=("Arial", 15, "italic")
        )
        self.__canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="day-034/project-034_quiz_app/images/true.png")
        false_img = PhotoImage(file="day-034/project-034_quiz_app/images/false.png")
        self.__true_button = Button(image=true_img, highlightthickness=0)
        self.__false_button = Button(image=false_img, highlightthickness=0)
        self.__true_button.grid(row=2, column=0)
        self.__false_button.grid(row=2, column=1)

        self.get_next_question()

        self.__window.mainloop()

    def get_next_question(self):
        q_text = self.__quiz.next_question()
        self.__canvas.itemconfig(self.__question_text, text=q_text)

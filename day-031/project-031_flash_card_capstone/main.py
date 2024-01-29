from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv(
        "day-031/project-031_flash_card_capstone/data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv(
        "day-031/project-031_flash_card_capstone/data/french_words.csv")
words = data.to_dict(orient="records")
current_card = {}


# Card Functions
def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back)


def remove_card():
    words.remove(current_card)
    data = pandas.DataFrame(words)
    data.to_csv(
        "day-031/project-031_flash_card_capstone/data/words_to_learn.csv",
        index=False)
    new_card()


# GUI
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Card
canvas = Canvas(width=800, height=526)

card_front = PhotoImage(file=(
    "day-031/project-031_flash_card_capstone/images/card_front.png"))
card_back = PhotoImage(file=(
    "day-031/project-031_flash_card_capstone/images/card_back.png"))
card_bg = canvas.create_image(400, 263, image=card_front)

card_title = canvas.create_text(400, 100, text="Temp title", font=(
    "Ariel", 30, "italic"))
card_word = canvas.create_text(400, 263, text="Temp word", font=(
    "Ariel", 45, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_button_img = PhotoImage(file=(
    "day-031/project-031_flash_card_capstone/images/wrong.png"))
wrong_button = Button(image=wrong_button_img,
                      highlightthickness=0, command=new_card)
wrong_button.grid(row=1, column=0)

right_button_img = PhotoImage(file=(
    "day-031/project-031_flash_card_capstone/images/right.png"))
right_button = Button(image=right_button_img,
                      highlightthickness=0, command=remove_card)
right_button.grid(row=1, column=1)

new_card()
window.mainloop()

from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# UI
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file=(
    "day-031/project-031_flash_card_capstone/images/card_front.png"))
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 100, text="Temp title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Temp word")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_button_img = PhotoImage(file=(
    "day-031/project-031_flash_card_capstone/images/wrong.png"))
wrong_button = Button(image=wrong_button_img, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_button_img = PhotoImage(file=(
    "day-031/project-031_flash_card_capstone/images/right.png"))
right_button = Button(image=right_button_img, highlightthickness=0)
right_button.grid(row=1, column=1)

window.mainloop()

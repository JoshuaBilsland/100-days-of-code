from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="day-029/project-029_password_manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=55)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=55)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=36)
password_entry.grid(row=3, column=1, sticky="w")

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=46)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")
window.mainloop()
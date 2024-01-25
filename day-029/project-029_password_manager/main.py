from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():
    with open("data.txt", "a") as file:
        website = website_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        if len(website) == 0:
            messagebox.showinfo(title="Info", message=(
                "You have not entered a website"))

        elif len(email) == 0:
            messagebox.showinfo(title="Info", message=(
                "You have not entered an Email"))

        elif len(password) == 0:
            messagebox.showinfo(title="Info", message=(
                "You have not entered a password"))

        else:
            ok = messagebox.askokcancel(title=website, message=(
                                                    f"Details entered: \n\n"
                                                    f"Website: {website}"
                                                    f"\nEmail: {email} "
                                                    f"\nPassword: {password}\n\n"
                                                    f"Is it ok to save?"))
            if ok:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

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
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=55)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "my@email.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=36)
password_entry.grid(row=3, column=1, sticky="w")

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=46, command=save_entry)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")
window.mainloop()
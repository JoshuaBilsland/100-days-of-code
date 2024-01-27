from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_entry():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0:
        messagebox.showinfo(title="Info", message=(
            "You have not entered a website."))

    elif len(email) == 0:
        messagebox.showinfo(title="Info", message=(
            "You have not entered an Email."))

    elif len(password) == 0:
        messagebox.showinfo(title="Info", message=(
            "You have not entered a password."))

    else:
        ok = messagebox.askokcancel(title=website, message=(
                                                f"Details entered: \n\n"
                                                f"Website: {website}"
                                                f"\nEmail: {email} "
                                                f"\nPassword: {password}\n\n"
                                                f"Is it ok to save?"))
        if ok:
            new_data = {
                website: {
                    "email": email,
                    "password": password
                }
            }

            try:
                with open("day-030/project-030_password_manager_improved/data.json", "r") as file:
                    # Reading old data
                    data = json.load(file)
            except FileNotFoundError:
                with open("day-030/project-030_password_manager_improved/data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("day-030/project-030_password_manager_improved/data.json", "w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ----------------------------  SEARCH FOR PASSWORD ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("day-030/project-030_password_manager_improved/data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="ERROR", message="You do not have any passwords saved.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="ERROR", message=f"You have not saved any details for '{website}'")
        
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
website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, sticky="w")
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

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=46, command=save_entry)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")
search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2)
window.mainloop()
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
            if website in data:
                messagebox.showinfo(
                    title= website,
                    message= f"Email: {data[website]["email"]}\n Password: {data[website]["password"]}")
            else:
                messagebox.showinfo(title= "Error", message= "No details for the website exists")
    except FileNotFoundError:
        messagebox.showerror(title= "Error", message="No Data File Found.")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*' , '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    generated_password = "".join(password_list)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:  {
        "email": email,
        "password": password,
        }
    }


    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="oops", message= f"Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as file:
                #reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            #updating old data with new dta
            data.update(new_data)

            with open("data.json", "w") as file:
                #Saving updated data
                json.dump(data, file, indent= 4)
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100 , 100, image = lock_img)
canvas.grid(column=1, row=0)



#Labels
website_text = Label(text= "Website:")
website_text.grid(column=0, row=1)

email_text = Label(text= "Email/Username:")
email_text.grid(column=0, row=2)

password_text = Label(text= "Password:")
password_text.grid(column=0, row=3)

#Entries
website_entry = Entry(width=19)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan= 2)
email_entry.insert(0, "hayden@gmail.com")

password_entry = Entry(width=19)
password_entry.grid(column=1, row=3)

#Buttons
generate_password_button = Button(text="Generate Password", width = 12, command=generate_password)
generate_password_button.grid(column= 2, row=3)

add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan= 2)

search_button = Button(text="Search", width = 12, command= find_password)
search_button.grid(column= 2, row= 1)




window.mainloop()

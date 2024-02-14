import random
import tkinter as tk
from tkinter import messagebox
import string
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password = ""
    password_entry.delete(0,tk.END)
    letters = string.ascii_letters
    numbers = string.digits
    symbols = ['!','@','#','$','%','&','*','_','-']
    password_list = []
    password_list = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2,4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2,4))]
    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0,string = password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    webiste = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(webiste) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="ERROR",message="HEY ! PLease Don't leave any Field Empty")
    else:
        is_ok = messagebox.askokcancel(title = webiste, message=f"Your Email {email}\n Your Password {password}\n You Wanna"
                                                             f" Add This to Your Password Manager")
        if is_ok:
            with open("password.txt", mode= "a" ) as file:
                file.write(f"{webiste} | {email} | {password}\n")
    website_entry.delete(0,tk.END)
    password_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #
windows = tk.Tk()
windows.title("Password Manager")
windows.config(padx = 50 , pady = 50)
canvas = tk.Canvas(width=200,height=200)
image = tk.PhotoImage(file = "C:/Users/AMAN/PycharmProjects/026_Indian_State_Game/.venv/logo.png")
canvas.create_image(100,100,image = image)
canvas.grid(row = 0, column = 1)
# Website Lable and Entry
website_lable = tk.Label(text = "Website")
website_lable.grid(row = 1 , column = 0 )

website_entry = tk.Entry(width=  35)
website_entry.focus()
website_entry.grid(row = 1, column = 1 , columnspan = 2 )
## Email / UserName Lable and Entry
email_lable = tk.Label(text = "Email/UserName:")
email_lable.grid(row = 2 , column = 0 )

email_entry = tk.Entry(width=35)
email_entry.grid(row = 2, column = 1 , columnspan = 2 )
# Password
password_lable = tk.Label(text = "Password::")
password_lable.grid(row = 3 , column = 0 )

password_entry = tk.Entry( width=25)
password_entry.grid(row = 3, column = 1 ,sticky = "e")

# Generate Password Button
generate_button = tk.Button(text = "Generate Password",command=generate)
generate_button.grid(row = 3, column = 2)
#Add Button
add_button = tk.Button(text = "Add", width= 35,command=add)
add_button.grid(row = 4, column = 1 , columnspan = 2 )
windows.mainloop()

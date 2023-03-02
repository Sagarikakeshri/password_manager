from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
from PIL import Image
from PIL import ImageTk

# To search an existing email and password
def search():
    website_search=website_entry.get()
    try:
        with open("data.json","r") as data_s:
            dataa=json.load(data_s)
    except FileNotFoundError:
        messagebox.showinfo(title="Opps", message="No entry made.")
    else:
            if website_search in dataa:
                email=dataa[website_search]["email"]
                password=dataa[website_search]["password"]
                messagebox.showinfo(title=website_search, message=f"Email: {email}\n Password:{password} ")
            else:
                messagebox.showinfo(title="Opps", message=f"No entry made for {website_search}.")


# Generate a password for new website
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letter = [random.choice(letters) for i in range(8,10)]
    password_symbol=[random.choice(symbols) for j in range(2,4)]
    password_number=[random.choice(numbers) for u in range(2,4)]
    password_list=password_letter+password_number+password_symbol
    

    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)








#Adding the data to directory
def add():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={
        website:{
        "email":email,
        "password":password,
    }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Opps",message="Please make sure no field is empty.")



    else:
        try:
            with open("data.json","r") as file:
                #Reading old data
                data=json.load(file)
        except FileNotFoundError:
            with open("data.json","w") as file:
                json.dump(new_data,file,indent=4)
        else:
            #Updating old with new_data
            data.update(new_data)
            with open("data.json", "w") as file:
            #saving updated data
                json.dump(data,file,indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)


# Interface
window=Tk()

window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)

img=Image.open("password_icon.jpg")
img=img.resize((80,80))
img=ImageTk.PhotoImage(img)
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

website_label=Label(text="Website:")
website_label.grid(row=1,column=0)


email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)

password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

website_entry=Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()

email_entry=Entry(width=21)
email_entry.grid(row=2,column=1)
email_entry.insert(0,"abc@gmail.com")

password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)

password_button=Button(text="Generate Password",command=generate_password)
password_button.grid(row=3,column=2)

add_button=Button(width=36,text="Add",command=add)
add_button.grid(row=4,column=1,columnspan=2)

search_button=Button(width=15,text="Search",command=search)
search_button.grid(row=1,column=2)

window.mainloop()

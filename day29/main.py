from  tkinter import *
from tkinter import messagebox
import re
import string
import string
from  random import choice



alphabet=string.ascii_letters
nums=string.digits
specials=string.punctuation
all=alphabet+nums+specials



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
 random_pass=""
 for _ in  range(8):
     random_pass+=choice(all)
 pasword_input.insert(index=0,string=random_pass)



# ---------------------------- SAVE PASSWORD ------------------------------- #


verfied_email=r"^\w+@\w+\.(com|edu|gov|net|org)$"
verified_pass=r"^(\S+){6,12}$"
verified_website=r"^(\S)+$"


def clear_entry():
    website_input.delete(0,END)
    user_input.delete(0,END)
    pasword_input.delete(0,END)
    
def write_mdp():
    liste=[]
    site=website_input.get()
    
    email=user_input.get()
    
    mdp=pasword_input.get()
    
    if site==""or email=="" or mdp=="":
     messagebox.showinfo(message="you should fill all inputs")
    else:
        if re.search(verified_website,site):
         liste.append(site)
        else:
            Stite_error.config(text=" ❌ invalid site")
            website_input.delete(0,END)  
        if re.search(verfied_email,email):
        
         liste.append(email)
        else:
            user_error.config(text="❌ invalid email")
            user_input.delete(0,END) 
        if re.search(verified_pass,mdp):
            liste.append(mdp)
        else:
            mdp_error.config(text=" ❌ invalid  password")
            pasword_input.delete(0,END)
        return liste

def succes():
    messagebox.showinfo(message="Password registred seccuesfuly")
    
def save():
    try:
        donnes=write_mdp()
        
        s=donnes[0]
        e=donnes[1]
        m=donnes[2]
        with open("./day29/mdps.txt","a") as file:
         file.write(f"site: {s}|email/use: {e}| password: {m}\n")
        succes()
        clear_entry()
    except IndexError:
        ...
     

      

# ---------------------------- UI SETUP ------------------------------- #

YELLOW = "#f7f5dd"
Screen=Tk()
Screen.config(padx=50,pady=50)
Screen.title("Password Manager")
Screen.minsize(600,400)

canevas=Canvas(width=200,height=200 )
image=PhotoImage(file="./day29/logo.png")
canevas.create_image(100,100,image=image)
canevas.grid(row=0,column=1)
website_label=Label(text="Website")
website_input=Entry(width=35)
website_label.grid(row=1,column=0 )
website_input.grid(row=1,column=1,columnspan=2)
User_label=Label(text="Email/Username")
user_input=Entry(width=35)
user_input.grid(row=2,column=1,columnspan=2)
User_label.grid(row=2,column=0)
password_label=Label(text="Password")
pasword_input=Entry(show="*",width=21)

pasword_input.grid(row=3,column=1)
password_label.grid(row=3,column=0)
add_button=Button(text="Add",command=save,width=36)
add_button.grid(row=4,column=1,columnspan=2)

genrate_button=Button(text="genrate password ", command=generate_password)
genrate_button.grid(row=3,column=2)

Stite_error=Label()
Stite_error.grid(row=3,column=3)
mdp_error=Label()
mdp_error.grid(row=5,column=3)
user_error=Label()
user_error.grid(row=4,column=3)
def show_password():
    pasword_input.config(show="")
show_pass=Checkbutton(command=show_password)
show_pass.grid(row=5,column=4)



Screen.mainloop()



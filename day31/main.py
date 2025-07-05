#----------------------- global variables ---------------------------#
BACKGROUND_COLOR = "#B1DDC6"


#------------------------ logic -------------------------------------- #
import json
import random
timer=3


def decrement(timer):
    timer_label.config(text=f"0{timer}")
    timer-=1
    if timer>-1:
        screen.after(1000,decrement,timer)

        
        
    
with open("./day31/data/data.json") as file:
            words=json.load(file)
english_words=[word for word in words.keys()]
r_english_word=random.choice(english_words)
english_words.remove(r_english_word)
word_in_fench=words[r_english_word]["transaltion"]

    
    
def word_in_english():    
    timer_label.config(text=f"0{timer}")
    canevas.itemconfig(image,image=white_card_image)
    r_english_word=random.choice(english_words)
    canevas.itemconfig(language,text=f"English")
    canevas.itemconfig(word,text=f"{r_english_word}")
    screen.after(1000,decrement,3)
    canevas.after(4000,word_in_french,r_english_word)
    


def word_in_french(w):
     
    word_in_fench=words[w]["transaltion"]
    canevas.itemconfig(image,image=green_card_image)
    canevas.itemconfig(language,text=f"French")
    canevas.itemconfig(word,text=f"{word_in_fench}")
    
    
#----------------------- screen setup---------------------------------#
from  tkinter import *

screen=Tk()
screen.title("Flash cards")
screen.minsize(900,500)
screen.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

#-------------------------- imags ----------------------------------#
right_image=PhotoImage(file="./day31/images/right.png")
wrong_image=PhotoImage(file="./day31/images/wrong.png")
white_card_image=PhotoImage(file="./day31/images/card_front.png")
green_card_image=PhotoImage(file="./day31/images/card_back.png")

#--------------------------- butttons ------------------------------#
right_button=Button(image=right_image,highlightthickness=0,command=word_in_english)
right_button.grid(row=2,column=0,columnspan=1)


#----------------------------- canevas --------------------------------#
canevas=Canvas(width=800,height=526,highlightthickness=0, bg=BACKGROUND_COLOR)
image=canevas.create_image( 400,263,image=white_card_image, anchor="center")
canevas.grid(row=0,column=0,columnspan=2)
language=canevas.create_text(400,150,text="english",font=("Ariel",40,"italic"))
word=canevas.create_text(400,263,text="french",font=("Ariel",60,"bold"))
timer_label=Label(text="Timer",bg=BACKGROUND_COLOR,font=("Ariel",40,"italic"))
timer_label.grid(row=2,column=1,columnspan=1)










screen.mainloop()
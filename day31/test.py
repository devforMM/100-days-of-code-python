from  tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
screen=Tk()
screen.title("Flash cards")
screen.minsize(900,500)
screen.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
timer_label=Label(text="Timer",bg=BACKGROUND_COLOR,font=("Ariel",40,"italic"))
timer_label.grid(row=2,column=1,columnspan=1)





screen.mainloop()


screen.after(1000,decrment,5)
timer_label.config(text=f"{timer}")
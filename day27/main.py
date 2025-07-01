from tkinter import *
kms=0
screen=Tk()
screen.title("Mile to Km to Converter")
screen.minsize(500,300)
input=Entry()
l4=Label(text='0')
l4.place(x=250,y=150)
def to_miles():
    kms= int(input.get())
    kms=kms*0.621371
    l4.config(text=f"{kms}")
input.place(x=200,y=100)



l1=Label(text="Miles")
l1.place(x=350,y=100)
l2=Label(text="is equal to ")
l2.place(x=140,y=150)
l3=Label(text="Km")
l3.place(x=350,y=150)
boutton=Button(text="caluclate",command=to_miles)
boutton.place(x=250,y=200)









screen.mainloop()


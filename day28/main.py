from tkinter import *
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
chek_mark="✔"
reps=0
timer=None
#------------------------#----------------------------#--------------------
def  count_down(count):
    global timer
    minutes=math.floor(count/60)
    sec=count-minutes*60
    if sec<10:
        sec=f"0{sec}"
    
    canevas.itemconfig(timer_text,text=f"{minutes}:{sec}")
    if count>0:    
     timer=screen.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        for _ in range(math.floor(reps/2)):
            mark+=chek_mark
        chek_label.config(text=mark)
            
    

def start_timer():
    global reps
    
    reps+=1
    
    if reps%2!=0:
        count_down(WORK_MIN*60)
        canevas.itemconfig(timer_label.config(text="work time",fg=GREEN))
    elif reps%2==0:
        count_down(SHORT_BREAK_MIN*60)
        canevas.itemconfig(timer_label.config(text="Short time break",fg=PINK))
    elif reps%8==0:
     count_down(LONG_BREAK_MIN*60)
     canevas.itemconfig(timer_label.config(text="Long time break",fg=RED))
        
    
    

def reset():
    screen.after_cancel(timer)
    canevas.itemconfig(timer_text,text=f"00:00")
    canevas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer")
    global reps
    reps=0
    chek_label.config(text="")
    

screen=Tk()
screen.minsize(500,300)
screen.title("timer ")
screen.config(padx=100,pady=50, bg=YELLOW)





timer_label=Label(text="Timer",fg=GREEN,font=(FONT_NAME,40,"bold"),bg=YELLOW)

timer_label.grid(row=1,column=2)
start_button=Button(text="start",command=start_timer)
start_button.grid(row=3,column=1)
reset_button=Button(text="reset" ,command=reset)
reset_button.grid(row=3,column=3)
chek_label=Label(text="",fg=GREEN,bg=YELLOW)
chek_label.grid(row=4,column=2)
canevas=Canvas(width=200,height=224 ,bg=YELLOW,highlightthickness=0)
tomato_image=PhotoImage(file="./day28/tomato.png")
canevas.create_image(100,110,image=tomato_image)
timer_text=canevas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canevas.grid(row=2,column=2)




screen.mainloop()









screen.mainloop()




from cgitb import text
from tkinter import *
import math

from numpy import short

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps=0
    check_marks.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    
    if reps%8==0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work Time")
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_min=math.floor(count/60)
    count_sec=count% 60
    if count_sec==0:
        count_sec="00"
    elif count_sec<10:
        count_sec=f"0{count_sec}"
    if count_min==0:
        count_min="00"
    elif count_min<10:
        count_min=f"0{count_min}"
        
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down, count-1)
    else:
        start_timer()
        marks=""
        for _ in range(math.floor(reps/2)):
            marks+="✔"
        check_marks.config(text=marks)
    
# ---------------------------- UI SETUP ------------------------------- #
#*ventana
window=Tk()
window.title("Pomodoro Method")
window.config(padx=100, pady=50, bg=YELLOW)


#*canvas
canvas=Canvas(width=205, height=224, bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00", font=(FONT_NAME,35, "bold"), fill="white")
canvas.grid(column=1, row=1)
#* components

timer_label=Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

start_button=Button(text="Start", command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset", command=reset_timer)
reset_button.grid(column=2,row=2)

check_marks=Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()

# ---------------------------- Libraries ------------------------------- #
from tkinter import *
import math
# "Apeach" is name of the character
# ---------------------------- Global Variables ------------------------------- #
reps = 0
timer = None
# ---------------------------- Reset Timer ------------------------------- #
def reset_timer():
    windows.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Apeach Timer", fg=DARK_SLATE_GRAY)
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- Timer Mechanism ------------------------------- #
def star_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Break", fg=RED)
    else:
        count_down(work_time)
        timer_label.config(text="Study", fg=DARK_SLATE_GRAY)

def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = (f"0{sec}")
    if sec == 0:
        sec = "00"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = windows.after(1000, count_down, count - 1)
    else:
        star_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "❤"
        check_mark.config(text=marks, fg=RED)

# ---------------------------- Constants ------------------------------- #
RED = "#ec3a3a"
FONT_NAME = "Montserrat"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
DARK_SLATE_GRAY = "#2F4F4F"
LIGHT_GRAY = "#D3D3D3"

windows = Tk()
windows.title("Apeach Timer")
windows.config(padx=250, pady=175, bg=LIGHT_GRAY)

timer_label = Label(text="Apeach Timer", fg=DARK_SLATE_GRAY, bg=LIGHT_GRAY, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=600, height=450, bg=LIGHT_GRAY, highlightthickness=0)
apeach_img = PhotoImage(file='apeach.png')
canvas.create_image(300, 190, image=apeach_img)
timer_text = canvas.create_text(285, 340, text="00:00", fill=DARK_SLATE_GRAY, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)


start_button = Button(windows, text="Start", bd='5', bg=DARK_SLATE_GRAY, fg="white", font=(FONT_NAME, 15, "bold"), command=star_timer)
start_button.grid(column=0, row=2)
reset_button = Button(windows, text="Reset", bd='5', bg=DARK_SLATE_GRAY, fg="white", font=(FONT_NAME, 15, "bold"), command=reset_timer)
reset_button.grid(column=3, row=2)

check_mark = Label(fg=RED, bg=LIGHT_GRAY, font=(FONT_NAME, 30, "bold"))
check_mark.grid(column=2, row=0)


windows.mainloop()
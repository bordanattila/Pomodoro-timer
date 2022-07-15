from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_label, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work = WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long)
        title.config(text="Long Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short)
        title.config(text="Short Break", fg=PINK)

    else:
        count_down(work)
        title.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_label, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:

        if reps % 2 != 0:
            check_label = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18, "bold"))
            check_label.grid(column=1, row=3)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(104, 112, image=tomato)
timer_label = canvas.create_text(104, 130, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title = Label(text="Timer", font=(FONT_NAME, 42, "bold"), fg=GREEN, bg=YELLOW)
title.grid(column=1, row=0)
start_button = Button(text="Start", font=(FONT_NAME, 12, "bold"), command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", font=(FONT_NAME, 12, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)
check_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18, "bold"))
check_label.grid(column=1, row=3)

window.mainloop()

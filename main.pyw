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
    # turn off timer (for clarity, check out global variable timer and see if set in count_down)
    window.after_cancel(timer)
    # timer text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # set timer label to "timer"
    timer_label.config(text="Timer", fg=GREEN)
    # reset check marks
    check_marks["text"] = ""
    # reset reps
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    print(reps)

    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60

    # if it's 1st/3rd/5th/7th rep then work
    if reps % 2 == 1:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    # if it's 2nd/4th/6th rep
    elif reps % 2 == 0:
        # if it's the 8th rep
        if reps % 8 == 0:
            count_down(long_break_sec)
            timer_label.config(text="Break", fg=RED)
        else:
            count_down(short_break_sec)
            timer_label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps

    count_min = math.floor(count/60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # print(count)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif reps <= 8:
        if reps % 2 == 0:
            check_marks["text"] += "✓"
        if reps < 8:
            start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas()
canvas.config(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, justify="center", font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", bg=PINK, font=(FONT_NAME, 10, "normal"))
start_button.grid(column=0, row=2)
start_button["command"] = start_timer

reset_button = Button(text="Reset", bg=PINK, font=(FONT_NAME, 10, "normal"), command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 14, "normal"))
check_marks.grid(column=1, row=3)



window.mainloop()

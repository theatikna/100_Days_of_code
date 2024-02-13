import tkinter as tk
from tkinter import messagebox

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Variables
REPS = 0
MARKS = ""
TIMER = None

# Functions
def reset_timer():
    global REPS, MARKS
    canvas.after_cancel(TIMER)
    REPS = 0
    MARKS = ""
    canvas.itemconfig(timer_text_canvas, text="00:00")
    timer_label.config(text="TIMER")
    tick_label.config(text="")

def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        timer_label.config(text="BREAK", foreground=GREEN)
        count_down(LONG_BREAK_MIN)
        messagebox.showinfo("Timer Notification", "Long break is over. Get ready to work again!")
    elif REPS % 2 == 0:
        timer_label.config(text="BREAK", foreground=PINK)
        count_down(SHORT_BREAK_MIN)
        messagebox.showinfo("Timer Notification", "Short break is over. Get back to work!")
    else:
        timer_label.config(text="WORK", foreground=RED)
        count_down(WORK_MIN)

def count_down(count):
    global MARKS
    count_mins = count // 60
    count_secs = count % 60
    canvas.itemconfig(timer_text_canvas, text=f"{count_mins:02d}:{count_secs:02d}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count-1)
    else:
        start_timer()
        MARKS = ["✓" for _ in range(REPS // 2)]
        tick_label.config(text=MARKS)

# UI Setup
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=100, background=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(row=1, column=1)

timer_label = tk.Label(text="TIMER", background=YELLOW, font=(FONT_NAME, "30", "bold"), fg=RED)
timer_label.grid(row=0, column=1)

img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text_canvas = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, "35", "bold"), fill="white")

start_button = tk.Button(text="START", highlightthickness=0, command=start_timer)
start_button.grid(row=3, column=0)

stop_button = tk.Button(text="RESTART", highlightthickness=0, command=reset_timer)
stop_button.grid(row=3, column=2)

tick_label = tk.Label(text="", background=YELLOW, foreground=GREEN, font=(FONT_NAME, "15"))
tick_label.grid(row=3, column=1)

window.mainloop()

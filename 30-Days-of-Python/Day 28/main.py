from tkinter import *
import math
import winsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

is_paused = False
is_running = False
current_count = 0


# ---------------------------- RESET ------------------------------- #
def reset_timer():
    global reps, is_paused, is_running, timer

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")

    reps = 0
    is_paused = False
    is_running = False


# ---------------------------- PAUSE ------------------------------- #
def pause_timer():
    global is_paused, is_running, timer

    window.after_cancel(timer)
    is_paused = True
    is_running = False


# ---------------------------- SOUND ------------------------------- #
def play_sound():
    try:
        winsound.Beep(1000, 400)
    except:
        pass


# ---------------------------- START / RESUME ------------------------------- #
def start_timer():
    global reps, is_running, is_paused

    is_running = True

    # resume
    if is_paused:
        is_paused = False
        count_down(current_count)
        return

    # new session
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)

    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)

    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN ------------------------------- #
def count_down(count):
    global timer, current_count, is_running

    current_count = count

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0 and is_running:
        timer = window.after(1000, count_down, count - 1)

    elif count == 0:
        play_sound()

        # ❗ مهم: نوقف التشغيل التلقائي المباشر
        # بدل ما نعمل start_timer فورًا
        is_running = False

        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

        title_label.config(text="Done", fg=GREEN)


# ---------------------------- UI ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file=r"Day 28\tomato.png")

canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)

canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

pause_button = Button(text="Pause", command=pause_timer)
pause_button.grid(column=1, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()

from tkinter import *
from random import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
BACKGROUND_COLOR_ALT = "#DF7861"
TITLE_FONT = ("Arial", 30, "italic")
FONT = ("Arial", 60, "bold")
current_card = {}
learning = {}

try:
    data = pandas.read_csv("data/es_words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/es_words_1.csv")
    learning = original_data.to_dict(orient="records")
else:
    learning = data.to_dict(orient="records")


# FLASHCARD FUNCTIONALITY
def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(learning)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_image, image=card_back)


def remove_card():
    learning.remove(current_card)
    # print(len(learning))
    data = pandas.DataFrame(learning)
    data.to_csv("data/es_words_to_learn.csv", index=False)
    new_card()


# USER INTERFACE
window = Tk()
window.title("LERNT")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

# Get images from the Images folder
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")


# Displays flashcard
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=TITLE_FONT)
card_word = canvas.create_text(400, 263, text="", font=FONT)
canvas.grid(row=0, column=1, columnspan=2)

# Display buttons
wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_card)
wrong_button.grid(row=1, column=1)
right_button = Button(image=right_img, highlightthickness=0, command=remove_card)
right_button.grid(row=1, column=2)

new_card()
window.mainloop()

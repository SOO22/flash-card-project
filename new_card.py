from tkinter import *
import pandas
from random import *
from screen import *

BACKGROUND_COLOR = "#B1DDC6"
BACKGROUND_COLOR_ALT = "#DF7861"
TITLE_FONT = ("Arial", 30, "italic")
FONT = ("Arial", 60, "bold")
current_card = {}
learning = {}


class NewCard:
    def __init__(self):
        global current_card, flip_timer
        self.window.after_cancel(flip_timer)
        current_card = choice(learning)
        canvas.itemconfig(card_title, text="Spanish", fill="black")
        canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
        canvas.itemconfig(card_image, image=card_front)
        flip_timer = window.after(3000, func=flip_card)

    def flip_card(self):
        canvas.itemconfig(card_word, text=current_card["English"], fill="white")
        canvas.itemconfig(card_title, text="English", fill="white")
        canvas.itemconfig(card_image, image=card_back)

    def remove_card(self):
        learning.remove(current_card)
        # print(len(learning))
        data = pandas.DataFrame(learning)
        data.to_csv("data/es_words_to_learn.csv", index=False)
        new_card()

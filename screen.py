from tkinter import *
from new_card import *

BACKGROUND_COLOR = "#B1DDC6"
BACKGROUND_COLOR_ALT = "#DF7861"
TITLE_FONT = ("Arial", 30, "italic")
FONT = ("Arial", 60, "bold")
current_card = {}
learning = {}


class Screen:

    def __init__(self):
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
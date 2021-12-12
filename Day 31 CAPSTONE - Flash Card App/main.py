from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
current_word = {}

try:
    df = pd.read_csv('data/words_to_learn.csv')
    data = df.to_dict(orient="records")
except FileNotFoundError:
    df = pd.read_csv('data/french_words.csv')
    data = df.to_dict(orient="records")


def generate_word():
    global current_word
    current_word = random.choice(data)
    canvas.itemconfig(word, text=current_word["French"])
    window.after(9000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_pic)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_word["English"], fill="white")


def is_known():
    data.remove(current_word)
    generate_word()
    remaining_words = pd.DataFrame(data)
    remaining_words.to_csv("data/words_to_learn.csv", index=False)

# Window
window = Tk()
window.title("Flash card app")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526)
front_pic = PhotoImage(file="images/card_front.png")
back_pic = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_pic)
language = canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT)
word = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, columns=1, columnspan=2)

generate_word()

# Button
wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_word)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_image, highlightthickness=0, command=lambda: [generate_word(), is_known()])
right_button.grid(row=1, column=1)

window.mainloop()

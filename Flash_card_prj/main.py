from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
word_list = {}
current_word = {}



try:
    data =pandas.read_csv(r"data/word_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv(r"data/french_words.csv")
    word_list = original_data.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")


def nextcard():
    global flip_timmer,current_word
    window.after_cancel(flip_timmer)
    current_word = random.choice(word_list)
    canvas.itemconfig(card_Title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_word["French"],fill="black")
    canvas.itemconfig(card_bg_image,image=card_front_image)
    flip_timmer = window.after(3000,func=flipcard)


def flipcard(): 
    canvas.itemconfig(card_Title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_word["English"],fill="white")
    canvas.itemconfig(card_bg_image,image=card_back_image)

def isKnown():
    word_list.remove(current_word)
    data = pandas.DataFrame(word_list)
    data.to_csv("data/word_to_learn.csv",index=False)
    nextcard()

window = Tk()
window.title("Cardy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timmer = window.after(3000,func=flipcard)

canvas = Canvas(width=800,height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_bg_image = canvas.create_image(400,263,image=card_front_image)
card_Title = canvas.create_text(400,150,text="Title",font=("ariel",40,"italic"))
card_word = canvas.create_text(400,363,text="Word",font=("ariel",60,"italic"))

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0,command=nextcard)
unknown_button.grid(row=1,column=0)

tick_image =PhotoImage(file="images/right.png")
right_button = Button(image=tick_image,highlightthickness=0,command=isKnown)
right_button.grid(row=1,column=1)

nextcard()

window.mainloop()


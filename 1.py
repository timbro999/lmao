from tkinter import *
from sentencegen import sentence_list
from tkinter import ttk
import random

import time
words = []

def start_game():
    game = Tk()
    game.geometry("800x800")
    game.title(sentencegen.sentence_list[0])















root = Tk()
root.geometry("500x120")
root.title("Typer Game")

header_text = StringVar()
header_text.set("Welcome to the typer racer game, press start to play")

header_label = ttk.Label(root, textvariable=header_text, wraplength=300)
header_label.grid(row=0, column=0, columnspan=2, padx=120, pady=10)
header_label.config(font=("Courier", 11))


play_button = ttk.Button(root, text="Play", command=start_game)
play_button.grid(row=50, column=0, pady=20, columnspan = 2 )



















root.mainloop()
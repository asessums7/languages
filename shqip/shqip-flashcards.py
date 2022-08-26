### SHQIP-E
### Alfabeti Shqip Language Learning Flaschard Set
# Developed by Alex Sessums
# August 2022

# %%
# Import Libraries
import pandas as pd
from tkinter import *
from random import randint
from art import tprint
import time

# print logo
print ("\n\n\n" + '\033[94m')
tprint('SHQIP-E')

# welcome message
print ('\033[94m' + "Përshëndetje!\n\n'SHQIP-E' is a little Python program that will help you learn Albanian words and phrases.\nTo begin learning, select your preferences below.\n\nType", '\033[1m', "exit" + '\033[0m' + '\033[94m'  + "  to exit\n\n")
print ("---------------------------------")
print ("\n")

# %%
## User input 1, requesting which flashcard set they would like to study.
content = input('\033[94m' + 'First, what would you like to study today? Select from one of the options below: \n \n    1. Numbers\n    2. Colors\n    3. Food\n    4. Household\n    5. Clothing\n    6. Family\n    7. Weather\n    8. Transport\n    *** For a flashcard set of all words, type "dictionary" *** \n' + '\033[95m')
print(f'You selected {content}...')
time.sleep(.15)

## User input 2, requesting word order. i.e - English to Albanian or Albanian to English.
word_order = input('\033[94m' + '\nHow would you like to learn?\n' + '\n     Option 1: Type 0 for English to Albanian\n     Option 2: Type 1 for Albanian to English\n' + '\033[95m')
# print(f'You selected if({word_order}) == 1': print('English to Albanian') else print('Albanian to English'))
time.sleep(.15)

# Flashcard Formatting
root = Tk()
root.title("Alfabeti Shqip Flashcards")
root.geometry("800x500")

# %%
# Read in data from text files
df = pd.read_csv(f'./data/{content}.txt', sep = ",", index_col=1)
df = df.reset_index()
# df.columns = ["English", "Shqip", "Unnamed: 2"]
df.drop(['Unnamed: 2'], axis=1, inplace=True)
values = df.values
words = values.tolist()

# %%
# Length of Words List
count = len(words)

# %%
# Define a function to create a random word
def next():
    global hinter, hint_count
    '''Clear the screen'''
    answer_label.config(text="")
    my_entry.delete(0, END)
    hint_label.config(text = "")
    # Reset hint
    hinter = ""
    hint_count = 0
    
    '''Create a global variable as a random selection'''
    global random_word
    random_word = randint(0, count-1)
    '''Update the label with a Shqip word'''
    shqip_word.config(text=words[random_word][0])
    
# %%
# Define a function to return the answer
def answer():
    if my_entry.get().capitalize() == words[random_word][1]:
        answer_label.config(text=f"Correct! {words[random_word][0]} is {words[random_word][1]}")
    else:
        answer_label.config(text=f"Incorrect! {words[random_word][0]} is not {my_entry.get().capitalize()}")

# %%
# Define a function to give a hint
hinter = ""
hint_count = 0

def hint():
    global hint_count
    global hinter

    if hint_count < len(words[random_word][1]):
        hinter = hinter + words[random_word][1][hint_count]
        hint_label.config(text = hinter)
        hint_count += 1

# %%
# Get a count of the word list
shqip_word = Label(root, text="", font=("TW Cen MT", 50))
shqip_word.pack(pady=50)

answer_label = Label(root, text="")
answer_label.pack(pady=20)

info = StringVar()
my_entry = Entry(root, textvariable=info, font=("TW Cen MT", 35))
my_entry.pack(pady=20)
my_entry.get()

# str(EntryAnswer)
# EntryAnswer.pack(pady=20)

# %%
# Create Answer, Next & Hint Buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

answer_button = Button(button_frame, text="Answer", command=answer)
answer_button.grid(row=0, column=0, padx=20)

hint_button = Button(button_frame, text="Hint", command=hint)
hint_button.grid(row=0, column=1)

next_button = Button(button_frame, text="Next", command=next)
next_button.grid(row=0, column=2, padx=20)

# Create Hint Label
hint_label = Label(root, text="")
hint_label.pack(pady=40)

# %%
# Run next function when program starts
next()

# %%
# Loop through the program to keep it running
root.mainloop()

# Resources
# https://www.youtube.com/watch?v=Pd3XoLSQ5wg
# https://www.youtube.com/watch?v=t51bT7WbeCM
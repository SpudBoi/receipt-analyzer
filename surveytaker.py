"""
Survey Taker

This program will utilize the Selenium WebDriver to automate the process of
filling the survey. We will have preset review choices which the user may choose
from. This will then output the validation code in which the user will use to
redeem the voucher.
"""

from selenium import webdriver
import tkinter as tk
import os

path = os.getcwd()

colors = ['#fefefe', '#ff8989']

def character_limit(entry_text):
    if len(entry_text.get()) > 5:
        entry_text.set(entry_text.get()[:-1])

def special_character_limit(entry_text):
    if len(entry_text.get()) > 1:
        entry_text.set(entry_text.get()[:-1])

def user_interface():

    window = tk.Tk()
    window.resizable(False,False)

    #configuring main window
    window.title("McDonald's Survey Bot")
    window.geometry('400x500')
    window.configure(bg = colors[0])

    bg = tk.PhotoImage(file = path + "\\visual_assets\\background.png")
    tk.Label(window, image = bg, bg = colors[0]).place(x = -5, y = -5)

    title = tk.PhotoImage(file = path + "\\visual_assets\\title.png")
    tk.Label(window, image = title, bg = colors[1]).place(x = 25, y =10)

    chan = tk.PhotoImage(file = path + "\\visual_assets\\waitress.png")
    tk.Label(window, image = chan, bg = colors[0]).place(x=0,y=150)

    entryx = 60
    entryy = 100

    entry_text1 = tk.StringVar()
    entry1 = tk.Entry(window, bg = colors[0], textvariable = entry_text1)
    entry1.place(height = 20, width = 40, x = entryx, y = entryy)

    entry_text2 = tk.StringVar()
    entry2 = tk.Entry(window, bg = colors[0], textvariable = entry_text2)
    entry2.place(height = 20, width = 40, x = entryx + 50, y = entryy)

    entry_text3 = tk.StringVar()
    entry3 = tk.Entry(window, bg = colors[0], textvariable = entry_text3)
    entry3.place(height = 20, width = 40, x = entryx + 100, y = entryy)

    entry_text4 = tk.StringVar()
    entry4 = tk.Entry(window, bg = colors[0], textvariable = entry_text4)
    entry4.place(height = 20, width = 40, x = entryx + 150, y = entryy)

    entry_text5 = tk.StringVar()
    entry5 = tk.Entry(window, bg = colors[0], textvariable = entry_text5)
    entry5.place(height = 20, width = 40, x = entryx + 200, y = entryy)

    entry_text6 = tk.StringVar()
    entry6 = tk.Entry(window, bg = colors[0], textvariable = entry_text6)
    entry6.place(height = 20, width = 20, x = entryx + 250, y = entryy)

    entry_text1.trace("w", lambda *args: character_limit(entry_text1))
    entry_text2.trace("w", lambda *args: character_limit(entry_text2))
    entry_text3.trace("w", lambda *args: character_limit(entry_text3))
    entry_text4.trace("w", lambda *args: character_limit(entry_text4))
    entry_text5.trace("w", lambda *args: character_limit(entry_text5))
    entry_text6.trace("w", lambda *args: special_character_limit(entry_text6))

    window.mainloop()


######################3333333333333333333333333333333

user_interface()

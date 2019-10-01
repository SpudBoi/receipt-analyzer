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

colors = ['#fff6de']

def user_interface():

    window = tk.Tk()
    window.resizable(False,False)

    #configuring main window
    window.title("McDonald's Survey Bot")
    window.geometry('300x400')
    window.configure(bg = colors[0])

    chan = tk.PhotoImage(file = path + "\\visual_assets\\mcdonalds-chan.png")
    tk.Label(window, image = chan, bg = colors[0]).place(x=42,y=100)

    window.mainloop()


######################3333333333333333333333333333333

user_interface()

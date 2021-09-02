from tkinter import *


def __init__(self):

    window = Tk()
    window.title("Loan Calculator")

    Label(window, text = "Annual Interest Rate").grid(row=1, column=1, sticky= W)

    Label(window, text = "Number of Years").grid(row=2, column=1, sticky= W)

    Label(window, text = "Loan Amount").grid(row=3, column=1, sticky= W)

    Label(window, text = "Monthly Payment").grid(row=4, column=1, sticky= W)

    Label(window, text = "Total Payment").grid(row=5, column=1, sticky= W)
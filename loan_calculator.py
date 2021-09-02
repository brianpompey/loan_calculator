from tkinter import *


def __init__(self):

    window = Tk()
    window.title("Loan Calculator")

    Label(window, text = "Annual Interest Rate").grid(row=1, column=1, sticky= W)

    Label(window, text = "Number of Years").grid(row=2, column=1, sticky= W)

    Label(window, text = "Loan Amount").grid(row=3, column=1, sticky= W)

    Label(window, text = "Monthly Payment").grid(row=4, column=1, sticky= W)

    Label(window, text = "Total Payment").grid(row=5, column=1, sticky= W)


    self.annualInterestRateVar = StringVar()
    Entry(window, textvariable= self.annualInterestRateVar, justify= RIGHT).grid(row=1, column=2)

    self.numberOfYearsVar = StringVar()
    Entry(window, textvariable= self.numberOfYearsVar, justify= RIGHT).grid(row=2, column=2)

    self.loanAmmountVar = StringVar()
    Entry(window, textvariable= self.loanAmmountVar, justify= RIGHT).grid(row=3, column=2)

    self.monthlyPaymentVar = StringVar()
    

    self.totalPaymentVar = StringVar()
    Entry(window, textvariable= self.annualInterestRateVar, justify= RIGHT).grid(row=1, column=2)
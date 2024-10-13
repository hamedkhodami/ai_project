from tkinter import *
from customtkinter import *
from pl import Predict
import pyodbc


if __name__=="__main__":
    screen=CTk()
    screen.geometry("%dx%d+%d+%d" % (900,700,470,50))
    Pageme = Predict.App(screen)
    screen.title("خوش آمدید")
    screen.iconbitmap("iconapp.ico")
    screen.resizable(False,False)
    set_appearance_mode("dark")
    screen.mainloop()


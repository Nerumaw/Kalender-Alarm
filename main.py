import datetime
import calendar
from tkinter import *

window = Tk()
window.title("Kalender Anwendung")

width = 600
height = 400
x = 500
y = 200

window.geometry(f"{width}x{height}+{x}+{y}")

class SetCalender():
    def __init__(self):
        self.current_year = datetime.date.today().year() #Aktuelles Jahr bestimmen
        self.m1 = datetime.date.today().month() #Aktueller Monat
        self.m2 = self.m1 + 1 #Nächster Monat; benötigt für das Modul


window.mainloop()
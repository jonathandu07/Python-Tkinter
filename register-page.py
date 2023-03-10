from tkinter import *

from xlwings.pro.reports.filters import height

window = Tk()
height = 650
width = 1240
x (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 4) - (height // 4)
window.geometry('{}x+{}+{}+{}'.format(width, height, x, y))

window.configure(bg='#525561')

#================================================================ Background Image ================================================================

from tkinter import *


#window size and Placment

AccountSystem = Tk()
AccountSystem.rowconfigure(0, weight=1)
AccountSystem.columnconfigure(0, weight=1)
height = 650
width = 1240
x = (AccountSystem.winfo_screenwidth() //2) - (width // 2)
y = (AccountSystem.winfo_screenheight() //4) - (height // 4)
AccountSystem.geometry('{}x{}+{}+{}'.format(width, height, x ,y))

AccountSystem.title('Account System')

# Navigating trough windows
sign_in =Frame(AccountSystem)
singn_up =Frame(AccountSystem)

for frame in (sign_in, singn_up):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkkraise()

show_frame(singn_up)

#=======================================================================================================================================================
#================================================================ Sign page start Here =================================================================
#=======================================================================================================================================================


AccountSystem.resizable(False, False)
AccountSystem.mainloop()
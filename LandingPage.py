from tkinter import *


window = Tk()

window.geometry("800x550")
window.configure(bg="#FFFFFF")

welcome_label = Label(text='HOME PAGE', bg='#2F6C6D', font=("Trebuchet Ms", 15, "bold"), fg='#FFFFFF')
welcome_label.place(x=160, y=70)

window.mainloop()

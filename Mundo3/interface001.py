from tkinter import *

root = Tk()

root.title("hello World")
root.geometry('500x600')

Entry().grid(row=0,column=0)
Entry(show='*').grid(row=10,column=0)
Button(text='Enviar').grid(row=30,column=0)



root.mainloop()
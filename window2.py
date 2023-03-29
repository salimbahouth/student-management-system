import smtplib
from tkinter import *
from tkinter import messagebox



def newWindow():
    window2 = Tk()
    window2.title("Cmail")
    window2.geometry('350x350')
    window2.configure(bg='#333333')

    options_frame = Frame(window2, bg='#c3c3c3').pack(side=LEFT)
    home_btn = Button(options_frame, text='Home').place(x=10, y=50)

    options_frame.pack_propagate(False)
    options_frame.configure(width=100, height=400)

    main_frame = Frame(window2)
    main_frame.pack(side=LEFT)
    main_frame.pack_propagate(False)
    main_frame.configure(width=500, height=400)



    window2.mainloop()
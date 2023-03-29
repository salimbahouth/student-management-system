import tkinter
from tkinter import *
from tkinter import messagebox
from window2 import *
from PIL import ImageTk

window1 = Tk()
window1.title("Login")
window1.geometry('1250x700+0+0')
window1.configure(bg='#333333')

backgroundImage = ImageTk.PhotoImage(file='bg.jpg')
bglabel = Label(window1, image=backgroundImage)
bglabel.place(x=0, y=0)


def login():
    if username_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror(title='Error', message='Fields cannot be empty!')
    elif username_entry.get() == "salim" and password_entry.get() == "123":
        messagebox.showinfo(title='Success', message='Welcome')
        window1.destroy()
        import sms
    else:
        messagebox.showerror(title='Error', message='Please insert correct credentials')








def exit():
    msg_b = messagebox.askquestion(title='Exit', message='Sure you want to exit?')
    if msg_b == 'yes':
        window1.destroy()


loginframe = Frame(window1, bg='white')
loginframe.place(x=400, y=150)

logoimage = PhotoImage(file='logo.png')
logolabel = Label(loginframe, image=logoimage)
logolabel.grid(row=0, column=0, columnspan=2, pady=10)

usernameimage = PhotoImage(file='user.png')
username_label = Label(loginframe, image=usernameimage, text='Username', compound=LEFT,
                      bg='white', font=('Times new roman',20, 'bold'))
username_label.grid(row=1, column=0, pady=10, padx=15)
username_entry = Entry(loginframe, font=('Times new roman',17))
username_entry.grid(row=1, column=1, pady=10, padx=15)

passwordimage = PhotoImage(file='password.png')
password_label = Label(loginframe, image=passwordimage, text='Password', compound=LEFT,
                      bg='white', font=('Times new roman',20, 'bold'))
password_label.grid(row=2, column=0, pady=10, padx=15)
password_entry = Entry(loginframe, font=('Times new roman',17), show='*')
password_entry.grid(row=2, column=1, pady=10, padx=15)

login_btn = Button(loginframe, text='Login', font=('Times new roman',14,'bold'),width=20,
                   fg='white', bg='cornflowerblue', activebackground='cornflowerblue',
                   activeforeground='white', command=login)
login_btn.grid(row=3, column=1)



# frame = Frame(window1, bg='#333333')
#
# login_label = Label(window1, text="Login", bg='#333333', fg='#ffffff', font=('Arial', 18))
# login_label.grid(row=0, column=0, pady=20, columnspan=2, sticky='news')
#
# username_label = Label(window1,text="Username", bg='#333333', fg='#ffffff')
# username_label.grid(row=1, column=0)
# username_entry = Entry(window1)
# username_entry.grid(row=1, column=1, pady=5)
#
#
# pass_label = Label(window1,text="Password", bg='#333333', fg='#ffffff')
# pass_label.grid(row=2, column=0)
# password_entry = Entry(window1, show="*")
# password_entry.grid(row=2, column=1)
#
# login_btn = Button(window1, text="Login", command=login)
# login_btn.grid(row=3, column=0, columnspan=2, pady=10)
# close_btn = Button(window1, text="Exit", command=exit)
# close_btn.grid(row=3, column=2, columnspan=4, pady=10)


# frame.pack()



window1.mainloop()
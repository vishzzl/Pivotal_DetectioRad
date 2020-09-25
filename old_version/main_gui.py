from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import Register
import sqlite3
import time

with sqlite3.connect('database.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL,password TEXT NOT NULL,name TEXT NOT NULL, age INT NOT NULL,PH NO INT NOT NULL,D_ID TEXT NOT NULL PRIMARY KEY );')
db.commit()
db.close()


class splalsh_screen:
    global start_root

    start_root=Tk()
    start_root.config(bg="black")
    start_root.title("DetectioRad")
    Logo=Image.open(r"C:\Users\yovis\Documents\FIles_projects\Internships\Pivotal_Teleradiology\Covid-model\DetectioRad\LOGO_v1.png")
    w_x=Logo.size[0]
    w_y=Logo.size[1]
    start_root.minsize(w_x,w_y)
    start_root.resizable(0,0)
    Logo_in=ImageTk.PhotoImage(Logo)
    Logo_label=Label(start_root,image=Logo_in,padx=100,pady=100)
    Logo_label.image=Logo_in
    Logo_label.place(x=0,y=0)
    loading_bar=ttk.Progressbar(start_root,orient=HORIZONTAL,length=w_x-50,mode='determinate')
    loading_bar.config(maximum=100, value=25)
    loading_bar.place(x=25,y=w_y-30)
    loading_lable=Label(start_root,text=loading_bar['value'])
    loading_lable.place(x=(w_x-50)//2,y=w_y-30)
    loading_bar['value']=0
    start_root.update()
    while loading_bar['value']<100:
        loading_bar['value']+=10
        loading_lable.config(text=loading_bar['value'])
        start_root.update()
        time.sleep(0.5)

def mainroot():
    def submit():
        with sqlite3.connect('database.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(login_id.get()),(password.get())])
        result = c.fetchall()
        if result:
            print("hello")
        else:
            messagebox.showerror('Oops!','Username Not Found.')

    def signup_window():
        Register.vp_start_gui()

    global login_id, password
    root = Tk()
    root.geometry("400x500")
    root.resizable(0,0)
    root.title("Login")
    login_id=Entry(root,width=40)
    login_id.grid(row=3,column=1,pady=25)
    password=Entry(root,width=40)
    password.grid(row=4,column=1,pady=25)
    login_id_label=Label(root,text="Login ID")
    login_id_label.grid(row=3,column=0,sticky=E,padx=15)

    password_label=Label(root,text="password")
    password_label.grid(row=4,column=0,sticky=E,padx=15)

    login_btn=Button(root,text="Login",command=submit)
    login_btn.grid(row=5,column=1,columnspan=2,pady=20,ipadx=100)

    signup_btn=Button(root,text="register",command=signup_window)
    signup_btn.grid(row=6,column=1,columnspan=2,pady=10,ipadx=100)




    # After this call the main window here


def call_mainroot():
	start_root.destroy()
	mainroot()

start_root.after(3000,call_mainroot)         #TimeOfSplashScreen
mainloop()

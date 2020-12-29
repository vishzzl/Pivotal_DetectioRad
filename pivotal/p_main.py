
import sqlite3
from tkinter import *
import os
from tkinter import messagebox
from tkinter import ttk
#import Register 
from PIL import Image, ImageTk
import time
import sys
import pivotal_form








conn = sqlite3.connect("_pivotal.db")

s1=conn.cursor()

s1.execute('''CREATE TABLE IF NOT  EXISTS   doctor_records(
                reg_id text(255) NOT NULL,
                name  text NOT NULL,
                age  string NOT NULL,
                phone_no integer(10) NOT NULL,
                password text NOT NULL,
                PRIMARY KEY(reg_id)
                )''')


conn.commit()

def register():
   
    top.destroy()
    global register_screen
    register_screen =Tk()
    #register_screen=Toplevel(top)
    """register_screen.title("register")
    register_screen.minsize(w_x,w_y)
    register_screen.resizable(0,0)
    Button(register_screen, text="Back", width=5, height=1, bg="blue", command = back_command).place(x=5, y=5)"""

    width_value=register_screen.winfo_screenwidth()
    height_value=register_screen.winfo_screenheight()
    register_screen.geometry("%dx%d+0+0"%(width_value,height_value))
    #register_screen.minsize("800x600")
    #register_screen.maxsize(1924, 1055)
    register_screen.resizable(50,50)
    register_screen.title("Register")
    register_screen.configure(background="#002448")
    

    global reg_id
    global registrationId
    global name
    global name_entry
    global age
    global age_entry
    global phone
    global phone_entry
    global password
    global pass_entry
    global comf_pass_entry
    global comfPass
    
    registrationId= StringVar()
    name = StringVar()
    password = StringVar()
    comfPass = StringVar()
    age=StringVar()
    phone=StringVar()
    
    


    '''This class configures and populates the toplevel window.
     top is the toplevel containing window.'''
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
    font11 = "-family {Segoe UI Emoji} -size 11 -weight bold"
    font12 = "-family {Sitka Heading} -size 13 -weight bold"
    font9 = "-family {Segoe UI Black} -size 14 -weight bold"
   
   
    
   
    Canvas1 = Canvas(register_screen)
    Canvas1.place(relx=0.072, rely=0.051, relheight=0.804 , relwidth=0.847)
    Canvas1.configure(background="#808080")
    Canvas1.configure(borderwidth="2")
    Canvas1.configure(highlightbackground="#d9d9d9")
    Canvas1.configure(highlightcolor="#646464646464")
    Canvas1.configure(insertbackground="black")
    Canvas1.configure(relief="raised")
    Canvas1.configure(selectbackground="#808080")
    Canvas1.configure(selectforeground="white")
   
    Label1 = Label(Canvas1)
    Label1.place(relx=0.122, rely=0.063, height=40, width=1300)
    Label1.configure(activebackground="#000071")
    Label1.configure(activeforeground="white")
    Label1.configure(activeforeground="#f0f0f0f0f0f0")
    Label1.configure(background="#ababab")
    Label1.configure(borderwidth="5")
    Label1.configure(compound='center')
    Label1.configure(disabledforeground="#000040")
    Label1.configure(font=font9)
    Label1.configure(foreground="#000040")
    Label1.configure(highlightbackground="#d9d9d9")
    Label1.configure(highlightcolor="#808080")
    Label1.configure(text='''Register User''')
  
    reg_lable = Label(Canvas1)
    reg_lable.place(relx=0.171, rely=0.189, height=40, width=184)
    reg_lable.configure(background="#808080")
    reg_lable.configure(borderwidth="5")
    reg_lable.configure(compound='center')
    reg_lable.configure(disabledforeground="#a3a3a3")
    reg_lable.configure(font=font11)
    reg_lable.configure(foreground="#000000")
    reg_lable.configure(text='''Registration no. *''')
  
    reg_id = Entry(Canvas1)
    reg_id.place(relx=0.403, rely=0.189,height=40, relwidth=0.432)
    reg_id.configure(background="#ffffff")
    reg_id.configure(borderwidth="5")
    reg_id.configure(disabledforeground="#a3a3a3")
    reg_id.configure(font="TkFixedFont")
    reg_id.configure(foreground="#000000")
    reg_id.configure(insertbackground="black")
    reg_id.configure(relief="groove")
    reg_id.configure(textvariable=registrationId)
  
    name_lable = Label(Canvas1)
    name_lable.place(relx=0.195, rely=0.294, height=40, width=164)
    name_lable.configure(activebackground="#f9f9f9")
    name_lable.configure(activeforeground="black")
    name_lable.configure(background="#808080")
    name_lable.configure(borderwidth="5")
    name_lable.configure(compound='center')
    name_lable.configure(disabledforeground="#a3a3a3")
    name_lable.configure(font=font11)
    name_lable.configure(foreground="#000000")
    name_lable.configure(highlightbackground="#d9d9d9")
    name_lable.configure(highlightcolor="black")
    name_lable.configure(text='''Name *''')
  
    age_lable = Label(Canvas1)
    age_lable.place(relx=0.195, rely=0.399, height=40, width=164)
    age_lable.configure(activebackground="#f9f9f9")
    age_lable.configure(activeforeground="black")
    age_lable.configure(background="#808080")
    age_lable.configure(borderwidth="5")
    age_lable.configure(compound='center')
    age_lable.configure(disabledforeground="#a3a3a3")
    age_lable.configure(font=font11)
    age_lable.configure(foreground="#000000")
    age_lable.configure(highlightbackground="#d9d9d9")
    age_lable.configure(highlightcolor="black")
    age_lable.configure(text='''Age*''')
  
    phone_lable = Label(Canvas1)
    phone_lable.place(relx=0.183, rely=0.504, height=40, width=174)
    phone_lable.configure(activebackground="#f9f9f9")
    phone_lable.configure(activeforeground="black")
    phone_lable.configure(background="#808080")
    phone_lable.configure(borderwidth="5")
    phone_lable.configure(compound='center')
    phone_lable.configure(disabledforeground="#a3a3a3")
    phone_lable.configure(font="-family {Segoe UI Emoji} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    phone_lable.configure(foreground="#000000")
    phone_lable.configure(highlightbackground="#d9d9d9")
    phone_lable.configure(highlightcolor="black")
    phone_lable.configure(text='''Phone no. *''')
  
    pass_lable = Label(Canvas1)
    pass_lable.place(relx=0.195, rely=0.609, height=40, width=164)
    pass_lable.configure(activebackground="#f9f9f9")
    pass_lable.configure(activeforeground="black")
    pass_lable.configure(background="#808080")
    pass_lable.configure(borderwidth="5")
    pass_lable.configure(compound='center')
    pass_lable.configure(disabledforeground="#a3a3a3")
    pass_lable.configure(font="-family {Segoe UI Emoji} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    pass_lable.configure(foreground="#000000")
    pass_lable.configure(highlightbackground="#d9d9d9")
    pass_lable.configure(highlightcolor="black")
    pass_lable.configure(text='''Password *''')
  
    comf_pass = Label(Canvas1)
    comf_pass.place(relx=0.159, rely=0.714, height=40, width=194)
    comf_pass.configure(activebackground="#f9f9f9")
    comf_pass.configure(activeforeground="black")
    comf_pass.configure(background="#808080")
    comf_pass.configure(borderwidth="5")
    comf_pass.configure(compound='center')
    comf_pass.configure(disabledforeground="#a3a3a3")
    comf_pass.configure(font="-family {Segoe UI Emoji} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
    comf_pass.configure(foreground="#000000")
    comf_pass.configure(highlightbackground="#d9d9d9")
    comf_pass.configure(highlightcolor="black")
    comf_pass.configure(text='''Comfirm Password*''')
  
    name_entry = Entry(Canvas1)
    name_entry.place(relx=0.403, rely=0.294,height=40, relwidth=0.432)
    name_entry.configure(background="#ffffff")
    name_entry.configure(borderwidth="5")
    name_entry.configure(disabledforeground="#a3a3a3")
    name_entry.configure(font="TkFixedFont")
    name_entry.configure(foreground="#000000")
    name_entry.configure(highlightbackground="#d9d9d9")
    name_entry.configure(highlightcolor="black")
    name_entry.configure(insertbackground="black")
    name_entry.configure(relief="groove")
    name_entry.configure(selectbackground="blue")
    name_entry.configure(selectforeground="white")
    name_entry.configure(textvariable=name)
  
    age_entry = Entry(Canvas1)
    age_entry.place(relx=0.403, rely=0.399,height=40, relwidth=0.432)
    age_entry.configure(background="#ffffff")
    age_entry.configure(borderwidth="5")
    age_entry.configure(disabledforeground="#a3a3a3")
    age_entry.configure(font="TkFixedFont")
    age_entry.configure(foreground="#000000")
    age_entry.configure(highlightbackground="#d9d9d9")
    age_entry.configure(highlightcolor="black")
    age_entry.configure(insertbackground="black")
    age_entry.configure(relief="groove")
    age_entry.configure(selectbackground="blue")
    age_entry.configure(selectforeground="white")
    age_entry.configure(textvariable=age)
  
    phone_entry = Entry(Canvas1)
    phone_entry.place(relx=0.403, rely=0.504, height=40, relwidth=0.432)
  
    phone_entry.configure(background="#ffffff")
    phone_entry.configure(borderwidth="5")
    phone_entry.configure(disabledforeground="#a3a3a3")
    phone_entry.configure(font="TkFixedFont")
    phone_entry.configure(foreground="#000000")
    phone_entry.configure(highlightbackground="#d9d9d9")
    phone_entry.configure(highlightcolor="black")
    phone_entry.configure(insertbackground="black")
    phone_entry.configure(relief="groove")
    phone_entry.configure(selectbackground="blue")
    phone_entry.configure(selectforeground="white")
    phone_entry.configure(textvariable=phone)
  
    pass_entry = Entry(Canvas1, show="*")
    pass_entry.place(relx=0.403, rely=0.609,height=40, relwidth=0.432)
    pass_entry.configure(background="#ffffff")
    pass_entry.configure(borderwidth="5")
    pass_entry.configure(disabledforeground="#a3a3a3")
    pass_entry.configure(font="TkFixedFont")
    pass_entry.configure(foreground="#000000")
    pass_entry.configure(highlightbackground="#d9d9d9")
    pass_entry.configure(highlightcolor="black")
    pass_entry.configure(insertbackground="black")
    pass_entry.configure(relief="groove")
    pass_entry.configure(selectbackground="blue")
    pass_entry.configure(selectforeground="white")
    pass_entry.configure(textvariable=password)
  
    comf_pass_entry = Entry(Canvas1,show="*")
    comf_pass_entry.place(relx=0.403, rely=0.714, height=40 ,relwidth=0.432)
    comf_pass_entry.configure(background="#ffffff")
    comf_pass_entry.configure(borderwidth="5")
    comf_pass_entry.configure(disabledforeground="#a3a3a3")
    comf_pass_entry.configure(font="TkFixedFont")
    comf_pass_entry.configure(foreground="#000000")
    comf_pass_entry.configure(highlightbackground="#d9d9d9")
    comf_pass_entry.configure(highlightcolor="black")
    comf_pass_entry.configure(insertbackground="black")
    comf_pass_entry.configure(relief="groove")
    comf_pass_entry.configure(selectbackground="blue")
    comf_pass_entry.configure(selectforeground="white")
    comf_pass_entry.configure(textvariable=comfPass)
  
    Button1 = Button(Canvas1)
    Button1.place(relx=0.370, rely=0.84, height=50, width=225)
    Button1.configure(activebackground="#ffffff")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#1a1a1a")
    Button1.configure(borderwidth="5")
    Button1.configure(command=register_user)
    Button1.configure(compound='center')
    Button1.configure(disabledforeground="#ffffff")
    Button1.configure(font=font12)
    Button1.configure(foreground="#ffffff")
    Button1.configure(highlightbackground="#ffffff")
    Button1.configure(highlightcolor="#ffffff")
    Button1.configure(highlightthickness="5")
    Button1.configure(overrelief="raised")
    Button1.configure(padx="5")
    Button1.configure(pady="5")
    Button1.configure(text='''REGISTER''')

    Button2 = Button(register_screen)
    Button2.place(relx=0.0, rely=0.0, height=33, width=66)
    Button2.configure(activebackground="#ececec")
    Button2.configure(activeforeground="#000000")
    Button2.configure(background="#808080")
    Button2.configure(command=back_command)
    Button2.configure(disabledforeground="#a3a3a3")
    Button2.configure(foreground="#000000")
    Button2.configure(highlightbackground="#d9d9d9")
    Button2.configure(highlightcolor="black")
    Button2.configure(pady="0")
    Button2.configure(relief="flat")
    Button2.configure(text='''Back''')

    register_screen.mainloop()

def register_user():
    RegistrationId=registrationId.get()
    Name=name.get()
    Age=age.get()
    Phone=phone.get()
    Password=password.get()
    ComfPass=comfPass.get()

    
    
    if RegistrationId != "":
        if Name != "" and Name.isdigit() == False:
            if  Age !="" and Age.isdigit() == True:
                if Phone != "" and len(str(Phone)) == 10 and Phone.isdigit() == True:
                    if Password != "" and len(Password) >= 8 and Password == ComfPass:
                        try:
                            s1.execute("""INSERT INTO doctor_records(reg_id , name , age, phone_no , password ) VALUES( ?,?,?,?,?)""",(RegistrationId,Name,Age,Phone,Password))
                            conn.commit()
                            messagebox.showinfo("SUCCESSFULL","registrtion done!")
                            reg_id.delete(0,END)
                            name_entry.delete(0,END)
                            age_entry.delete(0,END)
                            phone_entry.delete(0,END)
                            pass_entry.delete(0,END)
                            comf_pass_entry.delete(0,END)
                            


                        except sqlite3.IntegrityError as err:
                             messagebox.showerror("ERROR","Enter another registration number")
                    
                        
                    else:
                         messagebox.showerror("ERROR","Password does not match")
                else:
                     messagebox.showerror("ERROR","PLEASE! Enter correct phone number")
            else:
                messagebox.showerror("ERROR","PLEASE! Enter Age")
        else:
            messagebox.showerror("ERROR","PLEASE! Enter Name")
    else:
        messagebox.showerror("ERROR","PLEASE! Enter correct registration number")

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()

    global doctor_name
    global doctor_id

    doctor_name = StringVar()
    doctor_id = StringVar()
    
    try:
        sql="select COUNT(name), password from doctor_records where name='"+username1+"'or reg_id='"+username1+"'"
        s1.execute(sql)
        check_pass=s1.fetchone()
    except sqlite3.Error as err:
        messagebox.showerror("ERROR","something went wrong")
    
    if check_pass[0] != 0: 
        if check_pass[1] == password1:
            Label(top, text="Login Success").pack()
            sql= "select name , reg_id from doctor_records where reg_id='"+username1+"'"
            s1.execute(sql)
            a=s1.fetchall()
            doctor_id = a[0][1]
            doctor_name = a[0][0]
            print(doctor_id)
            
            pivotal_form.form_page()
            
            
        else:
            messagebox.showerror( "INCORRECT PASSWORD","PLEASE ENTER CORRECT PASSWORD")
    else:
        messagebox.showerror("WRONG ID.","PLEASE ENTER CORRECT REGISTRATION NO.")

def forgot_pass():
    top.destroy()
    global pass_screen
    pass_screen =Tk()

    
    width_value=pass_screen.winfo_screenwidth()
    height_value=pass_screen.winfo_screenheight()
    pass_screen.geometry("%dx%d+0+0"%(width_value,height_value))
    
    #pass_screen.minsize(w_x,w_y)
    #register_screen.maxsize(1924, 1055)
    pass_screen.resizable(0,0)
    pass_screen.title("Forgot Password")
    pass_screen.configure(background="#002448")
    
    

    global RESISTRATION_ID
    global PASSWORD
    global PASSWORD_ENTRY
    global REGIS_ENTRY
    global CONFIRM_PASS
    global COMF_PASS_ENTRY



    RESISTRATION_ID = StringVar()
    PASSWORD = StringVar()
    CONFIRM_PASS = StringVar()


    '''This class configures and populates the toplevel window.
     top is the toplevel containing window.'''
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
    font11 = "-family {Segoe UI Emoji} -size 11 -weight bold"
    font12 = "-family {Sitka Heading} -size 13 -weight bold"
    font9 = "-family {Segoe UI Black} -size 14 -weight bold"
   
   
    
   
    Canvas1 = Canvas(pass_screen)
    Canvas1.place(relx=0.072, rely=0.051, relheight=0.804 , relwidth=0.847)
    Canvas1.configure(background="#808080")
    Canvas1.configure(borderwidth="2")
    Canvas1.configure(highlightbackground="#d9d9d9")
    Canvas1.configure(highlightcolor="#646464646464")
    Canvas1.configure(insertbackground="black")
    Canvas1.configure(relief="raised")
    Canvas1.configure(selectbackground="#808080")
    Canvas1.configure(selectforeground="white")

    
   
    Label1 = Label(Canvas1)
    Label1.place(relx=0.122, rely=0.063, height=36, width=1300)
    Label1.configure(activebackground="#000071")
    Label1.configure(activeforeground="white")
    Label1.configure(activeforeground="#f0f0f0f0f0f0")
    Label1.configure(background="#ababab")
    Label1.configure(borderwidth="5")
    Label1.configure(compound='center')
    Label1.configure(disabledforeground="#000040")
    Label1.configure(font=font9)
    Label1.configure(foreground="#000040")
    Label1.configure(highlightbackground="#d9d9d9")
    Label1.configure(highlightcolor="#808080")
    Label1.configure(text='''forgot Password''')
  
    label2 = Label(Canvas1)
    label2.place(relx=0.171, rely=0.189, height=40, width=184)
    label2.configure(background="#808080")
    label2.configure(borderwidth="5")
    label2.configure(compound='center')
    label2.configure(disabledforeground="#a3a3a3")
    label2.configure(font=font11)
    label2.configure(foreground="#000000")
    label2.configure(text='''Registration no. *''')
  
    REGIS_ENTRY = Entry(Canvas1)
    REGIS_ENTRY.place(relx=0.403, rely=0.189,height=40, relwidth=0.432)
    REGIS_ENTRY.configure(background="#ffffff")
    REGIS_ENTRY.configure(borderwidth="5")
    REGIS_ENTRY.configure(disabledforeground="#a3a3a3")
    REGIS_ENTRY.configure(font="TkFixedFont")
    REGIS_ENTRY.configure(foreground="#000000")
    REGIS_ENTRY.configure(insertbackground="black")
    REGIS_ENTRY.configure(relief="groove")
    REGIS_ENTRY.configure(textvariable=RESISTRATION_ID)

    
    lable = Label(Canvas1)
    lable.place(relx=0.195, rely=0.294, height=40, width=164)
    lable.configure(activebackground="#f9f9f9")
    lable.configure(activeforeground="black")
    lable.configure(background="#808080")
    lable.configure(borderwidth="5")
    lable.configure(compound='center')
    lable.configure(disabledforeground="#a3a3a3")
    lable.configure(font=font11)
    lable.configure(foreground="#000000")
    lable.configure(highlightbackground="#d9d9d9")
    lable.configure(highlightcolor="black")
    lable.configure(text='''Password *''')
  
    c_lable = Label(Canvas1)
    c_lable.place(relx=0.195, rely=0.399, height=40, width=164)
    c_lable.configure(activebackground="#f9f9f9")
    c_lable.configure(activeforeground="black")
    c_lable.configure(background="#808080")
    c_lable.configure(borderwidth="5")
    c_lable.configure(compound='center')
    c_lable.configure(disabledforeground="#a3a3a3")
    c_lable.configure(font=font11)
    c_lable.configure(foreground="#000000")
    c_lable.configure(highlightbackground="#d9d9d9")
    c_lable.configure(highlightcolor="black")
    c_lable.configure(text='''Confirm Password*''')

    PASSWORD_ENTRY = Entry(Canvas1, show="*")
    PASSWORD_ENTRY.place(relx=0.403, rely=0.294,height=40, relwidth=0.432)
    PASSWORD_ENTRY.configure(background="#ffffff")
    PASSWORD_ENTRY.configure(borderwidth="5")
    PASSWORD_ENTRY.configure(disabledforeground="#a3a3a3")
    PASSWORD_ENTRY.configure(font="TkFixedFont")
    PASSWORD_ENTRY.configure(foreground="#000000")
    PASSWORD_ENTRY.configure(highlightbackground="#d9d9d9")
    PASSWORD_ENTRY.configure(highlightcolor="black")
    PASSWORD_ENTRY.configure(insertbackground="black")
    PASSWORD_ENTRY.configure(relief="groove")
    PASSWORD_ENTRY.configure(selectbackground="blue")
    PASSWORD_ENTRY.configure(selectforeground="white")
    PASSWORD_ENTRY.configure(textvariable=PASSWORD)
  
    COMF_PASS_ENTRY= Entry(Canvas1, show="*")
    COMF_PASS_ENTRY.place(relx=0.403, rely=0.399,height=40, relwidth=0.432)
    COMF_PASS_ENTRY.configure(background="#ffffff")
    COMF_PASS_ENTRY.configure(borderwidth="5")
    COMF_PASS_ENTRY.configure(disabledforeground="#a3a3a3")
    COMF_PASS_ENTRY.configure(font="TkFixedFont")
    COMF_PASS_ENTRY.configure(foreground="#000000")
    COMF_PASS_ENTRY.configure(highlightbackground="#d9d9d9")
    COMF_PASS_ENTRY.configure(highlightcolor="black")
    COMF_PASS_ENTRY.configure(insertbackground="black")
    COMF_PASS_ENTRY.configure(relief="groove")
    COMF_PASS_ENTRY.configure(selectbackground="blue")
    COMF_PASS_ENTRY.configure(selectforeground="white")
    COMF_PASS_ENTRY.configure(textvariable=CONFIRM_PASS)


    
    Button2 = Button(pass_screen)
    Button2.place(relx=0.0, rely=0.0, height=33, width=66)
    Button2.configure(activebackground="#ececec")
    Button2.configure(activeforeground="#000000")
    Button2.configure(background="#808080")
    Button2.configure(command=back_command2)
    Button2.configure(disabledforeground="#a3a3a3")
    Button2.configure(foreground="#000000")
    Button2.configure(highlightbackground="#d9d9d9")
    Button2.configure(highlightcolor="black")
    Button2.configure(pady="0")
    Button2.configure(relief="flat")
    Button2.configure(text='''Back''')

    Button1 = Button(Canvas1)
    Button1.place(relx=0.400, rely=0.676, height=40, width=280)
    Button1.configure(activebackground="#ffffff")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#1a1a1a")
    Button1.configure(borderwidth="5")
    Button1.configure(command=update_pass)
    Button1.configure(compound='center')
    Button1.configure(disabledforeground="#ffffff")
    Button1.configure(font=font12)
    Button1.configure(foreground="#ffffff")
    Button1.configure(highlightbackground="#ffffff")
    Button1.configure(highlightcolor="#ffffff")
    Button1.configure(highlightthickness="5")
    Button1.configure(overrelief="raised")
    Button1.configure(padx="5")
    Button1.configure(pady="5")
    Button1.configure(text='''UPDATE''')

def update_pass():
    old_id=RESISTRATION_ID.get()
    new_pass=PASSWORD.get()
    new_c_pass=CONFIRM_PASS.get()

    try:
        sql="select count(reg_id) from doctor_records where reg_id='"+old_id+"'"
        s1.execute(sql)
        count=s1.fetchone()
        print(count)
    except sqlite3.Error as err:
        messagebox.showerror("ERROR","something went wrong")

    
    if old_id != "" and count[0] > 0:
        if new_pass != "" and len(new_pass) >= 8 and new_pass == new_c_pass:
            try:
                sql="UPDATE doctor_records SET password = '"+new_pass+"' WHERE reg_id ='"+old_id+"'"
                s1.execute(sql)
                conn.commit()
                messagebox.showinfo("SUCCESSFULL","password updated!")
                REGIS_ENTRY.delete(0,END)
                PASSWORD_ENTRY.delete(0,END)
                COMF_PASS_ENTRY.delete(0,END)

                
                
            except sqlite3.Error as err:
                messagebox.showerror("ERROR","something went wrong")
        else:
            messagebox.showerror("ERROR","Password did not match")
    else:
        messagebox.showerror("ERROR","enter correct registration number")

def back_command():
   
    register_screen.destroy()
    main_account_screen()

def back_command2():
    pass_screen.destroy()
    main_account_screen()


def main_account_screen():
    '''This class configures and populates the toplevel window.
               top is the toplevel containing window.'''
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92
    
    
    global top
   
    
    global username_verify
    global password_verify

    
    
    top=Tk()
    #top.minsize(w_x,w_y)
    width_value=top.winfo_screenwidth()
    height_value=top.winfo_screenheight()
    top.geometry("%dx%d+0+0"%(width_value,height_value))
    
    
    #top.maxsize(1924, 1055)
    top.resizable(0,0)
    top.title("Login page")
    top.configure(background="#002448")
    top.configure(highlightbackground="#d9d9d9")
    top.configure(highlightcolor="black")

    username_verify = StringVar()
    password_verify = StringVar()

    canvas1=Canvas(top)
    canvas1.place(relx=0.091, rely=0.044, relheight=0.825, relwidth=0.807)
    canvas1.configure(background="#808080")
    canvas1.configure(borderwidth="2")
    canvas1.configure(highlightbackground="#d9d9d9")
    canvas1.configure(highlightcolor="#646464646464")
    canvas1.configure(insertbackground="black")
    canvas1.configure(relief="raised")
    canvas1.configure(selectbackground="#808080")
    canvas1.configure(selectforeground="white")

    Label1=Label(canvas1)
    Label1.place(relx=0.185, rely=0.249, height=40, width=198)
    Label1.configure(activebackground="#808080")
    Label1.configure(activeforeground="#000000")
    Label1.configure(background="#808080")
    Label1.configure(borderwidth="0")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(font="-family Arial -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
    Label1.configure(foreground="#0c0c0c")
    Label1.configure(highlightbackground="#ffffff")
    Label1.configure(highlightcolor="#808080")
    Label1.configure(padx="2")
    Label1.configure(pady="2")
    Label1.configure(text='''Registration no.''')

    Entry1 = Entry(canvas1, textvariable=username_verify)
    Entry1.place(relx=0.39, rely=0.249,height=40, relwidth=0.343)
    Entry1.configure(background="#ffffff")
    Entry1.configure(borderwidth="2")
    Entry1.configure(disabledforeground="#a3a3a3")
    Entry1.configure(font="TkFixedFont")
    Entry1.configure(foreground="#000000")
    Entry1.configure(highlightbackground="#d9d9d9")
    Entry1.configure(highlightcolor="black")
    Entry1.configure(insertbackground="black")
    Entry1.configure(relief="raised")
    Entry1.configure(selectbackground="blue")
    Entry1.configure(selectforeground="white")

    Entry1_5 = Entry(canvas1, show="*")
    Entry1_5.place(relx=0.39, rely=0.391,height=40, relwidth=0.343)
    Entry1_5.configure(background="#ffffff")
    Entry1_5.configure(borderwidth="2")
    Entry1_5.configure(disabledforeground="#a3a3a3")
    Entry1_5.configure(font="TkFixedFont")
    Entry1_5.configure(foreground="#000000")
    Entry1_5.configure(highlightbackground="#d9d9d9")
    Entry1_5.configure(highlightcolor="black")
    Entry1_5.configure(insertbackground="black")
    Entry1_5.configure(relief="raised")
    Entry1_5.configure(selectbackground="blue")
    Entry1_5.configure(selectforeground="white")
    Entry1_5.configure(textvariable=password_verify)

    Label1_6 = Label(canvas1)
    Label1_6.place(relx=0.185, rely=0.391, height=40, width=198)
    Label1_6.configure(activebackground="#808080")
    Label1_6.configure(activeforeground="#000000")
    Label1_6.configure(background="#808080")
   
  
    Label1_6.configure(borderwidth="0")
    Label1_6.configure(disabledforeground="#a3a3a3")
    Label1_6.configure(font="-family Arial -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
    Label1_6.configure(foreground="#0c0c0c")
    Label1_6.configure(highlightbackground="#ffffff")
    Label1_6.configure(highlightcolor="#808080")
    Label1_6.configure(padx="2")
    Label1_6.configure(pady="2")
    Label1_6.configure(text='''Password''')
   
    Label2 = Label(canvas1)
    Label2.place(relx=0.164, rely=0.071, height=40, width=1100)
    Label2.configure(activebackground="#000071")
    Label2.configure(activeforeground="white")
    Label2.configure(activeforeground="black")
    Label2.configure(background="#ababab")
    Label2.configure(borderwidth="5")
    Label2.configure(compound='center')
    Label2.configure(disabledforeground="#000040")
    Label2.configure(font="-family {Segoe UI Black} -size 14 -weight bold -slant roman -underline 0 -overstrike 0")
    Label2.configure(foreground="#000040")
    Label2.configure(highlightbackground="#d9d9d9")
    Label2.configure(highlightcolor="#808080")
    Label2.configure(text='''Login User''')
   
    Button1 = Button(canvas1, command=forgot_pass)
    Button1.place(relx=0.400, rely=0.676, height=40, width=350)
    Button1.configure(activebackground="#ececec")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#808080")
    Button1.configure(borderwidth="0")
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(font="-family {Segoe UI Black} -size 11 -weight bold -slant roman -underline 1 -overstrike 0")
    Button1.configure(foreground="#eb0214")
    Button1.configure(highlightbackground="#d9d9d9")
    Button1.configure(highlightcolor="black")
    Button1.configure(overrelief="flat")
    Button1.configure(pady="0")
    Button1.configure(text='''Forgot Password?''')
   
    Button2 = Button(canvas1,command=login_verify)
    Button2.place(relx=0.240, rely=0.801, height=70, width=400)
    Button2.configure(activebackground="#ffffff")
    Button2.configure(activeforeground="#000000")
    Button2.configure(background="#1a1a1a")
    Button2.configure(borderwidth="5")
    Button2.configure(compound='center')
    Button2.configure(disabledforeground="#ffffff")
    Button2.configure(font="-family {Sitka Heading} -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
    Button2.configure(foreground="#ffffff")
    Button2.configure(highlightbackground="#ffffff")
    Button2.configure(highlightcolor="#ffffff")
    Button2.configure(highlightthickness="5")
    Button2.configure(overrelief="raised")
    Button2.configure(padx="5")
    Button2.configure(pady="5")
    Button2.configure(text='''LOGIN''')
   
    Button2_8 = Button(canvas1,command=register)
    Button2_8.place(relx=0.558, rely=0.801, height=70, width=400)
    Button2_8.configure(activebackground="#ffffff")
    Button2_8.configure(activeforeground="#000000")
    Button2_8.configure(background="#1a1a1a")
    Button2_8.configure(borderwidth="5")
    Button2_8.configure(compound='center')
    Button2_8.configure(disabledforeground="#ffffff")
    Button2_8.configure(font="-family {Sitka Heading} -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
    Button2_8.configure(foreground="#ffffff")
    Button2_8.configure(highlightbackground="#ffffff")
    Button2_8.configure(highlightcolor="#ffffff")
    Button2_8.configure(highlightthickness="5")
    Button2_8.configure(overrelief="raised")
    Button2_8.configure(padx="5")
    Button2_8.configure(pady="5")
    Button2_8.configure(text='''REGISTER''')
  
    
    top.mainloop()       
    
"""def call_mainroot():
    start_gui.start_root.destroy()
    main_account_screen()


start_gui.start_root.after(3000,call_mainroot())"""

       


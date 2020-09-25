import sqlite3
from tkinter import *
import os
from tkinter import messagebox


conn = sqlite3.connect("_pivotal.db")

s1=conn.cursor()

s1.execute("""CREATE TABLE doctor_records(
                reg_id text(255) NOT NULL,
                name  text NOT NULL,
                age  string NOT NULL,
                phone_no integer(10) NOT NULL,
                password text NOT NULL,
                PRIMARY KEY(reg_id)
                )""")


conn.commit()




def register():
   
    main_screen.destroy()
    global register_screen
    register_screen =Tk()
    #register_screen=Toplevel(main_screen)
    register_screen.title("register")
    register_screen.geometry("500x450")
    Button(register_screen, text="Back", width=5, height=1, bg="blue", command = back_command).place(x=5, y=5)
    

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
    
    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()
    
    reg_lable = Label(register_screen, text="REGISTRATION NUMBER *")
    reg_lable.pack()
    reg_id = Entry(register_screen, textvariable=registrationId)
    reg_id.pack()
    
    name_lable = Label(register_screen, text="NAME *")
    name_lable.pack()
    name_entry = Entry(register_screen, textvariable=name)
    name_entry.pack()
    
    age_lable = Label(register_screen, text="AGE *")
    age_lable.pack()
    age_entry = Entry(register_screen, textvariable=age)
    age_entry.pack()

    phone_lable = Label(register_screen, text="PHONE NUMBER *")
    phone_lable.pack()
    phone_entry = Entry(register_screen, textvariable=phone)
    phone_entry.pack()
    
    pass_lable = Label(register_screen, text="PASSWORD *")
    pass_lable.pack()
    pass_entry = Entry(register_screen, textvariable=password, show='*')
    pass_entry.pack()

    comf_pass = Label(register_screen, text="CONFIRM PSSWORD*")
    comf_pass.pack()
    comf_pass_entry = Entry(register_screen, textvariable=comfPass,show="*")
    comf_pass_entry.pack()



    

    Button(register_screen, text="Register", width=15, height=1, bg="blue", command = register_user).pack(pady=20)

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
                            Label(register_screen, text="register successfull").pack()
                        except sqlite3.IntegrityError as err:
                             messagebox.showinfo("Enter another registration number")
                    
                        
                    else:
                         messagebox.showinfo("Password does not match")
                else:
                     messagebox.showinfo("PLEASE! Enter correct phone number")
            else:
                messagebox.showinfo("PLEASE! Enter Age")
        else:
            messagebox.showinfo("PLEASE! Enter Name")
    else:
        messagebox.showinfo("PLEASE! Enter correct registration number")

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    
    try:
        sql="select COUNT(name), password from doctor_records where name='"+username1+"'or reg_id='"+username1+"'"
        s1.execute(sql)
        check_pass=s1.fetchone()
    except sqlite3.Error as err:
        messagebox.showinfo("something went wrong")
    
    if check_pass[0] != 0: 
        if check_pass[1] == password1:
            Label(main_screen, text="Login Success").pack()
        else:
            messagebox.showinfo("Incorrect Password ")
    else:
        messagebox.showinfo("REGISTRATION NUMBER DOES NOT EXISTS")

def forgot_pass():
    main_screen.destroy()
    global pass_screen
    pass_screen =Tk()
    #register_screen=Toplevel(main_screen)
    pass_screen.title("Forgot password")
    pass_screen.geometry("500x450")
    Button(pass_screen, text="Back", width=5, height=1, bg="blue", command = back_command2).place(x=5, y=5)

    global RESISTRATION_ID
    global PASSWORD
    global PASSWORD_ENTRY
    global REGIS_ENTRY
    global CONFIRM_PASS
    global COMF_PASS_ENTRY

    RESISTRATION_ID = StringVar()
    PASSWORD = StringVar()
    CONFIRM_PASS = StringVar()
    
    Label(pass_screen, text=" REGISTRATION ID *").pack()
    REGIS_ENTRY= Entry(pass_screen, textvariable=RESISTRATION_ID, width=30)
    REGIS_ENTRY.pack()
    
    
    Label(pass_screen, text="PASSWORD * ").pack()
    PASSWORD_ENTRY= Entry(pass_screen, textvariable=PASSWORD, show= '*', width=30)
    PASSWORD_ENTRY.pack()
    
    Label(pass_screen, text="CONFIRM PASSWORD * ").pack()
    COMF_PASS_ENTRY= Entry(pass_screen, textvariable=CONFIRM_PASS, show= '*', width=30)
    COMF_PASS_ENTRY.pack()
    
    Label(pass_screen, text="").pack()

    Button(pass_screen, text="UPDATE", width=20, height=2,  command = update_pass).pack(pady=3,padx=5)

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
        messagebox.showinfo("something went wrong")

    
    if old_id != "" and count[0] > 0:
        if new_pass != "" and len(new_pass) >= 8 and new_pass == new_c_pass:
            try:
                sql="UPDATE doctor_records SET password = '"+new_pass+"' WHERE reg_id ='"+old_id+"'"
                s1.execute(sql)
                conn.commit()
                Label(pass_screen, text="Login Success").pack()
                
                
            except sqlite3.Error as err:
                messagebox.showinfo("something went wrong")
        else:
            messagebox.showinfo("enter correct password")
    else:
        messagebox.showinfo("enter correct registration number")

def main_account_screen():
    global main_screen
    main_screen=Tk()
    main_screen.geometry("500x450")
    main_screen.title("Account Login")
    Label(text="Fill details", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    
    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(main_screen, text="Username / Registrarion Id *").pack()
    username_login_entry = Entry(main_screen, textvariable=username_verify, width=30)
    username_login_entry.pack(pady=3,padx=3)
    
    Label(main_screen, text="").pack()
    
    Label(main_screen, text="Password * ").pack()
    password_login_entry = Entry(main_screen, textvariable=password_verify, show= '*', width=30)
    password_login_entry.pack()
    
    Label(main_screen, text="").pack()
    
    Button(main_screen, text="Login", width=30, height=2, command = login_verify).pack(pady=3)
    
    Button(text="FORGOT PASSWORD" , bd=0,command=forgot_pass ).pack()
    
    Label(text="").pack(pady=1)
    
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()

def back_command():
   
    register_screen.destroy()
    main_account_screen()

def back_command2():
    pass_screen.destroy()
    main_account_screen()
    
main_account_screen()

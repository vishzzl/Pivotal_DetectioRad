import sqlite3
import main
from tkinter import *
import tkinter as tk
import os
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk , Image
from tkinter import filedialog

conn = sqlite3.connect("patients_pivotal_record.db")

s1=conn.cursor()

s1.execute('''CREATE TABLE IF NOT EXISTS patients_records(
                patient_id text(255)  NOT NULL,
                patient_name text(255) NOT NULL,
                patient_age integer NOT NULL,
                patient_gender string NOT NULL,
                patient_history text,
                old_xray blob,
                new_xray blob,
                PRIMARY KEY(patient_id)
                )''')


conn.commit()

global form_page

def openfilename():
    global filename

    filename = filedialog.askopenfilename(title='"choose photo')
    #return filename
    print(filename)

    try:
        Logo=Image.open(filename)
        print("done")
        Label21['text']="uploaded"
        
        #Logo_in=ImageTk.PhotoImage(Logo)
    except:
        messagebox.showinfo("please upload image format .jpg or .png")
    


    

    
    
def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData
   
    
   
    #Logo_label=Label(start_root,image=Logo_in,padx=100,pady=100)
    #Logo_label.image=Logo_in
    #Logo_label.pack()

    
    

def back_command3():
    form_screen.destroy()
    main.main_account_screen()

def back_command4():
    try:
        #new_patients_screen.destroy()
        form_page()
    except:
        pass

def update_form():

    
    p_name=c_name_entry.get()
    p_age=c_age_entry.get()
    p_id=c_id_entry.get()
    p_gender=c_gender_entry.get()
    p_histoty= history_Entry.get("1.0","end")
    empPhoto = convertToBinaryData(filename)

    if p_id != "":
        if p_name != "" and p_name.isdigit() == False:
            if p_age != "" and p_age.isdigit() == True:
                if p_gender != "":
                    try:
                    
                        s1.execute(""" INSERT INTO patients_records
                                    (patient_id,patient_name,patient_age, patient_gender,patient_history,old_xray) VALUES (?, ?, ?,?,?,?)""",(p_id,p_name,p_age,p_gender,p_histoty,empPhoto))
                        
                        conn.commit()
                        messagebox.showinfo("Image and file inserted successfully as a BLOB into a table")
                        conn.close()

                    

                    except sqlite3.Error as error:
                        print("Failed to insert blob data into sqlite table", error)

                else:
                    messagebox.showwarning("enter gender")
            else:
                messagebox.showwarning("enter age")
        else:
            messagebox.showwarning("enter name")
    else:
        messagebox.showwarning("enter id")
    
    

      
    
def new_patients():

    form_screen.destroy()
    global new_patients_screen
    new_patients_screen = Tk()

    new_patients_screen.geometry("1208x681+180+100")
    #form_screen.minsize(w_x,w_y)
    #register_screen.maxsize(1924, 1055)
    new_patients_screen.resizable(0,0)
    new_patients_screen.title("Register")
    new_patients_screen.configure(background="#002448")

    global c_name_entry
    global c_age_entry
    global c_id_entry
    global c_gender_entry
    global history_entry
    global history_Entry
    global nameEntry
    global nameEntry
    global genderEntry
    global idEntry
    global Label21
    

    c_name_entry=StringVar()
    c_age_entry=StringVar()
    c_gender_entry=StringVar()
    c_id_entry = StringVar()
    history_entry = StringVar()
    

    '''This class configures and populates the toplevel window.
     top is the toplevel containing window.'''
    _bgcolor = '#c0c0c0'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#c0c0c0' # X11 color: 'gray85'
    _ana1color = '#c0c0c0' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
    font11 = "-family {Segoe UI Emoji} -size 11 -weight bold"
    font12 = "-family {Sitka Heading} -size 13 -weight bold"
    font9 = "-family {Segoe UI Black} -size 14 -weight bold"
   
    
   
    Canvas1 = Canvas(new_patients_screen)
    Canvas1.place(relx=0.072, rely=0.051, relheight=0.804 , relwidth=0.847)
    Canvas1.configure(background="#c0c0c0")
    Canvas1.configure(borderwidth="2")
    Canvas1.configure(highlightbackground="#c0c0c0")
    Canvas1.configure(highlightcolor="#646464646464")
    Canvas1.configure(insertbackground="black")
    Canvas1.configure(relief="raised")
    Canvas1.configure(selectbackground="#c0c0c0")
    Canvas1.configure(selectforeground="white")
   
    Label1 = Label(Canvas1)
    Label1.place(relx=0.122, rely=0.063, height=36, width=750)
    Label1.configure(activebackground="#000071")
    Label1.configure(activeforeground="white")
    Label1.configure(activeforeground="#f0f0f0f0f0f0")
    Label1.configure(background="#ababab")
    Label1.configure(borderwidth="5")
    Label1.configure(compound='center')
    Label1.configure(disabledforeground="#000040")
    Label1.configure(font=font9)
    Label1.configure(foreground="#000040")
    Label1.configure(highlightbackground="#c0c0c0")
    Label1.configure(highlightcolor="#c0c0c0")
    Label1.configure(text='''Fill Customer Details''')

    label_id = Label(Canvas1)
    label_id.place(relx=0.194, rely=0.185, height=36, width=192)
    label_id.configure(background="#c0c0c0")
    label_id.configure(disabledforeground="#a3a3a3")
    label_id.configure(font=font9)
    label_id.configure(foreground="#000000")
    label_id.configure(text='''Patient Id''')
   
    idEntry = Entry(Canvas1)
    idEntry.place(relx=0.388, rely=0.185,height=34, relwidth=0.402)
    idEntry.configure(background="white")
    idEntry.configure(disabledforeground="#a3a3a3")
    idEntry.configure(font="TkFixedFont")
    idEntry.configure(foreground="#000000")
    idEntry.configure(insertbackground="black")
    idEntry.configure(relief="groove")
    idEntry.configure(textvariable=c_id_entry)
   
    label_name = Label(Canvas1)
    label_name.place(relx=0.194, rely=0.277, height=36, width=188)
    label_name.configure(activebackground="#f9f9f9")
    label_name.configure(activeforeground="black")
    label_name.configure(background="#c0c0c0")
    label_name.configure(disabledforeground="#a3a3a3")
    label_name.configure(font="-family {Segoe UI Black} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
    label_name.configure(foreground="#000000")
    label_name.configure(highlightbackground="#c0c0c0")
    label_name.configure(highlightcolor="black")
    label_name.configure(text='''Name''')
  
    nameEntry = Entry(Canvas1)
    nameEntry.place(relx=0.388, rely=0.277,height=34, relwidth=0.402)
    nameEntry.configure(background="white")
    nameEntry.configure(disabledforeground="#a3a3a3")
    nameEntry.configure(font="TkFixedFont")
    nameEntry.configure(foreground="#000000")
    nameEntry.configure(highlightbackground="#c0c0c0")
    nameEntry.configure(highlightcolor="black")
    nameEntry.configure(insertbackground="black")
    nameEntry.configure(relief="groove")
    nameEntry.configure(selectbackground="blue")
    nameEntry.configure(selectforeground="white")
    nameEntry.configure(textvariable=c_name_entry)
  
    label_age = Label(Canvas1)
    label_age.place(relx=0.194, rely=0.369, height=36, width=188)
    label_age.configure(activebackground="#f9f9f9")
    label_age.configure(activeforeground="black")
    label_age.configure(background="#c0c0c0")
    label_age.configure(disabledforeground="#a3a3a3")
    label_age.configure(font="-family {Segoe UI Black} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
    label_age.configure(foreground="#000000")
    label_age.configure(highlightbackground="#c0c0c0")
    label_age.configure(highlightcolor="black")
    label_age.configure(text='''Age''')
  
    ageEntry = Entry(Canvas1)
    ageEntry.place(relx=0.388, rely=0.369,height=34, relwidth=0.402)
    ageEntry.configure(background="white")
    ageEntry.configure(disabledforeground="#a3a3a3")
    ageEntry.configure(font="TkFixedFont")
    ageEntry.configure(foreground="#000000")
    ageEntry.configure(highlightbackground="#c0c0c0")
    ageEntry.configure(highlightcolor="black")
    ageEntry.configure(insertbackground="black")
    ageEntry.configure(relief="groove")
    ageEntry.configure(selectbackground="blue")
    ageEntry.configure(selectforeground="white")
    ageEntry.configure(textvariable=c_age_entry)
  
    label_gender =Label(Canvas1)
    label_gender.place(relx=0.194, rely=0.461, height=36, width=188)
    label_gender.configure(activebackground="#f9f9f9")
    label_gender.configure(activeforeground="black")
    label_gender.configure(background="#c0c0c0")
    label_gender.configure(disabledforeground="#a3a3a3")
    label_gender.configure(font="-family {Segoe UI Black} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
    label_gender.configure(foreground="#000000")
    label_gender.configure(highlightbackground="#c0c0c0")
    label_gender.configure(highlightcolor="black")
    label_gender.configure(text='''Gender''')
  
    genderEntry = Entry(Canvas1)
    genderEntry.place(relx=0.388, rely=0.461, height=34, relwidth=0.402)
  
    genderEntry.configure(background="white")
    genderEntry.configure(disabledforeground="#a3a3a3")
    genderEntry.configure(font="TkFixedFont")
    genderEntry.configure(foreground="#000000")
    genderEntry.configure(highlightbackground="#c0c0c0")
    genderEntry.configure(highlightcolor="black")
    genderEntry.configure(insertbackground="black")
    genderEntry.configure(relief="groove")
    genderEntry.configure(selectbackground="blue")
    genderEntry.configure(selectforeground="white")
    genderEntry.configure(textvariable=c_gender_entry)
  
    label_history = Label(Canvas1)
    label_history.place(relx=0.194, rely=0.572, height=36, width=188)
    label_history.configure(activebackground="#f9f9f9")
    label_history.configure(activeforeground="black")
    label_history.configure(background="#c0c0c0")
    label_history.configure(disabledforeground="#a3a3a3")
    label_history.configure(font="-family {Segoe UI Black} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
    label_history.configure(foreground="#000000")
    label_history.configure(highlightbackground="#c0c0c0")
    label_history.configure(highlightcolor="black")
    label_history.configure(text='''Medical History''')
  
    history_Entry = Text(Canvas1)
    history_Entry.place(relx=0.388, rely=0.554, height=184, relwidth=0.402)
    history_Entry.configure(background="white")
    history_Entry.configure(font="TkFixedFont")
    history_Entry.configure(foreground="#000000")
    history_Entry.configure(highlightbackground="#c0c0c0")
    history_Entry.configure(highlightcolor="black")
    history_Entry.configure(insertbackground="black")
    history_Entry.configure(relief="groove")
    history_Entry.configure(selectbackground="blue")
    
  
    label_xray = Label(Canvas1)
    label_xray.place(relx=0.184, rely=0.904, height=36, width=188)
    label_xray.configure(activebackground="#f9f9f9")
    label_xray.configure(activeforeground="black")
    label_xray.configure(background="#c0c0c0")
    label_xray.configure(disabledforeground="#a3a3a3")
    label_xray.configure(font="-family {Segoe UI Black} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
    label_xray.configure(foreground="#000000")
    label_xray.configure(highlightbackground="#c0c0c0")
    label_xray.configure(highlightcolor="black")
    label_xray.configure(text='''X-ray''')
  
    img = Button(Canvas1)
    img.place(relx=0.388, rely=0.923, height=33, width=136)
    img.configure(activebackground="#ececec")
    img.configure(activeforeground="#000000")
    img.configure(background="#141414")
    img.configure(command=openfilename)
    img.configure(disabledforeground="#a3a3a3")
    img.configure(font=font11)
    img.configure(foreground="#ffffff")
    img.configure(highlightbackground="#c0c0c0")
    img.configure(highlightcolor="black")
    img.configure(pady="0")
    img.configure(text='''select image''')

    submit = Button(Canvas1)
    submit.place(relx=0.602, rely=0.923, height=33, width=166)
    submit.configure(activebackground="#ececec")
    submit.configure(activeforeground="#000000")
    submit.configure(background="#0f0f0f")
    submit.configure(borderwidth="5")
    submit.configure(command=update_form)
    submit.configure(disabledforeground="#a3a3a3")
    submit.configure(font=font9)
    submit.configure(foreground="#ffffff")
    submit.configure(highlightbackground="#d9d9d9")
    submit.configure(highlightcolor="black")
    submit.configure(padx="5")
    submit.configure(pady="5")
    submit.configure(text='''Submit''')

    Label21= Label(Canvas1)
    Label21.place(relx=0.524, rely=0.923, height=26, width=75)
    Label21.configure(background="#d9d9d9")
    Label21.configure(disabledforeground="#a3a3a3")
    Label21.configure(foreground="#000000")
    Label21['text']="not uploaded"
        
    

    
        

  
    

    Button2 = Button(new_patients_screen)
    Button2.place(relx=0.0, rely=0.0, height=33, width=66)
    Button2.configure(activebackground="#ececec")
    Button2.configure(activeforeground="#000000")
    Button2.configure(background="#c0c0c0")
    Button2.configure(command=back_command4)
    Button2.configure(disabledforeground="#a3a3a3")
    Button2.configure(foreground="#000000")
    Button2.configure(highlightbackground="#d9d9d9")
    Button2.configure(highlightcolor="black")
    Button2.configure(pady="0")
    Button2.configure(relief="flat")
    Button2.configure(text='''Back''')

    
    


   

def form_page():
    try:
        main.top.destroy()
    except:
        new_patients_screen.destroy()
    global form_screen

    form_screen=Tk()
    #Button(form_screen
    doctorname = main.doctor_name
    doctorid= main.doctor_id

    print(doctorid, doctorname)
    
    
    
    form_screen.geometry("1208x681+180+100")
    #form_screen.minsize(w_x,w_y)
    #register_screen.maxsize(1924, 1055)
    form_screen.resizable(0,0)
    form_screen.title("Register")
    form_screen.configure(background="#002448")

    '''This class configures and populates the toplevel window.
     top is the toplevel containing window.'''
    _bgcolor = '#c0c0c0'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#c0c0c0' # X11 color: 'gray85'
    _ana1color = '#c0c0c0' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
    font11 = "-family {Segoe UI Emoji} -size 11 -weight bold"
    font12 = "-family {Sitka Heading} -size 13 -weight bold"
    font9 = "-family {Segoe UI Black} -size 14 -weight bold"
   
   
    
   
    Canvas1 = Canvas(form_screen)
    Canvas1.place(relx=0.072, rely=0.051, relheight=0.804 , relwidth=0.847)
    Canvas1.configure(background="#c0c0c0")
    Canvas1.configure(borderwidth="2")
    Canvas1.configure(highlightbackground="#c0c0c0")
    Canvas1.configure(highlightcolor="#646464646464")
    Canvas1.configure(insertbackground="black")
    Canvas1.configure(relief="raised")
    Canvas1.configure(selectbackground="#c0c0c0")
    Canvas1.configure(selectforeground="white")
   
    Label1 = Label(Canvas1)
    Label1.place(relx=0.122, rely=0.063, height=36, width=750)
    Label1.configure(activebackground="#000071")
    Label1.configure(activeforeground="white")
    Label1.configure(activeforeground="#f0f0f0f0f0f0")
    Label1.configure(background="#ababab")
    Label1.configure(borderwidth="5")
    Label1.configure(compound='center')
    Label1.configure(disabledforeground="#000040")
    Label1.configure(font=font9)
    Label1.configure(foreground="#000040")
    Label1.configure(highlightbackground="#c0c0c0")
    Label1.configure(highlightcolor="#c0c0c0")
    Label1.configure(text='''Customer Detail''')

    

    n_patients = Button(Canvas1)
    n_patients.place(relx=0.316, rely=0.314, height=53, width=376)
    n_patients.configure(activebackground="#ececec")
    n_patients.configure(activeforeground="#000000")
    n_patients.configure(background="#092748")
    n_patients.configure(borderwidth="5")
    n_patients.configure(command=new_patients)
    n_patients.configure(disabledforeground="#a3a3a3")
    n_patients.configure(font=font9)
    n_patients.configure(foreground="#ffffff")
    n_patients.configure(highlightbackground="#c0c0c0")
    n_patients.configure(highlightcolor="black")
    n_patients.configure(overrelief="raised")
    n_patients.configure(padx="5")
    n_patients.configure(pady="5")
    n_patients.configure(text='''Add new patient''')
   
    o_patients_1 = Button(Canvas1)
    o_patients_1.place(relx=0.316, rely=0.517, height=53, width=376)
    o_patients_1.configure(activebackground="#ececec")
    o_patients_1.configure(activeforeground="#000000")
    o_patients_1.configure(background="#092748")
    o_patients_1.configure(borderwidth="5")
    #o_patients_1.configure(command=view_record)
    o_patients_1.configure(disabledforeground="#a3a3a3")
    o_patients_1.configure(font="-family {Segoe UI Black} -size 14 -weight bold -slant roman -underline 0 -overstrike 0")
    o_patients_1.configure(foreground="#ffffff")
    o_patients_1.configure(highlightbackground="#c0c0c0")
    o_patients_1.configure(highlightcolor="black")
    o_patients_1.configure(overrelief="raised")
    o_patients_1.configure(padx="5")
    o_patients_1.configure(pady="5")
    o_patients_1.configure(text='''Existing patient''')

    Label3 = Label(Canvas1, text=doctorname)
    Label3.place(relx=0.041, rely=0.207, height=26, width=142)
    Label3.configure(background="#c0c0c0")
    #Label3.configure(disabledforeground="#a3a3a3")
    Label3.configure(foreground="#000000")
    
   
    Label2 = Label(Canvas1, text=doctorid)
    Label2.place(relx=0.336, rely=0.207, height=26, width=111)
    Label2.configure(background="#c0c0c0")
    #Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(foreground="#000000")
    
   
    Button1 = Button(Canvas1)
    Button1.place(relx=0.783, rely=0.207, height=33, width=90)
    Button1.configure(activebackground="#ececec")
    Button1.configure(activeforeground="#000000")
    #Button1.configure(background="#c0c0c0")
    Button1.configure(borderwidth=0)
    Button1.configure(command=back_command3)
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(foreground="#000000")
    #Button1.configure(highlightbackground="#c0c0c0")
    Button1.configure(highlightcolor="black")
    Button1.configure(pady=0)
    Button1.configure(text='''Logout''')


  

    form_screen.mainloop()



import sqlite3
from tkinter import *
import tkinter as tk
import os
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk , Image
from tkinter import filedialog
import p_main
import mlf

conn = sqlite3.connect("patients_pivotal_record.db")

s1=conn.cursor()

s1.execute('''CREATE TABLE IF NOT EXISTS patients_records_pivotalss(
                patient_id text(255)  NOT NULL,
                patient_name text(255) NOT NULL,
                patient_age integer NOT NULL,
                patient_gender string NOT NULL,
                patient_history text,
                old_xray blob,
                disease string,
                new_xray blob,
                feedback text,
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
        messagebox.showerror("ERROR","please upload image format .diacom")
        
def convertToBinaryData(filename):
    #Convert digital data to binary format
    
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData
    
        
    
   
    #Logo_label=Label(start_root,image=Logo_in,padx=100,pady=100)
    #Logo_label.image=Logo_in
    #Logo_label.pack()

def back_command3():
    import p_main as mmm
    form_screen.destroy()
    mmm.main_account_screen()
def back_command4():
    form_page()
def delete_patient():
    get_regi=c_id_entry.get()
    try:
        s1.execute(" DELETE FROM patients_records_pivotalss  WHERE patient_id='"+get_regi+"'")
        conn.commit()
        messagebox.showinfo("SUCCESSFULL","Data successfully Removed")
        idEntry.delete(0,END)
    except sqlite3.Error as err:
        messagebox.showerror("FAILED",err)
        


def update_patients():
    get_regi=c_id_entry.get()
    if get_regi=="":
        messagebox.showerror("ERROR","Please enter id")
    else:
        pass
        
    
    try:
        p_name=c_name_entry.get()
        if p_name=="":
            pass
        else:
            s1.execute("UPDATE patients_records_pivotalss SET patient_name=? WHERE patient_id='"+get_regi+"'",([p_name]))
            conn.commit()
            nameEntry.delete(0,END)

    except:
        pass
    try:
        p_age=c_age_entry.get()
        if p_age=="":
            pass
        else:
            s1.execute("UPDATE patients_records_pivotalss SET patient_age=? WHERE patient_id='"+get_regi+"'",([p_age]))
            conn.commit()
            ageEntry.delete(0,END)
                           


    except:
        pass
    try:
        p_gender=c_gender_entry.get()
        if p_gender =="":
            pass
        else:
            s1.execute("UPDATE patients_records_pivotalss SET patient_gender=? WHERE patient_id='"+get_regi+"'",([p_gender]))
            conn.commit()

    except:
        pass
    try:
        P_d=disease_entry.get()
        if P_d=="":
            pass
        else:
            s1.execute("UPDATE patients_records_pivotalss SET disease=? WHERE patient_id='"+get_regi+"'",([P_d]))
            conn.commit()
    except:
        pass
    try:
        p_histoty= history_Entry.get("1.0","end")
        if p_histoty=="":
            pass
        else:
            s1.execute("UPDATE patients_records_pivotalss SET patient_history=? WHERE patient_id='"+get_regi+"'",([p_histoty]))
            conn.commit()
            history_Entry.delete("1.0","end")
                            

    except:
        pass
    
    try:
        empPhoto = convertToBinaryData(filename)
        if empPhoto=="":
            pass
        else:
            s1.execute("UPDATE patients_records_pivotalss SET old_xray=? WHERE patient_id='"+get_regi+"'",([empPhoto]))
            conn.commit()
            Label21['text']= "Not Uploaded"

    except:
        pass



def update_form():
    
    

    global p_id

    

    
    p_name=c_name_entry.get()
    p_age=c_age_entry.get()
    p_id=c_id_entry.get()
    p_gender=c_gender_entry.get()
    P_d=disease_entry.get()
    p_histoty= history_Entry.get("1.0","end")
    print(p_gender)
    print(P_d)
    try:
        empPhoto = convertToBinaryData(filename)
    except:
        empPhoto=""

    

    

    if p_id != "":
        if p_name != "" and p_name.isdigit() == False:
            if p_age != "" and p_age.isdigit() == True:
                if p_gender != "":
                    if empPhoto != "":
                        try:
                    
                            s1.execute(""" INSERT INTO patients_records_pivotalss
                                    (patient_id,patient_name,patient_age, patient_gender,patient_history,old_xray,disease) VALUES (?, ?, ?,?,?,?,?)""",(p_id,p_name,p_age,p_gender,p_histoty,empPhoto,P_d))
                        
                        
                            conn.commit()
                            messagebox.showinfo("SUCCESSFULL","Data successfully stored")
                            
                            nameEntry.delete(0,END)
                            idEntry.delete(0,END)
                            ageEntry.delete(0,END)
                            history_Entry.delete("1.0","end")
                            Label21['text']= "Not Uploaded"


                        
                        
                            mlf.start_ml()
                        

                    

                        except sqlite3.Error as error:
                            messagebox.showerror("Failed", error)
                    else:
                        messagebox.showerror("ERROR","Please update your xray")
                else:
                    messagebox.showerror("ERROR","Please enter gender")
            else:
                messagebox.showerror("ERROR","Please enter age")
        else:
            messagebox.showerror("ERROR","Please enter name")
    else:
        messagebox.showerror("ERROR","Please enter id")
   
def new_patients():

    form_screen.destroy()
    global new_patients_screen
    new_patients_screen = Tk()

    width_value=new_patients_screen.winfo_screenwidth()
    height_value=new_patients_screen.winfo_screenheight()
    new_patients_screen.geometry("%dx%d+0+0"%(width_value,height_value))
    
    
    #form_screen.minsize(w_x,w_y)
    #register_screen.maxsize(1924, 1055)
    new_patients_screen.resizable(0,0)
    new_patients_screen.title("Register")
    new_patients_screen.configure(background="#002448")
    new_patients_screen.iconbitmap(r"pivotal\LOGO_v1.ico")

    global c_name_entry
    global c_age_entry
    global c_id_entry
    global c_gender_entry
    global history_Entry
    global history_entry
    global nameEntry
    global genderEntry
    global idEntry
    global Label21
    global ageEntry
    global disease_entry
    

    c_name_entry=StringVar()
    c_age_entry=StringVar()
    c_gender_entry=StringVar()
    c_id_entry = StringVar()
    history_entry = StringVar()
    disease_entry=StringVar()
    

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
    Canvas1.configure(background="#808080")
    Canvas1.configure(borderwidth="2")
    Canvas1.configure(highlightbackground="#808080")
    Canvas1.configure(highlightcolor="#646464646464")
    Canvas1.configure(insertbackground="black")
    Canvas1.configure(relief="raised")
    Canvas1.configure(selectbackground="#808080")
    Canvas1.configure(selectforeground="white")

    
    img = Image.open(r"pivotal\LOGO_v2.jpg")
    img = img.resize((240, 102), Image.ANTIALIAS)
			
    img0 = ImageTk.PhotoImage(img,master=Canvas1)
			
    Label1=Label(Canvas1,image=img0)
    Label1.image=img0
    Label1.place(relx=0.842, rely=0.011, height=102, width=240)
   
    Label1 = Label(Canvas1)
    Label1.place(relx=0.122, rely=0.140, height=36, width=1300)
    Label1.configure(activebackground="#000071")
    Label1.configure(activeforeground="white")
    Label1.configure(activeforeground="#f0f0f0f0f0f0")
    Label1.configure(background="#ababab")
    Label1.configure(borderwidth="5")
    Label1.configure(compound='center')
    Label1.configure(disabledforeground="#000040")
    Label1.configure(font=font9)
    Label1.configure(foreground="#000040")
    Label1.configure(highlightbackground="#808080")
    Label1.configure(highlightcolor="#808080")
    Label1.configure(text='''Fill patient's Details''')

    label_id = Label(Canvas1)
    label_id.place(relx=0.194, rely=0.215, height=40, width=192)
    label_id.configure(background="#808080")
    label_id.configure(disabledforeground="#a3a3a3")
    label_id.configure(font="-family Arial -size 15 -weight bold -slant roman -underline 0 -overstrike 0")
    label_id.configure(foreground="#0A1172")
    label_id.configure(text='''Patient Id''')

    reg1_lable = Label(Canvas1)
    reg1_lable.place(x=1450, y=810, height=30, width=100)
    reg1_lable.configure(background="#808080")
    reg1_lable.configure(text="5/7")
    reg1_lable.configure(font="-family Arial -size 15 -weight bold -slant roman -underline 0 -overstrike 0")
  
   
    idEntry = Entry(Canvas1)
    idEntry.place(relx=0.388, rely=0.215,height=40, relwidth=0.402)
    idEntry.configure(background="white")
    idEntry.configure(disabledforeground="#a3a3a3")
    idEntry.configure(font="TkFixedFont")
    idEntry.configure(foreground="#000000")
    idEntry.configure(insertbackground="black")
    idEntry.configure(relief="groove")
    idEntry.configure(textvariable=c_id_entry)
   
    label_name = Label(Canvas1)
    label_name.place(relx=0.194, rely=0.307, height=40, width=188)
    label_name.configure(activebackground="#f9f9f9")
    label_name.configure(activeforeground="black")
    label_name.configure(background="#808080")
    label_name.configure(disabledforeground="#a3a3a3")
    label_name.configure(font="-family Arial -size 15 -weight bold -slant roman -underline 0 -overstrike 0")
    label_name.configure(foreground="#0A1172")
    label_name.configure(highlightbackground="#808080")
    label_name.configure(highlightcolor="black")
    label_name.configure(text='''Name''')
  
    nameEntry = Entry(Canvas1)
    nameEntry.place(relx=0.388, rely=0.307,height=40, relwidth=0.402)
    nameEntry.configure(background="white")
    nameEntry.configure(disabledforeground="#a3a3a3")
    nameEntry.configure(font="TkFixedFont")
    nameEntry.configure(foreground="#000000")
    nameEntry.configure(highlightbackground="#808080")
    nameEntry.configure(highlightcolor="black")
    nameEntry.configure(insertbackground="black")
    nameEntry.configure(relief="groove")
    nameEntry.configure(selectbackground="blue")
    nameEntry.configure(selectforeground="white")
    nameEntry.configure(textvariable=c_name_entry)
  
    label_age = Label(Canvas1)
    label_age.place(relx=0.194, rely=0.399, height=40, width=188)
    label_age.configure(activebackground="#f9f9f9")
    label_age.configure(activeforeground="black")
    label_age.configure(background="#808080")
    label_age.configure(disabledforeground="#a3a3a3")
    label_age.configure(font="-family Arial -size 15 -weight bold -slant roman -underline 0 -overstrike 0")
    label_age.configure(foreground="#0A1172")
    label_age.configure(highlightbackground="#808080")
    label_age.configure(highlightcolor="black")
    label_age.configure(text='''Age''')
  
    ageEntry = Entry(Canvas1)
    ageEntry.place(relx=0.388, rely=0.399,height=40, relwidth=0.402)
    ageEntry.configure(background="white")
    ageEntry.configure(disabledforeground="#a3a3a3")
    ageEntry.configure(font="TkFixedFont")
    ageEntry.configure(foreground="#000000")
    ageEntry.configure(highlightbackground="#808080")
    ageEntry.configure(highlightcolor="black")
    ageEntry.configure(insertbackground="black")
    ageEntry.configure(relief="groove")
    ageEntry.configure(selectbackground="blue")
    ageEntry.configure(selectforeground="white")
    ageEntry.configure(textvariable=c_age_entry)
  
    label_gender =Label(Canvas1)
    label_gender.place(relx=0.194, rely=0.475, height=40, width=188)
    label_gender.configure(activebackground="#f9f9f9")
    label_gender.configure(activeforeground="black")
    label_gender.configure(background="#808080")
    label_gender.configure(disabledforeground="#a3a3a3")
    label_gender.configure(font="-family Arial -size 15 -weight bold -slant roman -underline 0 -overstrike 0")
    label_gender.configure(foreground="#0A1172")
    label_gender.configure(highlightbackground="#808080")
    label_gender.configure(highlightcolor="black")
    label_gender.configure(text='''Gender''')
  
  
    R1=Radiobutton(Canvas1,text="Male", variable=c_gender_entry,value="M",indicatoron=0)
    R1.place(relx=0.388, rely=0.475,width=150)
    R1.configure(background="#808080")
    R1.configure(font="-family Arial -size 15 -weight bold -slant roman -underline 0 -overstrike 0")

    R2=Radiobutton(Canvas1,text="Female", variable=c_gender_entry ,value="F",indicatoron=0)
    R2.place(relx=0.503, rely=0.475,width=150)
    R2.configure(background="#808080")
    R2.configure(font="-family Arial -size 15 -weight bold -slant roman -underline 0 -overstrike 0")

    
    label_gender =Label(Canvas1)
    label_gender.place(relx=0.194, rely=0.535, height=40, width=188)
    label_gender.configure(activebackground="#f9f9f9")
    label_gender.configure(activeforeground="black")
    label_gender.configure(background="#808080")
    label_gender.configure(disabledforeground="#a3a3a3")
    label_gender.configure(font="-family Arial -size 15 -weight bold -slant roman -underline 0 -overstrike 0")
    label_gender.configure(foreground="#0A1172")
    label_gender.configure(highlightbackground="#808080")
    label_gender.configure(highlightcolor="black")
    label_gender.configure(text='''Disease''')
  
  
    R3=Radiobutton(Canvas1,text="Covid-19", variable=disease_entry,value="covid",indicatoron=0)
    R3.place(relx=0.388, rely=0.535, width=150)
    R3.configure(background="#808080")
    R3.configure(font="-family Arial -size 15 -weight bold -slant roman -underline 0 -overstrike 0")

    R4=Radiobutton(Canvas1,text="TB", variable=disease_entry ,value="tb",indicatoron=0)
    R4.place(relx=0.503, rely=0.535,width=150)
    R4.configure(background="#808080")
    R4.configure(font="-family Arial -size 15 -weight bold -slant roman -underline 0 -overstrike 0")
  
  
    label_history = Label(Canvas1)
    label_history.place(relx=0.194, rely=0.630, height=40, width=188)
    label_history.configure(activebackground="#f9f9f9")
    label_history.configure(activeforeground="black")
    label_history.configure(background="#808080")
    label_history.configure(disabledforeground="#a3a3a3")
    label_history.configure(font="-family Arial -size 15 -weight bold -slant roman -underline 0 -overstrike 0")
    label_history.configure(foreground="#0A1172")
    label_history.configure(highlightbackground="#808080")
    label_history.configure(highlightcolor="black")
    label_history.configure(text='''Medical History''')
  
    history_Entry = Text(Canvas1)
    history_Entry.place(relx=0.388, rely=0.594, height=200, relwidth=0.410)
    history_Entry.configure(background="white")
    history_Entry.configure(font="TkFixedFont")
    history_Entry.configure(foreground="#000000")
    history_Entry.configure(highlightbackground="#808080")
    history_Entry.configure(highlightcolor="black")
    history_Entry.configure(insertbackground="black")
    history_Entry.configure(relief="groove")
    history_Entry.configure(selectbackground="blue")
    
  
    label_xray = Label(Canvas1)
    label_xray.place(relx=0.184, rely=0.855, height=40, width=188)
    label_xray.configure(activebackground="#f9f9f9")
    label_xray.configure(activeforeground="black")
    label_xray.configure(background="#808080")
    label_xray.configure(disabledforeground="#a3a3a3")
    label_xray.configure(font="-family Arial -size 15 -weight bold -slant roman -underline 0 -overstrike 0")
    label_xray.configure(foreground="#0A1172")
    label_xray.configure(highlightbackground="#808080")
    label_xray.configure(highlightcolor="black")
    label_xray.configure(text='''X-ray''')
  
    img = Button(Canvas1)
    img.place(relx=0.388, rely=0.855, height=40, width=145)
    img.configure(activebackground="#ececec")
    img.configure(activeforeground="#000000")
    img.configure(background="#141414")
    img.configure(command=openfilename)
    img.configure(disabledforeground="#a3a3a3")
    img.configure(font="-family Arial -size 15 -weight bold -slant roman -underline 0 -overstrike 0")
    img.configure(foreground="#48AAAD")
    img.configure(highlightbackground="#808080")
    img.configure(highlightcolor="black")
    img.configure(pady="0")
    img.configure(text='''select image''')

    submit = Button(Canvas1)
    submit.place(relx=0.234, rely=0.923, height=40, width=300)
    submit.configure(activebackground="#ececec")
    submit.configure(activeforeground="#000000")
    submit.configure(background="#0f0f0f")
    submit.configure(borderwidth="5")
    submit.configure(command=update_patients)
    submit.configure(disabledforeground="#a3a3a3")
    submit.configure(font="-family {Segoe UI Black} -size 17 -weight bold -slant roman -underline 0 -overstrike 0")
    submit.configure(foreground="#48AAAD")
    submit.configure(highlightbackground="#d9d9d9")
    submit.configure(highlightcolor="black")
    submit.configure(padx="5")
    submit.configure(pady="5")
    submit.configure(text='''Update''')

    submit = Button(Canvas1)
    submit.place(relx=0.432, rely=0.923, height=40, width=300)
    submit.configure(activebackground="#ececec")
    submit.configure(activeforeground="#000000")
    submit.configure(background="#0f0f0f")
    submit.configure(borderwidth="5")
    submit.configure(command=update_form)
    submit.configure(disabledforeground="#a3a3a3")
    submit.configure(font="-family {Segoe UI Black} -size 17 -weight bold -slant roman -underline 0 -overstrike 0")
    submit.configure(foreground="#48AAAD")
    submit.configure(highlightbackground="#d9d9d9")
    submit.configure(highlightcolor="black")
    submit.configure(padx="5")
    submit.configure(pady="5")
    submit.configure(text='''Submit''')

    submit = Button(Canvas1)
    submit.place(relx=0.622, rely=0.923, height=40, width=300)
    submit.configure(activebackground="#ececec")
    submit.configure(activeforeground="#000000")
    submit.configure(background="#0f0f0f")
    submit.configure(borderwidth="5")
    submit.configure(command=delete_patient)
    submit.configure(disabledforeground="#a3a3a3")
    submit.configure(font="-family {Segoe UI Black} -size 17 -weight bold -slant roman -underline 0 -overstrike 0")
    submit.configure(foreground="#48AAAD")
    submit.configure(highlightbackground="#d9d9d9")
    submit.configure(highlightcolor="black")
    submit.configure(padx="5")
    submit.configure(pady="5")
    submit.configure(text='''Delete''')



    Label21= Label(Canvas1)
    Label21.place(relx=0.524, rely=0.855, height=32, width=95)
    Label21.configure(background="#d9d9d9")
    Label21.configure(disabledforeground="#a3a3a3")
    Label21.configure(foreground="#000000")
    Label21['text']="not uploaded"
        
    

    
        

  
    

    Button2 = Button(new_patients_screen)
    Button2.place(relx=0.0, rely=0.0, height=40, width=66)
    Button2.configure(activebackground="#ececec")
    Button2.configure(activeforeground="#000000")
    Button2.configure(background="#808080")
    Button2.configure(command=back_command4)
    Button2.configure(disabledforeground="#a3a3a3")
    Button2.configure(foreground="#000000")
    Button2.configure(highlightbackground="#d9d9d9")
    Button2.configure(highlightcolor="black")
    Button2.configure(pady="0")
    Button2.configure(relief="flat")
    Button2.configure(text='''Back''')
    

def view_record():
    
    form_screen.destroy()
    
    global viewlog
    viewlog = Tk()

    width_value=viewlog.winfo_screenwidth()
    height_value=viewlog.winfo_screenheight()
    viewlog.geometry("%dx%d+0+0"%(width_value,height_value))
    #form_screen.minsize(w_x,w_y)
    #register_screen.maxsize(1924, 1055)
    viewlog.resizable(0,0)
    viewlog.title("Register")
    viewlog.configure(background="#002448")
    viewlog.iconbitmap(r"pivotal\LOGO_v1.ico")

    global get_reg
    global get_ename
    global name_ebox
    global Entry1_reg
    
    

    get_reg= StringVar()
    get_ename=StringVar()
    
    

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
   
    
   
    Canvas1 = Canvas(viewlog)
    Canvas1.place(relx=0.072, rely=0.051, relheight=0.804 , relwidth=0.847)
    Canvas1.configure(background="#808080")
    Canvas1.configure(borderwidth="2")
    Canvas1.configure(highlightbackground="#808080")
    Canvas1.configure(highlightcolor="#646464646464")
    Canvas1.configure(insertbackground="black")
    Canvas1.configure(relief="raised")
    Canvas1.configure(selectbackground="#808080")
    Canvas1.configure(selectforeground="white")

    
    img = Image.open(r"pivotal\LOGO_v2.jpg")
    img = img.resize((240, 102), Image.ANTIALIAS)
			
    img0 = ImageTk.PhotoImage(img,master=Canvas1)
			
    Label1=Label(Canvas1,image=img0)
    Label1.image=img0
    Label1.place(relx=0.842, rely=0.011, height=102, width=240)
   
    Label1 = Label(Canvas1)
    Label1.place(relx=0.122, rely=0.140, height=36, width=1300)
    Label1.configure(activebackground="#000071")
    Label1.configure(activeforeground="white")
    Label1.configure(activeforeground="#f0f0f0f0f0f0")
    Label1.configure(background="#ababab")
    Label1.configure(borderwidth="5")
    Label1.configure(compound='center')
    Label1.configure(disabledforeground="#000040")
    Label1.configure(font=font9)
    Label1.configure(foreground="#000040")
    Label1.configure(highlightbackground="#808080")
    Label1.configure(highlightcolor="#808080")
    Label1.configure(text='''Fill Patient Details''')

    reg1_lable = Label(Canvas1)
    reg1_lable.place(x=1450, y=810, height=30, width=100)
    reg1_lable.configure(background="#808080")
    reg1_lable.configure(text="6/7")
    reg1_lable.configure(font="-family Arial -size 15 -weight bold -slant roman -underline 0 -overstrike 0")
  

    registration = Label(Canvas1)
    registration.place(relx=0.209, rely=0.350, height=40, width=162)    
    registration.configure(background="#808080")
    registration.configure(disabledforeground="#a3a3a3")
    registration.configure(font="-family Arial -size 15 -weight bold -slant roman -underline 0 -overstrike 0")
    registration.configure(foreground="#0A1172")
    registration.configure(text='''registration no.''')
   
    Entry1_reg = Entry(Canvas1)
    Entry1_reg.place(relx=0.428, rely=0.350,height=40, relwidth=0.317)
    Entry1_reg.configure(background="white")
    Entry1_reg.configure(disabledforeground="#a3a3a3")
    Entry1_reg.configure(font="TkFixedFont")
    Entry1_reg.configure(foreground="#000000")
    Entry1_reg.configure(insertbackground="black")
    Entry1_reg.configure(textvariable=get_reg)
   
    name_box = Label(Canvas1)
    name_box.place(relx=0.209, rely=0.462, height=40, width=162)
    name_box.configure(background="#808080")
    name_box.configure(disabledforeground="#a3a3a3")
    name_box.configure(font="-family Arial -size 15 -weight bold -slant roman -underline 0 -overstrike 0")
    name_box.configure(foreground="#0A1172")
    name_box.configure(text='''Name''')
    
    
    name_ebox = Entry(Canvas1)
    name_ebox.place(relx=0.428, rely=0.462,height=40, relwidth=0.317)
    name_ebox.configure(background="white")
    name_ebox.configure(disabledforeground="#a3a3a3")
    name_ebox.configure(font="TkFixedFont")
    name_ebox.configure(foreground="#000000")
    name_ebox.configure(highlightbackground="#d9d9d9")
    name_ebox.configure(highlightcolor="black")
    name_ebox.configure(insertbackground="black")
    name_ebox.configure(selectbackground="blue")
    name_ebox.configure(selectforeground="white")
    name_ebox.configure(textvariable=get_ename)
  
    Button1 = Button(Canvas1,command=mlf.start_ml)
    Button1.place(relx=0.385, rely=0.635, height=45, width=306)
    Button1.configure(activebackground="#ececec")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#092748")
    Button1.configure(borderwidth="5")
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(font="-family {Segoe UI Black} -size 17 -weight bold -slant roman -underline 0 -overstrike 0")
    Button1.configure(foreground="#0492C2")
    Button1.configure(highlightbackground="#808080")
    Button1.configure(highlightcolor="black")
    Button1.configure(overrelief="raised")
    Button1.configure(padx="5")
    Button1.configure(pady="5")
    Button1.configure(text='submit')

    
    Button2 = Button(viewlog)
    Button2.place(relx=0.0, rely=0.0, height=40, width=66)
    Button2.configure(activebackground="#ececec")
    Button2.configure(activeforeground="#000000")
    Button2.configure(background="#808080")
    Button2.configure(command=back_command4)
    Button2.configure(disabledforeground="#a3a3a3")
    Button2.configure(foreground="#000000")
    Button2.configure(highlightbackground="#d9d9d9")
    Button2.configure(highlightcolor="black")
    Button2.configure(pady="0")
    Button2.configure(relief="flat")
    Button2.configure(text='''Back''')

    viewlog.mainloop()

def form_page():
    try:
        p_main.top.destroy()
        
        
    except:
        try:
            new_patients_screen.destroy()
        except:
            try:
                mlf.multi_screen.destroy()
            except:
                viewlog.destroy()
        
      
    
    
    global form_screen
 
    form_screen=Tk()
    
    
    doctorname = p_main.doctor_name
    doctorid= p_main.doctor_id
    

    #print(doctorid, doctorname)
    
    
    
    width_value=form_screen.winfo_screenwidth()
    height_value=form_screen.winfo_screenheight()
    form_screen.geometry("%dx%d+0+0"%(width_value,height_value))
    #form_screen.minsize(w_x,w_y)
    #register_screen.maxsize(1924, 1055)
    form_screen.resizable(0,0)
    form_screen.title("Patient Module")
    form_screen.configure(background="#002448")
    form_screen.iconbitmap(r"pivotal\LOGO_v1.ico")

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
    Canvas1.configure(background="#808080")
    Canvas1.configure(borderwidth="2")
    Canvas1.configure(highlightbackground="#808080")
    Canvas1.configure(highlightcolor="#646464646464")
    Canvas1.configure(insertbackground="black")
    Canvas1.configure(relief="raised")
    Canvas1.configure(selectbackground="#808080")
    Canvas1.configure(selectforeground="white")

    
    img = Image.open(r"pivotal\LOGO_v2.jpg")
    img = img.resize((240, 102), Image.ANTIALIAS)
			
    img0 = ImageTk.PhotoImage(img,master=Canvas1)
			
    Label1=Label(Canvas1,image=img0)
    Label1.image=img0
    Label1.place(relx=0.842, rely=0.011, height=102, width=240)
   
    Label1 = Label(Canvas1)
    Label1.place(relx=0.122, rely=0.140, height=36, width=1300)
    Label1.configure(activebackground="#000071")
    Label1.configure(activeforeground="white")
    Label1.configure(activeforeground="#f0f0f0f0f0f0")
    Label1.configure(background="#ababab")
    Label1.configure(borderwidth="5")
    Label1.configure(compound='center')
    Label1.configure(disabledforeground="#000040")
    Label1.configure(font=font9)
    Label1.configure(foreground="#000040")
    Label1.configure(highlightbackground="#808080")
    Label1.configure(highlightcolor="#808080")
    Label1.configure(text='''Patient Module''')

    

    n_patients = Button(Canvas1)
    n_patients.place(relx=0.360, rely=0.364, height=65, width=400)
    n_patients.configure(activebackground="#ececec")
    n_patients.configure(activeforeground="#000000")
    n_patients.configure(background="#092748")
    n_patients.configure(borderwidth="5")
    n_patients.configure(command=new_patients)
    n_patients.configure(disabledforeground="#a3a3a3")
    n_patients.configure(font="-family {Segoe UI Black} -size 17 -weight bold -slant roman -underline 0 -overstrike 0")
    n_patients.configure(foreground="#0492C2")
    n_patients.configure(highlightbackground="#808080")
    n_patients.configure(highlightcolor="black")
    n_patients.configure(overrelief="raised")
    n_patients.configure(padx="5")
    n_patients.configure(pady="5")
    n_patients.configure(text='''Add new patient''')

    reg1_lable = Label(Canvas1)
    reg1_lable.place(x=1450, y=810, height=30, width=100)
    reg1_lable.configure(background="#808080")
    reg1_lable.configure(text="4/7")
    reg1_lable.configure(font="-family Arial -size 15 -weight bold -slant roman -underline 0 -overstrike 0")
  
   
    o_patients_1 = Button(Canvas1)
    o_patients_1.place(relx=0.360, rely=0.567, height=65, width=400)
    o_patients_1.configure(activebackground="#ececec")
    o_patients_1.configure(activeforeground="#000000")
    o_patients_1.configure(background="#092748")
    o_patients_1.configure(borderwidth="5")
    o_patients_1.configure(command=view_record)
    o_patients_1.configure(disabledforeground="#a3a3a3")
    o_patients_1.configure(font="-family {Segoe UI Black} -size 17 -weight bold -slant roman -underline 0 -overstrike 0")
    o_patients_1.configure(foreground="#0492C2")
    o_patients_1.configure(highlightbackground="#808080")
    o_patients_1.configure(highlightcolor="black")
    o_patients_1.configure(overrelief="raised")
    o_patients_1.configure(padx="5")
    o_patients_1.configure(pady="5")
    o_patients_1.configure(text='''Existing patient''')


    g_patients_1 = Button(Canvas1)
    g_patients_1.place(relx=0.360, rely=0.770, height=65, width=400)
    g_patients_1.configure(activebackground="#ececec")
    g_patients_1.configure(activeforeground="#000000")
    g_patients_1.configure(background="#092748")
    g_patients_1.configure(borderwidth="5")
    g_patients_1.configure(command=mlf.multi_predict_screen)
    g_patients_1.configure(disabledforeground="#a3a3a3")
    g_patients_1.configure(font="-family {Segoe UI Black} -size 17 -weight bold -slant roman -underline 0 -overstrike 0")
    g_patients_1.configure(foreground="#0492C2")
    g_patients_1.configure(highlightbackground="#808080")
    g_patients_1.configure(highlightcolor="black")
    g_patients_1.configure(overrelief="raised")
    g_patients_1.configure(padx="5")
    g_patients_1.configure(pady="5")
    g_patients_1.configure(text='''Multiple Prediction''')


    Label3 = Label(Canvas1, text=doctorname)
    Label3.place(relx=0.041, rely=0.237, height=50, width=150)
    Label3.configure(background="#808080")
    Label3.configure(font="-family Arial -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
    Label3.configure(foreground="#0A1142")
    
   
    Label2 = Label(Canvas1, text=doctorid)
    Label2.place(relx=0.336, rely=0.237, height=50, width=150)
    Label2.configure(background="#808080")
    Label2.configure(font="-family Arial -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
    Label2.configure(foreground="#0A1172")
    
   
    Button1 = Button(Canvas1)
    Button1.place(relx=0.783, rely=0.237, height=40, width=95)
    Button1.configure(activebackground="#ececec")
    Button1.configure(activeforeground="#000000")
    #Button1.configure(background="#808080")
    Button1.configure(borderwidth=0)
    Button1.configure(command=back_command3)
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(foreground="#000000")
    #Button1.configure(highlightbackground="#808080")
    Button1.configure(highlightcolor="black")
    Button1.configure(pady=0)
    Button1.configure(text='''Logout''')


  

    form_screen.mainloop()



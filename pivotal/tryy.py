import sqlite3
from tkinter import *
import tkinter as tk
import os
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk , Image
from tkinter import filedialog
import os




conn = sqlite3.connect("patients_pivotal_record.db")

s1=conn.cursor()

conn.commit()
global way
"""def write_file(data):
    with open("result.png" ,'wb') as file:
        file.write(data)
        path_return()
        
    
def path_return():
    way=os.path.abspath("result.png")
    print(way)
    return way
        #display()"""

def readBLOB(patient_idr):
    #photo="result"
    patient=patient_idr
    s1.execute("SELECT * FROM patients_records_pivotalss WHERE patient_id ='"+patient+"'")
    record=s1.fetchall()
    for row in record:
        """ids = row[0]
        name=row[1]
        age=row[3]
        history=row[4]"""
        image= row[5]
        #write_file(image)
    with open("result.png" ,'wb') as file:
        file.write(image)
        
    way=os.path.abspath("result.png")
    print(way)
    return way

"""def loadBLOB(patient_idr):
    patient=patient_id
    addr=os.path.abspath("detect.png")

    with open(addr, 'rb') as file:
        detected = file.read()
    try:
        s1.execute("UPDATE  patients_records_pivotalss SET new_xray='"+detected+"'WHERE patient_id='"+patient+"'")
        conn.commit()
        delete_img() 
    except sqlite3.Error as err:
        print("task failed")   
        """
        
def display():       
    global start_root
    
    start_root=Tk()
    start_root.config(bg="black")
    start_root.title("DetectioRad")
    Logo=Image.open(r"result.png")
    Logo_in=ImageTk.PhotoImage(Logo)
    Logo_label=Label(start_root,image=Logo_in,padx=100,pady=100)
    Logo_label.image=Logo_in
    Logo_label.place(x=0,y=0)
    start_root.mainloop()
    os.remove(way)
#readBLOB("147")

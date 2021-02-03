import sqlite3
import os
from tkinter import messagebox
import mlf



conn = sqlite3.connect("patients_pivotal_record.db")

s1=conn.cursor()

conn.commit()

def delete_img(sign_o):
    global sign_d
    
    sign_d=sign_o
    os.remove(addr)
    mlf.top.destroy()
    if sign_d == "=":
        mlf.next_no("=")
    elif sign_d == "+":
        mlf.next_no("+") 
    elif sign_d == "-":
        mlf.next_no("-")

    

def loadBLOB(patient_id,sign_a):
    sign=sign_a
    global addr
    patient=patient_id
    addr=os.path.abspath("detect.png")
    print(addr)
    with open(addr, 'rb') as file:
        detected = file.read()
    try:
        s1.execute("UPDATE patients_records_pivotalss SET new_xray=? WHERE patient_id='"+patient+"'",([detected]))
        conn.commit()
        messagebox.showinfo("SUCCESSFULL","data stored successfully")
        print("done")
        delete_img(sign)

    except sqlite3.Error as err:
        print("task failed",err)
    
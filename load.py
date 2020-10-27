import sqlite3
import os



conn = sqlite3.connect("patients_pivotal_record.db")

s1=conn.cursor()

conn.commit()

def delete_img():
    os.remove(addr)

def loadBLOB(patient_id):
    global addr
    patient=patient_id
    addr=os.path.abspath("detect.png")
    print(addr)
    with open(addr, 'rb') as file:
        detected = file.read()
    try:
        s1.execute("UPDATE patients_records_pivotal SET new_xray=? WHERE patient_id='"+patient+"'",([detected]))
        conn.commit()
        print("done")
        delete_img()

    except sqlite3.Error as err:
        print("task failed")
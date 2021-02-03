from tkinter import *
import os
from tkinter import messagebox
from tkinter import ttk
#import Register 
from PIL import Image, ImageTk
import time
import sys
import p_main



class splalsh_screen:
    global start_root
    
    start_root=Tk()
    start_root.config(bg="black")
    start_root.title("DetectioRad")
    start_root.iconbitmap(r"pivotal\LOGO_v1.ico")

    Logo=Image.open(r"pivotal\LOGO_v1.png")
    global w_x
    global w_y
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
    

def call_mainroot():
    start_root.destroy()
    p_main.main_account_screen()

start_root.after(3000,call_mainroot()) 
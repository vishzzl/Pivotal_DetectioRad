from tkinter import *
from tkinter import ttk
import tensorflow as tf
from tensorflow import *
from tensorflow.keras.preprocessing import image
import tkinter as tk
from tkinter import *
import numpy as np
from tkinter.filedialog import askopenfile
from PIL import Image,ImageTk
from PIL import ImageDraw 
import random
import cv2
from   tensorflow.keras.preprocessing.image import img_to_array, load_img
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from keras.models import load_model
import load
import os
import sqlite3
import tryy
import pivotal_form
from PIL import ImageTk , Image
from tkinter import filedialog
 

conn = sqlite3.connect("patients_pivotal_record.db")

s1=conn.cursor()

conn.commit()




def end_process():
	os.remove(path)
	
	global sign_a

	sign_a=StringVar()
	
	feedback1=feedback_Entry.get("1.0","end")
	try:
		s1.execute("UPDATE patients_records_pivotal SET feedback=? WHERE patient_id='"+get_regi+"'",([feedback1]))
		conn.commit()
		print("done")
	except sqlite3.Error as err:
		print("task failed")
	sign_a="="
	print(sign_a)
	load.loadBLOB(get_regi,sign_a)

def end_process_1():
	os.remove(path)
	
	global sign_a

	sign_a=StringVar()
	
	feedback1=feedback_Entry.get("1.0","end")
	try:
		s1.execute("UPDATE patients_records_pivotal SET feedback=? WHERE patient_id='"+get_regi+"'",([feedback1]))
		conn.commit()
		print("done")
	except sqlite3.Error as err:
		print("task failed")
	sign_a="+"
	print(sign_a)
	load.loadBLOB(get_regi,sign_a)
def end_process_2():
	os.remove(path)
	
	global sign_a

	sign_a=StringVar()
	
	feedback1=feedback_Entry.get("1.0","end")
	try:
		s1.execute("UPDATE patients_records_pivotal SET feedback=? WHERE patient_id='"+get_regi+"'",([feedback1]))
		conn.commit()
		print("done")
	except sqlite3.Error as err:
		print("task failed")
	sign_a="-"
	print(sign_a)
	load.loadBLOB(get_regi,sign_a)



def get_model():
	#model=load_model(covid19.model)	
	model=tf.keras.models.load_model('pivotal\covid19.model')
	print(model.summary())
	return model
"""
def open_file():
	file= askopenfile(mode ='r')
	path = "result.png"
	if file is not None:
		path=file.name
		print(path)
	return(path)
	
	#print(path)"""

def predict(path,model):
	
	img_width, img_height = 224, 224
# Get test image ready
	test_image = image.load_img(path, target_size=(img_width, img_height))
	test_image = image.img_to_array(test_image)
	test_image = np.expand_dims(test_image, axis=0)
	
	#test_image = test_image.reshape(img_width, img_height,3)    # Ambiguity!
	# Should this instead be: test_image.reshape(img_width, img_height, 3) ??
	
	confidence = model.predict(test_image, batch_size=1)
	#print(decode_predictions(result))
	print (confidence)
	result = np.argmax(confidence, axis=1)
	print (result)
	img = Image.open(path)
	img = img.resize((560, 552), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img,master=Frame1)
	
	"""panel= Label(second_frame ,image=img)
	panel.image = img
    panel.place(x=530,y=195)"""
	Label3 = Label(Frame1,image=img)
	Label3.image=img
	Label3.place(relx=0.262, rely=0.253, height=560, width=552)
	Label3.configure(background="#d9d9d9")
	Label3.configure(disabledforeground="#a3a3a3")
	Label3.configure(foreground="#000000")
	heat_map(model,path)
	if (result>0.5):
		#label=Label(second_frame,compound=tk.RIGHT,text='Covid Infected',font = "Helvetica 16 bold").place(x=350,y=500)
		Label6 = Label(Frame1)
		Label6.place(relx=0.019, rely=0.888, height=64, width=325)
		Label6.configure(background="#82f3fd")
		Label6.configure(disabledforeground="#a3a3a3")
		Label6.configure(font="font19")
		Label6.configure(foreground="#000000")
		Label6.configure(relief="ridge")
		Label6.configure(text='''Positive''')
		return
	
		
	else:
		#Labelx=tk.Label(second_frame,compound=tk.RIGHT,text='Normal',font = "Helvetica 16 bold").place(x=350,y=500)
		Label6 = Label(Frame1)
		Label6.place(relx=0.019, rely=0.888, height=64, width=325)
		Label6.configure(background="#82f3fd")
		Label6.configure(disabledforeground="#a3a3a3")
		Label6.configure(font="font19")
		Label6.configure(foreground="#000000")
		Label6.configure(relief="ridge")
		Label6.configure(text='''Normal''')
		return
		
		

def heat_map(model,path):
	LAYER_NAME = 'block5_conv3'
	Corona_Index = 1
	
	img = tf.keras.preprocessing.image.load_img(path, target_size=(224, 224))
	img = tf.keras.preprocessing.image.img_to_array(img)
	
	
	# Create a graph that outputs target convolution and output
	grad_model = tf.keras.models.Model([model.inputs], [model.get_layer(LAYER_NAME).output, model.output])
	
	# Get the score for target class
	with tf.GradientTape() as tape:
	    conv_outputs, predictions = grad_model(np.array([img]))
	    loss = predictions[:, Corona_Index]
	
	# Extract filters and gradients
	output = conv_outputs[0]
	grads = tape.gradient(loss, conv_outputs)[0]
	
	
	# Average gradients spatially
	weights = tf.reduce_mean(grads, axis=(0, 1))
	
	# Build a ponderated map of filters according to gradients importance
	cam = np.ones(output.shape[0:2], dtype=np.float32)
	
	for index, w in enumerate(weights):
	    cam += w * output[:, :, index]
	
	# Heatmap visualization
	cam = cv2.resize(cam.numpy(), (224, 224))
	cam = np.maximum(cam, 0)
	heatmap = (cam - cam.min()) / (cam.max() - cam.min())
	
	cam = cv2.applyColorMap(np.uint8(255*heatmap), cv2.COLORMAP_JET)
	
	output_image = cv2.addWeighted(cv2.cvtColor(img.astype('uint8'), cv2.COLOR_RGB2BGR), 1, cam,0.4, 0)
	img = Image.fromarray(output_image)
	cv2.imwrite('detect.png',output_image)
	img = img.resize((561, 552), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img,master=Frame1)
	"""panel = Label(second_frame, image=img ) #,compound=root_ml
	panel.image = img

	panel.place(x=150,y=195)#root_ml was in brackets"""
	Label3_1 = Label(Frame1,image=img)
	Label3_1.image=img
	Label3_1.place(relx=0.625, rely=0.253, height=561, width=552)
	Label3_1.configure(activebackground="#f9f9f9")
	Label3_1.configure(activeforeground="black")
	Label3_1.configure(background="#d9d9d9")
	Label3_1.configure(disabledforeground="#a3a3a3")
	Label3_1.configure(foreground="#000000")
	Label3_1.configure(highlightbackground="#d9d9d9")
	Label3_1.configure(highlightcolor="black")
	
	




global start_ml
global reg_id



	
def start_ml():
	
	global top
	global get_regi 
	global feedback_Entry

	get_regi=StringVar()

	
	try:
		get_regi= pivotal_form.get_reg.get()
		print(get_regi,"byeee")
		get_enamei=pivotal_form.get_ename.get()
		pivotal_form.Entry1_reg.delete(0,END)
		pivotal_form.name_ebox.delete(0,END)
	except:
		try:
			pivotal_form.filename=""
			get_regi= pivotal_form.p_id
		except:
			get_regi=reg_id
			print("hello",get_regi)
	
	
	
	try:
		
		s1.execute("select * from patients_records_pivotal where patient_id='"+get_regi+"'")
		record=s1.fetchall()
		for row in record:
			ids = row[0]
			name=row[1]
			age=row[2]
			gender=row[3]
			history=row[4]
			feed=row[7]
			if feed == None:
				feed="fill your feedback"
				
				
		
				

			

		
	except sqlite3.Error as err:
		messagebox.showerror("ERROR","something went wrong")





	if get_regi != "":
		if not record:
			messagebox.showerror("ERROR","wrong Id")
		else:
			global Frame1
			
			global val, w, root
			global prog_location
			"""prog_call = sys.argv[0]
			prog_location = os.path.split(prog_call)[0]"""
			top= Tk()
    		#top = Toplevel1(root)
    		#final_screen_support.init(root, top)
			
			width_value=top.winfo_screenwidth()
			height_value=top.winfo_screenheight()
			top.geometry("%dx%d+0+0"%(width_value,height_value))
			#top.minsize(120, 1)
			top.maxsize(1924, 1061)
			top.resizable(1, 1)
			top.title("result")
			top.configure(background="#002448")
			
			Frame1 = Frame(top)
			Frame1.place(relx=0.024, rely=0.04, relheight=0.897, relwidth=0.961)
			Frame1.configure(relief='sunken')
			Frame1.configure(borderwidth="2")
			Frame1.configure(relief="sunken")
			Frame1.configure(background="#808080")
			
			
			#photo_location = os.path.join(prog_location,"LOGO_v1.png")
			img = Image.open(r"pivotal\LOGO_v2.jpg")
			img = img.resize((240, 102), Image.ANTIALIAS)
			
			img0 = ImageTk.PhotoImage(img,master=Frame1)
			
			Label1=Label(Frame1,image=img0)
			Label1.image=img0
			Label1.place(relx=0.842, rely=0.011, height=102, width=240)
			
			
			TSeparator1 =ttk.Separator(Frame1)
			TSeparator1.place(relx=0.248, rely=0.007, relheight=0.985)
			TSeparator1.configure(orient="vertical")
			
			Label2 = Label(Frame1)
			Label2.place(relx=0.038, rely=0.022, height=75, width=258)
			Label2.configure(background="#808080")
			Label2.configure(disabledforeground="#a3a3a3")
			Label2.configure(font="font11")
			Label2.configure(foreground="#000000")
			Label2.configure(text='''Patient Details''')
			
			
			
			Label4 = Label(Frame1)
			Label4.place(relx=0.262, rely=0.200, height=33, width=552)
			Label4.configure(background="gold")
			Label4.configure(disabledforeground="#a3a3a3")
			Label4.configure(font="font14")
			Label4.configure(foreground="#000000")
			Label4.configure(relief="groove")
			Label4.configure(text='''X-RAY''')
			
			Label4_2 = Label(Frame1)
			Label4_2.place(relx=0.625, rely=0.200, height=33, width=546)
			Label4_2.configure(activebackground="#f9f9f9")
			Label4_2.configure(activeforeground="black")
			Label4_2.configure(background="gold")
			Label4_2.configure(disabledforeground="#a3a3a3")
			Label4_2.configure(font="font14")
			Label4_2.configure(foreground="#000000")
			Label4_2.configure(highlightbackground="#d9d9d9")
			Label4_2.configure(highlightcolor="black")
			Label4_2.configure(relief="groove")
			Label4_2.configure(text='''Heat Map''')
			
			Button1 = Button(Frame1,command=end_process)
			Button1.place(relx=0.350, rely=0.921, height=44, width=250)
			Button1.configure(activebackground="#ececec")
			Button1.configure(activeforeground="#000000")
			Button1.configure(background="#437afc")
			Button1.configure(borderwidth="4")
			Button1.configure(disabledforeground="#a3a3a3")
			Button1.configure(font="font21")
			Button1.configure(foreground="#000000")
			Button1.configure(highlightbackground="#d9d9d9")
			Button1.configure(highlightcolor="black")
			Button1.configure(pady="0")
			Button1.configure(text='''Save''')


			Button_n= Button(Frame1,command=end_process_2)
			Button_n.place(relx=0.471, rely=0.921, height=44, width=250)
			Button_n.configure(activebackground="#ececec")
			Button_n.configure(activeforeground="#000000")
			Button_n.configure(background="#437afc")
			Button_n.configure(borderwidth="4")
			Button_n.configure(disabledforeground="#a3a3a3")
			Button_n.configure(font="font21")
			Button_n.configure(foreground="#000000")
			Button_n.configure(highlightbackground="#d9d9d9")
			Button_n.configure(highlightcolor="black")
			Button_n.configure(pady="0")
			Button_n.configure(text='''Previous''')

			ButtonP = Button(Frame1,command=end_process_1)
			ButtonP.place(relx=0.600, rely=0.921, height=44, width=250)
			ButtonP.configure(activebackground="#ececec")
			ButtonP.configure(activeforeground="#000000")
			ButtonP.configure(background="#437afc")
			ButtonP.configure(borderwidth="4")
			ButtonP.configure(disabledforeground="#a3a3a3")
			ButtonP.configure(font="font21")
			ButtonP.configure(foreground="#000000")
			ButtonP.configure(highlightbackground="#d9d9d9")
			ButtonP.configure(highlightcolor="black")
			ButtonP.configure(pady="0")
			ButtonP.configure(text='''Next''')
			
			
			
			Label5_3 = Label(Frame1)
			Label5_3.place(relx=0.088, rely=0.156, height=32, width=233)
			Label5_3.configure(activebackground="#f9f9f9")
			Label5_3.configure(activeforeground="black")
			Label5_3.configure(background="#ffffff")
			Label5_3.configure(disabledforeground="#a3a3a3")
			Label5_3.configure(foreground="#000000")
			Label5_3.configure(highlightbackground="#d9d9d9")
			Label5_3.configure(highlightcolor="black")
			Label5_3.configure(text=ids)
			
			Label5_4 = Label(Frame1)
			Label5_4.place(relx=0.088, rely=0.213, height=31, width=233)
			Label5_4.configure(activebackground="#f9f9f9")
			Label5_4.configure(activeforeground="black")
			Label5_4.configure(background="#ffffff")
			Label5_4.configure(disabledforeground="#a3a3a3")
			Label5_4.configure(foreground="#000000")
			Label5_4.configure(highlightbackground="#d9d9d9")
			Label5_4.configure(highlightcolor="black")
			Label5_4.configure(text=name)
			
			Label5_5 = Label(Frame1)
			Label5_5.place(relx=0.088, rely=0.267, height=31, width=233)
			Label5_5.configure(activebackground="#f9f9f9")
			Label5_5.configure(activeforeground="black")
			Label5_5.configure(background="#ffffff")
			Label5_5.configure(disabledforeground="#a3a3a3")
			Label5_5.configure(foreground="#000000")
			Label5_5.configure(highlightbackground="#d9d9d9")
			Label5_5.configure(highlightcolor="black")
			Label5_5.configure(text=gender)
			
			Label5_5 = Label(Frame1)
			Label5_5.place(relx=0.019, rely=0.427, height=92, width=357)
			Label5_5.configure(activebackground="#f9f9f9")
			Label5_5.configure(activeforeground="black")
			Label5_5.configure(background="#fdfdfd")
			Label5_5.configure(disabledforeground="#a3a3a3")
			Label5_5.configure(foreground="#000000")
			Label5_5.configure(highlightbackground="#d9d9d9")
			Label5_5.configure(highlightcolor="black")
			Label5_5.configure(text=history)
			
			Label5_5 = Label(Frame1)
			Label5_5.place(relx=0.088, rely=0.326, height=31, width=233)
			Label5_5.configure(activebackground="#f9f9f9")
			Label5_5.configure(activeforeground="black")
			Label5_5.configure(background="#ffffff")
			Label5_5.configure(disabledforeground="#a3a3a3")
			Label5_5.configure(foreground="#000000")
			Label5_5.configure(highlightbackground="#d9d9d9")
			Label5_5.configure(highlightcolor="black")
			Label5_5.configure(text=age)
			
			Label5 = Label(Frame1)
			Label5.place(relx=0.013, rely=0.156, height=32, width=113)
			Label5.configure(activebackground="lightsalmon")
			Label5.configure(background="lightsalmon")
			Label5.configure(disabledforeground="#a3a3a3")
			Label5.configure(font="font18")
			Label5.configure(foreground="#000000")
			Label5.configure(relief="raised")
			Label5.configure(state='active')
			Label5.configure(text='''ID''')
			
			feedback_Entry = Text(Frame1)
			feedback_Entry.place(relx=0.019, rely=0.607,height=150, relwidth=0.19)
			feedback_Entry.insert(INSERT, feed)
			
			Label5_6 = Label(Frame1)
			Label5_6.place(relx=0.013, rely=0.562, height=33, width=370)
			Label5_6.configure(activebackground="#f9f9f9")
			Label5_6.configure(activeforeground="black")
			Label5_6.configure(background="lightsalmon")
			Label5_6.configure(disabledforeground="#a3a3a3")
			Label5_6.configure(font="font17")
			Label5_6.configure(foreground="#000000")
			Label5_6.configure(highlightbackground="#d9d9d9")
			Label5_6.configure(highlightcolor="black")
			Label5_6.configure(relief="raised")
			Label5_6.configure(text='''Doctor Review''')
			
			Label5_7 = Label(Frame1)
			Label5_7.place(relx=0.013, rely=0.831, height=33, width=370)
			Label5_7.configure(activebackground="#f9f9f9")
			Label5_7.configure(activeforeground="black")
			Label5_7.configure(background="lightsalmon")
			Label5_7.configure(disabledforeground="#a3a3a3")
			Label5_7.configure(font="-family {Bahnschrift SemiBold} -size 14 -weight bold -slant roman -underline 0 -overstrike 0")
			Label5_7.configure(foreground="#000000")
			Label5_7.configure(highlightbackground="#d9d9d9")
			Label5_7.configure(highlightcolor="black")
			Label5_7.configure(relief="raised")
			Label5_7.configure(text='''Predicted Result''')
			
			Label5_8 = Label(Frame1)
			Label5_8.place(relx=0.013, rely=0.213, height=32, width=113)
			Label5_8.configure(activebackground="lightsalmon")
			Label5_8.configure(activeforeground="black")
			Label5_8.configure(background="lightsalmon")
			Label5_8.configure(disabledforeground="#a3a3a3")
			Label5_8.configure(font="-family {Bahnschrift SemiBold} -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
			Label5_8.configure(foreground="#000000")
			Label5_8.configure(highlightbackground="#d9d9d9")
			Label5_8.configure(highlightcolor="black")
			Label5_8.configure(relief="raised")
			Label5_8.configure(state='active')
			Label5_8.configure(text='''Name''')
			
			Label5_9 = Label(Frame1)
			Label5_9.place(relx=0.013, rely=0.27, height=32, width=113)
			Label5_9.configure(activebackground="lightsalmon")
			Label5_9.configure(activeforeground="black")
			Label5_9.configure(background="lightsalmon")
			Label5_9.configure(disabledforeground="#a3a3a3")
			Label5_9.configure(font="-family {Bahnschrift SemiBold} -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
			Label5_9.configure(foreground="#000000")
			Label5_9.configure(highlightbackground="#d9d9d9")
			Label5_9.configure(highlightcolor="black")
			Label5_9.configure(relief="raised")
			Label5_9.configure(state='active')
			Label5_9.configure(text='''Gender''')
			
			Label5_10 = Label(Frame1)
			Label5_10.place(relx=0.013, rely=0.326, height=32, width=113)
			Label5_10.configure(activebackground="lightsalmon")
			Label5_10.configure(activeforeground="black")
			Label5_10.configure(background="lightsalmon")
			Label5_10.configure(disabledforeground="#a3a3a3")
			Label5_10.configure(font="-family {Bahnschrift SemiBold} -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
			Label5_10.configure(foreground="#000000")
			Label5_10.configure(highlightbackground="#d9d9d9")
			Label5_10.configure(highlightcolor="black")
			Label5_10.configure(relief="raised")
			Label5_10.configure(state='active')
			Label5_10.configure(text='''Age''')
			
			Label5_11 = Label(Frame1)
			Label5_11.place(relx=0.013, rely=0.382, height=32, width=370)
			Label5_11.configure(activebackground="lightsalmon")
			Label5_11.configure(activeforeground="black")
			Label5_11.configure(background="lightsalmon")
			Label5_11.configure(disabledforeground="#a3a3a3")
			Label5_11.configure(font="-family {Bahnschrift SemiBold} -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
			Label5_11.configure(foreground="#000000")
			Label5_11.configure(highlightbackground="#d9d9d9")
			Label5_11.configure(highlightcolor="black")
			Label5_11.configure(relief="raised")
			Label5_11.configure(state='active')
			Label5_11.configure(text='''Medical History''')
			

			Label1 = Label(Frame1)
			Label1.place(relx=0.262, rely=0.155, height=27, width=19)
			Label1.configure(background="#ff1111")
			Label1.configure(disabledforeground="#a3a3a3")
			Label1.configure(foreground="#000000")
			
			Label1_1 = Label(Frame1)
			Label1_1.place(relx=0.500, rely=0.155, height=27, width=19)
			Label1_1.configure(activebackground="#f9f9f9")
			Label1_1.configure(activeforeground="black")
			Label1_1.configure(background="#f2fe12")
			Label1_1.configure(disabledforeground="#a3a3a3")
			Label1_1.configure(foreground="#000000")
			Label1_1.configure(highlightbackground="#d9d9d9")
			Label1_1.configure(highlightcolor="black")
			
			Label1_3 = Label(Frame1)
			Label1_3.place(relx=0.820, rely=0.155, height=27, width=19)
			Label1_3.configure(activebackground="#f9f9f9")
			Label1_3.configure(activeforeground="black")
			Label1_3.configure(background="#1282fe")
			Label1_3.configure(disabledforeground="#a3a3a3")
			Label1_3.configure(foreground="#000000")
			Label1_3.configure(highlightbackground="#d9d9d9")
			Label1_3.configure(highlightcolor="black")
			
			Label2 = Label(Frame1)
			Label2.place(relx=0.291, rely=0.155, height=27, width=84)
			Label2.configure(background="#808080")
			Label2.configure(disabledforeground="#a3a3a3")
			Label2.configure(foreground="#000000")
			Label2.configure(text='''highly infected''')
			
			Label2_5 = Label(Frame1)
			Label2_5.place(relx=0.530, rely=0.155, height=27, width=114)
			Label2_5.configure(activebackground="#f9f9f9")
			Label2_5.configure(activeforeground="black")
			Label2_5.configure(background="#808080")
			Label2_5.configure(disabledforeground="#a3a3a3")
			Label2_5.configure(foreground="#000000")
			Label2_5.configure(highlightbackground="#d9d9d9")
			Label2_5.configure(highlightcolor="black")
			Label2_5.configure(text='''moderately infected''')
			
			Label2_6 = Label(Frame1)
			Label2_6.place(relx=0.850, rely=0.155, height=27, width=82)
			Label2_6.configure(activebackground="#f9f9f9")
			Label2_6.configure(activeforeground="black")
			Label2_6.configure(background="#808080")
			Label2_6.configure(disabledforeground="#a3a3a3")
			Label2_6.configure(foreground="#000000")
			Label2_6.configure(highlightbackground="#d9d9d9")
			Label2_6.configure(highlightcolor="black")
			Label2_6.configure(text='''not infected''')
			
			
			
				
			
			
			global path

	
			path=tryy.readBLOB(get_regi)
			print(path)
			model=get_model()
			predict(path,model)
			top.mainloop()
			
			
			
			 
			

			
			
			
			
	else:
		messagebox.showerror("ERROR","registration id can not be empty")

registration_list=[]
global reg_id


def back_command5():
    
    pivotal_form.form_page()
    

def list_formation():

	global reg_id
	
	reg_id=StringVar()
	print(registration_list)
	reg_id=str(registration_list[0])
	print(reg_id)
	start_ml()

def next_no(sign_a):
	sign=sign_a
	global reg_id
	reg_id=get_regi
	if sign=="+":
		print(reg_id,"old")
		elem=reg_id
		reg_id=registration_list[registration_list.index(elem)+1]
		print(reg_id,"new",registration_list.index(reg_id))
		start_ml()
	if sign=="-":
		print(reg_id,"old")
		elem=reg_id
		reg_id=registration_list[registration_list.index(elem)-1]
		print(reg_id,"new",registration_list.index(reg_id))
		start_ml()
	if sign == "=":
			pass
	

	


def multi_predict_screen():
    pivotal_form.form_screen.destroy()
    
    global multi_screen
    multi_screen= Tk()

    width_value=multi_screen.winfo_screenwidth()
    height_value=multi_screen.winfo_screenheight()
    multi_screen.geometry("%dx%d+0+0"%(width_value,height_value))
    #form_screen.minsize(w_x,w_y)
    #register_screen.maxsize(1924, 1055)
    multi_screen.resizable(0,0)
    multi_screen.title("Multiple Prediction")
    multi_screen.configure(background="#002448")

    global get_reg
    global get_ename
    global name_ebox
    global Entry1_reg
    global get_reg_no
    global count
    global numberss
	

    
    get_reg_no=StringVar()
    get_reg= StringVar()
    get_ename=StringVar()


    numberss=1
    
    
    
    def addToList(event=None):
        registration_id=name_ebox.get()
        print(len(registration_list))
        while len(registration_list) < int(numberss):
            registration_list.append(registration_id)
            name_ebox.delete(0,END)
            name_box['text']="Enter Registration Id Of '"+str(len(registration_list)+1)+"'"
            break
        else:
            print("list length over please press submit")
           


    
    

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
   
    
   
    Canvas1 = Canvas(multi_screen)
    Canvas1.place(relx=0.072, rely=0.051, relheight=0.804 , relwidth=0.847)
    Canvas1.configure(background="#808080")
    Canvas1.configure(borderwidth="2")
    Canvas1.configure(highlightbackground="#808080")
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
    Label1.configure(highlightbackground="#808080")
    Label1.configure(highlightcolor="#808080")
    Label1.configure(text='''Fill Customer Details''')

    registration = Label(Canvas1)
    registration.place(relx=0.209, rely=0.24, height=40, width=250)    
    registration.configure(background="#808080")
    registration.configure(disabledforeground="#a3a3a3")
    registration.configure(font=font9)
    registration.configure(foreground="#000000")
    registration.configure(text='''Enter number of registration.''')
    
    
    def check_num(event=None):
        global numberss
        
        numberss=get_reg_no.get()
        print(numberss)
    
    #get_reg_no.set(1)
    Entry1_reg = OptionMenu(Canvas1,get_reg_no,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
    Entry1_reg.place(relx=0.428, rely=0.24,height=40, relwidth=0.317)
    #Entry1_reg.configure(background="white")
    Entry1_reg.configure(disabledforeground="#a3a3a3")
    Entry1_reg.configure(font="TkFixedFont")
    Entry1_reg.configure(foreground="#000000")
    #Entry1_reg.configure(insertbackground="black")
    #Entry1_reg.configure(textvariable="get_reg_no")
    Entry1_reg.bind('<Button>',check_num)
    
    


    
    

    name_box = Label(Canvas1)
    name_box.place(relx=0.209, rely=0.412, height=40, width=250)
    name_box.configure(background="#808080")
    name_box.configure(disabledforeground="#a3a3a3")
    name_box.configure(font=font9)
    name_box.configure(foreground="#000000")
    name_box.configure(text="Enter Registration Id Of 1st")
        
    name_ebox = Entry(Canvas1)
    name_ebox.place(relx=0.428, rely=0.412,height=40, relwidth=0.317)
    name_ebox.configure(background="white")
    name_ebox.configure(disabledforeground="#a3a3a3")
    name_ebox.configure(font="TkFixedFont")
    name_ebox.configure(foreground="#000000")
    name_ebox.configure(highlightbackground="#d9d9d9")
    name_ebox.configure(highlightcolor="black")
    name_ebox.configure(insertbackground="black")
    name_ebox.configure(selectbackground="blue")
    name_ebox.configure(selectforeground="white")
    name_ebox.configure(textvariable=get_reg)

    name_ebox.bind('<Return>',addToList)


  
    Button1 = Button(Canvas1,command=list_formation)
    Button1.place(relx=0.385, rely=0.635, height=45, width=306)
    Button1.configure(activebackground="#ececec")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#092748")
    Button1.configure(borderwidth="5")
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(font="-family {Segoe UI Black} -size 14 -weight bold -slant roman -underline 0 -overstrike 0")
    Button1.configure(foreground="#ffffff")
    Button1.configure(highlightbackground="#808080")
    Button1.configure(highlightcolor="black")
    Button1.configure(overrelief="raised")
    Button1.configure(padx="5")
    Button1.configure(pady="5")
    Button1.configure(text='submit')

    
    Button2 = Button(multi_screen)
    Button2.place(relx=0.0, rely=0.0, height=40, width=66)
    Button2.configure(activebackground="#ececec")
    Button2.configure(activeforeground="#000000")
    Button2.configure(background="#808080")
    Button2.configure(command=back_command5)
    Button2.configure(disabledforeground="#a3a3a3")
    Button2.configure(foreground="#000000")
    Button2.configure(highlightbackground="#d9d9d9")
    Button2.configure(highlightcolor="black")
    Button2.configure(pady="0")
    Button2.configure(relief="flat")
    Button2.configure(text='''Back''')

    multi_screen.mainloop()


#multi_predict_screen()
#print(registration_list)	







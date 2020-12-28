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


conn = sqlite3.connect("patients_pivotal_record.db")

s1=conn.cursor()

conn.commit()



def end_process():
	os.remove(path)
	feedback1=feedback_Entry.get("1.0","end")
	try:
		s1.execute("UPDATE patients_records_pivotal SET feedback=? WHERE patient_id='"+get_regi+"'",([feedback1]))
		conn.commit()
		print("done")
	except sqlite3.Error as err:
		print("task failed")

	load.loadBLOB(get_regi)



def get_model():
	#model=load_model(covid19.model)	
	model=tf.keras.models.load_model('covid19.model')
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
	
	

	





	
def start_ml():
	
	global top
	global get_regi 
	global feedback_Entry
	
	try:
		get_regi= pivotal_form.get_reg.get()
		get_enamei=pivotal_form.get_ename.get()
		pivotal_form.Entry1_reg.delete(0,END)
		pivotal_form.name_ebox.delete(0,END)
	except:
		pivotal_form.filename=""
		get_regi= pivotal_form.p_id
	
	
	
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
				
				
		
				

			

		#print(record)
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
			top.geometry("1656x992+252+14")
			#top.minsize(120, 1)
			top.maxsize(1924, 1061)
			top.resizable(1, 1)
			top.title("New Toplevel")
			top.configure(background="#002448")
			
			Frame1 = Frame(top)
			Frame1.place(relx=0.024, rely=0.04, relheight=0.897, relwidth=0.961)
			Frame1.configure(relief='sunken')
			Frame1.configure(borderwidth="2")
			Frame1.configure(relief="sunken")
			Frame1.configure(background="#c0c0c0")
			
			
			#photo_location = os.path.join(prog_location,"LOGO_v1.png")
			img = Image.open(r"LOGO_v2.jpg")
			img = img.resize((240, 102), Image.ANTIALIAS)
			
			img0 = ImageTk.PhotoImage(img,master=Frame1)
			
			Label1=Label(Frame1,image=img0)
			Label1.image=img0
			Label1.place(relx=0.842, rely=0.011, height=102, width=240)
			
			
			TSeparator1 =ttk.Separator(Frame1)
			TSeparator1.place(relx=0.248, rely=0.007, relheight=0.985)
			TSeparator1.configure(orient="vertical")
			
			Label2 = Label(Frame1)
			Label2.place(relx=0.038, rely=0.022, height=65, width=258)
			Label2.configure(background="#c0c0c0")
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
			Button1.place(relx=0.471, rely=0.921, height=44, width=457)
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
			
			Label5_3 = Label(Frame1)
			Label5_3.place(relx=0.088, rely=0.156, height=32, width=237)
			Label5_3.configure(activebackground="#f9f9f9")
			Label5_3.configure(activeforeground="black")
			Label5_3.configure(background="#ffffff")
			Label5_3.configure(disabledforeground="#a3a3a3")
			Label5_3.configure(foreground="#000000")
			Label5_3.configure(highlightbackground="#d9d9d9")
			Label5_3.configure(highlightcolor="black")
			Label5_3.configure(text=ids)
			
			Label5_4 = Label(Frame1)
			Label5_4.place(relx=0.088, rely=0.213, height=31, width=237)
			Label5_4.configure(activebackground="#f9f9f9")
			Label5_4.configure(activeforeground="black")
			Label5_4.configure(background="#ffffff")
			Label5_4.configure(disabledforeground="#a3a3a3")
			Label5_4.configure(foreground="#000000")
			Label5_4.configure(highlightbackground="#d9d9d9")
			Label5_4.configure(highlightcolor="black")
			Label5_4.configure(text=name)
			
			Label5_5 = Label(Frame1)
			Label5_5.place(relx=0.088, rely=0.267, height=31, width=237)
			Label5_5.configure(activebackground="#f9f9f9")
			Label5_5.configure(activeforeground="black")
			Label5_5.configure(background="#ffffff")
			Label5_5.configure(disabledforeground="#a3a3a3")
			Label5_5.configure(foreground="#000000")
			Label5_5.configure(highlightbackground="#d9d9d9")
			Label5_5.configure(highlightcolor="black")
			Label5_5.configure(text=gender)
			
			Label5_5 = Label(Frame1)
			Label5_5.place(relx=0.019, rely=0.427, height=92, width=339)
			Label5_5.configure(activebackground="#f9f9f9")
			Label5_5.configure(activeforeground="black")
			Label5_5.configure(background="#fdfdfd")
			Label5_5.configure(disabledforeground="#a3a3a3")
			Label5_5.configure(foreground="#000000")
			Label5_5.configure(highlightbackground="#d9d9d9")
			Label5_5.configure(highlightcolor="black")
			Label5_5.configure(text=history)
			
			Label5_5 = Label(Frame1)
			Label5_5.place(relx=0.088, rely=0.326, height=31, width=237)
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
			feedback_Entry.place(relx=0.019, rely=0.607,height=150, relwidth=0.21)
			feedback_Entry.insert(INSERT, feed)
			
			Label5_6 = Label(Frame1)
			Label5_6.place(relx=0.019, rely=0.562, height=33, width=338)
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
			Label5_7.place(relx=0.019, rely=0.831, height=33, width=328)
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
			Label5_11.place(relx=0.019, rely=0.382, height=32, width=344)
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
			Label2.configure(background="#c0c0c0")
			Label2.configure(disabledforeground="#a3a3a3")
			Label2.configure(foreground="#000000")
			Label2.configure(text='''highly infected''')
			
			Label2_5 = Label(Frame1)
			Label2_5.place(relx=0.530, rely=0.155, height=27, width=114)
			Label2_5.configure(activebackground="#f9f9f9")
			Label2_5.configure(activeforeground="black")
			Label2_5.configure(background="#c0c0c0")
			Label2_5.configure(disabledforeground="#a3a3a3")
			Label2_5.configure(foreground="#000000")
			Label2_5.configure(highlightbackground="#d9d9d9")
			Label2_5.configure(highlightcolor="black")
			Label2_5.configure(text='''moderately infected''')
			
			Label2_6 = Label(Frame1)
			Label2_6.place(relx=0.850, rely=0.155, height=27, width=82)
			Label2_6.configure(activebackground="#f9f9f9")
			Label2_6.configure(activeforeground="black")
			Label2_6.configure(background="#c0c0c0")
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
	





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
	img = img.resize((250, 250), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img,master=second_frame)
	panel= Label(second_frame ,image=img)
	panel.image = img
	
	panel.grid(row=15,column=3)
	heat_map(model,path)
	if (result>0.5):
		label=Label(second_frame,compound=tk.RIGHT,text='Covid Infected',font = "Helvetica 16 bold").grid(row=19,column=3)
		return
	
		
	else:
		Labelx=tk.Label(second_frame,compound=tk.RIGHT,text='Normal',font = "Helvetica 16 bold").grid(row=19,column=3)
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
	
	output_image = cv2.addWeighted(cv2.cvtColor(img.astype('uint8'), cv2.COLOR_RGB2BGR), 0.5, cam, 1, 0)
	img = Image.fromarray(output_image)
	cv2.imwrite('detect.png',output_image)
	img = img.resize((250, 250), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img,master=second_frame)
	panel = Label(second_frame, image=img ) #,compound=root_ml
	panel.image = img

	panel.grid(row=17,column=3)#root_ml was in brackets
	
	

	





	
def start_ml():
	
	global second_frame
	global get_regi 
	
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
			
			global root_ml
			root_ml=Tk()
			root_ml.title=("patient detalis")
			root_ml.geometry("1208x681+180+100")
			root_ml.configure(background="#002448")
			
			
			
			

			global feedback_Entry

			feedback_Entry = StringVar()

			main_frame=Frame(root_ml)
			main_frame.place(relx=0.072, rely=0.051, relheight=0.804 , relwidth=0.847)
			main_frame.configure(background="#c0c0c0")

			my_canvas=Canvas(main_frame)
			my_canvas.pack(side=LEFT, fill=BOTH,expand=1)

			my_scroll=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
			my_scroll.pack(side=RIGHT,fill=Y)

			my_canvas.configure(yscrollcommand=my_scroll.set)
			my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox('all')))
			
			second_frame=Frame(my_canvas)

			

			my_canvas.create_window((0,0), window=second_frame,anchor=NW)


			Label(second_frame, text="                   ").grid(row=0,column=0)
			Label(second_frame, text="                  ").grid(row=0,column=1)
			Label(second_frame, text="                                              ").grid(row=0,column=2)
			
			Label1 = Label(second_frame)
			Label1.grid(row=1,column=3)
			Label1.configure(activebackground="#000071")
			Label1.configure(activeforeground="white")
			Label1.configure(activeforeground="#f0f0f0f0f0f0")
			Label1.configure(background="#ababab")
			Label1.configure(borderwidth="5")
			Label1.configure(compound='center')
			Label1.configure(disabledforeground="#000040")
			Label1.configure(font="font9")
			Label1.configure(foreground="#000040")
			Label1.configure(highlightbackground="#c0c0c0")
			Label1.configure(highlightcolor="#c0c0c0")
			Label1.configure(text=''' Patient Details''')

			


			Label2 = Label(second_frame)
			Label2.grid(row=5,column=1)
			#Label2.configure(activebackground="#000071")
			#Label2.configure(activeforeground="white")
			#Label2.configure(activeforeground="#f0f0f0f0f0f0")
			#Label2.configure(background="#ababab")
			Label2.configure(borderwidth="5")
			Label2.configure(compound='center')
			#Label2.configure(disabledforeground="#000040")
			Label2.configure(font="font9")
			Label2.configure(foreground="#000040")
			#Label2.configure(highlightbackground="#c0c0c0")
			#Label2.configure(highlightcolor="#c0c0c0")
			Label2.configure(text=''' Id''')


			Label(second_frame, text=ids,font = "Helvetica 16 bold").grid(row=5, column=3)

			Label(second_frame, text="").grid(row=6,column=0)
			

			Label3 = Label(second_frame)
			Label3.grid(row=7,column=1)
			#Label2.configure(activebackground="#000071")
			#Label2.configure(activeforeground="white")
			#Label2.configure(activeforeground="#f0f0f0f0f0f0")
			#Label2.configure(background="#ababab")
			Label3.configure(borderwidth="5")
			Label3.configure(compound='center')
			#Label2.configure(disabledforeground="#000040")
			Label3.configure(font="font9")
			Label3.configure(foreground="#000040")
			#Label2.configure(highlightbackground="#c0c0c0")
			#Label2.configure(highlightcolor="#c0c0c0")
			Label3.configure(text=''' NAME''')

			
			Label(second_frame, text=name,font = "Helvetica 16 bold").grid(row=7, column=3)
			Label(second_frame, text="").grid(row=8,column=0)




			Label4 = Label(second_frame)
			Label4.grid(row=9,column=1)
			#Label2.configure(activebackground="#000071")
			#Label2.configure(activeforeground="white")
			#Label2.configure(activeforeground="#f0f0f0f0f0f0")
			#Label2.configure(background="#ababab")
			Label4.configure(borderwidth="5")
			Label4.configure(compound='center')
			#Label2.configure(disabledforeground="#000040")
			Label4.configure(font="font9")
			Label4.configure(foreground="#000040")
			#Label2.configure(highlightbackground="#c0c0c0")
			#Label2.configure(highlightcolor="#c0c0c0")
			Label4.configure(text=''' GENDER''')

			
			Label(second_frame, text=gender,font = "Helvetica 16 bold").grid(row=9, column=3)
			Label(second_frame, text="").grid(row=10,column=0)


			Label5 = Label(second_frame)
			Label5.grid(row=11,column=1)
			#Label2.configure(activebackground="#000071")
			#Label2.configure(activeforeground="white")
			#Label2.configure(activeforeground="#f0f0f0f0f0f0")
			#Label2.configure(background="#ababab")
			Label5.configure(borderwidth="5")
			Label5.configure(compound='center')
			#Label2.configure(disabledforeground="#000040")
			Label5.configure(font="font9")
			Label5.configure(foreground="#000040")
			#Label2.configure(highlightbackground="#c0c0c0")
			#Label2.configure(highlightcolor="#c0c0c0")
			Label5.configure(text=''' age''')

			Label(second_frame, text=age,font = "Helvetica 16 bold").grid(row=11, column=3)
			Label(second_frame, text="").grid(row=12,column=0)

			Label6 = Label(second_frame)
			Label6.grid(row=13,column=1)
			#Label2.configure(activebackground="#000071")
			#Label2.configure(activeforeground="white")
			#Label2.configure(activeforeground="#f0f0f0f0f0f0")
			#Label2.configure(background="#ababab")
			Label6.configure(borderwidth="5")
			Label6.configure(compound='center')
			#Label2.configure(disabledforeground="#000040")
			Label6.configure(font="font9")
			Label6.configure(foreground="#000040")
			#Label2.configure(highlightbackground="#c0c0c0")
			#Label2.configure(highlightcolor="#c0c0c0")
			Label6.configure(text=''' Medical History''')

			Label(second_frame, text=history,font = "Helvetica 16 bold").grid(row=13, column=3)
			Label(second_frame, text="").grid(row=14,column=0)
			Label7= Label(second_frame)
			Label7.grid(row=15,column=1)
			#Label2.configure(activebackground="#000071")
			#Label2.configure(activeforeground="white")
			#Label2.configure(activeforeground="#f0f0f0f0f0f0")
			#Label2.configure(background="#ababab")
			Label7.configure(borderwidth="5")
			Label7.configure(compound='center')
			#Label2.configure(disabledforeground="#000040")
			Label7.configure(font="font9")
			Label7.configure(foreground="#000040")
			#Label2.configure(highlightbackground="#c0c0c0")
			#Label2.configure(highlightcolor="#c0c0c0")
			Label7.configure(text=''' X-ray''')
			
			Label(second_frame, text="").grid(row=16,column=0)

			Label8= Label(second_frame)
			Label8.grid(row=17,column=1)
			#Label2.configure(activebackground="#000071")
			#Label2.configure(activeforeground="white")
			#Label2.configure(activeforeground="#f0f0f0f0f0f0")
			#Label2.configure(background="#ababab")
			Label8.configure(borderwidth="5")
			Label8.configure(compound='center')
			#Label2.configure(disabledforeground="#000040")
			Label8.configure(font="font9")
			Label8.configure(foreground="#000040")
			#Label2.configure(highlightbackground="#c0c0c0")
			#Label2.configure(highlightcolor="#c0c0c0")
			Label8.configure(text='''Result  X-ray''')


			
			Label(second_frame, text="").grid(row=18,column=0)

			Label9= Label(second_frame)
			Label9.grid(row=19,column=1)
			#Label2.configure(activebackground="#000071")
			#Label2.configure(activeforeground="white")
			#Label2.configure(activeforeground="#f0f0f0f0f0f0")
			#Label2.configure(background="#ababab")
			Label9.configure(borderwidth="5")
			Label9.configure(compound='center')
			#Label2.configure(disabledforeground="#000040")
			Label9.configure(font="font9")
			Label9.configure(foreground="#000040")
			#Label2.configure(highlightbackground="#c0c0c0")
			#Label2.configure(highlightcolor="#c0c0c0")
			Label9.configure(text='''Result''')


			Label(second_frame, text="").grid(row=20,column=0)


			Label10= Label(second_frame)
			Label10.grid(row=21,column=1)
			#Label2.configure(activebackground="#000071")
			#Label2.configure(activeforeground="white")
			#Label2.configure(activeforeground="#f0f0f0f0f0f0")
			#Label2.configure(background="#ababab")
			Label10.configure(borderwidth="5")
			Label10.configure(compound='center')
			#Label2.configure(disabledforeground="#000040")
			Label10.configure(font="font9")
			Label10.configure(foreground="#000040")
			#Label2.configure(highlightbackground="#c0c0c0")
			#Label2.configure(highlightcolor="#c0c0c0")
			Label10.configure(text='''Feedback''')








			
			feedback_Entry = Text(second_frame)
			feedback_Entry.grid(row=21,column=3)
			feedback_Entry.configure( height=10, width=50)
			feedback_Entry.configure(background="white")
			feedback_Entry.configure(font="TkFixedFont")
			feedback_Entry.configure(foreground="#000000")
			feedback_Entry.configure(highlightbackground="#c0c0c0")
			feedback_Entry.configure(highlightcolor="black")
			feedback_Entry.configure(insertbackground="black")
			feedback_Entry.configure(relief="groove")
			feedback_Entry.configure(selectbackground="blue")
			feedback_Entry.insert(INSERT, feed)

			Label(second_frame, text="").grid(row=22,column=0)


			
			Button1 = Button(second_frame, command=end_process)
			Button1.grid(row=23,column=3)
			Button1.configure (height=1, width=10)
			Button1.configure(activebackground="#ececec")
			Button1.configure(activeforeground="#000000")
			Button1.configure(background="#092748")
			Button1.configure(borderwidth="5")
			Button1.configure(disabledforeground="#a3a3a3")
			Button1.configure(font="-family {Segoe UI Black} -size 14 -weight bold -slant roman -underline 0 -overstrike 0")
			Button1.configure(foreground="#ffffff")
			Button1.configure(highlightbackground="#c0c0c0")
			Button1.configure(highlightcolor="black")
			Button1.configure(overrelief="raised")
			Button1.configure(padx="5")
			Button1.configure(pady="5")
			Button1.configure(text='submit')

			Label(second_frame, text="").grid(row=24,column=0)
			Label(second_frame, text="").grid(row=25,column=0)
			Label(second_frame, text="").grid(row=26,column=0)
				
			
			
			global path
	
			path=tryy.readBLOB(get_regi)
			print(path)
			model=get_model()
			predict(path,model)
			root_ml.mainloop()
			 
			

			
			
			
			
	else:
		messagebox.showerror("ERROR","registration id can not be empty")
	


#start_ml()



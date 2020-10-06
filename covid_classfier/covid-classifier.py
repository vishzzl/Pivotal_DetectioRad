import tensorflow as tf
from tensorflow.keras.preprocessing import image
import tkinter as tk
import numpy as np
from tkinter.filedialog import askopenfile
from PIL import Image,ImageTk
from PIL import ImageDraw 
import random
import cv2
from   tensorflow.keras.preprocessing.image import img_to_array, load_img
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def get_model():	
	model=tf.keras.models.load_model("covid19.model")
	print(model.summary())
	return model

def open_file():
	file= askopenfile(mode ='r')
	if file is not None:
		path=file.name
		print(path)
	return(path)

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
	img = ImageTk.PhotoImage(img)
	panel = tk.Label(root, image=img)
	panel.image = img
	panel.pack()
	heat_map(model,path)
	if (result>0.5):
		Label=tk.Label(root,compound=tk.RIGHT,text='Covid Infected',font = "Helvetica 16 bold").pack(side=tk.RIGHT)
		return
		
	else:
		Labelx=tk.Label(root,compound=tk.RIGHT,text='Normal',font = "Helvetica 16 bold").pack(side=tk.RIGHT)
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
	img = img.resize((250, 250), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = tk.Label(root, image=img,compound=tk.TOP )
	panel.image = img
	panel.pack(side=tk.TOP)

	
		
	   


def main():
	path=open_file()
	model=get_model()
	predict(path,model)
	
	
root=tk.Tk()
root.geometry("800x800")
root.resizable(width=True, height=True)
button=tk.Button(root,text='Open',command=main).pack()
root.mainloop()


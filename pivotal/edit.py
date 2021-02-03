
import os
import win32ui
from reportlab.pdfgen import canvas
from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
import tempfile
import win32com.client
import webbrowser 


def drawMyRuler(pdf):
    pdf.drawString(100,810, 'x100')
    pdf.drawString(200,810, 'x200')
    pdf.drawString(300,810, 'x300')
    pdf.drawString(400,810, 'x400')
    pdf.drawString(500,810, 'x500')

    pdf.drawString(10,100, 'y100')
    pdf.drawString(10,200, 'y200')
    pdf.drawString(10,300, 'y300')
    pdf.drawString(10,400, 'y400')
    pdf.drawString(10,500, 'y500')
    pdf.drawString(10,600, 'y600')
    pdf.drawString(10,700, 'y700')
    pdf.drawString(10,800, 'y800') 








# ###################################
# Content
fileName = 'MyDoc.pdf'
documentTitle = 'Medical Report'
title = ' X-ray Report'
subTitle = '(AI Generated report)'

textLines = [
'The Tasmanian devil (Sarcophilus harrisii) is',
'a carnivorous marsupial of the family',
'Dasyuridae.'
]

image = 'pivotal\LOGO_v1.png'


# ###################################
# 0) Create document 


pdf = canvas.Canvas(fileName)
pdf.setTitle(documentTitle)



#drawMyRuler(pdf)
# ###################################
# 1) Title :: Set fonts 
# # Print available fonts
# for font in pdf.getAvailableFonts():
#     print(font)










# ###################################
# 2) Sub Title 
# RGB - Red Green and Blue
pdf.setFillColorRGB(0, 0, 255)
pdf.setFont("Courier-Bold", 24)
pdf.drawCentredString(290,720, title)


sub=pdf.beginText(225,705)
sub.setFont('Courier',12)
sub.setFillColor(colors.black)
sub.textLine(subTitle)
pdf.drawText(sub)


reg=pdf.beginText(50,670)
reg.setFont("Courier-Bold",16)
reg.setFillColor(colors.black)
reg.textLine("Registration no.:")
pdf.drawText(reg)


reg_p=pdf.beginText(230,670)
reg_p.setFont("Courier",16)
reg_p.setFillColor(colors.black)
reg_p.textLine("123")
pdf.drawText(reg_p)

age=pdf.beginText(360,670)
age.setFont("Courier-Bold",16)
age.setFillColor(colors.black)
age.textLine("Age:")
pdf.drawText(age)

age_p=pdf.beginText(410,670)
age_p.setFont("Courier",16)
age_p.setFillColor(colors.black)
age_p.textLine("12")
pdf.drawText(age_p)

name_p=pdf.beginText(120,630)
name_p.setFont("Courier",16)
name_p.setFillColor(colors.black)
name_p.textLine("vidhika")
pdf.drawText(name_p)


name=pdf.beginText(50,630)
name.setFont("Courier-Bold",16)
name.setFillColor(colors.black)
name.textLine("Name:")
pdf.drawText(name)

sex=pdf.beginText(360,630)
sex.setFont("Courier-Bold",16)
sex.setFillColor(colors.black)
sex.textLine("Sex:")
pdf.drawText(sex)

sex_p=pdf.beginText(410,630)
sex_p.setFont("Courier",16)
sex_p.setFillColor(colors.black)
sex_p.textLine("F")
pdf.drawText(sex_p)

covid=pdf.beginText(50,590)
covid.setFont("Courier-Bold",16)
covid.setFillColor(colors.black)
covid.textLine("Covid-19 Predicted Result:")
pdf.drawText(covid)

covid_r=pdf.beginText(320,590)
covid_r.setFont("Courier-Bold",16)
covid_r.setFillColor(colors.blue)
covid_r.textLine("Negative")
pdf.drawText(covid_r)



med=pdf.beginText(50,540)
med.setFont("Courier-Bold",16)
med.setFillColor(colors.black)
med.textLine("Medical History:")
pdf.drawText(med)

drf=pdf.beginText(50,430)
drf.setFont("Courier-Bold",16)
drf.setFillColor(colors.black)
drf.textLine("Doctor's Feedback:")
pdf.drawText(drf)

comment = pdf.beginText(70, 400)
comment.setFont("Courier", 16)
comment.setFillColor(colors.red)
for line in textLines:
    comment.textLine(line)

pdf.drawText(comment)




# ###################################
# 3) Draw a line
pdf.line(30, 690, 550,690 )

pdf.line(30, 90, 550,90 )

drm=pdf.beginText(50,110)
drm.setFont('Courier',12)
drm.setFillColor(colors.black)
drm.textLine("doctor's name, Degree")
pdf.drawText(drm)

sig=pdf.beginText(360,110)
sig.setFont('Courier',12)
sig.setFillColor(colors.black)
sig.textLine("doctor' Signature")
pdf.drawText(sig)











# ###################################
# 4) Text object :: for large amounts of text


text = pdf.beginText(70, 510)
text.setFont("Courier", 16)
text.setFillColor(colors.red)
for line in textLines:
    text.textLine(line)

pdf.drawText(text)





# ###################################
# 5) Draw a image
pdf.drawInlineImage(image, 50,750, width=500,height=100)




pdf.save()








chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
chrome_path_NW = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --new-window"
firefox_path = "C:\\Program Files\\Mozilla Firefox\\Firefox.exe"


controller = webbrowser.get(chrome_path)
controllerNW = webbrowser.get(chrome_path_NW)

controller.open("MyDoc.pdf", new=2)




#os.remove("MyDoc.pdf")


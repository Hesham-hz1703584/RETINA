import tkinter as tk
import pandas as pd
import numpy as np
import cv2 as cv
from tkinter import *
from tkinter import filedialog, Text
from PIL import Image, ImageTk

# =================================MAIN=================================
# Main Window Layout
root = tk.Tk()
root.resizable(width=0, height=0)
defaultbg = root.cget('bg')
canvas = tk.Canvas(root, height=600, width=1250, bg='white')
canvas.grid()
df = pd.read_csv('D:/Hesham/HBKU/RA/Rertina/TestData.csv', delimiter=';')

#Global Data




# ENTRIES
PhotoEntry = Text(canvas, width=30, height=10, font='Helvetica 16', bg=defaultbg)
PhotoEntry.place(x=20, y=50)
PhotoEntry.config(state="disabled")

CroppedPhoto = Text(canvas, width=30, height=10, font='Helvetica 16', bg=defaultbg)
CroppedPhoto.place(x=400, y=50)
CroppedPhoto.config(state="disabled")

DiagnosisEntry = Text(canvas, width=62, height=8, font='Helvetica 16', bg=defaultbg)
DiagnosisEntry.place(x=20, y=400)
DiagnosisEntry.config(state="disabled")


def click(event):
    CommentsEntry.config(state=NORMAL)
    CommentsEntry.delete('1.0', END)


CommentsEntry = Text(canvas, width=35, height=6, font='Helvetica 16', bg='light grey', borderwidth=2, border=2)
CommentsEntry.place(x=170, y=440)
CommentsEntry.insert(INSERT, "Doctor's Comments:")
# CommentsEntry.config(state="disabled")
# CommentsEntry.bind("<Button-1>", click)

GTruthEntry = Text(canvas, width=35, height=6, font='Helvetica 16', bg='light grey')
GTruthEntry.place(x=800, y=50)
GTruthEntry.config(state="disabled")

DsummaryEntry = Text(canvas, width=35, height=6, font='Helvetica 16', bg='light grey')
DsummaryEntry.place(x=800, y=205)
DsummaryEntry.config(state="disabled")

StatisticsEntry = Text(canvas, width=35, height=6, font='Helvetica 16', bg='light grey')
StatisticsEntry.place(x=800, y=360)
StatisticsEntry.config(state="disabled")

# labels
DiagnosisLable = tk.Label(canvas, text='Diagnosis', font='Helvetica 16', bg='white')
DiagnosisLable.place(x=350, y=15)

DiagnosisLable = tk.Label(canvas, text='Diagnose:', font='Helvetica 16')
DiagnosisLable.place(x=26, y=405)

l1 = tk.Label(canvas, text='Model'"'"'s Prediction', font='Helvetica 16', bg='light grey')
l1.place(x=815, y=215)

l2 = tk.Label(canvas, text='Evaluation', font='Helvetica 16', bg='white')
l2.place(x=950, y=10)

ModelPredLable = tk.Label(canvas, text='-  Model'"'"'s Diagnosis: Diabetic (76.3%)', font='Helvetica 16',
                          bg='light grey')
ModelPredLable.place(x=815, y=245)

GroundTruthData = tk.Label(canvas, text='-  Actual Diagnosis: Diabetic', font='Helvetica 16', bg='light grey')
GroundTruthData.place(x=815, y=275)

l2 = tk.Label(canvas, text='Doctor'"'"'s Statistics:', font='Helvetica 16', bg='light grey')
l2.place(x=815, y=370)

l3 = tk.Label(canvas, text='-  Number of evaluated cases: 5', font='Helvetica 16', bg='light grey')
l3.place(x=815, y=400)

l4 = tk.Label(canvas, text='-  Number of correct diagnosis: 4', font='Helvetica 16', bg='light grey')
l4.place(x=815, y=430)

l5 = tk.Label(canvas, text='-  Number of incorrect diagnosis: 1', font='Helvetica 16', bg='light grey')
l5.place(x=815, y=460)
# =================================BUTTONS=================================
# buttons
Uploadbtn = tk.Button(canvas, text='Upload', font=('Helvetica 16', 15), command=lambda: upload_file(), bg='#6495ED',
                      fg='white', width=10, height=2)
Uploadbtn.place(x=140, y=315)
Cropbtn = tk.Button(canvas, text='Crop', font=('Helvetica 16', 15), command=lambda: RetinaDetiction(imge) ,bg='#6495ED', fg='white', width=10, height=2)
Cropbtn.place(x=525, y=315)
SDbtn = tk.Button(canvas, text='SubmitDiagnosis', font=('Helvetica 16', 12), bg='#6495ED', fg='white', width=13,
                  height=3)
SDbtn.place(x=620, y=440)
DRbtn = tk.Button(canvas, text='DiagnosisReport', font=('Helvetica 16', 12), command=lambda: evaluation_tab(var.get()),
                  bg='#6495ED', fg='white', width=13, height=3)
DRbtn.place(x=620, y=520)
PDFbtn = tk.Button(canvas, text='Generate PDF', font=('Helvetica 16', 12), bg='#6495ED', fg='white', width=13, height=3)
PDFbtn.place(x=1100, y=530)
# =================================Radiobutton=================================
var = IntVar()
Radiobutton(root, text="DIABETIC", font=('Helvetica 16', 15), variable=var, value=1).place(x=35, y=450)
Radiobutton(root, text="NORMAL", font=('Helvetica 16', 15), variable=var, value=2).place(x=35, y=480)


# if (value == 1):
# value = "Diabetic"

# if (value == 2):
# value = "Normal"

# =================================FUNCTIONS=================================
# Upload_file
def upload_file():
    f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]  # type of files to select
    filename = tk.filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)  # read the image file
    print(filename)
    img = img.resize((360, 245))  # new width & height
    img = ImageTk.PhotoImage(img)
    e1 = tk.Label(canvas)
    e1.place(x=19, y=46)
    e1.image = img
    e1['image'] = img  # garbage collection
    HcNo = filename.split('.')
    HcNo = HcNo[0].split('/')
    HcNo = HcNo[-1].split()[0]
    GenerateGroundTruth(HcNo)

    image = cv.imread(filename)
    output = image.copy()
    img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # Find circles
    circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1.3, 100)
    # If some circle is found
    if circles is not None:
        # Get the (x, y, r) as integers
        circles = np.round(circles[0, :]).astype("int")
        print(circles)
        # loop over the circles
        for (x, y, r) in circles:
            cv.circle(output, (x, y), r, (0, 255, 0), 2)
    # show the output image
    cv.imshow("circle", output)
    cv.waitKey(0)


    RetinaDetiction(filename)





def GenerateGroundTruth(HcNo):
    Data = df.loc[df.HCnumber == HcNo]
    DataFiltered = np.array(Data.get(['Gender', 'Age', 'Nationality', 'HCnumber', 'Diagnosis']))
    GTruthEntry = Text(canvas, width=35, height=6, font='Helvetica 16', bg='light grey')
    GTruthEntry.place(x=800, y=50)
    GroundTruth = tk.Label(canvas, text=f'Gender: {DataFiltered[0][0]}', font='Helvetica 16', bg='light grey')
    GroundTruth.place(x=815, y=55)
    GroundTruth = tk.Label(canvas, text=f'Age: {DataFiltered[0][1]}', font='Helvetica 16', bg='light grey')
    GroundTruth.place(x=815, y=82)
    GroundTruth = tk.Label(canvas, text=f'Nationality: {DataFiltered[0][2]}', font='Helvetica 16', bg='light grey')
    GroundTruth.place(x=815, y=110)
    GroundTruth = tk.Label(canvas, text=f'HC Number: {DataFiltered[0][3]}', font='Helvetica 16', bg='light grey')
    GroundTruth.place(x=815, y=138)
    GroundTruth = tk.Label(canvas, text=f'Diagnosis: {DataFiltered[0][4]}', font='Helvetica 16', bg='light grey')
    GroundTruth.place(x=815, y=165)

def RetinaDetiction(ImgPath):
    print(ImgPath)

# =================================CALLING ROOT=================================
root.mainloop()

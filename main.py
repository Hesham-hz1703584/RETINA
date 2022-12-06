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
df = pd.read_csv('G:/HBKU/Work/TestData.csv', delimiter=';')

# global data
DataFiltered = np.array(0)
No_Diagnosis = 0
NoC_Diagnosis = 0
NoW_Diagnosis = 0

# ENTRIES
PhotoEntry = Text(canvas, width=30, height=10, font='Helvetica 16', bg=defaultbg)
PhotoEntry.place(x=20, y=50)
PhotoEntry.config(state="disabled")

CroppedPhoto = Text(canvas, width=21, height=10, font='Helvetica 16', bg=defaultbg)
CroppedPhoto.place(x=460, y=50)
CroppedPhoto.config(state="disabled")

GTruthEntry = Text(canvas, width=35, height=6, font='Helvetica 16', bg='light grey')
GTruthEntry.place(x=800, y=50)
GTruthEntry.config(state="disabled")

DsummaryEntry = Text(canvas, width=35, height=6, font='Helvetica 16', bg='light grey')
DsummaryEntry.place(x=800, y=205)
DsummaryEntry.config(state="disabled")

StatisticsEntry = Text(canvas, width=35, height=6, font='Helvetica 16', bg='light grey')
StatisticsEntry.place(x=800, y=360)
StatisticsEntry.config(state="disabled")

DiagnosisEntry = Text(canvas, width=62, height=8, font='Helvetica 16', bg=defaultbg)
DiagnosisEntry.place(x=20, y=400)
DiagnosisEntry.config(state="disabled")

CommentsEntry = Text(canvas, width=35, height=6, font='Helvetica 16', bg='light grey', borderwidth=2, border=2)
CommentsEntry.place(x=170, y=440)
CommentsEntry.insert(INSERT, "Doctor's Comments:")
# labels
DiagnosisLable = tk.Label(canvas, text='Diagnosis', font='Helvetica 16', bg='white')
DiagnosisLable.place(x=350, y=15)

DiagnosisLable = tk.Label(canvas, text='Diagnose:', font='Helvetica 16')
DiagnosisLable.place(x=26, y=405)

# =================================BUTTONS=================================
# buttons

# Global Data
ImgPath = ''

Uploadbtn = tk.Button(canvas, text='Upload', font=('Helvetica 16', 15), command=lambda: upload_file(), bg='#6495ED',
                      fg='white', width=10, height=2)
Uploadbtn.place(x=140, y=315)
Cropbtn = tk.Button(canvas, text='Crop', font=('Helvetica 16', 15), command=lambda: CropImg(ImgPath), bg='#6495ED',
                    fg='white', width=10, height=2)
Cropbtn.place(x=525, y=315)
SDbtn = tk.Button(canvas, text='SubmitDiagnosis', font=('Helvetica 16', 12), command=lambda: SubmitDiagnosis(var.get()),
                  bg='#6495ED',
                  fg='white', width=13, height=3)
SDbtn.place(x=620, y=440)
DRbtn = tk.Button(canvas, text='DiagnosisReport', font=('Helvetica 16', 12), bg='#6495ED', fg='white', width=13,
                  height=3)
DRbtn.place(x=620, y=520)
PDFbtn = tk.Button(canvas, text='Generate PDF', font=('Helvetica 16', 12), bg='#6495ED', fg='white', width=13, height=3)
PDFbtn.place(x=1100, y=530)
# =================================Radiobutton=================================
var = IntVar()
Radiobutton(root, text="DIABETIC", font=('Helvetica 16', 15), variable=var, value=1).place(x=35, y=450)
Radiobutton(root, text="NORMAL", font=('Helvetica 16', 15), variable=var, value=2).place(x=35, y=480)


# =================================FUNCTIONS=================================
# Upload_file
def upload_file():
    global ImgPath

    # Cleaning Data
    DsummaryEntry.config(state="normal")
    DsummaryEntry.delete("1.0", "end")
    DsummaryEntry.config(state="disabled")
    GTruthEntry.config(state="normal")
    GTruthEntry.delete("1.0", "end")
    GTruthEntry.config(state="disabled")

    # Choosing Photo
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
    ImgPath = filename


def GenerateGroundTruth(HcNo):
    global DataFiltered
    # Allocating Data and filtering it
    Data = df.loc[df.HCnumber == HcNo]
    DataFiltered = np.array(Data.get(['Gender', 'Age', 'Nationality', 'Group', 'HCnumber', 'Diagnosis']))

    # Data Generation and Placement
    GTruthEntry.config(state="normal")
    GTruthEntry.delete("1.0", "end")
    GTruthEntry.insert(INSERT, f'\t   Ground Truth Data \n   Gender: {DataFiltered[0][0]}\n'
                               f'   Age: {DataFiltered[0][1]}\n'
                               f'   Nationality: {DataFiltered[0][2]}\n'
                               f'   HC Number: {DataFiltered[0][4]}\n')
    GTruthEntry.config(state="disabled")


def CropImg(ImgPath):
    # Load image, convert to grayscale, and find edges
    image = cv.imread(ImgPath)

    # Resize
    scale_percent = 25  # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    image = cv.resize(image, dim, interpolation=cv.INTER_AREA)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    thresh = cv.threshold(gray, 0, 255, cv.THRESH_OTSU + cv.THRESH_BINARY)[1]

    # Find contour and sort by contour area
    cnts = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=cv.contourArea, reverse=True)

    # Find bounding box and extract ROI
    for c in cnts:
        x, y, w, h = cv.boundingRect(c)
        ROI = image[y:y + h, x:x + w]
        break

    # Place image
    blue, green, red = cv.split(ROI)
    img = cv.merge((red, green, blue))
    im = Image.fromarray(img)
    im = im.resize((250, 240))  # new width & height
    imgtk = ImageTk.PhotoImage(image=im)
    e1 = tk.Label(canvas)
    e1.place(x=460, y=50)
    e1.image = imgtk
    e1['image'] = imgtk  # garbage collection

    cv.waitKey()


def SubmitDiagnosis(choice):
    global No_Diagnosis
    global NoC_Diagnosis
    global NoW_Diagnosis

    # Diagnosis Data
    Diagnos = ''
    DrDiagnosis = ''
    if int(DataFiltered[0][3]) < 3:
        Diagnos = "Diabetic"
    if int(DataFiltered[0][3]) >= 3:
        Diagnos = "Normal"

    if choice != 0:
        if choice == 1:
            DrDiagnosis = "Diabetic"
        if choice == 2:
            DrDiagnosis = "Normal"
        DsummaryEntry.config(state="normal")
        DsummaryEntry.delete("1.0", "end")
        DsummaryEntry.insert(INSERT,
                             f'\t         Evaluation\n\n   Doctor Diagnosis: {DrDiagnosis}\n   Actual Diagnosis: {Diagnos}')
        DsummaryEntry.config(state="disabled")

    No_Diagnosis += 1
    if Diagnos == DrDiagnosis:
        NoC_Diagnosis += 1
    else:
        NoW_Diagnosis += 1

    # Diagnosis info
    StatisticsEntry.config(state="normal")
    StatisticsEntry.delete("1.0", "end")
    StatisticsEntry.insert(INSERT, f'\t   Doctors Statistics\n\n' f'    Number of evaluated cases: {No_Diagnosis}\n'
                                   f'    Number of correct diagnosis: {NoC_Diagnosis}\n'
                                   f'    Number of incorrect diagnosis: {NoW_Diagnosis}')
    StatisticsEntry.config(state="disabled")


# l2 = tk.Label(canvas, text='Doctor'"'"'s Statistics:', font='Helvetica 16', bg='light grey')

# =================================CALLING ROOT=================================
root.mainloop()

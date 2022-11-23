import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os
from PIL import Image, ImageTk

#hello

#=================================MAIN=================================
# Main Window Layout
root = tk.Tk()
root.resizable(width=0, height=0)
defaultbg = root.cget('bg')
canvas = tk.Canvas(root, height=720, width=1024)
canvas.grid()

#labels
PhotoLable = tk.Label(canvas, text='Photo', font=('Berlin Sans FB', 25))
PhotoLable.place(x= 50, y= 25)

DiagnosisLable = tk.Label(canvas, text='Diagnosis', font=('Berlin Sans FB', 25))
DiagnosisLable.place(x= 512, y= 25)

DoctorsLable = tk.Label(canvas, text='DOCTOR'"'"'S Diagnosis', font=('Berlin Sans FB', 25))
DoctorsLable.place(x= 50, y= 500)

DoctorsDescLable = tk.Label(canvas, text='DOCTOR'"'"'S Description (if any)', font=('Berlin Sans FB', 25))
DoctorsDescLable.place(x= 512, y= 500)

#ENTRIES
PhotoEntry = Text(canvas, width=29, height=14, font=('Helvetica 16'), bg= defaultbg)
PhotoEntry.place(x= 50, y= 75)
PhotoEntry.config(state="disabled")

DiagnosisEntry = Text(canvas, width=40, height=14, font=('Helvetica 16'), bg = "white")
DiagnosisEntry.place(x=512, y=75)
DiagnosisEntry.config(state="disabled")

DrDiagnosisEntry = Text(canvas, width=40, height=5, font=('Helvetica 16'), bg = "white")
DrDiagnosisEntry.place(x=512, y=550)

#=================================BUTTONS=================================
# button frame
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
# buttons
btn1 = tk.Button(buttonframe, text='Upload Files', font=('Helvetica 16', 18), command=lambda: upload_file(), bg= 'black', fg='white', activebackground= 'Black', width= 24)
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
btn2 = tk.Button(buttonframe, text='Diagnose', font=('Helvetica 16', 18), command=lambda: diagnose(),bg= 'black', fg='white' , activebackground= 'Black', width= 24)
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
btn3 = tk.Button(buttonframe, text='Evaluate', font=('Helvetica 16', 18), command=lambda: evaluation_tab(var.get()), bg= 'black', fg='white', activebackground= 'Black', width=24)
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
buttonframe.grid()

#=================================Radiobutton=================================
var = IntVar()
Radiobutton(root, text="DIABETIC", font=('Helvetica 16', 25), variable=var, value=1).place(x= 50, y= 550)
Radiobutton(root, text="NORMAL",  font=('Helvetica 16', 25), variable=var, value=2).place(x= 50, y= 600)



#=================================FUNCTIONS=================================
# Upload_file
def upload_file():
    f_types = [('Jpg Files', '*.jpg'),('PNG Files', '*.png')]  # type of files to select
    filename = tk.filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)  # read the image file
    img = img.resize((350, 350))  # new width & height
    img = ImageTk.PhotoImage(img)
    e1 = tk.Label(canvas)
    e1.place(x= 50, y= 75)
    e1.image = img
    e1['image'] = img  # garbage collection

def diagnose():
    DiagnosisEntry.config(state="normal")
    DiagnosisEntry.delete('1.0', END)
    Fact = """DIAGNOSIS: DIABETIC \n===================== \nDESCRIPTION: Breakfast agreeable incommode departure it an. By ignorant at on wondered relation. Enough at tastes really so cousin am of. Extensive therefore supported by extremity of contented. Is pursuit compact demesne invited elderly be. View him she roof tell her case has sigh. Moreover is possible he admitted sociable concerns. By in cold no less been sent hard hill."""
    DiagnosisEntry.insert(tk.END, Fact)
    DiagnosisEntry.config(state="disabled")

def evaluation_tab(value):
    ev_window = tk.Tk()
    ev_window.resizable(width=0, height=0)
    ev_window.geometry("720x512")  # Size of the window
    ev_window.title('Evaluation Tab')

    if(value == 1):
        value = "DIABETIC"

    if (value == 2):
        value = "NORMAL"
    l2 = tk.Label(ev_window, text='Evaluation', font=('Berlin Sans FB', 25))
    l2.pack(padx=20, pady=20)

    #Labels
    GroundTruthLable = tk.Label(ev_window, text='GROUND TRUTH', font=('Berlin Sans FB', 25))
    GroundTruthLable.place(x= 50, y= 100)

    DrDiagLable = tk.Label(ev_window, text='DOCTOR'"'"'S DIAGNOSIS', font=('Berlin Sans FB', 25))
    DrDiagLable.place(x=50, y=200)

    ModelPredLable = tk.Label(ev_window, text='MODEL'"'"'S PREDECTION ', font=('Berlin Sans FB', 25))
    ModelPredLable.place(x=50, y=300)

    AccLable = tk.Label(ev_window, text='ACCURECY ', font=('Berlin Sans FB', 25))
    AccLable.place(x=200, y=400)

    #Data
    GroundTruthData = tk.Label(ev_window, text='DIABETIC', font=('Berlin Sans FB', 25))
    GroundTruthData.place(x= 550, y= 100)

    DrDiagData = tk.Label(ev_window, text=value, font=('Berlin Sans FB', 25))
    DrDiagData.place(x= 550, y= 200)

    ModelPredData = tk.Label(ev_window, text='DIABETIC', font=('Berlin Sans FB', 25))
    ModelPredData.place(x= 550, y= 300)

    AccData = tk.Label(ev_window, text='100% ', font=('Berlin Sans FB', 25))
    AccData.place(x=400, y=400)

#=================================CALLING ROOT=================================
root.mainloop()
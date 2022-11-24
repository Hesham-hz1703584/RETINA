import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os
from PIL import Image, ImageTk

# =================================MAIN=================================
# Main Window Layout
root = tk.Tk()
root.resizable(width=0, height=0)
defaultbg = root.cget('bg')
canvas = tk.Canvas(root, height=600, width=800, bg='white')
canvas.grid()

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
#CommentsEntry.config(state="disabled")
#CommentsEntry.bind("<Button-1>", click)

# labels
DiagnosisLable = tk.Label(canvas, text='Diagnosis', font=('Berlin Sans FB', 20), bg='white')
DiagnosisLable.place(x=330, y=5)

DiagnosisLable = tk.Label(canvas, text='Diagnose:', font=('Berlin Sans FB', 20))
DiagnosisLable.place(x=26, y=405)

# =================================BUTTONS=================================
# buttons
Uploadbtn = tk.Button(canvas, text='Upload', font=('Helvetica 16', 11), command=lambda: upload_file(), bg='#6495ED', fg='white', width=10, height=2)
Uploadbtn.place(x=50, y=325)
Cropbtn = tk.Button(canvas, text='Crop', font=('Helvetica 16', 11), bg='#6495ED', fg='white', width=10, height=2)
Cropbtn.place(x=400, y=325)
SDbtn = tk.Button(canvas, text='SubmitDiagnosis', font=('Helvetica 16', 12), bg='#6495ED', fg='white', width=13, height=3)
SDbtn.place(x=620, y=440)
DRbtn = tk.Button(canvas, text='DiagnosisReport', font=('Helvetica 16', 12), command=lambda: evaluation_tab(var.get()), bg='#6495ED', fg='white', width=13, height=3)
DRbtn.place(x=620, y=520)
# =================================Radiobutton=================================
var = IntVar()
Radiobutton(root, text="DIABETIC", font=('Helvetica 16', 15), variable=var, value=1).place(x=35, y=450)
Radiobutton(root, text="NORMAL", font=('Helvetica 16', 15), variable=var, value=2).place(x=35, y=480)


# =================================FUNCTIONS=================================
# Upload_file
def upload_file():
    f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]  # type of files to select
    filename = tk.filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)  # read the image file
    img = img.resize((360, 245))  # new width & height
    img = ImageTk.PhotoImage(img)
    e1 = tk.Label(canvas)
    e1.place(x=19, y=46)
    e1.image = img
    e1['image'] = img  # garbage collection


def diagnose():
    DiagnosisEntry.config(state="normal")
    DiagnosisEntry.delete('1.0', END)
    Fact = """DIAGNOSIS: DIABETIC \n===================== \nDESCRIPTION: Breakfast agreeable incommode departure it 
    an. By ignorant at on wondered relation. Enough at tastes really so cousin am of. Extensive therefore supported 
    by extremity of contented. Is pursuit compact demesne invited elderly be. View him she roof tell her case has 
    sigh. Moreover is possible he admitted sociable concerns. By in cold no less been sent hard hill. """
    DiagnosisEntry.insert(tk.END, Fact)
    DiagnosisEntry.config(state="disabled")


def evaluation_tab(value):
    ev_window = tk.Tk()
    # ev_window.resizable(width=0, height=0)
    ev_window.geometry("400x600")  # Size of the window
    ev_window.title('Evaluation Tab')

    DsummaryEntry = Text(ev_window, width=31, height=6, font='Helvetica 16', bg='light grey')
    DsummaryEntry.place(x=11, y=60)
    DsummaryEntry.config(state="disabled")

    DstatisticsEntry = Text(ev_window, width=31, height=6, font='Helvetica 16', bg='light grey')
    DstatisticsEntry.place(x=11, y=250)
    DstatisticsEntry.config(state="disabled")

    PDFbtn = tk.Button(ev_window, text='Generate PDF', font=('Helvetica 16', 12), bg='#6495ED', fg='white', width=13, height=3)
    PDFbtn.place(x=250, y=520)

    if (value == 1):
        value = "Diabetic"

    if (value == 2):
        value = "Normal"

    l2 = tk.Label(ev_window, text='Evaluation', font=('Berlin Sans FB', 15))
    l2.place(x=150, y=10)

    # Labels
    l1 = tk.Label(ev_window, text='Diagnosis Summary:', font=('Berlin Sans FB', 15), bg='light grey')
    l1.place(x=13, y=65)

    DrDiagLable = tk.Label(ev_window, text='-  Doctor'"'"f's Diagnosis: {value}', font=('Berlin Sans FB', 16), bg='light grey')
    DrDiagLable.place(x=13, y=100)

    ModelPredLable = tk.Label(ev_window, text='-  Model'"'"'s Diagnosis: Diabetic (76.3%)', font=('Berlin Sans FB', 16), bg='light grey')
    ModelPredLable.place(x=13, y=130)

    GroundTruthData = tk.Label(ev_window, text='-  Actual Diagnosis: Diabetic', font=('Berlin Sans FB', 16),  bg='light grey')
    GroundTruthData.place(x=13, y=160)

    l2 = tk.Label(ev_window, text='Doctor'"'"'s Statistics:', font=('Berlin Sans FB', 15), bg='light grey')
    l2.place(x=13, y=255)

    l3 = tk.Label(ev_window, text='-  Number of evaluated cases: 5', font=('Berlin Sans FB', 16), bg='light grey')
    l3.place(x=13, y=295)

    l4 = tk.Label(ev_window, text='-  Number of correct diagnosis: 4', font=('Berlin Sans FB', 16),  bg='light grey')
    l4.place(x=13, y=325)

    l5 = tk.Label(ev_window, text='-  Number of incorrect diagnosis: 1', font=('Berlin Sans FB', 16),  bg='light grey')
    l5.place(x=13, y=355)


# =================================CALLING ROOT=================================
root.mainloop()

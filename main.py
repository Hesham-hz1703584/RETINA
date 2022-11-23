import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

# Main_window
my_window = tk.Tk()
my_window.geometry("720x512")  # Size of the window
my_window.resizable(width=0, height=0)
my_window.title('Retina Picker')
my_font1 = ('times', 18, 'bold')
l1 = tk.Label(my_window, text='Upload Photo & Evaluate', font=('Arial', 18))
l1.pack(padx=20, pady=20)
# button frame
buttonframe = tk.Frame(my_window)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
# buttons
btn1 = tk.Button(buttonframe, text='Upload Files', font=('Arial', 18), command=lambda: upload_file(), bg= 'cyan', fg='black', bd=4 , activebackground= 'grey')
btn1.grid(row=0, column=0, padx=1)
btn2 = tk.Button(buttonframe, text='Diagnose', font=('Arial', 18), command=lambda: upload_file(),bg= 'cyan', fg='black', bd=4 , activebackground= 'grey')
btn2.grid(row=0, column=1, padx=15)
btn3 = tk.Button(buttonframe, text='Evaluate', font=('Arial', 18), command=lambda: evaluation_tab(), bg= 'cyan', fg='black', bd=4 , activebackground= 'grey')
btn3.grid(row=0, column=2, padx=15)
buttonframe.pack(fill='x', padx=100)


# Upload_file
def upload_file():
    f_types = [('Jpg Files', '*.jpg'),('PNG Files', '*.png')]  # type of files to select
    filename = tk.filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)  # read the image file
    img = img.resize((200, 200))  # new width & height
    img = ImageTk.PhotoImage(img)
    e1 = tk.Label(my_window)
    e1.pack(padx=50, side=tk.LEFT)
    e1.image = img
    e1['image'] = img  # garbage collection

# Second_window
def evaluation_tab():
    my_window2 = tk.Tk()
    my_window2.geometry("720x512")  # Size of the window
    my_window2.title('Evaluation Tab')

    l2 = tk.Label(my_window2, text='Evaluation', font=('Arial', 18))
    l2.pack(padx=20, pady=20)


my_window.mainloop()  # Keep the window open

from cProfile import label
from cgitb import text
from fileinput import filename
from cProfile import label
from cgitb import text
from fileinput import filename
import os
from tkinter import *
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
  
# Tkinter GUI
os.system("clear")
root = Tk() 
root.title("Enigma~Testing")
root.geometry('900x900') 



# ------>plotting the dashboard
def tracer():
    file_name = myTextbox.get()
    size = []
    speed = []
    for i in range(1,11):
        size_of_file = os.path.getsize(file_name)
        size.append(i*size_of_file)
        bashCommand = "openssl speed -bytes " + str(size_of_file) + "  aes-128-cbc 2> open "
        os.system(bashCommand) 
        os.system("cut -d' ' -f2,10 open >output.txt")
        os.system("cat file_name | tee -a file_name > /dev/null")
        # or os.system("cp file_name file_name")
        with open('output.txt') as f:
            first_line = f.readline()
            print(first_line)
            first_line = first_line.split(' ')
            speed.append(int(first_line[1]))
    
    plt.plot(size ,speed)
    plt.show()

#---->solve app ui
def solve():
    #file_name = myTextbox.get()
    #size_of_file = os.path.getsize(file_name)
    #label1 = Label(root,font = ("Helvetica" , 15),text="The size of the current file is "+str(size_of_file) + " bytes")
    #label1.pack()
    tracer()
    os.system("clear")
    # exit button
    button = Button (root, text="Exit", font = ("Helvetica" , 15) ,command=root.destroy)
    button.pack()


label2 = Label(root , text="Enter file name! " , font = ("Helvetica" , 15))
label2.pack()

myTextbox = Entry(root , width=40)
myTextbox.pack()

myButton = Button(root , text="Test the speed!" ,font = ("Helvetica" , 15) ,command=solve)
myButton.pack()


root.mainloop()

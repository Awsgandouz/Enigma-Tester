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
  
# Tkinter GUI
os.system("clear")
root = Tk() 
root.title("Enigma~Testing")
root.geometry('900x900') 

def plot():
    file_name = myTextbox.get()
    # get the size of the file
    size_of_file = os.path.getsize(file_name)
    bashCommand = "openssl speed -bytes " + str(size_of_file) + "  aes-128-cbc aes-192-cbc aes-256-cbc 2> open "
    os.system(bashCommand) 
    os.system("cut -d' ' -f2,10 open >output.txt")
    
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5),dpi = 100)
    algo = []
    nb = []
    f = open('output.txt','r')
    for row in f:
        row = row.split(' ')
        algo.append(row[0])
        nb.append(int(row[1]))  
    
    plot1 = fig.add_subplot()
    # plotting the graph
    plot1.bar(algo, nb, color = 'g', label = 'File Data')
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,master = root)  
    canvas.draw()
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,root)
    toolbar.update()
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


#---->solve app ui
def solve():
    file_name = myTextbox.get()
    size_of_file = os.path.getsize(file_name)
    label1 = Label(root,font = ("Helvetica" , 15),text="The size of the current file is "+str(size_of_file) + " bytes")
    label1.pack()
    plot()
    button = Button (root, text="Exit", font = ("Helvetica" , 15) ,command=root.destroy)
    button.pack()


label2 = Label(root , text="Enter file name! " , font = ("Helvetica" , 15))
label2.pack()

myTextbox = Entry(root , width=40)
myTextbox.pack()

myButton = Button(root , text="Test the speed!" ,font = ("Helvetica" , 15) ,command=solve)
myButton.pack()



root.mainloop()


from cProfile import label
from cgitb import text
from fileinput import filename
from tkinter import *
import os

os.system("clear")


# Tkinter GUI
root = Tk() 
root.title("Enigma~Testing")
root.geometry('900x900') 


#---->get the size of the file 
def size():
    file_name = myTextbox.get()
    size_of_file = os.path.getsize(file_name)
    bashCommand = "openssl speed -bytes " + str(size_of_file) + "  aes-128-cbc aes-192-cbc aes-256-cbc 2> open "
    os.system(bashCommand) 
    os.system("cut -d' ' -f2,10,14 open >output")
    
    

    

#---->solve app ui
def solve(): 
    size()
    file_name = myTextbox.get()
    size_of_file = os.path.getsize(file_name)

    main_label = Label(root,font = ("Helvetica" , 15),text="The size of the current file is "+str(size_of_file) + " bytes")
    main_label.pack()

    button = Button (root, text="Exit", font = ("Helvetica" , 15) ,command=root.destroy)
    button.pack()
 


mylabel = Label(root , text="Enter file name! " , font = ("Helvetica" , 15))
mylabel.pack()

myTextbox = Entry(root , width=40)
myTextbox.pack()

myButton = Button(root , text="Test the speed!" ,font = ("Helvetica" , 15) ,command=solve)
myButton.pack()





root.mainloop

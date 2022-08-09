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
    bashCommand = "openssl speed -bytes " + str(size_of_file) + "  md5 sha1 sha256 sha512 des des-ede3 aes-128-cbc aes-192-cbc aes-256-cbc rsa" 
    os.system(bashCommand) 

#---->solve app ui
def solve():
    file_name = myTextbox.get()
    size_of_file = os.path.getsize(file_name) 
    
    hello_label = Label(root,text="The size of the current file is "+str(size_of_file) + " bytes")
    hello_label.pack()

    size()

    hello_label = Label(root,text="Dashboard:")
    hello_label.pack()  


mylabel = Label(root , text="Enter file name! ")
mylabel.pack()

myTextbox = Entry(root , width=30)
myTextbox.pack()

myButton = Button(root , text="Test the speed!" , command=solve)
myButton.pack()



root.mainloop()

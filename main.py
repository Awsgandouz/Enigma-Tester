from cProfile import label
from cgitb import text
from ctypes import sizeof
from fileinput import filename
from cProfile import label
from cgitb import text
from fileinput import filename
import os
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
  
# Tkinter GUI
os.system("clear")
root = Tk() 
root.title("Enigma~Testing")
root.geometry('900x900') 

# ------>plotting the dashboard
def tracer():
    file_name = myTextbox1.get()
    if(myTextbox2.get()=="aes"):
        size = []
        speed = []
        for i in range(1,11,2):
            size_of_file = os.path.getsize(file_name)
            size.append(i*size_of_file)
            bashCommand = "openssl speed -bytes " + str(size_of_file) + " aes-128-cbc 2> open "
            os.system(bashCommand) 
            os.system("cut -d' ' -f2,10 open >output.txt")
            os.system("cat file_name | tee -a file_name > /dev/null")
            # or os.system("cp file_name file_name")
            with open('output.txt') as f:
                first_line = f.readline()
                #print(first_line)
                first_line = first_line.split(' ')
                speed.append(int(first_line[1]))
        
        data = {'Size': size,'Speed': speed}
        df = DataFrame(data,columns=['Size','Speed'])
        fig = plt.Figure(figsize=(6,5), dpi=100)
        ax = fig.add_subplot(111)
        line = FigureCanvasTkAgg(fig, root)
        line.get_tk_widget().pack(fill=BOTH)
        df = df[['Size','Speed']].groupby('Size').sum()
        df.plot(kind='line', legend=True, ax=ax, color='r',marker='o', fontsize=10)
        ax.set_title('Size Vs. Speed')
    else :
        size_of_key1 = [] 
        size_of_key2 = []
        speed1 = [] 
        speed2= []
        
        '''
        bashCommand = " openssl speed rsa 2> open "
        os.system(bashCommand) 
        '''
        
        os.system("grep -w private open | cut -d' ' -f8,9 > pv.txt ")
        os.system("grep -w public open | cut -d' ' -f8,9 > pb.txt ")
        
        f1 = open('pb.txt' , "r")
        lines = f1.readlines()
        for s in lines :
            line = s.split(' ')
            size_of_key1.append(int(s[1]))
            speed1.append(int(s[0]))
        f1.close()
        
        data = {'Size': size_of_key1,'Speed': speed1}
        df = DataFrame(data,columns=['Size','Speed'])
        fig = plt.Figure(figsize=(6,5), dpi=100)
        ax = fig.add_subplot(111)
        line = FigureCanvasTkAgg(fig, root)
        line.get_tk_widget().pack(fill=BOTH)
        df = df[['Size','Speed']].groupby('Size').sum()
        df.plot(kind='line', legend=True, ax=ax, color='r',marker='o', fontsize=10)
        ax.set_title('Size of key Vs. Speed for public key')
        

        f2 = open('pv.txt' , "r")
        lines = f2.readlines()
        for s in lines :
            line = s.split(' ')
            size_of_key2.append(int(s[1]))
            speed2.append(int(s[0]))
        f2.close()
        
        data = {'Size': size_of_key2,'Speed': speed2}
        df = DataFrame(data,columns=['Size','Speed'])
        fig = plt.Figure(figsize=(6,5), dpi=100)
        ax = fig.add_subplot(111)
        line = FigureCanvasTkAgg(fig, root)
        line.get_tk_widget().pack(fill=BOTH)
        df = df[['Size','Speed']].groupby('Size').sum()
        df.plot(kind='line', legend=True, ax=ax, color='r',marker='o', fontsize=10)
        ax.set_title('Size of key Vs. Speed for private key')
        
    
#---->solve app ui
def solve():
    #file_name = myTextbox.get()
    #size_of_file = os.path.getsize(file_name)
    #label1 = Label(root,font = ("Helvetica" , 15),text="The size of the current file is "+str(size_of_file) + " bytes")
    #label1.pack()
    
    tracer()
    #os.system("clear")
    # exit button
    button = Button (root, text="Exit", font = ("Helvetica" , 15) ,command=root.destroy)
    button.pack()


label1 = Label(root , text="Enter file name! " , font = ("Helvetica" , 15))
label1.pack()

myTextbox1 = Entry(root , width=40)
myTextbox1.pack()

label2 = Label(root , text="Select RSA or AES! " , font = ("Helvetica" , 15))
label2.pack()

myTextbox2 = Entry(root , width=40)
myTextbox2.pack()


myButton = Button(root , text="Test the speed!" ,font = ("Helvetica" , 15) ,command=solve)
myButton.pack()


root.mainloop()

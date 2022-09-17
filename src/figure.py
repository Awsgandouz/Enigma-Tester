from cProfile import label
from cgitb import text
from ctypes import sizeof
from fileinput import filename
from cProfile import label
from cgitb import text
from fileinput import filename
import os
from sys import argv
from tkinter import *
from turtle import bgcolor, color
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
  
# Tkinter GUI
os.system("clear")
root = Tk() 
root.title("Enigma Tester")
root.geometry('900x600') 
root.configure(background='#ababab')


# ------>plotting the dashboard
def tracer():

    if(argv[2]=="AES" or argv[2]=="aes"):
        size = []
        speed = []
        file_name = argv[1]
        for i in range(1,30,2):
            os.system("clear")
            size_of_file = os.path.getsize(file_name)
            size.append(i*size_of_file)
            bashCommand = "openssl speed -bytes " + str(size_of_file) + " aes-128-cbc 2> open_aes "
            os.system(bashCommand) 
            os.system("cut -d' ' -f2,10 open_aes >output.txt") 
            os.system("cat file_name | tee -a file_name > /dev/null")

            with open('output.txt') as f:
                first_line = f.readline()
                first_line = first_line.split(' ')
                speed.append(int(first_line[1]))
        
        data = {'Size': size,'Speed': speed}
        df = DataFrame(data,columns=['Size','Speed'])
        fig = plt.Figure(figsize=(6,5), dpi=100)
        fig.patch.set_facecolor('#ababab')
        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('#ababab')
        line = FigureCanvasTkAgg(fig, root)
        
        line.get_tk_widget().pack(fill=BOTH)
        df = df[['Size','Speed']].groupby('Size').sum()
        df.plot(kind='line', legend=True, ax=ax, color='r',marker='o', fontsize=10)
        ax.set_title('Speed Vs. File Size')
    else :
        size_of_key1 = [] 
        size_of_key2 = []
        speed1 = [] 
        speed2= []
        
        bashCommand = " openssl speed rsa 2> open_rsa "
        os.system(bashCommand) 
      
        os.system("grep -w private open_rsa | cut -d' ' -f8,9 > pv.txt ")
        os.system("grep -w public open_rsa | cut -d' ' -f8,9 > pb.txt ")
        
        f1 = open('pb.txt' , "r")
        lines = f1.readlines()
        for s in lines :
            line = s.split(' ')
            size_of_key1.append(int(line[1]))
            speed1.append(int(line[0]))
        f1.close()
        
        data = {'Size': size_of_key1,'Speed': speed1}
        df = DataFrame(data,columns=['Size','Speed'])
        fig = plt.Figure(figsize=(6,5), dpi=90)
        fig.patch.set_facecolor('#ababab')
        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('#ababab')
        line = FigureCanvasTkAgg(fig, root)
        line.get_tk_widget().pack(fill=BOTH)
        df = df[['Size','Speed']].groupby('Size').sum()
        df.plot(kind='line', legend=True, ax=ax, color='r',marker='o', fontsize=10)
        ax.set_title('Speed Vs. Size of Public key')
        

        f2 = open('pv.txt' , "r")
        lines = f2.readlines()
        for s in lines :
            line = s.split(' ')
            size_of_key2.append(int(line[1]))
            speed2.append(int(line[0]))
        f2.close()
        
        data = {'Size': size_of_key2,'Speed': speed2}
        df = DataFrame(data,columns=['Size','Speed'])
        fig = plt.Figure(figsize=(6,5), dpi=90)
        fig.patch.set_facecolor('#ababab')
        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('#ababab')
        line = FigureCanvasTkAgg(fig, root)
        line.get_tk_widget().pack(fill=BOTH)
        df = df[['Size','Speed']].groupby('Size').sum()
        df.plot(kind='line', legend=True, ax=ax, color='r',marker='o', fontsize=10)
        ax.set_title('Speed Vs. Size of Private key')        
    
#---->solve app ui
def solve():
    tracer()
    # exit button
    button = Button (root, text="Exit", font = ("Helvetica" , 15) , command=root.destroy)
    button.pack()


if __name__ == "__main__":
    solve()
    root.mainloop()

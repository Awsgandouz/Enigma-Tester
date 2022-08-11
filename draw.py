from cProfile import label
from cgitb import text
from fileinput import filename
from tkinter import *
import os

import matplotlib.pyplot as plt
algo = []
nb = []

f = open('output.txt','r')
for row in f:
    row = row.split(' ')
    algo.append(row[0])
    nb.append(int(row[1]))

plt.bar(algo, nb, color = 'g', label = 'File Data')

plt.xlabel('AES~algorithms', fontsize = 12)
plt.ylabel('Speed', fontsize = 12)

plt.title('Speed Test', fontsize = 20)
plt.legend()
plt.show()

# -*- coding: utf-8 -*-
"""
Created by Vincenzo Sammartano
email:  v.sammartano@gmail.com
"""
import tkinter as tk
from tkinter import messagebox
from tkinter import font
import numpy as np

##Tkinter Window
root = tk.Tk()
root.geometry("300x280+100+50")
root.title("Noise converter")
root.resizable(width=False, height=False)
##root.iconbitmap('fan.ico')

##Fonts
f_H12B = font.Font(family='Helvetica', size=12, weight='bold')
f_H12 = font.Font(family='Helvetica', size=12, weight='normal')
f_H11 = font.Font(family='Helvetica', size=11, weight='bold')
f_H10 = font.Font(family='Helvetica', size=10, weight='bold')
f_H08 = font.Font(family='Helvetica', size=8, weight='normal')
font.families()

####Frames texts
text0 = "Noise inputs"
text1 = "Output"

# main Frames
top_frame = tk.Frame(root, width=250)
top_frame.grid(row=0, column=0, rowspan=2, sticky="w")
bottom_frame = tk.Frame(root, width=250)
bottom_frame.grid(row=3, column=0, sticky="w")

# subframes
# for input/outputs
frame00 = tk.LabelFrame(top_frame, text=text0, width=280, height=150, font=f_H12B)
frame00.grid(row=0, column=0, padx=15, pady=8, ipadx=20, ipady=10)
frame00.config(borderwidth=4)

frame01 = tk.LabelFrame(top_frame, text=text1, width=150, height=15, font=f_H12B)
frame01.grid(row=1, column=0, padx=13, pady=10, ipadx=15, ipady=5)
frame01.config(borderwidth=4)

botton_frame = tk.LabelFrame(top_frame, text="", width=150, height=15, font=f_H12B)
botton_frame.grid(row=2, column=0, padx=13, pady=10, ipadx=15, ipady=5)
botton_frame.config(borderwidth=4)

##########################################
##Functions
def ex():
    root.destroy()
def con():
    #from m/s2 to dB
    U = float(FS_.get())
    U0 = 1
    SdB = 20 *np.log10(U/U0)
    print("The noise value in m s^-2 is = ",U)
    printout(SdB)
def printout(out):
    labels = ["{:5.2f}".format(out)]
    for ii, r in enumerate(labels):
        tk.Label(frame01, text=r, bg="white", width=11, font=f_H12B, anchor='center',
                 borderwidth=2, relief="groove").grid(row=ii,column=1, padx=1)
###end of Functions
###########################################

###########Main    
# INPUT
fs_lab = tk.Label(frame00, text="Noise[m/s^2] = ", font=f_H12)
fs_lab.grid(row=0, column=0, padx=15, sticky="E")

FS_ = tk.StringVar()
FS = tk.Entry(frame00, textvariable=FS_, width=6, justify="center", font=f_H12)
FS.grid(row=0, column=1, pady=5)
FS.insert('end', 1)
FS.configure(state='normal')

# Outputs
VarList = ['Noise [dB]']

for i, var in enumerate(VarList):
    tk.Label(frame01, text=var, font=f_H12).grid(row=i,
                                                 column=0,
                                                 sticky="E",
                                                 pady=11, padx=5)
    tk.Frame(frame01, height=32, width=125, colormap="new",
             relief="sunken", bd=2).grid(row=i,
                                         column=1,
                                         sticky="E",
                                         padx=10,
                                         pady=11)

###############Buttons

cc = tk.Button(botton_frame, text="RUN", command=con, font=f_H12)
cc.config(height=1, width=5)
cc.pack(side='left', padx = 10, expand = True)

ex = tk.Button(botton_frame, text="EXIT", command=ex, font=f_H12)
ex.config(height=1, width=5)
ex.pack(side='right', padx = 10, expand = True)
######################

if __name__ == '__main__':
    root.mainloop()

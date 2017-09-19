#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
/*****************************************************************************/
/* Created on Fri Aug 11 19:54:49 2017                                       */
/* Type        : Python Script                                               */
/* Description : Steuerung der Drohne.                                       */
/* Module      : Crazyflie_test                                              */
/* Resources   : tkinter.                                                    */ 
/* Input       : Bildschirm                                                  */
/* Output      : Bildschirm und und Crazyflie_test.ScanCfly().               */
/*                                                                           */
/* @author     : Hermann Kulbartz                                            */
/*****************************************************************************/
"""
print(__doc__)
from tkinter import *
import sys
print("vOR IMPORT")
import Crazyflie_test 
# print(dir(Crazyflie_test))
print("Nach Import")

M = Crazyflie_test.ScanCfly()
print(type(M))
# sys.exit(1)

thrust = 0
def mouse_wheel(event):
    
    # respond to Linux or Windows wheel event
    if event.num == 5 or event.delta == -120:
        count -= 500
    if event.num == 4 or event.delta == 120:
        count += 500
    label['text'] = count #int(var1.get())
    #thrust = count
    #int(var1,get()) = count

def sel():
   selection1 = "thrust = " + str(var1.get()) + "  yawrate = " + str(var2.get()) + " °"
   label1.config(text = selection1)
   selection2 = "roll = " + str(var3.get()) + " °" + "  pitch = " + str(var4.get()) + " °"
   label2.config(text = selection2)
   print(selection1, selection2)
   
   thrust = count  #int(var1.get())
   print(thrust)
   M.motorsthrust(thrust)
#
#   yawrate = int(var2.get())
#   M.motorsyawrate(yawrate)
#   
#   roll = int(var3.get())
#   M.motorsroll(roll)
#   
#   pitch = int(var2.get())
#   M.motorspitch(pitch)

def MotorThrust(count):
   thrust = count  #int(var1.get())
   print(thrust)
   M.motorsthrust(thrust)
   
def Close():
   M.Close()
   
def Open():
   M.Open()
   
root = Tk()
root.title("Drohnen Kanzel")
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

scale1 = Scale( root, variable = var1, from_ = 60000, to = 0, length = 200, tickinterval = 10000)
scale1.pack(side = RIGHT)
scale1.set(9000)

scale4 = Scale( root, variable = var4, from_ = 180, to = -180, length = 200, tickinterval = 90 )
scale4.pack(side = LEFT)


scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

root.bind("<Button-4>", mouse_wheel)
root.bind("<Button-5>", mouse_wheel)
label = Label(root, font=('courier', 12, 'bold'), width=10)
label.pack(padx=80, pady=40)


#scale4 = Scale( root, variable = var4, from_ = 180, to = -180, length = 400, tickinterval = 90 )
#scale4.pack(side = LEFT)


scale2 = Scale( root, variable = var2, from_ = -180, to = 180, length = 600, tickinterval=90, orient=HORIZONTAL )
scale2.pack()

scale3 = Scale( root, variable = var3, from_ = -180, to = 180, length = 600, tickinterval=90, orient=HORIZONTAL )
scale3.pack()


button1 = Button(root, text="Get Scale Values", command=sel)
button1.pack()

button2 = Button(root, text="Close Link", bg = '#C1281F',command=Close)
button2.pack(side = 'right')

button3 = Button(root, text="Open Link", bg = 'green',command=Open)
button3.pack(side = 'left')


label1 = Label(root)
label1.pack()

label2 = Label(root)
label2.pack()

label3 = Label(root)
label3.pack()

label4 = Label(root)
label4.pack()

while True:
    root.update_idletasks()
    root.update() 

    MotorThrust(thrust)

#    time.sleep(0.5)
#root.mainloop()

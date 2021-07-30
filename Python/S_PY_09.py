#  Ask the user to enter the radius of a circle in order to alert its calculated area and circumference.

import math
import tkinter
from tkinter import messagebox

# This code is to hide the main tkinter window
root = tkinter.Tk()
root.withdraw()


def find_Circumference(radius):
    return 2 * math.pi * radius


def find_Area(radius):
    return math.pi * math.pow(radius,2)


r = float(input("enter the radius of the circle : "))
circumference = find_Circumference(r)
area = find_Area(r)
# print("Area of the circle is " ,(math.pi*math.pow(r,2)))
# print("Circumference of the circle is " , (2*math.pi*r))


messagebox.showinfo("Circumference", circumference)
messagebox.showinfo("Area", area)

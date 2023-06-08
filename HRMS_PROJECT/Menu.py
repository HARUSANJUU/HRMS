import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import ImageTk, Image
import ttkbootstrap as ttk
import os
#WINDOW
window = ttk.Window(themename='darkly')
window.title('Menu Window')
window.geometry("1000x700")


header = ttk.Label(window, text='Hotel Reception Management System', font='Arial 20 bold', anchor='nw')
header.pack(anchor='nw', padx=10, pady=10)

header.pack()


# BUTTOM FRAME 
btm_frame = ttk.Frame(window)

OR = Image.open('Image\BUTTON.png')
DS = (100, 80)
RI = OR.resize(DS)
main_btn = ImageTk.PhotoImage(RI)

menu_btn1 = tk.Button(btm_frame, image=main_btn, borderwidth=0)
menu_btn1.grid(row=0, column=0, padx=10, pady=10)
label1 = ttk.Label(btm_frame, text="Check-In", font='Arial 10 bold')
label1.grid(row=1, column=0)

menu_btn2 = tk.Button(btm_frame, image=main_btn, borderwidth=0)
menu_btn2.grid(row=0, column=1, padx=10, pady=10)
label2 = ttk.Label(btm_frame, text="Check-out", font='Arial 10 bold')
label2.grid(row=1, column=1)

def reservation():
    os.system("python reservation.py")
menu_btn3 = tk.Button(btm_frame, image=main_btn,command=reservation,borderwidth=0)
menu_btn3.grid(row=2, column=0, padx=10, pady=10)
label3 = ttk.Label(btm_frame, text="  Booking &\nReservation", font='Arial 10 bold')
label3.grid(row=3, column=0)

menu_btn4 = tk.Button(btm_frame, image=main_btn, borderwidth=0)
menu_btn4.grid(row=2, column=1, padx=10, pady=10)
label4 = ttk.Label(btm_frame, text="Rooms", font='Arial 10 bold')
label4.grid(row=3, column=1)


menu_btn5 = tk.Button(btm_frame, image=main_btn,borderwidth=0)
menu_btn5.grid(row=4, column=0, padx=13, pady=20, columnspan=2)
label5 = ttk.Label(btm_frame, text="Archive", font='Arial 10 bold')
label5.grid(row=5, column=0,columnspan=2)


btm_frame.pack(side="left", fill="y")


#SLIDESHOW 

style = ttk.Style()
style.configure('Red.TFrame')
slide_frame = ttk.Frame(window, style='Red.TFrame')

image1 = ImageTk.PhotoImage(Image.open("1.png").resize((600, 350)))
image2 = ImageTk.PhotoImage(Image.open("2.png").resize((600, 350)))
image3 = ImageTk.PhotoImage(Image.open("3.png").resize((600, 350)))
image4 = ImageTk.PhotoImage(Image.open("4.png").resize((600, 350)))
image5 = ImageTk.PhotoImage(Image.open("5.png").resize((600, 350)))

image_list = [image1, image2, image3, image4, image5]

counter = 0

def ChangeImage():
    global counter
    if counter < len(image_list) - 1:
        counter += 1
    else:
        counter = 0
    imageLabel.config(image=image_list[counter])
    window.after(3000, ChangeImage) 


imageLabel = Label(slide_frame, image=image1)


imageLabel.pack()


window.after(3000, ChangeImage)

slide_frame.pack(side="right", fill="y")

window.mainloop()

import tkinter as tk
from tkinter import ttk
#from PIL import ImageTk, Image
import ttkbootstrap as ttk
#import mysql.connector as mysql
#import pymysql

window = ttk.Window(themename='darkly')
window.title('Reservation Window')
window.geometry('840x560')

header = ttk.Label(window, text='Reservation',font='Arial 20 bold')
header.pack()

# 1st frame
gst_frame = ttk.Frame(window)

gst_info = ttk.Label(gst_frame, text='GUEST INFORMATION', font='Arial 18')
gst_info.grid(row=0,column=0,sticky='e')

gst_label = ttk.Label(gst_frame, text='Guest: ', font='Arial 15')
gst_label.grid(row=1, sticky='e', pady=5)
gst_entry = ttk.Entry(gst_frame, width=30)
gst_entry.grid(row=1, column=1, padx=5, pady=5)

phn_label = ttk.Label(gst_frame, text='Phone Number: ', font='Arial 15')
phn_label.grid(row=2, sticky='e',pady=5)
phn_entry = ttk.Entry(gst_frame, width=30)
phn_entry.grid(row=2, column=1, padx=5, pady=5)

adr_label = ttk.Label(gst_frame, text='Address: ', font='Arial 15')
adr_label.grid(row=3, sticky='e', pady=5)
adr_entry = ttk.Entry(gst_frame, width=30)
adr_entry.grid(row=3, column=1, padx=5, pady=5)

gst_frame.pack()

# 2nd frame
rmd_frame = ttk.Frame(window)

rdm_label = ttk.Label(rmd_frame, text='ROOM DETAILS', font='Arial 18')
rdm_label.grid(row=0,column=0,sticky='e')

rnum_label = ttk.Label(rmd_frame, text='Room Number: ', font='Arial 15')
rnum_label.grid(row=1, sticky='e', pady=5)
rnum_entry = ttk.Entry(rmd_frame, width=30)
rnum_entry.grid(row=1, column=1, padx=5, pady=5)

ckin_label = ttk.Label(rmd_frame, text='Check-in: ', font='Arial 15')
ckin_label.grid(row=2, sticky='e', pady=5)
ckin_entry = ttk.Entry(rmd_frame, width=30)
ckin_entry.grid(row=2, column=1, padx=5, pady=5)

cout_label = ttk.Label(rmd_frame, text='Check-out: ', font='Arial 15')
cout_label.grid(row=3, sticky='e', pady=5)
cout_entry = ttk.Entry(rmd_frame, width=30)
cout_entry.grid(row=3, column=1, padx=5, pady=5)

addn_label = ttk.Label(rmd_frame, text='Add-On: ', font='Arial 15')
addn_label.grid(row=4, sticky='e', pady=5)
addn_entry = ttk.Entry(rmd_frame, width=30)
addn_entry.grid(row=4, column=1, padx=5, pady=5)

rmd_frame.pack()

# 3rd frame
btm_frame = ttk.Frame(window)

qty_label = ttk.Label(btm_frame, text='Quantity: ', font='Arial 10')
qty_label.pack(pady=10)

tlb_label = ttk.Label(btm_frame, text='Total Bill: ', font='Arial 13 bold')
tlb_label.pack(pady=10)

menu_btn = ttk.Button(btm_frame, text='Menu', width=20)
menu_btn.pack(side='left',pady=20)

rsv_btn = ttk.Button(btm_frame, text='Reserve', width=20)
rsv_btn.pack(side='left', padx=50)

btm_frame.pack()

window.mainloop()
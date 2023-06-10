import tkinter as tk
from tkinter import ttk
#from PIL import ImageTk, Image
import ttkbootstrap as tkb
#import mysql.connector as mysql
#import pymysql
import customtkinter
import os





def toggle_frame(event):
    selected_value = clicked.get()

def add_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(foreground='gray')

    def on_entry_click(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(foreground='black')

    def on_focus_out(event):
        if entry.get() == '':
            entry.insert(0, placeholder)
            entry.config(foreground='gray')

    entry.bind("<FocusIn>", on_entry_click)
    entry.bind("<FocusOut>", on_focus_out)

def update_label(event):
    fn = gst_entry_fn.get() +" "+gst_entry_ln.get()
    concat_var.set(fn)

    cont = phn_entry.get()
    cont_set.set(cont)

    addr = adr_entry.get()
    addr_var.set(addr)

    room = rnum_entry.get()
    rmn_set.set(room)

    chin = ckin_entry.get()
    cin_set.set(chin)

    chot = cout_entry.get()
    cot_set.set(chot)


def add_on():
    #saved_text = clicked.get()
    #addon_list.append(saved_text)
    #sv = clicked.get()
    #rst_adns.config(text=sv)


    print("working")
    print(addon_list)

def add_on_list():
    saved_text = clicked.get()
    addon_list.append(saved_text)

    for i, saved_text in enumerate(addon_list):
            addon_label = ttk.Label(rcpt_frame, text=saved_text, font='Arial 15')
            addon_label.grid(row=7+i, column=1,padx=5, pady=5, sticky='w')



window = tkb.Window(themename='darkly')
window.title('Reservation Window')
window.geometry('1000x700')

concat_var = tk.StringVar()
cont_set = tk.StringVar()
addr_var = tk.StringVar()
rmn_set = tk.StringVar()
cin_set = tk.StringVar()
cot_set = tk.StringVar()

header = ttk.Label(window, text='Reservation Form',font='Arial 20 bold')
header.pack()

# 1st frame
gst_frame = ttk.Frame(window)

gst_info = ttk.Label(gst_frame, text='GUEST INFORMATION', font='Arial 18')
gst_info.grid(row=0,column=0,sticky='e')

gst_label = ttk.Label(gst_frame, text='Guest: ', font='Arial 15')
gst_label.grid(row=1, pady=5)

gst_entry_fn = ttk.Entry(gst_frame, width=22)
gst_entry_fn.place(x=160, y=35)
add_placeholder(gst_entry_fn, "First Name")
gst_entry_fn.bind("<KeyRelease>", update_label)

gst_entry_ln = ttk.Entry(gst_frame, width=22)
gst_entry_ln.place(x=310, y=35)
add_placeholder(gst_entry_ln, "Last Name")
gst_entry_ln.bind("<KeyRelease>", update_label)

phn_label = ttk.Label(gst_frame, text='Phone Number: ', font='Arial 15')
phn_label.grid(row=2, sticky='e',pady=5)
phn_entry = ttk.Entry(gst_frame, width=30)
phn_entry.grid(row=2, column=1, padx=5, pady=5)
phn_entry.bind("<KeyRelease>", update_label)

adr_label = ttk.Label(gst_frame, text='Address: ', font='Arial 15')
adr_label.grid(row=3, sticky='e', pady=5)
adr_entry = ttk.Entry(gst_frame, width=30)
adr_entry.grid(row=3, column=1, padx=5, pady=5)
adr_entry.bind("<KeyRelease>", update_label)

gst_frame.place(x=50,y=50)

# 2nd frame
rmd_frame = ttk.Frame(window)

addon = ["Add-on 1", "Add-on 2", "Add-on 3", "Add-on 4"]

rdm_label = ttk.Label(rmd_frame, text='ROOM DETAILS', font='Arial 18')
rdm_label.grid(row=0,column=0,sticky='e')

rnum_label = ttk.Label(rmd_frame, text='Room Number: ', font='Arial 15')
rnum_label.grid(row=1, sticky='e', pady=5)
rnum_entry = ttk.Entry(rmd_frame, width=30)
rnum_entry.grid(row=1, column=1, padx=5, pady=5)
rnum_entry.bind("<KeyRelease>", update_label)

ckin_label = ttk.Label(rmd_frame, text='Check-in: ', font='Arial 15')
ckin_label.grid(row=2, sticky='e', pady=5)
ckin_entry = ttk.Entry(rmd_frame, width=30)
ckin_entry.grid(row=2, column=1, padx=5, pady=5)
ckin_entry.bind("<KeyRelease>", update_label)

cout_label = ttk.Label(rmd_frame, text='Check-out: ', font='Arial 15')
cout_label.grid(row=3, sticky='e', pady=5)
cout_entry = ttk.Entry(rmd_frame, width=30)
cout_entry.grid(row=3, column=1, padx=5, pady=5)
cout_entry.bind("<KeyRelease>", update_label)

addn_label = ttk.Label(rmd_frame, text='Add-On: ', font='Arial 15')
addn_label.grid(row=4, sticky='e', pady=5)
clicked = tk.StringVar()
clicked.set(addon[0])
drop_down = tk.OptionMenu(rmd_frame, clicked, *addon, command=toggle_frame)
drop_down.config(width=25)
drop_down.grid(row=4, column=1, padx=5, pady=5)

addn_btn = ttk.Button(rmd_frame, text='Add', command=add_on)
addn_btn.grid(row=4,column=2,pady=5)

addn_btns = ttk.Button(rmd_frame, text='Add', command=add_on_list)
addn_btns.grid(row=5,column=2,pady=5)

rmd_frame.place(x=125,y=210)

# 3rd frame
btm_frame = ttk.Frame(window)
add = 0

qty_label = ttk.Label(btm_frame, text='Quantity: ', font='Arial 10')
qty_label.grid(row=0, column=0, sticky='e', pady=5)

tlb_label = ttk.Label(btm_frame, text='Total Bill: ', font='Arial 13 bold')
tlb_label.grid(row=1, column=0, sticky='e', pady=10)

adt_spb = tk.Spinbox(btm_frame, from_=0, to=10, width=10)
adt_spb.grid(row=0,column=1,padx=5)

err_msg = ttk.Label(btm_frame, text='')
err_msg.grid(row=1,column=1)

btm_frame.place(x=225,y=400)

# 4th frame
btn_frame = ttk.Frame(window)

def menu():
    window.withdraw()
    os.system("python Menu.py")
menu_btn = ttk.Button(btn_frame, text='Menu',command=menu, width=20)
menu_btn.pack(side='left',pady=20)

rsv_btn = ttk.Button(btn_frame, text='Reserve', width=20)
rsv_btn.pack(side='left', padx=50)

btn_frame.place(x=200, y=475)

# 5th frame
rcpt_frame = ttk.Frame(window)

rcpt_lbl = ttk.Label(rcpt_frame, text='RECEIPT', font='Arial 18')
rcpt_lbl.grid()

rcpt_name = ttk.Label(rcpt_frame, text='Full Name: ', font='Arial 15')
rcpt_name.grid(pady=5, sticky='e')
rst_name = ttk.Label(rcpt_frame, textvariable=concat_var, font='Arial 15')
rst_name.grid(row=1, column=1, padx=5, pady=5, sticky='w')

rcpt_pnm = ttk.Label(rcpt_frame, text='Contact Number: ', font='Arial 15')
rcpt_pnm.grid(pady=5, sticky='e')
rst_cont = ttk.Label(rcpt_frame, textvariable=cont_set, font='Arial 15')
rst_cont.grid(row=2, column=1, padx=5, pady=5, sticky='w')

rcpt_adr = ttk.Label(rcpt_frame, text='Address: ', font='Arial 15')
rcpt_adr.grid(pady=5, sticky='e')
rst_adr = ttk.Label(rcpt_frame, textvariable=addr_var, font='Arial 15')
rst_adr.grid(row=3, column=1, padx=5, pady=5, sticky='w')

rcpt_rmn = ttk.Label(rcpt_frame, text='Room Number: ', font='Arial 15')
rcpt_rmn.grid(pady=5, sticky='e')
rst_rmn = ttk.Label(rcpt_frame, textvariable=rmn_set, font='Arial 15')
rst_rmn.grid(row=4, column=1, padx=5, pady=5, sticky='w')

rcpt_cin = ttk.Label(rcpt_frame, text='Check-in Date: ', font='Arial 15')
rcpt_cin.grid(pady=5, sticky='e')
rst_cin = ttk.Label(rcpt_frame, textvariable=cin_set, font='Arial 15')
rst_cin.grid(row=5, column=1, padx=5, pady=5, sticky='w')

rcpt_cot = ttk.Label(rcpt_frame, text='Check-out Date: ', font='Arial 15')
rcpt_cot.grid(pady=5, sticky='e')
rst_cot = ttk.Label(rcpt_frame, textvariable=cot_set, font='Arial 15')
rst_cot.grid(row=6, column=1, padx=5, pady=5, sticky='w')

rcpt_adns = ttk.Label(rcpt_frame, text='Add-Ons: ', font='Arial 15')
rcpt_adns.grid(pady=5, sticky='e')
#rst_adns = ttk.Label(rcpt_frame,text='', font='Arial 15')
#rst_adns.grid(row=7, column=1, padx=5, pady=5, sticky='w')

addon_list = []

rcpt_frame.place(x=600,y=50)


window.mainloop()
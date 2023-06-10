import customtkinter
from tkinter import *
from tkcalendar import Calendar, DateEntry

#customtkinter.set_apprearance_mode()
#customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

root.geometry("1000x700")

def login():
    print("Bobo")
def show():
    label ( text = clicked.get() )

def show1(options):
    if clicked.get() == "Card": 
        Acc_lbl.pack()
        Acc_lbl.place(x=500, y=240)
        Acc_No.pack()
        Acc_No.place(x=600, y=240) 
        Exp_lbl.pack()
        Exp_lbl.place(x=500, y=280)
        Exp_Dt.pack()
        Exp_Dt.place(x=600, y=280)
        
    elif clicked.get() == "Online":
        Ref_lbl.pack()
        Ref_lbl.place(x=500, y=240)
        Ref_No.pack()
        Ref_No.place(x=600, y=240)
    else:
        Acc_lbl.pack_forget()
        Acc_No.pack_forget()
        Exp_lbl.pack_forget()
        Exp_Dt.pack_forget()

options = [
    "Card",
    "Online",
    "Cash"
]

clicked = StringVar()
clicked.set( "Cash" )

click = StringVar()
click.set(None)

click1 = StringVar()
click1.set(None)
    
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=12, padx=10, fill="both", expand=True)

CHECK_IN = customtkinter.CTkLabel(master=frame, text="CHECK IN", font=("Copperplate Gothic Bold", 24))
CHECK_IN.pack()

Guest_Info = customtkinter.CTkLabel(master=frame, text="GUEST INFORMATION", font=("Garamond", 18,))
Guest_Info.pack()
Guest_Info.place(x=10, y=50)


name_label = customtkinter.CTkLabel(master=frame, text="Guest name", font=("Garamond", 16,))
name_label.pack(pady=12, padx=10)
name_label.place(x=10, y=80)
Fname = customtkinter.CTkEntry(master=frame, placeholder_text="First name")
Fname.pack(pady=12, padx=10)
Fname.place(x=100, y=80)

Lname = customtkinter.CTkEntry(master=frame, placeholder_text="Last name")
Lname.pack(pady=12, padx=10)
Lname.place(x=260, y=80)

dob_label = customtkinter.CTkLabel(master=frame, text="Date of birth", font=("Garamond", 16,))
dob_label.pack(pady=12, padx=10)
dob_label.place(x=10, y=120)
Dob = DateEntry(master=frame, width= 28, background= "magenta3", foreground= "white",bd=2)
Dob.pack(pady=12, padx=10)
Dob.place(x=100, y=120)

Cn_label = customtkinter.CTkLabel(master=frame, text="Contact no.", font=("Garamond", 16,))
Cn_label.pack(pady=12, padx=10)
Cn_label.place(x=10, y=160)
Cn = customtkinter.CTkEntry(master=frame, placeholder_text="Contact no.", width=190)
Cn.pack(pady=12, padx=10)
Cn.place(x=100, y=160)

Add_label = customtkinter.CTkLabel(master=frame, text="Address", font=("Garamond", 16,))
Add_label.pack(pady=12, padx=10)
Add_label.place(x=10, y=200)
Add = customtkinter.CTkEntry(master=frame, placeholder_text="Address", width=190)
Add.pack(pady=12, padx=10)
Add.place(x=100, y=200)

R12_label = customtkinter.CTkLabel(master=frame, text="Reservation", font=("Garamond", 16,))
R12_label.pack(pady=12, padx=10)
R12_label.place(x=10, y=240)
R1 = Radiobutton(master=frame, text="Yes", variable = click, value = "Yes", command=login, font=("Garamond", 11,))
R1.pack()
R1.place(x=100, y=240)
R2 = Radiobutton(master=frame, text="No", variable = click, value = "No", command=login, font=("Garamond", 11,))
R2.pack()
R2.place(x=260, y=240)

Room_Detail = customtkinter.CTkLabel(master=frame, text="ROOM DETAILS", font=("Garamond", 18,))
Room_Detail.pack(pady=12, padx=10)
Room_Detail.place(x=10, y=300)

Room_No = customtkinter.CTkLabel(master=frame, text="Room no.", font=("Garamond", 16,))
Room_No.pack(pady=12, padx=10)
Room_No.place(x=10, y=340)
Room = customtkinter.CTkEntry(master=frame, placeholder_text="Room number", width=170)
Room.pack(pady=12, padx=100)
Room.place(x=100, y=340)

Adult = customtkinter.CTkLabel(master=frame, text="Adult", font=("Garamond", 16,))
Adult.pack(pady=12, padx=10)
Adult.place(x=30, y=380)
Adult_Sb = Spinbox(master=frame, from_=0, to=10, width=10)
Adult_Sb.pack(pady=12, padx=10)
Adult_Sb.place(x=80, y=380)

Child = customtkinter.CTkLabel(master=frame, text="Child", font=("Garamond", 16,))
Child.pack(pady=12, padx=10)
Child.place(x=170, y=380)
Child_Sb = Spinbox(master=frame, from_=0, to=10, width=10)
Child_Sb.pack(pady=12, padx=10)
Child_Sb.place(x=220, y=380)

Check_In = customtkinter.CTkLabel(master=frame, text="Check in", font=("Garamond", 16,))
Check_In.pack(pady=12, padx=10)
Check_In.place(x=30, y=420)
Time_in = DateEntry(master=frame, width= 19, background= "magenta3", foreground= "white",bd=2)
Time_in.pack(pady=12, padx=100)
Time_in.place(x=120, y=420)

Check_Out = customtkinter.CTkLabel(master=frame, text="Check Out", font=("Garamond", 16,))
Check_Out.pack(pady=12, padx=10)
Check_Out.place(x=30, y=460)
Check_In.place(x=30, y=420)
Time_Out = DateEntry(master=frame, width= 19, background= "magenta3", foreground= "white",bd=2)
Time_Out.pack(pady=12, padx=100)
Time_Out.place(x=120, y=460)

Add_on = customtkinter.CTkLabel(master=frame, text="Add On", font=("Garamond", 16,))
Add_on.pack(pady=12, padx=10)
Add_on.place(x=30, y=500)
Addon = customtkinter.CTkEntry(master=frame, placeholder_text="Add on")
Addon.pack(pady=12, padx=100)
Addon.place(x=120, y=500)

PAYMENT = customtkinter.CTkLabel(master=frame, text="PAYMENT", font=("Garamond", 18,))
PAYMENT.pack(pady=12, padx=10)
PAYMENT.place(x=500, y=50)

Total_lbl = customtkinter.CTkLabel(master=frame, text="Total", font=("Garamond", 16,))
Total_lbl.pack(pady=12, padx=10)
Total_lbl.place(x=500, y=80)

R_lbl = customtkinter.CTkLabel(master=frame, text="Discount", font=("Garamond", 16,))
R_lbl.pack(pady=12, padx=10)
R_lbl.place(x=500, y=120)
R3 = Radiobutton(master=frame, text="PWD", variable = click1, value = "PWD", command= lambda: [ID_lbl.pack(),ID_lbl.place(x=550, y=160),ID_no.pack(),ID_no.place(x=650, y=160)],font=("Garamond", 11,))
R3.pack()
R3.place(x=600, y=120)
R4 = Radiobutton(master=frame, text="Senior Citizen", variable = click1, value = "Senior Citizen", command= lambda: [ID_lbl.pack(),ID_lbl.place(x=550, y=160),ID_no.pack(),ID_no.place(x=650, y=160)], font=("Garamond", 11,))
R4.pack()
R4.place(x=700, y=120)

ID_lbl = customtkinter.CTkLabel(master=frame, text="ID number", font=("Garamond", 16,))
ID_lbl.pack_forget()
ID_lbl.place()
ID_no = customtkinter.CTkEntry( master=frame, placeholder_text="ID number")
ID_no.pack_forget()
ID_no.place()

Billing_lbl = customtkinter.CTkLabel(master=frame, text="BILLING", font=("Garamond", 16,))
Billing_lbl.pack(pady=12, padx=10)
Billing_lbl.place(x=500, y=200)

drop1 = OptionMenu( root , clicked , *options, command=show1 )
drop1.pack()
drop1.place(x=600, y=210)

Acc_lbl = customtkinter.CTkLabel(master=frame, text="Account no", font=("Garamond", 16,))
Acc_No = customtkinter.CTkEntry(master=frame)

Exp_lbl = customtkinter.CTkLabel(master=frame, text="Exp Date", font=("Garamond", 16,))
Exp_Dt = customtkinter.CTkEntry(master=frame)

Ref_lbl = customtkinter.CTkLabel(master=frame, text="Ref no", font=("Garamond", 16,))
Ref_No = customtkinter.CTkEntry(master=frame)

Amt_lbl = customtkinter.CTkLabel(master=frame, text="Amount Paid", font=("Garamond", 16,))
Amt_lbl.pack()
Amt_lbl.place(x=500, y=320)
Amt_Pd = customtkinter.CTkEntry(master=frame, placeholder_text="Amount paid")
Amt_Pd.pack(pady=12, padx=100)
Amt_Pd.place(x=600, y=320)

Blnc_lbl = customtkinter.CTkLabel(master=frame, text="Balance", font=("Garamond", 16,))
Blnc_lbl.pack(pady=12, padx=10)
Blnc_lbl.place(x=500, y=360)

Menu_Btn = customtkinter.CTkButton(master=frame, text=u"Menu", command=login)
Menu_Btn.pack(pady=12, padx=10)
Menu_Btn.place(x=240, y=590)

ChkIn_Btn = customtkinter.CTkButton(master=frame, text="Check in", command = show )
ChkIn_Btn.pack(pady=12, padx=10)
ChkIn_Btn.place(x=480, y=590)

Cncl_Btn = customtkinter.CTkButton(master=frame, text="Cancel", command = show )
Cncl_Btn.pack(pady=12, padx=10)
Cncl_Btn.place(x=720, y=590)

root.mainloop()
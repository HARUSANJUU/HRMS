from tkinter import *

root = Tk()

root.geometry("1000x700")

frame = Frame(master=root)
frame.pack(pady=12, padx=10, fill="both", expand=True)

def show():
    if clicked.set() == "Card": 
        lambda: [Acc_lbl.pack(),Acc_lbl.place(x=550, y=160),Acc_No.pack(),Acc_No.place(x=650, y=160), Exp_lbl.pack(),Exp_lbl.place(x=550, y=160),Exp_Dt.pack(),Exp_Dt.place(x=650, y=160)]
        return True
    else:
        print("wala")
        return False
                       

options = [
	"Card",
	"Cash",
    "Online"
]

clicked = StringVar()
clicked.set( "Card" )

drop = OptionMenu(master=frame, clicked , *options, command = show).pack()

Acc_lbl = Label(master=frame, text="Account no", font=("Garamond", 16,))
Acc_lbl.pack_forget()
Acc_lbl.place()
Acc_No = Entry(master=frame)
Acc_No.pack_forget()
Acc_No.place()

Exp_lbl = Label(master=frame, text="Exp Date", font=("Garamond", 16,))
Exp_lbl.pack_forget()
Exp_lbl.place()
Exp_Dt = Entry(master=frame)
Exp_Dt.pack_forget()
Exp_Dt.place()

root.mainloop()
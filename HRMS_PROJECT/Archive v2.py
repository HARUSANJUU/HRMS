import tkinter as tk 
from tkinter import ttk
import tkinter.ttk as ttk
from tkinter import messagebox
import ttkbootstrap as ttk
import mysql.connector
#from mysql.connector import Error
#import datetime

class Security(ttk.Frame):
    def __init__(self,parent):
        ttk.Frame.__init__(self, parent, border=30)
        self.parent = parent

        con = mysql.connector.connect(host='localhost', database='db_trial', user='root', password='', port='3307')
        query = 'SELECT * FROM db_password ORDER BY date_modified DESC;'
        cur = con.cursor()
        cur.execute(query)
        latest_pass = cur.fetchone()

        def check_pass():
            print('button pressed')
            password=password_data.get()
            if password == latest_pass[1]:
                self.parent.show_page(1)
            else:
                messagebox.showerror("Error", "Incorrect password!")

        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,2), weight=1)
        
        label = tk.Label(self, text="Archive", font='Arial 28', border=25)
        label.grid(row=0, column=0, columnspan=2, pady=5, sticky="nsew")

        password = tk.Label(self, text='Password:', font='Arial 15')
        password.grid(row=1, column=0, padx=5, pady=5, sticky='e')

        pass_data = tk.StringVar()
        password_data = tk.Entry(self, width=30, font='Arial 15', show="*", textvariable=pass_data)
        password_data.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        enter_btn = tk.Button(self, text='Submit', width=30, font='Arial 15', command=check_pass)
        enter_btn.grid(row=2, column=1, padx=40, pady=50, sticky='w')

        back_btn = tk.Button(self, text='Back', width=30, font='Arial 15')
        back_btn.grid(row=2, column=0, padx=40, pady=50, sticky='e')
     
class MainArchive(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent=parent

        con = mysql.connector.connect(host='localhost', database='db_trial', user='root', password='', port='3307')
        query = 'SELECT YEAR(b.checkIn_date) FROM tbl_checkin AS b GROUP BY YEAR(b.checkIn_date) ORDER BY YEAR(b.checkIn_date) DESC'
        cur = con.cursor()
        cur.execute(query)
        years = cur.fetchall()
        
        title = tk.Label(self, text='ARCHIVE', font='Arial 28', border=25)
        title.pack()

        for year in years:
            year = tk.Label(self, text=str(year[0]), font='Arial 15', cursor="hand2", padx=10, pady=10)
            year.pack()
            year.bind("<Button-1>", lambda event: self.parent.next_page())

        back_btn = tk.Button(self, text="Back", width=20, font='Arial 15', command=self.parent.previous_page)
        back_btn.pack()
       
class ArchiveData(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent=parent

        con = mysql.connector.connect(host = 'localhost', database = 'db_trial', user='root', password='', port='3307')
        query='SELECT a.guest_ID, b.checkIn_date, c.checkOut_date, d.total_Bill FROM tb_guest AS a, tbl_checkin AS b, tbl_checkout AS c, tbl_payment AS d'
        cur=con.cursor()
        cur.execute(query)
        result=cur.fetchone() 

        title = tk.Label(self, text='year', font='Arial 28', border=25)
        title.pack()

        data_frame = ttk.Frame(self)

        self.treeview = ttk.Treeview(data_frame, columns=('Guest ID', 'Check-in Date', 'Check-out Date', 'Total Bill'))
        self.treeview.pack(side="left", fill="both", expand=True)
        
        self.treeview.heading("#0", text="Guest_ID")
        self.treeview.heading("#1", text="Check-in Date")
        self.treeview.heading("#2", text="Check-out Date")
        self.treeview.heading("#3", text="Total Bill")

        self.treeview.insert("", "end", text=result[0], values=(result[1], result[2], 'Php ' + str(result[3])))
        
        scrollbar = ttk.Scrollbar(data_frame, orient="vertical", command=self.treeview.yview)
        self.treeview.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        def on_item_click(event):
            # Perform the desired action or redirection based on the clicked row and column
            self.parent.next_page()

        self.treeview.bind("<Button-1>", on_item_click)

        data_frame.pack(padx=10, pady=10)

        back_btn = tk.Button(self, text="Back", width=20, font='Arial 15', command=self.parent.previous_page)
        back_btn.pack()

class GuestData(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent=parent

        con = mysql.connector.connect(host = 'localhost', database = 'db_trial', user='root', password='', port='3307')
        query='SELECT g.last_name, g.first_name, g.birth_date, g.contact_no, g.address, r.room_Num, ci.checkIn_date, co.checkOut_date, COALESCE(dr.disc_amount, 0) AS discount, p.total_Bill, p.payment_method FROM tb_guest g JOIN tbl_checkIn ci ON g.guest_ID = ci.guest_ID JOIN tbl_checkOut co ON g.guest_ID = co.guest_ID JOIN tbl_room r ON ci.room_ID = r.room_ID JOIN tbl_payment p ON ci.checkIn_ID = p.checkIn_ID LEFT JOIN tbl_discountRec dr ON p.discRec_ID = dr.discRec_ID LEFT JOIN tbl_discount d ON dr.disc_ID = d.disc_ID'
        cur=con.cursor()
        cur.execute(query)
        result=cur.fetchone() 

        self.grid_columnconfigure((0,1), weight=1)
    
        label = tk.Label(self, text="Archive", font='Arial 28', border=25)
        label.grid(row=0, column=0, columnspan=2, pady=5, sticky="nsew")

        guest = tk.Label(self, text = "Guest: ", font='Arial 15')
        guest.grid(row=1, sticky="e", pady=5)
        guest_data = tk.Label(self, text=result[0]+', '+result[1], font='Arial 15')
        guest_data.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        bday = tk.Label(self, text = "Birthday: ", font='Arial 15')
        bday.grid(row=2, sticky="e", pady=5)
        bday_data = tk.Label(self, text=result[2], font='Arial 15')
        bday_data.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        contNum = tk.Label(self, text = "Contact Number: ", font='Arial 15')
        contNum.grid(row=3, sticky="e", pady=5)
        contNum_data = tk.Label(self, text=result[3], font='Arial 15')
        contNum_data.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        address = tk.Label(self, text = "Address: ", font='Arial 15')
        address.grid(row=4, sticky="e", pady=5)
        address_data = tk.Label(self, text=result[4], font='Arial 15')
        address_data.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        roomNum = tk.Label(self, text = "Room Number: ", font='Arial 15')
        roomNum.grid(row=5, sticky="e", pady=5)
        roomNum_data = tk.Label(self, text=result[5], font='Arial 15')
        roomNum_data.grid(row=5, column=1, padx=5, pady=5, sticky='w')

        checkin = tk.Label(self, text = "Check-in Date: ", font='Arial 15')
        checkin.grid(row=6, sticky="e", pady=5)
        checkin_data = tk.Label(self, text=result[6], font='Arial 15')
        checkin_data.grid(row=6, column=1, padx=5, pady=5, sticky='w')

        checkout = tk.Label(self, text = "Check-out Date: ", font='Arial 15')
        checkout.grid(row=7, sticky="e", pady=5)
        checkout_data = tk.Label(self, text=result[7], font='Arial 15')
        checkout_data.grid(row=7, column=1, padx=5, pady=5, sticky='w')
        
        discount = tk.Label(self, text = "Discount: ", font='Arial 15')
        discount.grid(row=8, sticky="e", pady=5)
        discount_data = tk.Label(self, text='Php ' + str(result[8]), font='Arial 15')
        discount_data.grid(row=8, column=1, padx=5, pady=5, sticky='w')

        totalBill = tk.Label(self, text = "Total Bill: ", font='Arial 15')
        totalBill.grid(row=9, sticky="e", pady=5)
        totalBill_Data = tk.Label(self, text='Php ' + str(result[9]), font='Arial 15')
        totalBill_Data.grid(row=9, column=1, padx=5, pady=5, sticky='w')

        pm = tk.Label(self, text = "Payment Method: ", font='Arial 15')
        pm.grid(row=10, sticky="e", pady=5)
        pm_data = tk.Label(self, text=result[10], font='Arial 15')
        pm_data.grid(row=10, column=1, padx=5, pady=5, sticky='w')

        back_btn = tk.Button(self, text="Back", width=20, font='Arial 15', command=self.parent.previous_page)
        back_btn.grid(row=11, column=0, columnspan=2, pady=20, sticky='ns')

        print(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10])
        
class Main(tk.Frame):
    def __init__(self, parent): #initialize and configure the object based on the provided arguments
        tk.Frame.__init__(self, parent) #to access the functionalities of tk.Frame
        self.parent=parent #allows you to access the parent widget or container from within the Main class
        
        p1 = Security(self)
        p2 = MainArchive(self)
        p3 = ArchiveData(self)
        p4 = GuestData(self)

        self.pages = [p1, p2, p3, p4]
        self.current_page = 0

        self.show_page()
    
    def show_page(self, page_index=None):
        if page_index is not None:
            self.current_page = page_index
        for page in self.pages:
            page.pack_forget()
        self.pages[self.current_page].pack()
    
    def previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.show_page()
    
    def next_page(self):
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1
            self.show_page()

if __name__ == "__main__":
    root = ttk.Window(themename='darkly') #root is the parent window
    main = Main(root) #Main class is placed inside the root window, and any widgets or frames created within the Main class will be added to the root window.
    main.pack(side="top", fill="both", expand=True)
    root.title('Archive')
    root.wm_geometry("1000x700")
    root.mainloop()

"""
SELECT g.guest_id, ci.checkIn_date, co.checkOut_date, p.total_Bill FROM tb_guest g JOIN tbl_checkin ci ON g.guest_id = ci.guest_ID JOIN tbl_checkout co ON g.guest_id = co.guest_ID JOIN tbl_payment p ON ci.checkIn_ID = p.checkIn_ID;


guest_id	checkIn_date	checkOut_date	total_Bill	
1           2023-06-07      2023-06-08      1000.00
2           2024-02-18      2024-02-20      3000.00
"""
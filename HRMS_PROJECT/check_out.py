import tkinter as tk

def search():
    # Function to perform search based on input
    search_term = search_entry.get()
    # Perform search logic here
    # You can access the window object if needed

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Search Window")

# set window size
window.geometry("1000x700")

# Create a frame to hold the search bar and button
search_frame = tk.Frame(window)
search_frame.pack(pady=10)

# Create the search bar
search_entry = tk.Entry(search_frame, width=40)
search_entry.pack(side=tk.LEFT)

# Create the search button
search_button = tk.Button(search_frame, text="Search", command=search)
search_button.pack(side=tk.LEFT)

# Create a frame for the text lines
text_frame = tk.Frame(window)
text_frame.pack(pady=10)

# Create the "Guest" text line
guest_text = tk.Label(text_frame, text="Guest: Guest Name")
guest_text.pack()

# Create the "Room number" text line
room_text = tk.Label(text_frame, text="Room number: room number")
room_text.pack()

# Create the "Checkout" text line
checkout_text = tk.Label(text_frame, text="Checkout: checkout date")
checkout_text.pack()

# Create a frame for the payment section
payment_frame = tk.Frame(window)
payment_frame.pack(pady=10, padx=10, anchor='w')

# Create the "Payment" label
payment_label = tk.Label(payment_frame, text="Payment")
payment_label.pack(anchor='w')

# Create the "Total Bill" label
total_bill_label = tk.Label(payment_frame, text="Total bill: number of bill")
total_bill_label.pack(anchor='w')

# Create the payment method label and text field
payment_method_label = tk.Label(payment_frame, text="Payment method:")
payment_method_label.pack(side=tk.LEFT)

payment_method_entry = tk.Entry(payment_frame, width=20)
payment_method_entry.pack(side=tk.LEFT)

# Create add-on method label and text field
addon_frame = tk.Frame(window)
addon_frame.pack(ipadx=300)

addon_method_label = tk.Label(addon_frame, text="Add-On method:")
addon_method_label.pack(side=tk.RIGHT)

addon_method_entry = tk.Entry(addon_frame, width=20)
addon_method_entry.pack(side=tk.RIGHT)

# Create account number label and text field 
acc_frame = tk.Frame(window)
acc_frame.pack(pady=10, padx=10, anchor='w')

acc_label = tk.Label(acc_frame, text="Account Number:")
acc_label.pack(side=tk.LEFT)

acc_label_entry = tk.Entry(acc_frame, width=20)
acc_label_entry.pack(side=tk.LEFT)

# Create exp. date label and text field
exp_frame = tk.Frame(window)
exp_frame.pack(pady=10, padx=10, anchor='w')

exp_label = tk.Label(exp_frame, text="Expiration Date:")
exp_label.pack(side=tk.LEFT)

exp_label_entry = tk.Entry(exp_frame, width=20)
exp_label_entry.pack(side=tk.LEFT)

# Create amount paid and text field
amount_frame = tk.Frame(window)
amount_frame.pack(pady=10, padx=10, anchor='w')

amount_label = tk.Label(amount_frame, text="Amount Paid:")
amount_label.pack(side=tk.LEFT)

amount_label_entry = tk.Entry(amount_frame, width=20)
amount_label_entry.pack(side=tk.LEFT)

# Menu button 
menu_frame = tk.Frame(window)
menu_frame.pack(padx=10, pady=10, anchor='w')


button = tk.Button(menu_frame, text="Menu")
button.pack(side=tk.RIGHT)




# Start the tkinter event loop
window.mainloop()

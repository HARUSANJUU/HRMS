import customtkinter as ctk
import tkinter


def navigate_to_details(button_index):

    main_window.withdraw()


    details_window = ctk.CTk()
    details_window.geometry("1000x700")
    details_window.title('Details')

    def go_back():
        details_window.destroy()
        main_window.deiconify()  # Show the main window again

    back_button = ctk.CTkButton(master=details_window, text="Back", command=go_back)
    back_button.place(relx=0.05, rely=0.05, anchor=tkinter.NW)


    label = ctk.CTkLabel(master=details_window, text="Room Number")
    label.place(relx=0.5, rely=0, anchor=tkinter.N)

    guest_label = ctk.CTkLabel(master=details_window, text="Guest: Guest Name")
    guest_label.place(relx=0.5, rely=0.2, anchor=tkinter.N)

    category_label = ctk.CTkLabel(master=details_window, text="Room Category: Category")
    category_label.place(relx=0.5, rely=0.3, anchor=tkinter.N)

    capacity_label = ctk.CTkLabel(master=details_window, text="Capacity: capacity")
    capacity_label.place(relx=0.5, rely=0.4, anchor=tkinter.N)

    description_label = ctk.CTkLabel(master=details_window, text="Description: description")
    description_label.place(relx=0.5, rely=0.5, anchor=tkinter.N)

    status_label = ctk.CTkLabel(master=details_window, text="Status: status")
    status_label.place(relx=0.5, rely=0.6, anchor=tkinter.N)

    details_window.mainloop()


main_window = ctk.CTk()
main_window.geometry("750x450")
main_window.title('Rooms')


window_width = 750
window_height = 450
button_width = window_width // 8
button_height = window_height // 8
button_gap_x = (window_width - button_width * 6) // 7
button_gap_y = (window_height - button_height * 4) // 5


buttons = []
for i in range(24):
    button_col = i % 6
    button_row = i // 6
    button_x = button_gap_x * (button_col + 1) + button_width * button_col
    button_y = button_gap_y * (button_row + 1) + button_height * button_row
    button = ctk.CTkButton(master=main_window, text=f"Button {i+1}", width=button_width, height=button_height,
                           command=lambda idx=i: navigate_to_details(idx))
    button.place(x=button_x, y=button_y)
    buttons.append(button)

main_window.mainloop()
#Jackelyn

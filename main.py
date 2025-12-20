from tkinter import *
import employee_setup as setup

root = Tk()

# ##############################################################################################
# WIDGETS
# ##############################################################################################

# Setup buttons
setup_label = Label(root, text='EMPLOYEE SETUP',borderwidth=1, relief='solid')

add_employee_button = Button(root, text='Add Employee', width=12, command=setup.add_employee)
update_employee_button = Button(root, text='Update Employee', width=12, command=setup.update_employee)

# ##############################################################################################
# BIND WIDGETS
# ##############################################################################################

# Setup Buttons
setup_label.grid(row=0, column=0, columnspan=4 ,sticky=W+E, padx=(5,5), pady=(0,10))

add_employee_button.grid(row=1, column=0, padx=(5,10))
update_employee_button.grid(row=1, column=1, padx=(5,10))
# setup_button2.grid(row=1, column=1, padx=(0,10))
# setup_button3.grid(row=1, column=2, padx=(0,10))
# setup_button4.grid(row=1, column=3, padx=(0,5))
# setup_button5.grid(row=2, column=0, columnspan=2 ,sticky=W+E, padx=(5,5) ,pady=(10,10))
# setup_button6.grid(row=2, column=2, columnspan=2 ,sticky=W+E, padx=(5,5) ,pady=(10,10))

















# ROOT WINDOW CONFIG
root.title('Annual / Sick Leave')
# root.iconbitmap('icons/smoking.ico')
root.geometry('440x490')
# root.columnconfigure(0, weight=1)

# RUN WINDOW
root.mainloop()
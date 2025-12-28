from tkinter import *
from tkinter import ttk


top = Toplevel()
top.attributes('-topmost', 'true')
top.geometry("300x300")
top.title("Edit Leave")

# ##############################################################################################
# TREE VIEW
# ##############################################################################################
# Add Some Style
style = ttk.Style()

# Pick A Theme
style.theme_use('default')

# Configure the Treeview Colors
style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3")

# Change Selected Color
style.map('Treeview',
	background=[('selected', "#347083")])

# Create a Treeview Frame
tree_frame = Frame()
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Columns
my_tree['columns'] = ("ID", "First Name", "Last Name", "Start Date", "Leave Available")

# Format Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=W, width=150)
my_tree.column("First Name", anchor=W, width=150)
my_tree.column("Last Name", anchor=W, width=150)
my_tree.column("Start Date", anchor=CENTER, width=100)
my_tree.column("Leave Available", anchor=CENTER, width=110)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("ID", text="ID", anchor=W)
my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("Start Date", text="Start Date", anchor=CENTER)
my_tree.heading("Leave Available", text="Leave Available", anchor=CENTER)

# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")
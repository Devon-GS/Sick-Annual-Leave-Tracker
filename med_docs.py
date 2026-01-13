import os
from tkinter import messagebox
from database import collect_data_docs


# Make folder if not exists
try:
	if not os.path.exists('Medical Documents'):
		os.mkdir('Medical Documents')
except Exception as error:
	messagebox.showerror(title='Add Medical Docments Folder', message=error)

def create_med_folder(fname, sname):
	try:
		# Make employee folder if not exists
		for employee in collect_data_docs():
			if not os.path.exists(f'Medical Documents/{employee[1]} {employee[2]}'):
				os.mkdir(f'Medical Documents/{employee[1]} {employee[2]}')
	except Exception as error:
		messagebox.showerror(title='Open Medical Docments Folder', message=error)

def open_med_doc(fname, sname):
	try:
		# Make employee folder if not exists
		for employee in collect_data_docs():
			if not os.path.exists(f'Medical Documents/{employee[1]} {employee[2]}'):
				os.mkdir(f'Medical Documents/{employee[1]} {employee[2]}')

		# Open folder or specific folder
		if fname == '':
			os.startfile('Medical Documents')
		else:
			os.startfile(os.path.join("Medical Documents", f"{fname} {sname}"))
	except Exception as error:
		messagebox.showerror(title='Open Medical Docments Folder', message=error)


	





import sqlite3
import os
from tkinter import messagebox

# ##############################################################################################
# INITIALIZE DATABASE
# ##############################################################################################

if not os.path.exists('employeeLeave.db'):
	con = sqlite3.connect("employeeLeave.db")
	c = con.cursor()

	# Turn on foreign keys
	c.execute('PRAGMA foreign_keys = ON')

	c.execute('''CREATE TABLE IF NOT EXISTS employees (
			ID TEXT NOT NULL PRIMARY KEY,
			firstName TEXT,
			lastName TEXT,
			startDate TEXT
			)'''
		)

	c.execute('''CREATE TABLE IF NOT EXISTS annualLeave (
			ID TEXT,
			leaveTaken INTEGER,
			leaveStart TEXT,
			LeaveEnd TEXT,
			FOREIGN KEY (ID) REFERENCES employees (ID)
			)'''
		)

	con.commit()
	con.close()

# ##############################################################################################
# DATABASE FUNCTIONS
# ##############################################################################################

def add_employee_db(id, fname, sname, start_date):
	try:
		con = sqlite3.connect("employeeLeave.db")
		c = con.cursor()

		# Turn on foreign keys
		c.execute('PRAGMA foreign_keys = ON')

		c.execute("INSERT INTO employees VALUES (:id, :firstName, :lastName, :startDate)",
						{
							'id' : id,
							'firstName' : fname,
							'lastName' : sname,
							'startDate' : start_date
						})
		
		con.commit()
		con.close()
		
		# Display complete
		messagebox.showinfo(title='Add Employee', message='Added Employee Successfully')

	except Exception as error:
		messagebox.showerror(title='Add Employee Error', message=error)






# MAKE INSERT AND COLLECT FUNCTIONS









# c.execute("INSERT INTO employees (ID, firstName, lastName, startDate) VALUES('910610', 'Devon', 'Schuin', '01/01/2025')")
# c.execute("INSERT INTO annualLeave (ID, leaveTaken, leaveStart, leaveEnd) VALUES('910610', 0, '0', '0')")
# c.execute("INSERT INTO annualLeave (ID, leaveTaken, leaveStart, leaveEnd) VALUES('910610', 22, '22', '22')")


# c.execute("SELECT * FROM employees")
# c.execute("SELECT * FROM annualLeave")
# records = c.fetchall()

# print(records)
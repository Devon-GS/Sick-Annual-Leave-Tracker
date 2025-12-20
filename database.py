import sqlite3

con = sqlite3.connect("employeeLeave.db")
c = con.cursor()

# Turn on foreign keys
c.execute('PRAGMA foreign_keys = ON')

c.execute('''CREATE TABLE IF NOT EXISTS empoyees (
		  ID TEXT,
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
		  FOREIGN KEY (ID) REFERENCES empoyees (ID)
		  )'''
		)

con.commit()
con.close()


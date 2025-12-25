from datetime import datetime
from dateutil import relativedelta


def cal_acc_leave(emp_rec, leave_taken):
	# Get date now
	now = datetime.now()
	date_now = now.strftime("%d/%m/%Y")

	# Make into list
	rec_list = []

	for x in emp_rec:
		rec_list.append([x[0], x[1], x[2], x[3]])

	# Add leave days to employee info
	empolyee_info = []

	for rec in rec_list:
		# convert string to date object
		start_date = datetime.strptime(rec[3], "%d/%m/%Y")
		end_date = datetime.strptime(date_now, "%d/%m/%Y")

		# Get the relativedelta between two dates
		delta = relativedelta.relativedelta(end_date, start_date)

		# Get months difference
		months = delta.months + (delta.years * 12)
		leave_days = months * 1.25
		
		# Get leave days already taken
		for leave in leave_taken:
			if rec[0] == leave[0]:
				leave_days -= leave[1]

		# Add leave days to eployee data
		emp_info = rec + [leave_days]
		# print(emp_info)
		empolyee_info.append(emp_info)

	return empolyee_info	
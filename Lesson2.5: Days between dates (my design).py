#My idea is to caculate the total days from 0 to current dates, for date1 and date2 respectively.
#I think its advantage is to be tolerant with the input that date2 is earlier.

def days_part1(year):
	year_list = []
	i = 1
	while i < year :
		year_list.append(i)
		i = i + 1
	days = 0
	for e in year_list:
		if e%400 == 0 or (e%4 == 0 and e%100 != 0):
			days = days + 366
		else:
			days = days +365
	return days

def days_part2(year,month,date):
	list_pm = [31,28,31,30,31,30,31,31,30,31,30,31]
	list_rm = [31,29,31,30,31,30,31,31,30,31,30,31]
	if year%400 == 0 or (year%4 == 0 and year%100 != 0):
		month_days = 0
		i = 1
		while i<month:
			month_days = month_days + list_rm[i-1]
			i=i+1
		return  month_days + date
	else:
		month_days = 0
		i = 1
		while i<month:
			month_days = month_days + list_pm[i-1]
			i=i+1
		return  month_days + date

def days_interval(year1,month1,date1,year2,month2,date2):
	return days_part1(year2)+days_part2(year2,month2,date2)-days_part1(year1)-days_part2(year1,month1,date1)

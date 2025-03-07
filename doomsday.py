def runDoomsday(date):
	date = date.split("-")
	day = int(date[0])
	month = int(date[1])
	year = int(date[2])
	weekdays = {0: 'Saturday', 1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday'}

	if month < 3:
		month += 12
		year -= 1

	year_part = year % 100
	century_part = year // 100

	weekday = (day + (13 * (month + 1)) // 5 + year_part + year_part // 4 + century_part // 4 - 2 * century_part) % 7
	print(f"The day of the week is {weekdays[weekday]}")

if __name__ == "__main__":
	date = input("Enter the date that you want to know the weekday of (dd-mm-yyyy) \nExample: 21-02-2004 \n--> ")
	runDoomsday(date)

import datetime
import calendar

# Get the current date and time
now = datetime.datetime.now()

# Print the current date
print("Current Date:", now.date())

# Print the current time
print("Current Time:", now.time())

# Get the current year and month
year = now.year
month = now.month

# Create a calendar for the current month
cal = calendar.monthcalendar(year, month)

# Print the calendar
print("\nCalendar:")
print(calendar.month_name[month], year)
print("Mo Tu We Th Fr Sa Su")
for week in cal:
    for day in week:
        if day != 0:
            print(f"{day:2}", end=' ')
        else:
            print("  ", end=' ')
    print()

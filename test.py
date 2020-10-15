import datetime

base = datetime.datetime.now()
now = base.strftime("%H:%M:%S")
print(f"{now}")
hours = 5
hours_added = datetime.timedelta(hours=hours)
base2 = base + hours_added
then = base2.strftime("%H:%M:%S")
print(then)

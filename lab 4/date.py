#1
from datetime import datetime, timedelta
current_date = datetime.now()
result_date = current_date - timedelta(days=5)
print("Current Date and Time:", current_date)
print("After Subtracting 5 Days:", result_date)

#2
from datetime import datetime, timedelta
current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)
print("Yesterday:", yesterday.strftime("%Y-%m-%d %H:%M:%S"))
print("Today:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d %H:%M:%S"))

#3
from datetime import datetime
current_datetime = datetime.now()
datetime_without_microseconds = current_datetime.replace(microsecond=0)
print("Original Datetime:", current_datetime)
print("Datetime without Microseconds:", datetime_without_microseconds)

#4
from datetime import datetime, timedelta

date1 = datetime.datetime(2024, 2, 13, 18, 56, 50)
date2 = datetime.datetime(2024, 2, 13, 18, 57, 0)

time_diff = date2 - date1
seconds = time_diff.total_seconds()

print(seconds)
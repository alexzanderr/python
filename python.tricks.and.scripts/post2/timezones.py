
""" HOW TO PRINT CURRENT TIME 
    FROM OTHER COUNTRIES """

# built in 'datetime' module
from datetime import datetime
import pytz # python time zones (built in)
time_format = '%H:%M:%S' 
# hours, minutes, seconds
# used as parameter for 'strftime' method

bucharest_timezone = 'Europe/Bucharest'
tokyo_timezone = 'Asia/Tokyo'
chicago_timezone = 'America/Chicago'

def print_current_time(timezone):
    current_time = datetime.now(
        pytz.timezone(timezone)
    ).strftime(time_format)
    print(f'Time in {timezone}: {current_time}')

print_current_time(bucharest_timezone)
print_current_time(tokyo_timezone)
print_current_time(chicago_timezone)
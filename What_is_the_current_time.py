#Simple Python program that fetches the time from datetime and prints out the current time
from datetime import datetime
now = datetime.now()

print ('The time is currently %s:%s:%s' % (now.hour, now.minute, now.second))

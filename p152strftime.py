from datetime import datetime

now = datetime.now()

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)


import time
current = time.localtime(time.time())
y=current.tm_year
print("Year:", y)

if y%4==0:
    print("Leap Year")
else:
    print("Not a Leap Year")
import time
current = time.localtime(time.time())
h=current.tm_hour
if h<13:
    print(h,"am")
else:
    print(h-12,"pm")
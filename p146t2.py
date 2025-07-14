import time
current = time.localtime(time.time())
h=current.tm_hour
print(h)

if 5<=h and h<12:
    print("Good Morning")

elif 12<=h and h<17:
    print("Good Afternoon")

elif 17<=h and h<21:
    print("Good Evening")

else:
    print("Good Night")
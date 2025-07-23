n=[11, 12, 15, 22, 99, 77, 200, 66, 2]
t = 0

for i in n:
    if i % 3 == 0:
        t=t+i

print("divisible by 3 sum=", t)

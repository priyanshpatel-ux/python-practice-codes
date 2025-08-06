month={
"January":2200,
"February":2350,
"March":2600,
"April":2130,
"May":2190,
"June":1980,
"July":2400,
"August":2250,
"September":2100,
"October":2400,
"November":2150,
"December":2500
}

d1=month["January"]
d2=month["February"]
d3=month["March"]
d4=month["April"]
d5=month["May"]
d6=month["June"]
d7=month["July"]
d8=month["August"]
d9=month["September"]
d10=month["October"]
d11=month["November"]
d12=month["December"]


cal1 = d2-d1
print("1:", cal1, "spent extra in February")


cal2 = d1+d2+d3
print("2:", cal2, "total expenses for the first quarter")

if 2400 in month.values():
    print("3: Yes, you spent exactly 2400 in at least one month.")
else:
    print("3: No, you never spent exactly 2400 in any month.")

month["June"] = 2080
d6 = month["June"]
print("4: Updated June expense =", d6)

month["April"] = month["April"] - 200
d4 = month["April"]
print("5: Updated April expense after $200 refund =", d4)


max=max(month.values())
for name, expense in month.items():
    if expense == max:
        print("8:", "Maximum is", expense, "in", name)

total = d1 + d2 + d3 + d4 + d5 + d6
avg = total / 6
print("7: Average monthly expense for Jan to June =", round(avg, 2))



min=min(month.values())
for name, expense in month.items():
    if expense == min:
        print("8:", "Minimum is", expense, "in", name)

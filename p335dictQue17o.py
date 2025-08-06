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
    
list1 = []
list2 = []

for m, a in month.items():
    list1.append(m)
    list2.append(a)

max1=max(list2)
index=list2.index(max1)
max2=list1[index]

min1=min(list2)
index=list2.index(min1)
min2=list1[index]


print("Highest Expense is in Month",max2,"and is",max1)
print("Lowest Expense is in Month",min2,"and is",min1)
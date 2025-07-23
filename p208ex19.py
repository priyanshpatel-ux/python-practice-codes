list1=[11, 44, 500]
list2=[77, 44, 11]

c=[]
for i in list1:
    if i in list2:
        c.append(i)
print(c)


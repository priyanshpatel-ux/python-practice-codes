list1=[11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]
list2=[]
for i in list1:
    if list1.count(i)==1:
        list2.append(i)
print(list2)

list1=[11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i) 
print(list2)
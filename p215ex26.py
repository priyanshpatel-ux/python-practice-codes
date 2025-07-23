list1=[11, 44, 500, 22, 99, 77, 200, 66, 2]
if len(list1) >= 2:
    s=list1[0]
    e=list1[-1]
    list1[0]=e
    list1[-1]=s
    print("Swap=", list1)
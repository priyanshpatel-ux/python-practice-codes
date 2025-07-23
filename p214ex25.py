list1=[11, 44, 500, 22, 99, 77, 200, 66, 2]
c1=0
c2=0
for n in list1:
    if n % 2 == 0:
        c1=c1+1
    else:
        c2=c2+1
print("Even count=", c1)
print("Odd count=", c2)
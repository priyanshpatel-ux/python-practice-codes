sno=int(input("Enter statring number =>"))
eno=int(input("Enter ending number =>"))

for j in range(sno,eno+1):
    no=j
    c=1
    for i in range(2,no):
        if no % i ==0:
            c=0
            break

    if c==1:
         print(no, end =" ")

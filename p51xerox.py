xer=int(input("Enter the Service Type(1 for print,2 for Type)="))

if xer==1:
    n=int(input("Enter Quantity="))
    
    if n>50:
        print("Print Price is 3Rs per page")
        total1=3*n
        print("Your Bill is",total1)
    else:
        print("Print Price is 5Rs per page")
        total1=5*n
        print("Your Bill is",total1)

elif xer==2:
    n=int(input("Enter Quantity="))
    
    if n>50:
        print("Type Price is 15Rs per page")
        total1=15*n
        print("Your Bill is",total1)
    else:
        print("Type Price is 20Rs per page")
        total1=20*n
        print("Your Bill is",total1)

else:
    print("Error Please enter 1, 2")
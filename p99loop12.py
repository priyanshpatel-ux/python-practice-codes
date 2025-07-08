total1=0
total2=0
total3=0
total4=0

while True:
    print("\n")
    xer=int(input("Enter the Service Type\n1 is for Xerox \n2 is for Type \n3 Total Bill \n Enter="))

    if xer==1:
        n=int(input("Enter Quantity="))
    
        if n>50:
            print("Print Price is 3Rs per page")
            total1=3*n
            print("Your Bill is",total1)
        
        else:
            print("Print Price is 5Rs per page")
            total2=5*n
            print("Your Bill is",total2)

    elif xer==2:
        n=int(input("Enter Quantity="))
    
        if n>50:
            print("Type Price is 15Rs per page")
            total3=15*n
            print("Your Bill is",total3)
        else:
            print("Type Price is 20Rs per page")
            total4=20*n
            print("Your Bill is",total4)
    
    elif xer==3:

        print("Total Bill=",total1+total2+total3+total4)
        break
    else:
        print("Error Please enter 1, 2")
xer=(input("Enter the Service Type (Print or Type)="))

if xer=='Print':
    n=int(input("Enter Quantity="))
    
    if n>50:
        print("Print Price is 3Rs per page")
        total1=3*n
        print("Your Bill is",total1)
    else:
        print("Print Price is 5Rs per page")
        total1=5*n
        print("Your Bill is",total1)

elif xer=='Type':
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
    print("Error Please enter Print or Type")
dish=int(input("Enter the desired dish (1 is for Pizza, 2 is for burger, 3 is for Softdrink-=)"))

if dish==1:
    print("Pizza Price is 500")
    n=int(input("Enter Quantity="))
    total1=500*n
    print("Your Bill is",total1)

elif dish==2:
    print("Burger Price is 300")
    n=int(input("Enter Quantity="))
    total1=300*n
    print("Your Bill is",total1)

elif dish==3:
    print("Soft Drink Price is 100Rs")
    n=int(input("Enter Quantity="))
    total1=100*n
    print("Your Bill is",total1)

else:
    print("Error Please enter 1, 2, or 3.")
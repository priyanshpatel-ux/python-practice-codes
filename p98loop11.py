total1=0
total2=0
total3=0
while True:
    print("\n")
    dish=int(input("Enter the desired dish \n1 is for Pizza \n2 is for burger \n3 is for Softdrink \n4 Total Bill \n Enter="))

    if dish==1: 
        print("Pizza Price is 500")
        n=int(input("Enter Quantity="))
        total1=500*n
        print("Your Bill is",total1)

    elif dish==2:
        print("Burger Price is 300")
        n=int(input("Enter Quantity="))
        total2=300*n
        print("Your Bill is",total2)

    elif dish==3:
        print("Soft Drink Price is 100Rs")
        n=int(input("Enter Quantity="))
        total3=100*n
        print("Your Bill is",total3)
    
    elif dish==4:

        print("Total Bill=",total1+total2+total3)
        break
    else:
        print("wrong option")
            
while True:
    print("\n")
    m=int(input("Select 1 or 2  or 3 or 4 or 5 \n1 is for Add \n2 is for Sub \n3 for Mul \n4 is for Div \n5 Exit \nEnter=>"))
    if m==1:
            n=int(input("Enter Number =>"))
            n1=int(input("Enter Number =>"))
            print("Ans = ",n+n1)
    elif m==2:
            n=int(input("Enter Number =>"))
            n1=int(input("Enter Number =>"))
            print("Ans = ",n-n1)
    elif m==3:
            n=int(input("Enter Number =>"))
            n1=int(input("Enter Number =>"))
            print("Ans = ",n*n1)
    elif m==4:
            n=int(input("Enter Number =>"))
            n1=int(input("Enter Number =>"))
            print("Ans = ",n/n1)

    elif m==5:
           break
    else:
            print("wrong option")
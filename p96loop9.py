while True:
    print("\n")
    m=int(input("Select 1 or 2  or 3(1 is for square \n2 is for cube \n3 for exit)\n Enter =>"))
    if m==1:
            n=int(input("Enter Number =>"))
            print("Square = ",n*n)
    elif m==2:
            n=int(input("Enter Number =>"))
            print("Cube = ",n*n*n)
    elif m==3:
           break
    else:
            print("wrong option")
        
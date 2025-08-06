n=int(input("Enter limit =>"))


for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end=" ")
    m=1
    for k in range(1,n-i+2):
        print(m,end=" ")
        m=m+1

    print("")

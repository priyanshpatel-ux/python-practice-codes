n=int(input("Enter limit =>"))

m=n+1
for i in range(1,n+1):
    m=m-1
    for j in range(1,i+1):
        print(" ",end=" ")
    for k in range(n,i-1,-1):
        print(m,end=" ")
    print("")

n=int(input("Enter Number="))
k=n+1
for i in range(1,n+1):
    k=k-1
    for j in range(n,i-1,-1):
        print(k,end=" ")
    print("")


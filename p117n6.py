n=int(input("Enter Number =>"))

for i in range(1,n+1):
    for j in range(0,k,i):
        print(k,end=" ")
        k=k-1
    print()

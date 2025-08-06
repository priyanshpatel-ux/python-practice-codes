n=int(input("Enter Number="))
k=1
for i in range(1,n+1):
    for j in range(i):
        print(k,end=" ")
        k=k+1
    print("")
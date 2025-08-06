n=int(input("Enter Number="))

for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(" ",end=" ")
    m=n-i+1        
    for k in range(n,i+n):                 
        print(m, end=" ")
        m+=1
    print("")

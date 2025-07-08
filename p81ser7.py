n=int(input("Enter Number =>"))
s=0
for i in range(1,n+1):
    if i%2==0:
        print(i,end=" + ")
    else:
        print(-i,end=" + ")
       
    s1=s+i
    s2=s-i
print("\nSum = ",s1,s2)
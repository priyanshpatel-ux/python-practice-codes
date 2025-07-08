n=int(input("Enter Number =>"))
s=0
for i in range(10,n+1,10):
    print(i,end=" + ")

    s=s+i
print("\nSum = ",s)
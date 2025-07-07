n=int(input("Enter Number =>"))
s=0
for i in range(1,n+1):
    print(i,end="*")
    s=s+i

print("\nSum = ",s)
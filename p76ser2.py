n=int(input("Enter Number =>"))
s=0
for i in range(1,n+2):
    print(i*2,end=" + ")
    s=s+i*2

print("\nSum = ",s)
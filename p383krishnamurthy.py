import math
y=0
n=int(input("Enter Number="))
c=n
while n>0:
    r=n%10
    y=y+math.factorial(r)
    n=n//10
print("Krishnamurthy=",y)

if y==c:
    print("Krishnamurthy Number")
else:
    print("Not an Krishnamurthy Number")
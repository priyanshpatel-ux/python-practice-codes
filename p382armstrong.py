y=0
n=int(input("Enter Number="))
c=n
while n>0:
    r=n%10
    y=y+r**3
    n=n//10
print("Armstrong=",y)

if y==c:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
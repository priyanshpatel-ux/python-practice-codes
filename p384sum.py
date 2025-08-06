y=0
n=int(input("Enter Number="))

while n>0:
    r=n%10
    y=y+r
    n=n//10
print("Sum=",y)

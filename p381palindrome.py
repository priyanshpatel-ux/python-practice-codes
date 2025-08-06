y=0
n=int(input("Enter Number="))
c=n
while n>0:
    r=n%10 #gives last digit
    y=y*10+r
    n=n//10 #removes last digit
print("Reverse=",y)

if y==c:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
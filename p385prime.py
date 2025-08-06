y=0
n=int(input("Enter Number="))
c=n
for i in range(2, n):
        if n%i==0:
            y=1
            break

if y==0:    
    print(n,"Prime Number")
else:
    print(n, "Not a Prime Number")

n=int(input("Enter Number =>"))
c=0
for i in range(2, n//2):
    if n%i==0:
        c=1
        break
if c==0:    
    print(n,"Prime Number")
else:
    print("Not a Prime Number")
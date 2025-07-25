tup = (11, 22, 33, 44, 55)
s=0
c=1

for n in tup:
    if n % 7 == 0:        
        print("Divisible=", n)

        c=c+1
        s=s+n

print("count=",c, "\nsum=",s)
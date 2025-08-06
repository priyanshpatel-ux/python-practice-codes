y=0
n=int(input("Enter Number="))
c=n
for i in range(2, n):
        if n%i==0:
            y=1
            break

if y==0:    
    print(n,"Prime Number")

    no=n+1
    while True:
        y=0
        for i in range(2, no):
            if no%i==0:
                y=1
                break
        if y==0:
            print("Next Prime =",no)
            break
        else:
            no=no+1

else:
    print(n,"Not a Prime Number")
n=input("Enter ISBN number=")
s=0

if len(n)==10:
    for i in range(10):
        d=int(n[i])
        p=i+1
        t=d*p
        s=s+t

    if s%11==0:
        print("Valid ISBN Number")
    else:
        print("Invalid ISBN Number")
else:
    print("Invalid ISBN Number")

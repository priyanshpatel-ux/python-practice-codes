eng=int(input("Enter marks of english =>"))
maths=int(input("Enter marks of maths =>"))
ss=int(input("Enter marks of ss =>"))

total= eng + maths + ss

if total < 50:
    print("C")
elif total > 100:
    print("A")
else:
    print("B")
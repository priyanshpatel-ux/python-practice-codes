def table():
    n=int(input("Enter number"))
    for i in range(1, 11):
        print(n,"*",i,"=",i*n)

def oddeven():
    n=int(input("Enter number="))
    for i in range(1,n+1):
        if i%2==0:
            print(i,"Even")
        else:
            print(i,"ODD")

def pn():
    n=int(input("Enter number="))
    for i in range(1,n+1):
        if i%2==0:
            print("",i,"Even")
        else:
            print(-i,"ODD")

def max3():
    x=int(input("Enter number"))
    y=int(input("Enter number"))
    z=int(input("Enter number"))
    if x>y and x>z:
        print("greater number is",x)
    elif y>x and y>z:
        print("greater number is",y)

    else:
        print("greater number is",z)

def prime():
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

def fact():
    n=int(input("Enter number"))
    f=1
    for i in range(n,0,-1):
        print(i ,end="x")
        f=f*i
    print("=",f)

def tri():

    h=int(input("Enter height =>"))
    b=int(input("Enter base =>"))

    area= h * b / 2
    print("Area = ",area)

def area():
    radius=int(input("Enter radius =>"))
    pi=22/7
    area= pi * radius * radius
    print("Area of circle = ",area)

def leap():

    year=int(input("Enter Year="))

    if year%4==0:
        print("It is a Leap Year")

    else:
        print("It is not a Leap Year")

def cube():
    n=int(input("Enter Number =>"))
    for i in range(n,n+1):
        print("Cube=",i*i*i)

def square():
    n=int(input("Enter Number =>"))
    for i in range(n,n+1):
        print("=",i*i)


print("Press 1 for square")
print("Press 2 for cube")
print("Press 3 for leap")
print("Press 4 for area")
print("Press 5 for tri")
print("Press 6 for fact")
print("Press 7 for prime")
print("Press 8 for max3")
print("Press 9 for pn")
print("Press 10 for oddeven")
print("Press 11 for table")






op=int(input("Enter option =>"))

if op==1:
    square()
if op==2:
    cube()
if op==3:
    leap()
if op==4:
    area()
if op==5:
    tri()
if op==6:
    fact()
if op==7:
    prime()
if op==8:
    max3()
if op==9:
    pn()
if op==10:
    oddeven()
if op==11:
    table()
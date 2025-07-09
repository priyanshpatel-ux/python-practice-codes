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

square()
cube()
leap()
area()
tri()
fact()
prime()
max3()
pn()
oddeven()
table()
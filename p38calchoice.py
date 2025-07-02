num1=int(input("Enter Number 1="))
num2=int(input("Enter Number 2="))
choice=int(input("Enter 1 for Add, 2 for Sub, 3 for Mul, 4 for Div="))

add=num1+num2
sub=num1-num2
mul=num1*num2
div=num1/num2

if choice==1:
    print("Output",add)

if choice==2:
    print("Output",sub)

if choice==3:
    print("Output",mul)

if choice==4:
    print("Output",div)
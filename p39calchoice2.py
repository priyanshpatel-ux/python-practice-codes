choice=(input("Enter + for Add, - for Sub, * for Mul, / for Div="))


if choice=='+':
    num1=int(input("Enter Number 1="))
    num2=int(input("Enter Number 2="))
    add=num1+num2
    print("Output",add)

elif choice=='-':
    num1=int(input("Enter Number 1="))
    num2=int(input("Enter Number 2="))
    sub=num1-num2
    print("Output",sub)

elif choice=='*':
    num1=int(input("Enter Number 1="))
    num2=int(input("Enter Number 2="))
    print("Output",num1*num2)

elif choice=='/':
    num1=int(input("Enter Number 1="))
    num2=int(input("Enter Number 2="))
    div=num1/num2
    print("Output",div)

else:
    print("Error, Enter Valid Characters")